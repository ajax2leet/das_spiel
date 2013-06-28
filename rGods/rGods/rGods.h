/*
 *  rGods.h
 *  created 28-Jun-2013
 *  by Lars Steffen Weinstock <schrodinger666@web.de>
 */

#ifndef RGODS_H
#define RGODS_H

#import <Foundation/Foundation.h>

@interface rGods : NSObject{
    /* Eigenschaften der Götter */
    int prudence;   // Besonnenheit <-> Tollkühnheit
    int wisdom;     // Weisheit <-> Intuition
    int creation;   // Erschaffung <-> Zerstörung
    int life;       // Leben <-> Tod
    int might;      // Macht <-> Ohnmacht
    int devotion;   // Hingabe <-> Authorität
    int craft;      // Handwerk <-> Natur
    int humanitiy;  // Menschlichkeit <-> Abstraktion
}

@property int prudence;
@property int wisdom;
@property int creation;
@property int life;
@property int might;
@property int devotion;
@property int craft;
@property int humanity;

// constructor mit Eigenschaften
-(rGods*) init_with_prudence: (int) pr wisdom: (int) wi creation: (int) cr life: (int) li might: (int) mi devotion: (int) de craft: (int)cra humantity: (int) hu;

@end

#endif
