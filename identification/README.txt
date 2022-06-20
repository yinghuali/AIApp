# data time: 2021.10.28
1.pkl trux01 down
2_1.pkl hpc down
2_2.pkl hpc down
3_1.pkl hpc down
3_2.pkl hpc down
4.pkl serval09 down
5.pkl trux01 down
6.pkl trux01 down
7.pkl serval09 down
8.pkl trux01 down
9_1.pkl hpc htian down
9_2.pkl serval09 down
10.pkl trux01 down
11_1.pkl trux01 down
11_2.pkl serval09 down
12.pkl trux01 down
13.pkl serval09 down
14.pkl trux01 down
15.pkl trux01 down



# 启动anaconda终端
source ~/anaconda3/bin/activate root

source /Users/yinghua.li/anaconda3/bin/activate root

# 启动bert
bert-serving-start -model_dir /Users/yinghua.li/Documents/Pycharm/wwm_uncased_L-24_H-1024_A-16 -num_worker=4 -port=5777 -port_out=5778

# python多进程最多设置个数
server09/10 -> 32
trux01 -> 96
80 + 28 + 28 = 150
进程28 处理500个 耗时 26分钟
进程28 处理10万个 耗时 2 days, 6:25:13.006138

# get metadata
curl -O --remote-header-name -G https://androzoo.uni.lu/play_meta/get/laozhaopianxiufu.cn
curl -O --remote-header-name -G https://androzoo.uni.lu/play_meta/get/video.like
http://play.google.com/store/apps/details?id=<package_name>
# package_name 路径
AndroidManifest.xml 第一行 package="laozhaopianxiufu.cn"
<?xml version="1.0" encoding="utf-8" standalone="no"?><manifest xmlns:android="http://schemas.android.com/apk/res/android" android:compileSdkVersion="29" android:compileSdkVersionCodename="10" package="laozhaopianxiufu.cn" platformBuildVersionCode="108" platformBuildVersionName="1.0.8">


# 后台运行shen
nohup /home/yinghua/anaconda3/bin/python -u analysis_lightweight_models_multiple.py > 2.log 2>&1 &
nohup /home/yinghua/anaconda3/bin/python -u down_decompilation_apk.py > /dev/null 2>&1 &
nohup /home/yinghua/anaconda3/bin/python -u test_unable_determine_framework.py > unable.log 2>&1 &
2211198

nohup /home/yinghua/anaconda3/bin/python main_multiprocessing.py > /dev/null 2>&1 &
nohup /home/yinghua/anaconda3/bin/python characteristics_ai_apps_google_play.py > 1.log 2>&1 &
18:24

/home/users/yili/anaconda3/bin/python -u main_multiprocessing.py



# HPC

ssh iris-cluster
# 作业提交
作业提交脚本至少必须包括节点数量、时间、分区和节点类型（资源分配约束和功能）以及服务质量 (QOS)。
sbatch start.sh

# 查看所有用户脚本运行情况
squeue
# 查看自己的脚本运行情况
squeue -u yili

# 查看正在运行的脚本信息
scontrol show job <jobid>
$  scontrol show job 2452212

# 取消特定作业：
scancel 2523840
/home/users/yili/pycharm/MobileModelIdentif

# si 进去程序调试节点

===============================start.sh====================================== sbatch start.sh
#!/bin/bash -l
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=28
#SBATCH --mem-per-cpu=4G
#SBATCH --time=13-23:00:00
#SBATCH --mail-type=end,fail
#SBATCH --mail-user=yinghua.li@uni.lu
#SBATCH --output=/dev/null
#SBATCH --qos=long
#SBATCH -p batch

module load lang/Java/1.8.0_241

source ~/anaconda3/bin/activate root
python main_multiprocessing.py
===============================start.sh======================================
# No more than 4 long jobs per User (MaxJobsPU) are allowed, using no more than 2 nodes per jobs.



