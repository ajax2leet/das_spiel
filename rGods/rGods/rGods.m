/*
 *  rGods.h
 *  created 28-Jun-2013
 *  by Lars Steffen Weinstock <schrodinger666@web.de>
 */

#ifndef RGODS_C
#define RGODS_C

#import "rGods.h"

@implementation rGods

@synthesize prudence;
@synthesize wisdom;
@synthesize creation;
@synthesize life;
@synthesize might;
@synthesize devotion;
@synthesize craft;
@synthesize humanity;

-(rGods*) init_with_prudence: (int) pr wisdom: (int) wi creation: (int) cr life: (int) li might: (int) mi devotion: (int) de craft: (int)cra humantity: (int) hu{
    self = [super init];        // constructor von NSObject aufrufen
    if ( self ){                // init erfolgreich
        self.prudence = pr;
        self.wisdom = wi;
        self.creation = cr;
        self.life = li;
        self.might = mi;
        self.devotion = de;
        self.craft = cra;
        self.humanity = hu;
    } else {
        // excpetion schmeissen!
    }
    
    return self;
}

@end

#endif
