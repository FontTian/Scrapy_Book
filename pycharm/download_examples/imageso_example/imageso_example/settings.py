# -*- coding: utf-8 -*-

BOT_NAME = 'imageso_example'

SPIDER_MODULES = ['imageso_example.spiders']
NEWSPIDER_MODULE = 'imageso_example.spiders'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'imageso_example.pipelines.ImagesoExamplePipeline': 300,
    'scrapy.pipelines.images.ImagesPipeline':1,
}
IMAGES_STORE = 'imageso_fold'

# # 缩略图
# IMAGES_THUMBS = {
#     'small':(50,50),
#     'big':(270,270)
# }
#
# # 过滤
# IMAGES_MIN_WIDTH = 100
# IMAGES_MIN_HEIGHT = 150
