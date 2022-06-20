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