# ag
ag /home/yinghua/pycharm/MobileModelIdentif/sha256_play_google_com_list_0_50.pkl -i -l --silent -m2 /Users/yinghua.li/Documents/Server/MobileModelIdentif
ag hed_lite_model_quantize.tflite -i -l --silent -m2 /Users/yinghua.li/Documents/Server/MobileModelIdentif/ai_apps_analysis/3F71EFAF7D2A4B0645EBBF819F4AC4BD80C8B76ADCD03E57321CDE40AAA5B885_compile
ag tflite -i -l --silent -m2 /Users/yinghua.li/Documents/Server/MobileModelIdentif/ai_apps_analysis/D3BB1EE87D425BD5B9C318A7900DF79EB95D384749E5380843D495B5E240B5E3_compile

# 远程文件拉取
scp -r yinghua@serval09.uni.lu:/home/yinghua/pycharm/MobileModelIdentif/ai_apps_analysis/tfmodel_updates_analysis /Users/yinghua.li/Documents/Server/Models/TFmodel_updates
scp yinghua@serval09.uni.lu:/home/yinghua/pycharm/MobileModelIdentif/result_sha256_list_0_4000.txt /Users/yinghua.li/Documents/Server/MobileModelIdentif
scp yinghua@serval09.uni.lu:/home/yinghua/pycharm/MobileModelIdentif/result/google_sha256_list_25.txt /Users/yinghua.li/Documents/Server/MobileModelIdentif/result/
scp -r yinghua@trux01.uni.lu:/home/yinghua/pycharm/AIApps/ai_apps_analysis/df_latest_new.csv /Users/yinghua.li/Documents/Pycharm/AIApps/data/analysis_result

scp yinghua@trux01.uni.lu:0A0819A816111FE5F2F4AB19E9396C3D6AC158CAEA5A3AEA0ED3F54A2429C66E_compile /Users/yinghua.li/Documents/Server/MobileModelIdentif/result

scp yinghua@trux01.uni.lu:/home/yinghua/pycharm/MobileModelIdentif/ai_apps_analysis/unable_determine_framework.txt /Users/yinghua.li/Documents/Server/MobileModelIdentif/result
scp -r iris-cluster:/home/users/yili/pycharm/MobileModelIdentif/000001A94F46A0C3DDA514E1F24E675648835BBA5EF3C3AA72D9C378534FCAD6_test /Users/yinghua.li/Desktop

scp -r iris-cluster:/home/users/yili/pycharm/bug_detection_ai/AIApp /Users/yinghua.li/Documents/Pycharm/AIAppsData

scp yinghua@trux01.uni.lu:/home/yinghua/pycharm/MobileModelIdentif/model_encryption_analysis/other.txt /Users/yinghua.li/Documents/Server/MobileModelIdentif/model_encryption_analysis

sh /home/yinghua/pycharm/Label/dex2jar/d2j-dex2jar.sh -f classes2.dex
java -jar /home/yinghua/pycharm/Label/cfr-0.150.jar classes2-dex2jar.jar >> java2.txt


# 本地数据上传服务器
scp -r /Users/yinghua.li/Documents/Pycharm/AIApps iris-cluster:/home/users/yili/pycharm
scp /Users/yinghua.li/Documents/Server/MobileModelIdentif/data/all_data/check_opencv_list.pkl yinghua@trux01.uni.lu:/home/yinghua/pycharm/MobileModelIdentif/data/all_data
scp -r /Users/yinghua.li/Documents/Server/MobileModelIdentif/ai_apps_analysis yinghua@serval09.uni.lu:/home/yinghua/pycharm
scp -r /Users/yinghua.li/Documents/Server/MobileModelIdentif iris-cluster:/home/users/yili/pycharm
scp /Users/yinghua.li/Documents/Server/MobileModelIdentif/ai_apps_analysis/unable_determine_framework_list.pkl yinghua@trux01.uni.lu:/home/yinghua/pycharm/MobileModelIdentif/data/unbale_determine/

scp /Users/yinghua.li/Documents/Server/MobileModelIdentif/apktool_2.5.0.jar yinghua@trux01.uni.lu:/home/yinghua/pycharm/MobileModelIdentif/model_encryption_analysis

scp -r /Users/yinghua.li/Documents/Pycharm/data yinghua@trux01.uni.lu:/home/yinghua/pycharm/
scp -r /Users/yinghua.li/Documents/Pycharm/AIApps iris-cluster:/home/users/yili/pycharm

