#!/bin/bash -l

#SBATCH -n 5
#SBATCH -N 1
#SBATCH -p gpu
#SBATCH --gres=gpu:1
#SBATCH --time=0-47:00:00
#SBATCH -C skylake
#SBATCH -J EGL
#SBATCH --mail-type=end,fail
#SBATCH --mail-type=all          # send email when job begins, ends and fails
#SBATCH --mail-user=yinghua.li@uni.lu

module purge
module load swenv/default-env/devel
module load system/CUDA numlib/cuDNN


#python -u ../../active_learning.py -metric 10 -results ../../new_results/RQ1/Lenet1/EGL.csv -model ../../new_models/RQ1/Lenet1/EGL.h5 -model_type lenet1
#python -u ../../active_learning.py -metric 10 -results ../../new_results/RQ1/Lenet5/EGL.csv -model ../../new_models/RQ1/Lenet5/EGL.h5 -model_type lenet5

for((i=0;i<10;i++));
do
python -u ../../NiN_egl.py
python -u ../../NIN_egl_train.py
done