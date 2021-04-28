#!/usr/bin/env python
# -*- coding: utf-8 -*-
import configparser

config_file = './config/config.ini'

class cfg:
    def read_config(section, option):
        # 读取配置文件
        config = configparser.ConfigParser()
        config.read_file(open(config_file))
        a = config.get(section, option)
        print('Read config: ' + '[' + section + ']: ' + 'option = ' + a)
        return a

    def write_config(section, option, value):
        # 写入配置文件
        config = configparser.ConfigParser()

        try:
            Config.read(config_file)
        except:
            # set a number of parameters
            config.add_section(section)
        else:
            print('Write section already exist')
        config.set(section, option, value)
        # write to file
        config.write(open(config_file, "a+")) # 没有新建  存在打开
        print('Write config: ' + '[' + section + ']: ' + 'option = ' + value)

#cfg.add_config('id2url', 'total', '20')
cfg.write_config('id2url', 'total', str(20))
