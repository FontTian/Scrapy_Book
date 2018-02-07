# -*- coding: utf-8 -*-

BOT_NAME = 'example'

SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'


ROBOTSTXT_OBEY = True
HTTPCACHE_ENABLED = True

# PipeLines
# ITEM_PIPELINES = {
#     'example.pipelines.PriceConverterPipeline':300,
#     'example.pipelines.DuplicatesPipeline':250,
# }
