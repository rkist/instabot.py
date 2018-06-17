#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time

from src import InstaBot
from src.check_status import check_status
from src.feed_scanner import feed_scanner
from src.follow_protocol import follow_protocol
from src.unfollow_protocol import unfollow_protocol

def ReadFileData(filePath):  
    with open(filePath) as f:
        content = f.readlines()
    data = [x.strip() for x in content]
    return data



loginData = ReadFileData(r"clinibem\login.botconf")
unwantedUsernameList = ReadFileData(r"clinibem\unwanted_username_list.botconf")
unfollowWhitelist = ReadFileData(r"clinibem\unfollow_whitelist.botconf")


bot = InstaBot(
    login=loginData[0],
    password=loginData[1],
    like_per_day=500,
    comments_per_day=0,
    tag_list=['follow4follow', 'f4f', 'cute'],
    tag_blacklist=['rain', 'thunderstorm'],
    user_blacklist={},
    max_like_for_one_tag=50,
    follow_per_day=300,
    follow_time=1 * 60,
    unfollow_per_day=300,
    unfollow_break_min=15,
    unfollow_break_max=30,
    log_mod=0,
    proxy='',
    # List of list of words, each of which will be used to generate comment
    # For example: "This shot feels wow!"
    comment_list=[["essa", "a", "sua"],
                  ["foto", "imagem"],
                  ["é", "é realmente"],
                  ["linda", "fantástica"],
                  [".", "..", "...", "!", "!!", "!!!"]],
    # Use unwanted_username_list to block usernames containing a string
    ## Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
    ### 'free_followers' will be blocked because it contains 'free'
    unwanted_username_list = unwantedUsernameList,
    unfollow_whitelist = unfollowWhitelist)

