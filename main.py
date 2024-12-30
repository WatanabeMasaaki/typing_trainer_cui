#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 23:17:34 2024

@author: watanabemasaaki
"""

import random

# トレーニングしたい文字が有効であるかを判定
def isValid(s):
    # 文字列がアルファベット（小文字）1文字以上なら、配列を返す
    chars = []
    
    if 1 <= len(s):
        for c in s:
            # print(c)
            if 'a' <= c <= 'z':
                if c not in chars:
                    chars.append(c)
            else:
                print('input must not contain any characters except for lower case alphabet')
                return None
                    
        return chars
    else:
        print('input must contain at least 1 character')
        return None
    



def main():
    
    trainChars = []
        
    # トレーニングしたいキーを入力させる
    while True:
        train_char = input('press the key which you want to train: ')
        trainChars = isValid(train_char)
        
        if trainChars != None:
            break
    
        
    #トレーニング開始
    #トレーニング開始表示
    disp = 'train start: '
    for c in trainChars:
        disp += c + ' '
    print(disp)
    
    
    #タイピング開始
    length = 2 #タイピングの文字列の長さ、進むごとに長くなる
    points = 0 #文字列の長さだけ、得点が増える
    #trainCharsの中の文字からランダムで文字列を生成
    while True:    
        word = ''
        for i in range(length):
            rand = random.randrange(len(trainChars))
            word += trainChars[rand]
        
        answer = input('[' + word + ']: ')
        
        if answer == word:
            points += length
            length += 1
            continue
        else:
            break
        
    print('game over')
    print(str(points) + ' points')
    
            
    
    
    
    


if __name__ == "__main__":
    main()