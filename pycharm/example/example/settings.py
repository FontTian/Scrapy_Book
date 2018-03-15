# -*- coding: utf-8 -*-

BOT_NAME = 'example'

SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

ROBOTSTXT_OBEY = True
HTTPCACHE_ENABLED = True

# PipeLines
ITEM_PIPELINES = {
    'example.pipelines.PriceConverterPipeline':300,
    # 'example.pipelines.DuplicatesPipeline':250,
}

# Exporter
# 指定导出数据的字段,并指定次序(默认导出全部,顺序随机)
FEED_EXPORT_FIELDS = ['title','category','price','description']

