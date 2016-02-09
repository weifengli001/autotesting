#!/bin/bash

#reset applications status
cd /Users/weifengli/github/happymango/test/scripts
sh reset_application.sh -U weifengli -P happymango 393
sh reset_application.sh -U weifengli -P happymango 430
sh reset_application.sh -U weifengli -P happymango 431
sh reset_application.sh -U weifengli -P happymango 474
sh reset_application.sh -U weifengli -P happymango 475

#run UI test
cd /Users/weifengli/PycharmProjects/happymango/getloan
python all_in_one.py

#run DB test
python dbTestStatus.py 475 474 431 430 393

#reset applications status
cd /Users/weifengli/github/happymango/test/scripts
sh reset_application.sh -U weifengli -P happymango 393
sh reset_application.sh -U weifengli -P happymango 430
sh reset_application.sh -U weifengli -P happymango 431
sh reset_application.sh -U weifengli -P happymango 474
sh reset_application.sh -U weifengli -P happymango 475