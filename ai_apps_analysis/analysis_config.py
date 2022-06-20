class Config:
    def __init__(self):

        self.privacy_concerns_keywords = ['name', 'email', 'address', 'birth', 'gender', 'phone number', 'location', 'country',
                                          'photo', 'image', 'user ID', 'audio', 'browsing history', 'video', 'search history',
                                          'account', 'device ID', 'device name', 'credit card', 'IMEI number', 'Android ID',
                                          'interaction', 'frequency of use']

        self.layer_list = ['Regularization', 'Add', 'Attention', 'Dropout', 'Average',
                           'Pool', 'Normalization', 'Bidirectional', 'CategoryEncoding', 'CenterCrop',
                           'Concatenate', 'Conv', 'ConvLSTM', 'Cropping', 'Dense', 'Discretization',
                           'ELU', 'Embedding', 'Flatten', 'GRU', 'Hashing', 'LSTM', 'LeakyReLU', 'Masking',
                           'Maximum', 'Minimum', 'Multiply', 'PReLU', 'Permute', 'RNN', 'RandomContrast',
                           'RandomCrop', 'RandomFlip', 'RandomHeight', 'RandomRotation', 'RandomTranslation',
                           'RandomWidth', 'RandomZoom', 'ReLU', 'RepeatVector', 'Rescaling', 'Reshape',
                           'Resizing', 'Softmax', 'StringLookup', 'Subtract', 'TextVectorization', 'TimeDistributed',
                           'UpSampling', 'Wrapper', 'ZeroPadding', 'deserialize']

        self.markets = ['play.google.com', 'PlayDrone', 'anzhi', 'appchina', 'VirusShare', 'mi.com', '1mobile', 'angeeks', 'slideme', 'fdroid',
                        'unknown', 'praguard', 'torrents', 'freewarelovers', 'proandroid', 'hiapk', 'genome', 'apk_bang']

        self.google_category = ['Art & Design', 'Augmented reality', 'Auto & Vehicles', 'Beauty', 'Books & Reference',
                                'Business', 'Comics', 'Communication', 'Dating', 'Daydream', 'Education', 'Entertainment',
                                'Events', 'Finance', 'Food & Drink', 'Health & Fitness', 'House & Home', 'Libraries & Demo', 'Lifestyle',
                                'Maps & Navigation', 'Medical', 'Music & Audio', 'News & Magazines', 'Parenting',
                                'Personalisation', 'Personalization',
                                'Photography',
                                'Productivity', 'Shopping', 'Social', 'Sports', 'Tools', 'Travel & Local', 'Video Players & Editors',
                                'Watch faces for Wear OS', 'Wear OS', 'Weather',
                                'Action', 'Adventure', 'Arcade', 'Board', 'Card', 'Casino', 'Casual', 'Educational', 'Music', 'Puzzle', 'Racing', 'Role Playing', 'Simulation', 'Sports', 'Strategy', 'Trivia', 'Word'
                                ]

        self.end_model_format = ['.tflite', '.lite', '.pt', '.ptl', '.param', '.mlmodel', '.model', '.caffemodel',
                                 '.feathermodel', '.chainermodel', 'PaddlePredictor.jar', 'libpaddle_lite_jni.so',
                                 '.nnet', 'libtvm_rumtime.so', '.moa', 'model.prof',
                                 '.mallet', '.classifier', '.inferencer', '.cntk']

        self.so_identify = {'tflite': [b'tensorflow/contrib/lite/kernels/', b'N5EigenForTFLite', b'kTfLiteNullBufferHandle', b'/google/android/libraries/vision/facenet/'],
                            'ncnn': [b'overwrite existing custom layer index', b'layer load_param failed', b'14ncnnClassifier', b'N4ncnn5LayerE', b'sqz set ncnn load param'],
                            'tensorflow': [b'N10tensorflow8GraphDefE', b'TF_AllocateTensor', b'TF_NewTensor', b'N18tensorflow20ReadOnlyMemoryRegionE', b'speech/tts/engine/neural_network/tensorflow_inference', b'org.tensorflow.framework'],
                            'caffe': [b'caffe-android-lib/', b'pIN5caffe5Caffe3RNG9G', b'caffe.BlobProto', b'N5caffe5LayerIfEE', b'caffe::Net<float>', b'N16caffe_client_9919', b'goturn.caffemodel'],
                            'caffe2': [b'Caffe2 alloc', b'N6caffe28OpSchema', b'N6caffe26NetDefE', b'caffe2/caffe2/core/', b'/gen/caffe2/caffe2Android'],
                            'MobileDeepLearning': [b'N3mdl5LayerE', b'/baidu/mdl/demo/'],
                            'deeplearning4j': [b'org/nd4j/nativeblas/Nd4jCpu', b'N4nd4j6random10IGeneratorE', b'N4nd4j3ops'],
                            'snpe': [b'snpe_dsp_setup', b'/SNPE/SecondParty/symphony/src/', b'snpe_get_tensor_dims'],
                            'mxnet': [b'N5mxnet6EngineE', b'N5mxnet13GraphExecutor'],
                            'mace': [b'libmace', b'mace_input_node_', b'./mace/core/', b'mace/kernels/', b'N4mace6BufferE', b'N4mace27PreallocatedPooledAllocatorE'],
                            'featherCNN': [b'feathercnn', b'feather::LayerParameter', b'feather::PoolingLayer'],
                            'xnn': [b'/xNN-wallet/Android/', b'/xNN/src/layers/', b'FALCONXNN'],
                            'mlpack': [b'mlpack/core/', b'mlpack/prereqs', b'mlpack::', b'namespace mlpack'],
                            'Shogun': [b'shogun::SGVector', b'shogun::', b'shogun/distributions'],
                            'opencv': [b'org.opencv.ml']
                            }

        self.ai_code_key_words = ['org.tensorflow',
                                  'org.tensorflow.lite',
                                  'libtensorflowlite.so',
                                  'org.deeplearning4j',
                                  'org.apache.mxnet',
                                  'com.xiaomi.mace',
                                  'CNNdroid',
                                  'org.pytorch',
                                  'pytorch_android',
                                  'org.pytorch.LiteModuleLoader',
                                  'com.baidu.paddle',
                                  'PaddlePredictor',
                                  'org.neuroph',
                                  'neuroph.sourceforge',
                                  'org.apache.tvm',
                                  'xgboost-predictor',
                                  'biz.k11i.xgboost',
                                  'DecisionTreeClassifier',
                                  'RandomForestClassifier',
                                  'ExtraTreesClassifier',
                                  'KNeighborsClassifier',
                                  'GaussianNB',
                                  'BernoulliNB',
                                  'MLPClassifier',
                                  'weka.classifiers.trees.J48',
                                  'weka.classifiers',
                                  'weka.core',
                                  'weka.filters',
                                  'weka.gui',
                                  'meka.core',
                                  'meka.classifiers',
                                  'MLPACK_METHODS_RANN_RA_MODEL_HPP',
                                  'org.shogun',
                                  'cc.mallet',
                                  'cc/mallet',
                                  'mallet.cs',
                                  'com.rapidminer',
                                  'rapidminer.com',
                                  'com.datumbox',
                                  'org.opencv.ml'
                                  ]

        self.dic_dl_framework_keywords = {
            'TensorFlow': ['N10tensorflow8GraphDefE', 'TF_AllocateTensor', 'TF_NewTensor', 'N18tensorflow20ReadOnlyMemoryRegionE',
                           'speech/tts/engine/neural_network/tensorflow_inference', 'org.tensorflow.framework', 'tensorflow'],
            'TfLite': ['tensorflow/contrib/lite/kernels/', 'N5EigenForTFLite', 'kTfLiteNullBufferHandle', '/google/android/libraries/vision/facenet/',
                       'org.tensorflow.lite', 'libtensorflowlite.so', '.tflite', '.lite', 'tflite'],
            'NCNN': ['overwrite existing custom layer index', 'layer load_param failed', '14ncnnClassifier',
                     'N4ncnn5LayerE', 'sqz set ncnn load param'],
            'Caffe': ['caffe-android-lib/', 'pIN5caffe5Caffe3RNG9G', 'caffe.BlobProto', 'N5caffe5LayerIfEE',
                      'caffe::Net<float>', 'N16caffe_client_9919', '.caffemodel'],
            'Caffe2': ['Caffe2 alloc', 'N6caffe28OpSchema', 'N6caffe26NetDefE', 'caffe2/caffe2/core/', '/gen/caffe2/caffe2Android'],
            'DeepLearning4j': ['org/nd4j/nativeblas/Nd4jCpu', 'N4nd4j6random10IGeneratorE', 'N4nd4j3ops', 'org.deeplearning4j'],
            'Snpe': ['snpe_dsp_setup', '/SNPE/SecondParty/symphony/src/', 'snpe_get_tensor_dims'],
            'MxNet': ['N5mxnet6EngineE', 'N5mxnet13GraphExecutor', 'org.apache.mxnet'],
            'Mace': ['libmace', 'mace_input_node_', './mace/core/', 'mace/kernels/', 'N4mace6BufferE', 'N4mace27PreallocatedPooledAllocatorE', 'com.xiaomi.mace'],
            'FeatherCNN': ['feathercnn', 'feather::LayerParameter', 'feather::PoolingLayer', '.feathermodel'],
            'Xnn': ['/xNN-wallet/Android/', '/xNN/src/layers/', 'FALCONXNN'],
            'CNNDroid': ['CNNdroid'],
            'CoreML': ['.mlmodel'],
            'Chainer': ['.chainermodel'],
            'Pytorch': ['org.pytorch', 'pytorch_android', 'org.pytorch.LiteModuleLoader', '.pt', '.ptl'],
            'PaddlePaddle': ['com.baidu.paddle', 'PaddlePredictor'],
            'Keras': ['.keras', '.h5'],
            'Neuroph': ['org.neuroph', 'neuroph.sourceforge', '.nnet'],
            'TVM': ['libtvm_rumtime.so', 'org.apache.tvm'],
            'OpenCV': ['org.opencv.ml'],
            'CNTK': ['namespace CNTK']
        }

        self.dic_ai_service_framework_keywords = {
            'Google AI': ['Google_AI'],
            'Amazon AI': ['Amazon_AI'],
            'Alexa AI': ['Alexa_AI'],
            'Azure AI': ['Azure_AI'],
            'Baidu NLP': ['Baidu_NLP'],
            'Baidu synthesizer': ['Baidu_synthesizer'],
            'Baidu OCR': ['Baidu_OCR']
        }

        self.dic_ml_framework_keywords = {
            'xgboost-predictor': ['xgboost-predictor', 'biz.k11i.xgboost'],
            'sklearn-porter': ['DecisionTreeClassifier', 'RandomForestClassifier', 'ExtraTreesClassifier', 'KNeighborsClassifier',
                               'GaussianNB', 'BernoulliNB', 'MLPClassifier'],
            'WEKA': ['weka.classifiers.trees.J48', 'weka.classifiers', 'weka.core', 'weka.filters', 'weka.gui'],
            'MEKA': ['meka.core', 'meka.classifiers'],
            'Mlpack': ['mlpack/core/', 'mlpack/prereqs', 'mlpack::', 'namespace mlpack'],
            'Shogun': ['shogun::SGVector', 'shogun::', 'shogun/distributions', 'org.shogun'],
            'MALLET': ['cc.mallet', 'cc/mallet', 'mallet.cs', '.classifier'],
            'Rapid Miner': ['rapidminer.com'],
            'Datumbox': ['com.datumbox']
        }

        self.list_dl_framework = ['TensorFlow', 'TfLite', 'NCNN', 'Caffe', 'Caffe2', 'DeepLearning4j', 'Snpe',
                                  'MxNet', 'Mace', 'FeatherCNN', 'Xnn', 'CNNDroid', 'Chainer',
                                  'Pytorch', 'PaddlePaddle', 'Neuroph', 'TVM', 'OpenCV', 'CNTK']

        self.list_ai_service_framework = ['Google AI', 'Amazon AI', 'Alexa AI', 'Azure AI', 'Baidu NLP',
                                          'Baidu synthesizer', 'Baidu OCR']

        self.list_ml_framework = ['xgboost-predictor', 'sklearn-porter', 'WEKA', 'MEKA', 'Mlpack', 'Shogun',
                                  'MALLET', 'Rapid Miner', 'Datumbox']

        self.path_result_directory = '/Users/yinghua.li/Documents/Pycharm/AIApps/data/identification_result'
        self.path_latest = '/Users/yinghua.li/Documents/Pycharm/latest.csv'
        # self.path_save_df_all = '/Users/yinghua.li/Documents/Pycharm/AIApps/data/analysis_result/df_all.csv'
        self.path_save_df_all = '/home/yinghua/pycharm/AIApps/data/analysis_result/df_all.csv'

        self.path_save_df_all_latest = '/Users/yinghua.li/Documents/Pycharm/AIApps/data/analysis_result/df_all_latest.csv'
        self.path_characteristics_ai_apps_result = '/Users/yinghua.li/Documents/Pycharm/AIApps/data/analysis_result/characteristics_ai_apps_result.txt'

        # self.path_google_metadata = '/Users/yinghua.li/Documents/Pycharm/AIApps/data/analysis_result/df_google_metadata.csv'
        self.path_google_metadata = '/home/yinghua/pycharm/AIApps/data/analysis_result/df_google_metadata.csv'