scp -r /Users/yinghua.li/Documents/Pycharm/AIApps yinghua@serval09.uni.lu:/home/yinghua/pycharm
/home/yinghua/pycharm/MobileModelIdentif/data/all_data/check_list_0.pkl

scp -r /Users/yinghua.li/Documents/Pycharm/latest.csv  yinghua@trux01.uni.lu:/home/yinghua/pycharm/AIApps/data
path_df_all
scp -r /Users/yinghua.li/Documents/Server/MobileModelIdentif/tfmodel_prediction  yinghua@trux01.uni.lu:/home/yinghua/pycharm/MobileModelIdentif
scp -r /Users/yinghua.li/Documents/Pycharm/data yinghua@serval09.uni.lu:/home/yinghua/pycharm
scp -r /Users/yinghua.li/Desktop/local/AIApps2_2 tsun-cluster:/home/users/tsun/yinghuali/pycharm
scp -r /Users/yinghua.li/Documents/Pycharm/data tsun-cluster:/home/users/tsun/yinghuali/pycharm

# apk分析
(apk_size为字节bytes)
1MB = 1024 * 1024 Byte
dex2jar
    /home/yinghua/pycharm/MobileModelIdentif/dex2jar
    /Users/yinghua.li/Documents/Server/MobileModelIdentif/dex2jar/d2j-dex2jar.sh

curl -O --remote-header-name -G -d apikey=8c08e1e623110c600186098a11ba882a7e323ad32b71868510c971a504eca3f9 -d sha256=771B8B89A9E8796C8705A6845EC38A6CAD7C87C5ED05FB24B1CD72DCFA9ED71F https://androzoo.uni.lu/api/download
apktool d -f 771B8B89A9E8796C8705A6845EC38A6CAD7C87C5ED05FB24B1CD72DCFA9ED71F.apk -o com_galaxys_camera4k_1
apktool d -s -f /home/yinghua/pycharm/MobileModelIdentif/Test/china.apk -o /home/yinghua/pycharm/MobileModelIdentif/Test/china_compile

ag caffe.BlobProto -i -l --silent -m2 /Users/yinghua.li/Desktop/data_analysis/com_galaxys_camera4k_1
ag stub -i -l --silent -m2 /Users/yinghua.li/Desktop/com
ag stub /Users/yinghua.li/Desktop/com
ag "org.tensorflow.lite.Interpreter" classes.txt

readelf -p .rodata /Users/yinghua.li/Desktop/data_analysis/com_galaxys_camera4k_0/lib/armeabi-v7a/libst_mobile.so >> /Users/yinghua.li/Desktop/data_analysis/com_galaxys_camera4k_0/lib/armeabi-v7a/so.txt

# 文件转换.dex -> .jar
sh /Users/yinghua.li/Documents/Server/MobileModelIdentif/dex2jar/d2j-dex2jar.sh -f classes.dex

chmod a+x /home/yinghua/pycharm/MobileModelIdentif/dex2jar/d2j_invoke.sh

java -jar /Users/yinghua.li/Documents/Server/MobileModelIdentif/cfr-0.150.jar classes-dex2jar.jar >> java.txt
tensorflow Interpreter lite

# .so 文件
# 判断
if filepath.endswith('.so') and 'armeabi' in filepath:
readelf -p .rodata /Users/yinghua.li/Documents/Server/MobileModelIdentif/Test/apk_decompile/lib/armeabi-v7a/libbrotli.so > /Users/yinghua.li/Desktop/test.txt

readelf -p .rodata /home/yinghua/pycharm/MobileModelIdentif/Test/apk_decompile/lib/armeabi-v7a/libjingle_peerconnection_so.so >> /home/yinghua/pycharm/MobileModelIdentif/Test/apk_decompile/so.txt
rodata的意义同样明显，ro代表 read only，即只读数据(const)。关于 rodata类型的数据，要注意以下几点

string *.so可以查看关键字

# google metadata
https://play.google.com/store/apps/details?id=com.vicovr.manager



# 工作流程

step1：获取 AI Apps 信息，得到result/ **.txt
       python main_multiprocessing.py

step2: 获取 df_all.csv  All AI apps features (56682)
       python get_result_information.py

