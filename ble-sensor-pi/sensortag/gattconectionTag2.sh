#!/bin/bash
sudo gatttool -b C4:BE:84:71:76:07 --char-read -a 0x21;sudo gatttool -b C4:BE:84:71:76:07 --char-write -a 0x24 -n 01;sudo gatttool -b C4:BE:84:71:76:07 --char-read -a 0x21;sudo gatttool -b C4:BE:84:71:76:07  --char-write-req -a 0x22 -n 0100 --listen;
