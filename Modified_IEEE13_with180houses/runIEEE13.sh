#!/bin/bash
(export FNCS_BROKER="tcp://*:5570" && exec fncs_broker 175 &> broker.log &)
(export FNCS_CONFIG_FILE=auction_Market_1.yaml && exec python auction_Market_1.py IEEE13 "2013-07-01 00:00:00" 172800 600  &> auctionMarket1.log &)
(export FNCS_CONFIG_FILE=tracer.yaml && exec fncs_tracer 2d tracer.out &> tracer.log &)
(exec ./launch_IEEE13_agents.sh &) # 173, not counting double_auction.py