step3: 获取 characteristics_ai_apps_result.txt
       python characteristics_ai_apps.py

step4: 获取 df_google_metadata.csv        特征 = ['pkg_name', 'link', 'metadata']
       python get_google_metadata.py

step5: 获取 df_google_apps_characteristic.csv      特征 = ['pkg_name', 'link', 'tag_metadata', 'score', 'installs', 'category', 'company']
       python characteristics_google_ai_apps.py

step6: 获取 google_play_result.txt (used for two pictures)     Categories of AI apps ([categories, number of ai apps, average score, average installs]), Companies of AI apps.
       python get_google_category_score_install_company.py

step7: covid-19 ai apps
       python get_ai_covid.py

step8: 获取 df_google_tflite_sha256_pkgname.csv
       python get_google_sha256_pkgname_tfmodel.py

step9: 获取 data_tfmodels
       python get_tfmodels.py

step10: 获取 所有tfmodel  (google_tflite)
       python get_tfmodels.py

step11: 获取 tfmodels_information.csv, [sha256_app, sha256_model, model_name]
       python analysis_tfmodels.py

step12: 获取 tensorflow lite hub, tf_hub_model_information.csv 模型信息 [model_sha256, model_name, task]
        python analysis_tfmodels_hub.py

step13: tf models analysis
        python model_analysis.py

step15: 获取 历史ai apps 历史版本待分析数据 df_latest_new_tag.csv, history_ai_sha256_list.pkl，进行验证获取 history_ai_sha256_list.txt
        python get_df_latest_new.py
        python ai_historic_apps.py 获取 df_history_ai_sha256_list.csv
        python analysis_historic_versions.py


step16: 获取 df_publicmodel_comany_task.csv 公共模型 公司 任务 (df_publicmodel_comany_task_picture.csv)

        python get_df_publicmodel_comany_task.py


step17: entropy models analysis
        python get_model_entropy.py  获取 模型 entropy
        python analysis_encrypted_model.py   绘图，the company of encrypted models

step18: tfmodel 模型层分析
        python analysis_models_layer.py


step19: RQ3 Model lightweight
        #python models_flops_analysis.py
        #python models_performance.py
        #python models_performance_analysis.py

# path adb
1 进入 cd /Users/yinghua.li/Documents/flops
# 安装测试apk
/Users/yinghua.li/Documents/tool/platform-tools/adb install -r -d -g android_aarch64_benchmark_model.apk

# push models
/Users/yinghua.li/Documents/tool/platform-tools/adb push /Users/yinghua.li/Desktop/models/dognet_a_dog_breed_identifier.tflite /data/local/tmp

# run model
/Users/yinghua.li/Documents/tool/platform-tools/adb shell am start -S \
  -n org.tensorflow.lite.benchmark/.BenchmarkModelActivity \
  --es args '"--graph=/data/local/lenet5.tflite \
              --num_threads=4"'



mobile model performance


adb push /Users/yinghua.li/Desktop/models/vgg.tflite /data/local/tmp
adb shell am start -S -n org.tensorflow.lite.benchmark/.BenchmarkModelActivity --es args '"--graph=/data/local/tmp/vgg.tflite --num_threads=4"'
adb logcat | grep "Average inference"


/Users/yinghua.li/Documents/tool/platform-tools/adb install -r -d -g android_aarch64_benchmark_model_plus_flex.apk


# 查看设备
/Users/yinghua.li/Documents/tool/platform-tools/adb devices
# 清楚数据
/Users/yinghua.li/Documents/tool/platform-tools/adb logcat -c
# 保存结果
/Users/yinghua.li/Documents/tool/platform-tools/adb logcat | ag "Average inference" > /Users/yinghua.li/Documents/Pycharm/AIApps/data/analysis_result/performance6.log

        python get_models_flops.py
        python models_flops_analysis.py


step20: RQ7 What kind of data feeds AI apps
        python data_feed_aiapps.py 获取
        python data_feed_aiapps_analysis.py

step21: RQ6: Privacy concerns with user data / check app policies
        result collected in pricacy_concerns.txt.
        python privacy_concerns.py  获取 privacy metadata
        python pricacy_concerns_analysis_statistics.py  统计方法：获取ai app对用户隐私数据


