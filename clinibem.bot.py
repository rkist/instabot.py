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
tagList = ReadFileData(r"clinibem\tag_list.botconf")
tagBlacklist = ReadFileData(r"clinibem\tag_blacklist.botconf")


bot = InstaBot(
    login=loginData[0],
    password=loginData[1],
    like_per_day=500,
    comments_per_day=0,
    tag_list = tagList,
    tag_blacklist = tagBlacklist,
    user_blacklist = {},
    max_like_for_one_tag= 30,
    follow_per_day= 100,
    follow_time= 4 * 60,
    unfollow_per_day = 90,
    unfollow_break_min = 20,
    unfollow_break_max = 40,
    log_mod = 0,
    proxy = '',
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

while True:
    #print("# MODE 0 = ORIGINAL MODE BY LEVPASHA")
    #print("## MODE 1 = MODIFIED MODE BY KEMONG")
    #print("### MODE 2 = ORIGINAL MODE + UNFOLLOW WHO DON'T FOLLOW BACK")
    #print("#### MODE 3 = MODIFIED MODE : UNFOLLOW USERS WHO DON'T FOLLOW YOU BASED ON RECENT FEED")
    #print("##### MODE 4 = MODIFIED MODE : FOLLOW USERS BASED ON RECENT FEED ONLY")
    #print("###### MODE 5 = MODIFIED MODE : JUST UNFOLLOW EVERYBODY, EITHER YOUR FOLLOWER OR NOT")

    ################################
    ##  WARNING   ###
    ################################

    # DON'T USE MODE 5 FOR A LONG PERIOD. YOU RISK YOUR ACCOUNT FROM GETTING BANNED
    ## USE MODE 5 IN BURST MODE, USE IT TO UNFOLLOW PEOPLE AS MANY AS YOU WANT IN SHORT TIME PERIOD

    mode = 2

    print("Running mode : %i" %(mode))
    print("CTRL + C to cancel this operation or wait 10 seconds to start")
    time.sleep(10)

    if mode == 0:
        bot.new_auto_mod()

    elif mode == 1:
        check_status(bot)
        while bot.self_following - bot.self_follower > 200:
            unfollow_protocol(bot)
            time.sleep(10 * 60)
            check_status(bot)
        while bot.self_following - bot.self_follower < 400:
            while len(bot.user_info_list) < 50:
                feed_scanner(bot)
                time.sleep(5 * 60)
                follow_protocol(bot)
                time.sleep(10 * 60)
                check_status(bot)

    elif mode == 2:
        bot.bot_mode = 1
        bot.new_auto_mod()

    elif mode == 3:
        unfollow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 4:
        feed_scanner(bot)
        time.sleep(60)
        follow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 5:
        bot.bot_mode = 2
        unfollow_protocol(bot)

    else:
        print("Wrong mode!")