//
//  main.m
//  rGods
//
//  Created by Runic on 28.06.13.
//  Copyright (c) 2013 run1c. All rights reserved.
//

#import <Foundation/Foundation.h>

#import "rGods.h"

int main(int argc, const char * argv[])
{
    @autoreleasepool {
        // insert code here...
        NSLog(@"Hello, World!");
        rGods* god1 = [[rGods alloc] init_with_prudence:10 wisdom:10 creation:10 life:10 might:10 devotion:10 craft:10 humantity:10];
        god1.wisdom = 2;
    }
    return 0;
}