step25: RQ5: What do app reviews highlight about AI  结果记录：reviews_analysis_data.txt
        python get_reviews_data.py  获取app评论数据 df_aiapp_review.csv
        python review_analysis.py
        python review_analysis_tfidf.py
        python review_analysis_textrank.py
        python review_analysis_lda.py



RQ3:
analysis_lightweight_models.py 获取df_lightweight_model.csv, ['path', 'label_int8', 'label_float16']





top_framework_x = ['TfLite', 'OpenCV', 'TensorFlow', 'Google AI', 'Caffe',
                   'Baidu synthesizer', 'NCNN', 'Baidu OCR', 'Amazon AI', 'Baidu NLP']

top_framework_y = ['TfLite', 'OpenCV', 'TensorFlow', 'Google AI', 'Caffe',
                   'Baidu synthesizer', 'NCNN', 'Baidu OCR', 'Amazon AI', 'Baidu NLP']

[[0, 10364, 11481, 5477, 2004, 277, 610, 87, 797, 161],
 [28534, 0, 11493, 9130, 1796, 276, 600, 80, 816, 166],
 [20701, 8407, 0, 8019, 1722, 276, 603, 80, 812, 160],
 [28476, 10707, 11513, 0, 2062, 277, 614, 91, 819, 172],
 [28632, 10716, 11554, 9369, 0, 276, 607, 91, 822, 171],
 [28696, 10747, 11583, 9393, 2062, 0, 621, 91, 823, 171],
 [28684, 10726, 11568, 9222, 2059, 277, 0, 91, 823, 162],
 [28695, 10750, 11585, 9393, 2062, 277, 621, 0, 823, 171],
 [28692, 10748, 11582, 9392, 2050, 277, 621, 91, 0, 172],
 [28697, 10750, 11582, 9393, 2061, 276, 620, 89, 823, 0]]




% \author{Yinghua Li}
% \email{yinghua.li@uni.lu}
% \affiliation{%
%   \institution{University of Luxembourg}
%  %  \streetaddress{P.O. Box 1212}
%  	\country{Luxembourg}
%  %  \state{Ohio}
%  %  \postcode{43017-6221}
% }


% \author{Xueqi Dang}\authornote{Corresponding author.}
% \email{xueqi.dang@uni.lu}
% \affiliation{%
%   \institution{University of Luxembourg}
%  %  \streetaddress{P.O. Box 1212}
%  	\country{Luxembourg}
%  %  \state{Ohio}
%  %  \postcode{43017-6221}
% }

% \author{Haoye Tian}
% \email{haoye.tian@uni.lu}
% \affiliation{%
%   \institution{University of Luxembourg}
%  %  \streetaddress{P.O. Box 1212}
%  	\country{Luxembourg}
%  %  \state{Ohio}
%  %  \postcode{43017-6221}
% }

% \author{Tiezhu Sun}
% \email{tiezhu.sun@uni.lu}
% \affiliation{%
%   \institution{University of Luxembourg}
%  %  \streetaddress{P.O. Box 1212}
%  	\country{Luxembourg}
%  %  \state{Ohio}
%  %  \postcode{43017-6221}
% }


% \author{Zhijie Wang}
% \email{zhijie.wang@ualberta.ca}
% \affiliation{%
%   \institution{University of Alberta}
%  %  \streetaddress{P.O. Box 1212}
%  	\country{Canada}
%  %  \state{Ohio}
%  %  \postcode{43017-6221}
% }

% \author{Lei Ma}
% \email{ma.lei@acm.org}
% \affiliation{%
%   \institution{University of Alberta}
%  %  \streetaddress{P.O. Box 1212}
%  	\country{Canada}
%  %  \state{Ohio}
%  %  \postcode{43017-6221}
% }

% \author{Jacques Klein}
% \email{jacques.klein@uni.lu}
% \author{Tegawend\'e F. Bissyand\'e}
% \email{tegawende.bissyande@uni.lu}
% \affiliation{%
%   \institution{University of Luxembourg}
% %  \streetaddress{No. 29, Jiangjun Avenue}
%   \country{Luxembourg}
% %  \postcode{211106}
% }










