from git import Repo
import shutil
import numpy as np
import metrics_service
import os
from shutil import copyfile
from HTMLGenerator import HTMLGenerator
import time


def clear_and_clone(url,folder_path):
    if (os.path.exists(folder_path)):
        shutil.rmtree(folder_path)
    Repo.clone_from(url, folder_path)

def perform_R_script(text_to_perform):
    return os.system(text_to_perform)


def perform_test_for_repository_4_1(url,folder_path):
    print('Starting test for '+url)
    clear_and_clone(url,folder_path)

    copyfile('test_data/4_1/test_x_4_1.csv', folder_path+'/test_x_4_1.csv')

    os.chdir(folder_path)
    result=perform_R_script('Rscript test_algorithm.R --save')
    print(result)
    os.chdir('../..')
    predicted_data_y=np.genfromtxt(folder_path+'/test_predicted_4_1.csv',delimiter=',')
    labels_data_y=np.genfromtxt('test_data/4_1/test_y_4_1.csv',delimiter=',')
    accuracy=metrics_service.print_full_metrics_classification(labels_data_y,predicted_data_y)
    HTMLGenerator().generate('%s_results_4_1.html'%folder_path.split('/')[1],accuracy)
    return accuracy

def summary_4_1_results():
    while True:
        team1_accuracy=perform_test_for_repository_4_1('https://github.com/MarcinStachowiak/wks_starter.git', 'target/team1')
        team2_accuracy = perform_test_for_repository_4_1('https://github.com/MarcinStachowiak/wks_starter.git','target/team2')
        print('For 4_1 team1 (accuracy) = %f and team2 (accuracy) = %f' % (team1_accuracy,team2_accuracy))
        time.sleep(5)

summary_4_1_results()