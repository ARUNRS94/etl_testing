import os
from pyspark.sql import SparkSession

cwd = os.getcwd()
len_dir = os.path.join(cwd, 'input\length.xlsx')
src_dat_dir = os.path.join(cwd, 'input\source.txt')

src_dat_open = open(src_dat_dir, "r")
dat_file = src_dat_open.readlines()
dat_file = [i.replace('\n', '') for i in dat_file]

spark = SparkSession.builder.appName('newsession').getOrCreate()
df = spark.read.format(len_dir)

'''import sys
from awsglue.context import GlueContext

len_dir = "s3a://idny/input/Length.xlsx"
src_dat_dir = "s3a://idny/input/source.txt"

sourceDyf = glueContext.create_dynamic_frame_from_options(
    connection_type="s3",
    format="text",
    connection_options={
        "paths": [src_dat_dir]
    })'''