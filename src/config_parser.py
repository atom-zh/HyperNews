#!/usr/bin/env python
# -*- coding: utf-8 -*-
import configparser

config_file = './config/config.ini'

class cfg:
    def read_config(section, option):
        # 读取配置文件
        config = configparser.ConfigParser()
        config.readfp(open(config_file))
        a = config.get(section, option)
        print(a)

    def add_config(section, option, value):
        # 写入配置文件
        config = configparser.ConfigParser()
        # set a number of parameters
        config.add_section(section)
        config.set(section, option, value)
        # write to file
        config.write(open(config_file, "w")) # 没有新建  存在打开

    def modify_cofnig(section, option, value):
        # 修改配置文件内容
        fixConfig = configparser.ConfigParser()
        fixConfig.read(config_file)
        a = fixConfig.add_section(section)
        fixConfig.set(section, option, value)
        fixConfig.write(open(config_file, "r+")) #可以把r+改成其他方式，看看结果:)

cfg.add_config('id2content', 'tatle', '20')
