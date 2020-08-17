@State
def RifleShotA():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1500)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(8000)
        AirUntechableTime(30)
        Hitstop(2)
        Unknown11001(10, 10, 15)
        Unknown9015(1)
        Unknown11050(2, 'rrbHitEff_Slash')
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 1)

        def upon_54():
            Unknown13(25)
            GFX_0('rrbBulletEff_Break', 0)
        Unknown53(1)
        teleportRelativeX(-150000)
        Unknown1056(3000)
        Unknown1064(2000)
        physicsXImpulse(150000)
    sprite('RifleShotAtk', 60)
    GFX_0('rrbBulletEff', 0)

@State
def RifleShotB():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1500)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(8000)
        AirUntechableTime(30)
        Hitstop(2)
        Unknown11001(10, 10, 15)
        Unknown9015(1)
        Unknown11050(2, 'rrbHitEff_Slash')
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 1)

        def upon_54():
            Unknown13(25)
            GFX_0('rrbBulletEff_Break', 0)
        Unknown53(1)
        teleportRelativeX(-150000)
        Unknown1056(3000)
        Unknown1064(2000)
        physicsXImpulse(150000)

        def upon_12():
            Unknown23029(3, 3001, 0)
    sprite('RifleShotAtk', 60)
    GFX_0('rrbBulletEff', 0)

@State
def RifleShotEx():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1500)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(8000)
        AirUntechableTime(30)
        Hitstop(2)
        Unknown11001(10, 10, 15)
        Unknown9015(1)
        Unknown11050(2, 'rrbHitEff_Slash')
        Unknown30065(0)
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 1)

        def upon_54():
            Unknown13(25)
            GFX_0('rrbBulletEff_Break', 0)
        Unknown53(1)
        teleportRelativeX(-150000)
        Unknown1056(3000)
        Unknown1064(2000)
        physicsXImpulse(150000)
    sprite('RifleShotAtk', 60)
    GFX_0('rrbBulletEff', 0)

@State
def AirRollingShot():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1000)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(20000)
        AirUntechableTime(30)
        Hitstop(2)
        Unknown9015(1)
        Unknown11050(2, 'rrbHitEff_Slash')
        Unknown11068(1)
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 1)

        def upon_54():
            Unknown13(25)
        Unknown53(1)

        def upon_12():
            Unknown23029(3, 3001, 0)
    sprite('AirShotAtk', 4)

@State
def AirRollingShotEx():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1000)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(60000)
        AirPushbackY(20000)
        Unknown9178(1)
        AirUntechableTime(60)
        Hitstop(2)
        Unknown11001(10, 0, 5)
        Unknown9015(1)
        Unknown11050(2, 'rrbHitEff_Slash')
        Unknown30065(0)
        MinimumDamagePct(10)
        Unknown11068(1)
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 1)

        def upon_54():
            Unknown13(25)
        Unknown53(1)

        def upon_12():
            Unknown23029(3, 3001, 0)
    sprite('AirShotAtk', 4)
    sprite('RifleShotAtk', 60)
    teleportRelativeX(-150000)
    Unknown1056(3000)
    Unknown1064(2000)
    physicsXImpulse(150000)
    GFX_0('rrbBulletEff', 0)
    clearUponHandler(54)

    def upon_54():
        Unknown13(25)
        GFX_0('rrbBulletEff_Break', 0)

@State
def RollingShot():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1500)
        Unknown11092(1)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(20000)
        AirUntechableTime(36)
        Hitstop(2)
        Unknown9015(1)
        Unknown11050(2, 'rrbHitEff_Slash')
        Unknown23182(3)
        Unknown11108(3)
        Unknown30065(0)
        MinimumDamagePct(10)
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 1)

        def upon_54():
            Unknown13(25)
        teleportRelativeX(440000)
        Unknown1007(250000)
        Unknown53(1)

        def upon_12():
            Unknown23029(3, 3001, 0)
    sprite('AirShotAtk', 4)

@State
def RollingShotASS():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1500)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(20000)
        AirPushbackY(30000)
        AirUntechableTime(36)
        Hitstop(2)
        Unknown9015(1)
        Unknown11050(2, 'rrbHitEff_Slash')
        Unknown11042(1)
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 1)

        def upon_54():
            Unknown13(25)
        teleportRelativeX(340000)
        Unknown1007(250000)
        Unknown53(1)
    sprite('AirShotAtk', 4)

@State
def ShotAtk():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(15000)
        AirPushbackY(20000)
        PushbackX(30400)
        AirUntechableTime(30)
        Unknown9015(1)
        Unknown11050(2, 'rrbHitEff_Slash')
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 1)

        def upon_54():
            Unknown13(25)
            GFX_0('rrbBulletEffB_Break', 0)
        Unknown53(1)
        teleportRelativeX(-150000)
        physicsXImpulse(80000)

        def upon_12():
            Unknown23029(3, 3001, 0)
    sprite('ShotAtk', 60)
    GFX_0('rrbBulletEffB', 0)

@State
def ShotAtk_Assist():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        AttackP1(70)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(15000)
        AirPushbackY(20000)
        AirUntechableTime(30)
        Unknown11042(1)
        Unknown9015(1)
        Unknown11050(2, 'rrbHitEff_Slash')
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 1)

        def upon_54():
            Unknown13(25)
            GFX_0('rrbBulletEffB_Break', 0)
        Unknown53(1)
        teleportRelativeX(-150000)
        physicsXImpulse(80000)
    sprite('ShotAtk', 60)
    GFX_0('rrbBulletEffB', 0)

@State
def UltimateAssault_AddAtk():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056()
        AttackLevel_(4)
        Damage(720)
        AttackP2(100)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(5)
        AirUntechableTime(120)
        PushbackX(0)
        Unknown11062(1)
        Unknown9016(1)
        Unknown11050(2, 'rrbHitEff_Slash')
        Unknown11064(1)
        Unknown11069('UltimateAssault_AddAtk')
        Hitstop(0)
        Unknown11001(0, 0, 0)
        Unknown11023(1)
        Unknown30048(1)
        Unknown11108(3)
        MinimumDamagePct(30)

        def upon_43():
            if (SLOT_48 == 4312):
                Damage(300)
                MinimumDamagePct(100)
                AttackP1(100)
                AttackP2(100)
                Unknown2037(1)
    sprite('RifleShotAtk', 5)
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('RifleShotAtk', 5)
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('RifleShotAtk', 5)
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('RifleShotAtk', 5)
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('RifleShotAtk', 5)
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('RifleShotAtk', 5)
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('RifleShotAtk', 5)
    Unknown23151(22, 105)
    RefreshMultihit()
    if SLOT_2:
        AttackP2(100)
        Damage(450)
    else:
        AttackP2(60)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(40000)
    AirPushbackY(40000)
    Unknown9202(20)
    Unknown11064(0)
    Unknown11069('')
    clearUponHandler(78)

    def upon_78():
        Unknown23029(3, 4311, 0)

@State
def UltimateAssaultOD_AddAtk():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056()
        AttackLevel_(4)
        Damage(600)
        AttackP2(100)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(5)
        AirUntechableTime(120)
        PushbackX(0)
        Unknown11062(1)
        Unknown9016(1)
        Unknown11050(2, 'rrbHitEff_Slash')
        Unknown11064(1)
        Unknown11069('UltimateAssaultOD_AddAtk')
        Hitstop(0)
        Unknown11001(0, 0, 0)
        Unknown11023(1)
        Unknown30048(1)
        Unknown11108(3)
        MinimumDamagePct(27)

        def upon_43():
            if (SLOT_48 == 4312):
                Damage(240)
                MinimumDamagePct(100)
                AttackP1(100)
                AttackP2(100)
                Unknown2037(1)
    sprite('RifleShotAtk', 3)
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('RifleShotAtk', 3)
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('RifleShotAtk', 3)
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('RifleShotAtk', 3)
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('RifleShotAtk', 3)
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('RifleShotAtk', 3)
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('RifleShotAtk', 3)
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('RifleShotAtk', 3)
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('RifleShotAtk', 3)
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('RifleShotAtk', 3)
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('RifleShotAtk', 5)
    Unknown23151(22, 105)
    RefreshMultihit()
    if SLOT_2:
        AttackP2(100)
        Damage(300)
    else:
        AttackP2(60)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(40000)
    AirPushbackY(40000)
    Unknown9202(20)
    Unknown11064(0)
    Unknown11069('')
    clearUponHandler(78)

    def upon_78():
        Unknown23029(3, 4311, 0)

@State
def rrbHitEff():

    def upon_IMMEDIATE():
        Unknown4009(2)
    sprite('null', 1)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef_hit_petal', 0)

@State
def rrbHitEff_Slash():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4010(2)
    sprite('null', 1)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef_hit_petal', 0)

@State
def rrbHitPetal_Burst():

    def upon_IMMEDIATE():
        Unknown4009(2)
    sprite('null', 1)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef_petal_burst', 0)

@State
def rrbHitPetal_Add():

    def upon_IMMEDIATE():
        Unknown4009(2)
    sprite('null', 1)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef_hit_petalB', 0)

@State
def rrbMuzzleEff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        Unknown4006(2)
        teleportRelativeX(-50000)
        Unknown1072(-90000)
    sprite('null', 12)
    GFX_2('rrbef_muzzle')
    GFX_0('rrbMuzzleEff2', 0)
    SFX_3('rrbse_02')

@State
def rrbMuzzleEff2():

    def upon_IMMEDIATE():
        Unknown4003('rrbef_muzzle01.DIG', '')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown3033()
        Unknown1056(4000)
        Unknown1064(5500)
        Unknown1099(150)
        Unknown3007(160)
        Unknown3013(210)
        Unknown23015(1)
    sprite('null', 6)
    sprite('null', 1)
    Unknown3001(180)
    sprite('null', 1)
    Unknown3001(128)

@State
def rrbMuzzleEff_B():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        Unknown4006(2)
        teleportRelativeX(-50000)
        Unknown1072(-90000)
        Unknown1096(900)
    sprite('null', 12)
    GFX_2('rrbef_muzzle')
    GFX_0('rrbMuzzleEff_B2', 0)
    GFX_0('rrbMuzzleEff_B3', 0)
    SFX_3('rrbse_02')

@State
def rrbMuzzleEff_B2():

    def upon_IMMEDIATE():
        Unknown4003('rrbef_muzzle01.DIG', '')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown3033()
        Unknown1056(4500)
        Unknown1064(4000)
        Unknown1099(150)
        Unknown3007(160)
        Unknown3013(210)
        Unknown23015(1)
    sprite('null', 6)
    sprite('null', 1)
    Unknown3001(180)
    sprite('null', 1)
    Unknown3001(128)

@State
def rrbMuzzleEff_B3():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown3033()
        Unknown23015(1)
        Unknown3000(0)
        Unknown4061(5)
        Unknown1064(1300)
        Unknown1056(1100)
        Unknown1067(-20)
        Unknown1059(20)
        Unknown1073(180000)
    sprite('vrrrbef_muzzle01', 4)
    sprite('vrrrbef_muzzle02', 1)
    sprite('vrrrbef_muzzle03', 1)
    sprite('vrrrbef_muzzle04', 2)
    Unknown1064(700)
    Unknown1059(5)
    sprite('vrrrbef_muzzle05', 2)

@State
def rrbMuzzleEff_C():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        Unknown4006(2)
        teleportRelativeX(-50000)
        Unknown1072(-90000)
    sprite('null', 12)
    Unknown4054(12)
    Unknown23067('rrbef_muzzle')
    GFX_0('rrbMuzzleEff_C2', 0)
    SFX_3('rrbse_02')

@State
def rrbMuzzleEff_C2():

    def upon_IMMEDIATE():
        Unknown4003('rrbef_muzzle01.DIG', '')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown3033()
        Unknown1056(4000)
        Unknown1064(5500)
        Unknown1099(150)
        Unknown3007(160)
        Unknown3013(210)
        Unknown23015(12)
    sprite('null', 6)
    sprite('null', 1)
    Unknown3001(180)
    sprite('null', 1)
    Unknown3001(128)

@State
def rrbBulletEff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        teleportRelativeX(150000)
        Unknown1007(0)
        Unknown2055(60)

        def upon_30():
            Unknown3001(0)
    sprite('null', 1)
    GFX_0('rrbef_bullet_head2', 0)
    GFX_0('rrbef_bullet_head', 0)
    GFX_0('rrbef_bullet_wind01', 0)
    GFX_0('rrbef_bullet_wind02', 0)
    GFX_0('rrbef_bullet_glow', 0)
    GFX_1('rrbef_bullet_dust', 0)
    sprite('null', 1)
    GFX_1('rrbef_bullet_dust', 0)
    label(0)
    sprite('null', 1)
    GFX_1('rrbef_bullet_dust', 0)
    sprite('null', 1)
    GFX_1('rrbef_bullet_dust', 0)
    GFX_1('rrbef_bullet_ring', 0)
    gotoLabel(0)

@State
def rrbef_bullet_head():

    def upon_IMMEDIATE():
        Unknown4003('rrbef_bullet.DIG', '')
        Unknown4007(2)
        Unknown4010(2)
        Unknown4025(2)
        Unknown53(1)
        Unknown3033()
        Unknown1096(8000)
        Unknown1064(12000)
        Unknown1072(180000)
        Unknown3007(180)
        Unknown3013(200)
    sprite('null', 1)
    Unknown1058(25)
    sprite('null', 59)
    Unknown1058(400)

@State
def rrbef_bullet_head2():

    def upon_IMMEDIATE():
        Unknown4003('rrbef_bullet_Normal.DIG', '')
        Unknown4007(2)
        Unknown4010(2)
        Unknown4025(2)
        Unknown53(1)
        Unknown3032()
        Unknown1096(8000)
        Unknown1064(12000)
        Unknown1072(180000)
        Unknown3007(60)
        Unknown3013(100)
    sprite('null', 1)
    Unknown1058(25)
    sprite('null', 59)
    Unknown1058(400)

@State
def rrbef_bullet_wind01():

    def upon_IMMEDIATE():
        Unknown4003('rrbef_bullet_wind', '')
        Unknown4007(2)
        Unknown4010(2)
        Unknown4025(2)
        Unknown53(1)
        Unknown1096(4000)
        Unknown1064(4000)
        Unknown3033()
        Unknown1072(180000)
        Unknown3003(50)
        Unknown3007(60)
        Unknown3013(100)
    sprite('null', 1)
    Unknown1058(25)
    sprite('null', 59)
    Unknown1058(400)

@State
def rrbef_bullet_wind02():

    def upon_IMMEDIATE():
        Unknown4003('rrbef_bullet_wind', '')
        Unknown4007(2)
        Unknown4010(2)
        Unknown4025(2)
        Unknown53(1)
        Unknown4009(3)
        Unknown3033()
        Unknown1096(6000)
        Unknown1064(3000)
        Unknown1072(180000)
        Unknown3003(50)
        Unknown3007(60)
        Unknown3013(100)
    sprite('null', 1)
    Unknown1058(25)
    sprite('null', 59)
    Unknown1058(400)

@State
def rrbef_bullet_glow():

    def upon_IMMEDIATE():
        Unknown4003('rrbef_glow.DIG', '')
        Unknown4007(2)
        Unknown4009(3)
        Unknown4010(2)
        Unknown4025(2)
        Unknown53(1)
        teleportRelativeX(-150000)
        Unknown1056(6000)
        Unknown1064(1800)
        Unknown1102(100, 0)
        Unknown3007(60)
        Unknown3013(100)
    sprite('null', 1)
    Unknown1058(25)
    sprite('null', 59)
    Unknown1058(400)

@State
def rrbBulletEff_Break():

    def upon_IMMEDIATE():
        Unknown4007(2)
        teleportRelativeX(200000)
        Unknown1007(0)
        Unknown2055(60)

        def upon_30():
            Unknown3001(0)
    sprite('null', 8)
    GFX_0('rrbef_bullet_head2_Break', 0)
    GFX_0('rrbef_bullet_head_Break', 0)
    GFX_0('rrbef_bullet_wind01_Break', 0)
    GFX_0('rrbef_bullet_wind02_Break', 0)
    GFX_0('rrbef_bullet_glow_Break', 0)

@State
def rrbef_bullet_head_Break():

    def upon_IMMEDIATE():
        Unknown4003('rrbef_bullet.DIG', '')
        Unknown4007(2)
        Unknown4025(2)
        Unknown53(1)
        Unknown3033()
        Unknown1056(8000)
        Unknown1064(12000)
        Unknown1072(180000)
        Unknown3007(180)
        Unknown3013(200)
    sprite('null', 6)
    Unknown1067(-1500)
    Unknown1059(-1000)

@State
def rrbef_bullet_head2_Break():

    def upon_IMMEDIATE():
        Unknown4003('rrbef_bullet_Normal.DIG', '')
        Unknown4007(2)
        Unknown4025(2)
        Unknown53(1)
        Unknown3032()
        Unknown1096(8000)
        Unknown1064(12000)
        Unknown1072(180000)
        Unknown3007(60)
        Unknown3013(100)
    sprite('null', 6)
    Unknown1067(-1500)
    Unknown1059(-1000)

@State
def rrbef_bullet_wind01_Break():

    def upon_IMMEDIATE():
        Unknown4003('rrbef_bullet_wind', '')
        Unknown4007(2)
        Unknown4025(2)
        Unknown53(1)
        Unknown1096(4000)
        Unknown1064(4000)
        Unknown3033()
        Unknown1072(180000)
        Unknown3003(50)
        Unknown3007(60)
        Unknown3013(100)

        def upon_3():
            Unknown3003(80)
    sprite('null', 8)
    Unknown1067(700)

@State
def rrbef_bullet_wind02_Break():

    def upon_IMMEDIATE():
        Unknown4003('rrbef_bullet_wind', '')
        Unknown4007(2)
        Unknown4025(2)
        Unknown53(1)
        Unknown4009(3)
        Unknown3033()
        Unknown1056(6000)
        Unknown1064(3000)
        Unknown1072(180000)
        Unknown3003(50)
        Unknown3007(60)
        Unknown3013(100)

        def upon_3():
            Unknown3003(80)
    sprite('null', 6)
    Unknown1067(600)

@State
def rrbef_bullet_glow_Break():

    def upon_IMMEDIATE():
        Unknown4003('rrbef_glow.DIG', '')
        Unknown4007(2)
        Unknown4009(3)
        Unknown4025(2)
        Unknown53(1)
        teleportRelativeX(-150000)
        Unknown1056(6000)
        Unknown1064(1800)
        Unknown1102(100, 0)
        Unknown3007(60)
        Unknown3013(100)

        def upon_3():
            Unknown3003(70)
    sprite('null', 6)

@State
def rrbBulletEffB():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        teleportRelativeX(150000)
        Unknown1007(0)
        Unknown2055(60)

        def upon_30():
            Unknown3001(0)
    sprite('null', 1)
    GFX_0('rrbef_bullet_head2B', 0)
    GFX_0('rrbef_bullet_headB', 0)
    GFX_0('rrbef_bullet_wind01B', 0)
    GFX_0('rrbef_bullet_wind02B', 0)
    GFX_0('rrbef_bullet_glowB', 0)
    GFX_1('rrbef_bullet_dust', 0)
    sprite('null', 1)
    GFX_1('rrbef_bullet_dust', 0)
    label(0)
    sprite('null', 1)
    GFX_1('rrbef_bullet_dust', 0)
    sprite('null', 1)
    GFX_1('rrbef_bullet_dust', 0)
    GFX_1('rrbef_bullet_ringB', 0)
    gotoLabel(0)

@State
def rrbef_bullet_headB():

    def upon_IMMEDIATE():
        Unknown4003('rrbef_bullet.DIG', '')
        Unknown4007(2)
        Unknown4010(2)
        Unknown4025(2)
        Unknown53(1)
        Unknown3033()
        Unknown1096(6000)
        Unknown1064(9000)
        Unknown1072(180000)
        Unknown3007(180)
        Unknown3013(200)
    sprite('null', 1)
    Unknown1058(25)
    sprite('null', 59)
    Unknown1058(400)

@State
def rrbef_bullet_head2B():

    def upon_IMMEDIATE():
        Unknown4003('rrbef_bullet_Normal.DIG', '')
        Unknown4007(2)
        Unknown4010(2)
        Unknown4025(2)
        Unknown53(1)
        Unknown3032()
        Unknown1096(6000)
        Unknown1064(9000)
        Unknown1072(180000)
        Unknown3007(60)
        Unknown3013(100)
    sprite('null', 1)
    Unknown1058(25)
    sprite('null', 59)
    Unknown1058(400)

@State
def rrbef_bullet_wind01B():

    def upon_IMMEDIATE():
        Unknown4003('rrbef_bullet_wind', '')
        Unknown4007(2)
        Unknown4010(2)
        Unknown4025(2)
        Unknown53(1)
        Unknown1096(3000)
        Unknown3033()
        Unknown1072(180000)
        Unknown3003(50)
        Unknown3007(60)
        Unknown3013(100)
    sprite('null', 1)
    Unknown1058(25)
    sprite('null', 59)
    Unknown1058(400)

@State
def rrbef_bullet_wind02B():

    def upon_IMMEDIATE():
        Unknown4003('rrbef_bullet_wind', '')
        Unknown4007(2)
        Unknown4011(3)
        Unknown4010(2)
        Unknown4025(2)
        Unknown53(1)
        Unknown4009(3)
        Unknown3033()
        Unknown1056(4500)
        Unknown1064(2250)
        Unknown1072(180000)
        Unknown3003(50)
        Unknown3007(60)
        Unknown3013(100)
    sprite('null', 1)
    Unknown1058(25)
    sprite('null', 59)
    Unknown1058(400)

@State
def rrbef_bullet_glowB():

    def upon_IMMEDIATE():
        Unknown4003('rrbef_glow.DIG', '')
        Unknown4007(2)
        Unknown4009(3)
        Unknown4011(3)
        Unknown4010(2)
        Unknown4025(2)
        Unknown53(1)
        teleportRelativeX(-150000)
        Unknown1056(4500)
        Unknown1064(1350)
        Unknown1102(100, 0)
        Unknown3007(60)
        Unknown3013(100)
    sprite('null', 1)
    Unknown1058(25)
    sprite('null', 59)
    Unknown1058(400)

@State
def rrbBulletEffB_Break():

    def upon_IMMEDIATE():
        Unknown4007(2)
        teleportRelativeX(200000)
        Unknown1007(0)
        Unknown2055(60)

        def upon_30():
            Unknown3001(0)
    sprite('null', 8)
    GFX_0('rrbef_bullet_head2B_Break', 0)
    GFX_0('rrbef_bullet_headB_Break', 0)
    GFX_0('rrbef_bullet_wind01B_Break', 0)
    GFX_0('rrbef_bullet_wind02B_Break', 0)
    GFX_0('rrbef_bullet_glowB_Break', 0)

@State
def rrbef_bullet_headB_Break():

    def upon_IMMEDIATE():
        Unknown4003('rrbef_bullet.DIG', '')
        Unknown4007(2)
        Unknown4025(2)
        Unknown53(1)
        Unknown3033()
        Unknown1056(6000)
        Unknown1064(9000)
        Unknown1072(180000)
        Unknown3007(180)
        Unknown3013(200)
    sprite('null', 6)
    Unknown1059(-750)
    Unknown1067(-1125)

@State
def rrbef_bullet_head2B_Break():

    def upon_IMMEDIATE():
        Unknown4003('rrbef_bullet_Normal.DIG', '')
        Unknown4007(2)
        Unknown4025(2)
        Unknown53(1)
        Unknown3032()
        Unknown1096(6000)
        Unknown1064(9000)
        Unknown1072(180000)
        Unknown3007(60)
        Unknown3013(100)
    sprite('null', 6)
    Unknown1059(-750)
    Unknown1067(-1125)

@State
def rrbef_bullet_wind01B_Break():

    def upon_IMMEDIATE():
        Unknown4003('rrbef_bullet_wind', '')
        Unknown4007(2)
        Unknown4025(2)
        Unknown53(1)
        Unknown1096(3000)
        Unknown1064(3000)
        Unknown3033()
        Unknown1072(180000)
        Unknown3003(50)
        Unknown3007(60)
        Unknown3013(100)

        def upon_3():
            Unknown3003(80)
    sprite('null', 8)
    Unknown1067(500)

@State
def rrbef_bullet_wind02B_Break():

    def upon_IMMEDIATE():
        Unknown4003('rrbef_bullet_wind', '')
        Unknown4007(2)
        Unknown4025(2)
        Unknown53(1)
        Unknown4009(3)
        Unknown3033()
        Unknown1056(4500)
        Unknown1064(2250)
        Unknown1072(180000)
        Unknown3003(50)
        Unknown3007(60)
        Unknown3013(100)

        def upon_3():
            Unknown3003(80)
    sprite('null', 6)
    Unknown1067(450)

@State
def rrbef_bullet_glowB_Break():

    def upon_IMMEDIATE():
        Unknown4003('rrbef_glow.DIG', '')
        Unknown4007(2)
        Unknown4009(3)
        Unknown4025(2)
        Unknown53(1)
        teleportRelativeX(-150000)
        Unknown1056(4500)
        Unknown1064(1350)
        Unknown1102(100, 0)
        Unknown3007(60)
        Unknown3013(100)

        def upon_3():
            Unknown3003(70)
    sprite('null', 6)

@State
def rrbCaseEff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown1056(900)
        Unknown1064(800)
    sprite('null', 60)
    GFX_2('rrbef_case')

@State
def rrbCaseEffB():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown1056(900)
        Unknown1064(800)
    sprite('null', 60)
    GFX_2('rrbef_caseB')

@State
def rrbCaseEffC():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown1056(900)
        Unknown1064(800)
    sprite('null', 60)
    Unknown4054(12)
    Unknown23067('rrbef_caseC')

@State
def rrbCaseEffD():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown1056(900)
        Unknown1064(800)
    sprite('null', 60)
    Unknown4054(12)
    Unknown23067('rrbef_caseD')

@State
def rrbGroundEff():

    def upon_IMMEDIATE():
        Unknown1064(700)
        teleportRelativeX(180000)
        teleportRelativeY(-18000)
        Unknown3033()
        Unknown3000(0)
        Unknown4061(5)
        Unknown23015(1)
    sprite('vrrrbef_ground01', 2)
    sprite('vrrrbef_ground02', 2)
    sprite('vrrrbef_ground03', 2)
    sprite('vrrrbef_ground04', 2)
    Unknown3004(-42)
    sprite('vrrrbef_ground05', 2)

@State
def rrb201Eff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(15000)
        Unknown1007(240000)
    sprite('null', 10)
    GFX_0('rrb201Eff_2', 0)
    GFX_0('rrb201Eff_1', 0)
    GFX_0('rrb201Eff_3', 0)

@State
def rrb201Eff_1():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp01')
        Unknown4003('rrbef201_1.DIG', '')
        Unknown1096(3800)
    sprite('null', 10)

@State
def rrb201Eff_2():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp02')
        Unknown4003('rrbef201_2.DIG', '')
        Unknown1096(3800)
    sprite('null', 10)

@State
def rrb201Eff_3():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp03')
        Unknown4003('rrbef201_3.DIG', '')
        Unknown1096(4200)
        Unknown1099(20)
        Unknown3001(90)
        Unknown3004(-11)
    sprite('null', 12)

@State
def rrb202Eff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(-15000)
        Unknown1007(230000)
    sprite('null', 10)
    GFX_0('rrb202Eff_2', 0)
    GFX_0('rrb202Eff_1', 0)
    GFX_0('rrb202Eff_3', 0)

@State
def rrb202Eff_1():

    def upon_IMMEDIATE():
        Unknown4003('rrbef202_1.DIG', '')
        callSubroutine('NormalArts_Temp01')
        Unknown1096(3800)
    sprite('null', 14)

@State
def rrb202Eff_2():

    def upon_IMMEDIATE():
        Unknown4003('rrbef202_2.DIG', '')
        callSubroutine('NormalArts_Temp02')
        Unknown1096(3800)
    sprite('null', 14)

@State
def rrb202Eff_3():

    def upon_IMMEDIATE():
        Unknown4003('rrbef202_3.DIG', '')
        callSubroutine('NormalArts_Temp03')
        Unknown1096(4150)
        Unknown3001(90)
        Unknown3004(-10)
    sprite('null', 12)

@State
def rrb203Eff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(0)
        Unknown1007(305000)
        Unknown1096(3700)
    sprite('null', 10)
    GFX_0('rrb203Eff_2', 0)
    GFX_0('rrb203Eff_1', 0)
    GFX_0('rrb203Eff_3', 0)

@State
def rrb203Eff_1():

    def upon_IMMEDIATE():
        Unknown4003('rrbef203_1.DIG', '')
        callSubroutine('NormalArts_Temp01')
        Unknown4013(2)
    sprite('null', 10)

@State
def rrb203Eff_2():

    def upon_IMMEDIATE():
        Unknown4003('rrbef203_2.DIG', '')
        callSubroutine('NormalArts_Temp02')
        Unknown4013(2)
    sprite('null', 10)

@State
def rrb203Eff_3():

    def upon_IMMEDIATE():
        Unknown4003('rrbef203_3.DIG', '')
        callSubroutine('NormalArts_Temp03')
        Unknown4013(2)
        Unknown3001(90)
        Unknown3004(-10)
    sprite('null', 8)

@State
def rrb231Eff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(-35000)
        Unknown1007(165000)
    sprite('null', 50)
    GFX_0('rrb231Eff_2', 0)
    GFX_0('rrb231Eff_1', 0)
    GFX_0('rrb231Eff_3', 0)

@State
def rrb231Eff_1():

    def upon_IMMEDIATE():
        Unknown4003('rrbef231_1.DIG', '')
        callSubroutine('NormalArts_Temp01')
        Unknown1096(3700)
    sprite('null', 12)

@State
def rrb231Eff_2():

    def upon_IMMEDIATE():
        Unknown4003('rrbef231_2.DIG', '')
        callSubroutine('NormalArts_Temp02')
        Unknown1096(3700)
    sprite('null', 12)

@State
def rrb231Eff_3():

    def upon_IMMEDIATE():
        Unknown4003('rrbef231_3.DIG', '')
        callSubroutine('NormalArts_Temp03')
        Unknown1096(4100)
        Unknown3001(90)
        Unknown3004(-10)
    sprite('null', 12)

@State
def rrb232Eff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(0)
        Unknown1007(80000)
    sprite('null', 50)
    GFX_0('rrb232Eff_2', 0)
    GFX_0('rrb232Eff_1', 0)
    GFX_0('rrb232Eff_3', 0)

@State
def rrb232Eff_1():

    def upon_IMMEDIATE():
        Unknown4003('rrbef232_1.DIG', '')
        callSubroutine('NormalArts_Temp01')
        Unknown1096(3700)
    sprite('null', 16)

@State
def rrb232Eff_2():

    def upon_IMMEDIATE():
        Unknown4003('rrbef232_2.DIG', '')
        callSubroutine('NormalArts_Temp02')
        Unknown1096(3700)
    sprite('null', 16)

@State
def rrb232Eff_3():

    def upon_IMMEDIATE():
        Unknown4003('rrbef232_3.DIG', '')
        callSubroutine('NormalArts_Temp03')
        Unknown1096(3700)
        Unknown3001(90)
        Unknown3004(-10)
    sprite('null', 16)

@State
def rrb251Eff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(0)
        Unknown1007(280000)
    sprite('null', 50)
    GFX_0('rrb251Eff_2', 0)
    GFX_0('rrb251Eff_1', 0)
    GFX_0('rrb251Eff_3', 0)

@State
def rrb251Eff_1():

    def upon_IMMEDIATE():
        Unknown4003('rrbef251_1.DIG', '')
        callSubroutine('NormalArts_Temp01')
        Unknown1096(3600)
    sprite('null', 8)

@State
def rrb251Eff_2():

    def upon_IMMEDIATE():
        Unknown4003('rrbef251_2.DIG', '')
        callSubroutine('NormalArts_Temp02')
        Unknown1096(3600)
    sprite('null', 8)

@State
def rrb251Eff_3():

    def upon_IMMEDIATE():
        Unknown4003('rrbef251_3.DIG', '')
        callSubroutine('NormalArts_Temp03')
        Unknown1096(4000)
        Unknown3001(90)
        Unknown3004(-10)
    sprite('null', 10)

@State
def rrb252Eff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(0)
        Unknown1007(270000)
    sprite('null', 50)
    GFX_0('rrb252Eff_2', 0)
    GFX_0('rrb252Eff_1', 0)
    GFX_0('rrb252Eff_3', 0)

@State
def rrb252Eff_1():

    def upon_IMMEDIATE():
        Unknown4003('rrbef252_1.DIG', '')
        callSubroutine('NormalArts_Temp01')
        Unknown1096(3700)
    sprite('null', 10)

@State
def rrb252Eff_2():

    def upon_IMMEDIATE():
        Unknown4003('rrbef252_2.DIG', '')
        callSubroutine('NormalArts_Temp02')
        Unknown1096(3700)
    sprite('null', 10)

@State
def rrb252Eff_3():

    def upon_IMMEDIATE():
        Unknown4003('rrbef252_3.DIG', '')
        callSubroutine('NormalArts_Temp03')
        Unknown1096(4100)
        Unknown3001(90)
        Unknown3004(-10)
    sprite('null', 10)

@State
def rrb270Eff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(7000)
        Unknown1007(245000)
    sprite('null', 9)
    GFX_0('rrb270Eff_1', 0)
    GFX_0('rrb270Eff_2', 0)
    GFX_0('rrb270Eff_3', 0)

@State
def rrb270Eff_1():

    def upon_IMMEDIATE():
        Unknown4003('rrbef270_1.DIG', '')
        callSubroutine('NormalArts_Temp01')
        Unknown1096(3800)
    sprite('null', 9)

@State
def rrb270Eff_2():

    def upon_IMMEDIATE():
        Unknown4003('rrbef270_2.DIG', '')
        callSubroutine('NormalArts_Temp02')
        Unknown1096(3800)
    sprite('null', 9)

@State
def rrb270Eff_3():

    def upon_IMMEDIATE():
        Unknown4003('rrbef270_3.DIG', '')
        callSubroutine('NormalArts_Temp03')
        Unknown1096(3900)
        Unknown3001(90)
    sprite('null', 9)

@State
def rrb271Eff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(-100000)
        Unknown1007(15000)
    sprite('null', 4)
    GFX_0('rrb271Eff_1', 0)
    GFX_0('rrb271Eff_2', 0)
    GFX_0('rrb271Eff_3', 0)
    sprite('null', 14)
    GFX_0('rrb271GroundEff', 0)

@State
def rrb271Eff_1():

    def upon_IMMEDIATE():
        Unknown4003('rrbef271_1.DIG', '')
        callSubroutine('NormalArts_Temp01')
        Unknown1096(3700)
    sprite('null', 14)

@State
def rrb271Eff_2():

    def upon_IMMEDIATE():
        Unknown4003('rrbef271_2.DIG', '')
        callSubroutine('NormalArts_Temp02')
        Unknown1096(3700)
    sprite('null', 14)

@State
def rrb271Eff_3():

    def upon_IMMEDIATE():
        Unknown4003('rrbef271_3.DIG', '')
        callSubroutine('NormalArts_Temp03')
        Unknown1096(3700)
        Unknown3001(90)
    sprite('null', 14)

@State
def rrb271GroundEff():

    def upon_IMMEDIATE():
        teleportRelativeX(360000)
        teleportRelativeY(0)
    sprite('null', 2)
    Unknown8003(100, 1, 1)

@State
def rrb311Eff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        Unknown4009(0)
        teleportRelativeX(2000)
        Unknown1007(270000)
    sprite('null', 26)
    GFX_0('rrb311Eff_2', 0)
    GFX_0('rrb311Eff_1', 0)
    GFX_0('rrb311Eff_3', 0)
    GFX_0('rrb311MuzzleEff', 0)
    Unknown35()

@State
def rrb311Eff_1():

    def upon_IMMEDIATE():
        Unknown4003('rrbef311_1.DIG', '')
        callSubroutine('NormalArts_Temp01')
        Unknown1096(3800)
    sprite('null', 17)

@State
def rrb311Eff_2():

    def upon_IMMEDIATE():
        Unknown4003('rrbef311_2.DIG', '')
        callSubroutine('NormalArts_Temp02')
        Unknown1096(3800)
    sprite('null', 17)

@State
def rrb311Eff_3():

    def upon_IMMEDIATE():
        Unknown4003('rrbef311_3.DIG', '')
        callSubroutine('NormalArts_Temp03')
        Unknown1096(4200)
        Unknown3001(90)
    sprite('null', 7)
    sprite('null', 9)
    Unknown3004(-10)

@State
def rrb311MuzzleEff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        teleportRelativeX(300000)
        Unknown1007(25000)
        Unknown1073(60000)
    sprite('null', 20)
    GFX_0('rrbMuzzleEff_B', 0)

@State
def rrb311EndEff():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4010(3)
        Unknown4011(3)
        Unknown1000(-65000)
        teleportRelativeY(285000)
        Unknown4061(6)
        Unknown21004(1)
        Unknown1096(2470)
    sprite('null', 2)
    Unknown4003('rrbef601_02.DIG', '')
    sprite('null', 2)
    Unknown4003('rrbef601_03.DIG', '')
    sprite('null', 2)
    Unknown4003('rrbef601_04.DIG', '')
    sprite('null', 2)
    Unknown4003('rrbef601_05.DIG', '')
    sprite('null', 2)
    Unknown4003('rrbef601_06.DIG', '')
    sprite('null', 2)
    Unknown4003('rrbef601_07.DIG', '')
    sprite('null', 2)
    Unknown4003('rrbef601_08.DIG', '')
    sprite('null', 2)
    Unknown4003('rrbef601_09.DIG', '')

@State
def rrb312Eff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(10000)
        Unknown1007(260000)
        Unknown1096(3800)
    sprite('null', 11)
    GFX_0('rrb312Eff_2', 0)
    GFX_0('rrb312Eff_1', 0)
    GFX_0('rrb312Eff_3', 0)

@State
def rrb312Eff_1():

    def upon_IMMEDIATE():
        Unknown4003('rrbef312_1.DIG', '')
        callSubroutine('NormalArts_Temp01')
        Unknown4013(2)
    sprite('null', 11)

@State
def rrb312Eff_2():

    def upon_IMMEDIATE():
        Unknown4003('rrbef312_2.DIG', '')
        callSubroutine('NormalArts_Temp02')
        Unknown4013(2)
    sprite('null', 11)

@State
def rrb312Eff_3():

    def upon_IMMEDIATE():
        Unknown4003('rrbef312_3.DIG', '')
        callSubroutine('NormalArts_Temp03')
        Unknown4013(2)
        Unknown3001(90)
        Unknown3004(-5)
    sprite('null', 8)

@State
def rrb312MuzzleEff():

    def upon_IMMEDIATE():
        teleportRelativeX(-170000)
        Unknown1007(-170000)
        Unknown1072(-140000)
    sprite('null', 20)
    GFX_0('rrbMuzzleEff_B', 0)

@State
def rrb400MuzzleEff():

    def upon_IMMEDIATE():
        teleportRelativeX(-180000)
        Unknown1007(200000)
        Unknown1072(-100000)
    sprite('null', 20)
    GFX_0('rrbMuzzleEff', 0)

@State
def rrb400PetalEff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown1007(170000)
        Unknown2055(30)
        sendToLabelUpon(32, 1)
    sprite('null', 2)
    sprite('null', 1)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef_move_petal', 0)
    sprite('null', 1)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef_move_petal', 0)
    label(0)
    sprite('null', 1)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef_move_petal', 0)
    Unknown4045('rrbef_speed', 0)
    gotoLabel(0)
    label(1)
    sprite('null', 3)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef_move_petal_end', 0)
    sprite('null', 3)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef_move_petal', 0)

@State
def rrb400AirPetalEff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        Unknown4011(3)
        Unknown4010(3)
        teleportRelativeX(10000)
        Unknown1007(180000)
        Unknown2055(30)
        sendToLabelUpon(32, 1)
    sprite('null', 2)
    label(0)
    sprite('null', 1)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef_move_petal', 0)
    gotoLabel(0)
    label(1)
    sprite('null', 3)
    Unknown4048(90000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef_move_petal', 0)
    sprite('null', 3)
    Unknown4048(90000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef_move_petal', 0)
    sprite('null', 3)
    Unknown4048(90000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef_move_petal', 0)

@State
def rrb401MuzzleEff():

    def upon_IMMEDIATE():
        teleportRelativeX(250000)
        Unknown1007(220000)
        Unknown1072(90000)
    sprite('null', 20)
    GFX_0('rrbMuzzleEff', 0)

@State
def rrb401PetalEff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown2055(30)
        Unknown1007(30000)
        Unknown1007(150000)
        sendToLabelUpon(32, 1)
    sprite('null', 2)
    sprite('null', 1)
    Unknown4051(0)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef_move_petal', 0)
    sprite('null', 1)
    Unknown4051(0)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef_move_petal', 0)
    label(0)
    sprite('null', 1)
    Unknown4051(0)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef_move_petal', 0)
    Unknown4051(0)
    Unknown4045('rrbef_speed', 0)
    sprite('null', 1)
    Unknown4051(0)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef_move_petal', 0)
    Unknown4051(0)
    Unknown4045('rrbef_speed', 0)
    sprite('null', 1)
    Unknown4051(0)
    Unknown4045('rrbef_speed', 0)
    gotoLabel(0)
    label(1)
    sprite('null', 3)
    Unknown4051(0)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef_move_petal', 0)
    sprite('null', 3)
    Unknown4051(0)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef_move_petal', 0)
    sprite('null', 3)
    Unknown4051(0)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef_move_petal', 0)

@State
def rrb402MuzzleEff():

    def upon_IMMEDIATE():
        teleportRelativeX(-120000)
        Unknown1007(35000)
        Unknown1072(-140000)
    sprite('null', 20)
    GFX_0('rrbMuzzleEff', 0)

@State
def rrb402PetalEff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown2055(30)
        Unknown1000(20000)
        teleportRelativeY(180000)
        sendToLabelUpon(32, 1)
    sprite('null', 2)
    label(0)
    sprite('null', 1)
    Unknown4048(-10000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef_move_petal', 0)
    Unknown4048(-37000)
    Unknown4045('rrbef_speed', 0)
    gotoLabel(0)
    label(1)
    sprite('null', 3)
    Unknown4048(90000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef_move_petal', 0)
    sprite('null', 3)
    Unknown4048(90000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef_move_petal', 0)
    sprite('null', 3)
    Unknown4048(90000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef_move_petal', 0)
    sprite('null', 20)

@State
def rrb403MuzzleEff():

    def upon_IMMEDIATE():
        teleportRelativeX(-160000)
        Unknown1007(380000)
        Unknown1072(-60000)
    sprite('null', 20)
    GFX_0('rrbMuzzleEff', 0)

@State
def rrb403PetalEff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown2055(60)
        Unknown1000(-40000)
        teleportRelativeY(180000)
        sendToLabelUpon(32, 1)
    sprite('null', 2)
    label(0)
    sprite('null', 1)
    Unknown4048(20000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef_move_petal', 0)
    Unknown4048(40000)
    Unknown4045('rrbef_speed', 0)
    gotoLabel(0)
    label(1)
    sprite('null', 3)
    Unknown4048(90000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef_move_petal', 0)
    sprite('null', 3)
    Unknown4048(90000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef_move_petal', 0)
    sprite('null', 3)
    Unknown4048(90000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef_move_petal', 0)
    sprite('null', 20)

@State
def rrb404Eff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(-5000)
        Unknown1007(265000)
    sprite('null', 6)
    GFX_0('rrb404Eff_2', 0)
    GFX_0('rrb404Eff_1', 0)
    GFX_0('rrb404Eff_3', 0)
    GFX_0('rrb404Eff_4', 0)
    sprite('null', 20)
    GFX_0('rrbGroundEff', 0)

@State
def rrb404Eff_1():

    def upon_IMMEDIATE():
        Unknown4003('rrbef404_1.DIG', '')
        callSubroutine('NormalArts_Temp01')
        Unknown1096(3700)
    sprite('null', 14)

@State
def rrb404Eff_2():

    def upon_IMMEDIATE():
        Unknown4003('rrbef404_2.DIG', '')
        callSubroutine('NormalArts_Temp02')
        Unknown1096(3700)
    sprite('null', 14)

@State
def rrb404Eff_3():

    def upon_IMMEDIATE():
        Unknown4003('rrbef404_3.DIG', '')
        callSubroutine('NormalArts_Temp03')
        Unknown1096(3700)
        Unknown3001(90)
    sprite('null', 6)
    sprite('null', 9)
    Unknown3004(-10)

@State
def rrb404Eff_4():

    def upon_IMMEDIATE():
        Unknown4003('rrbef404_4.DIG', '')
        callSubroutine('NormalArts_Temp')
        Unknown3033()
        Unknown1096(3700)
    sprite('null', 14)

@State
def rrb404EndEff():

    def upon_IMMEDIATE():
        Unknown4003('rrbef404_end.DIG', '')
        callSubroutine('NormalArts_Temp01')
        teleportRelativeX(-40000)
        Unknown1007(270000)
        Unknown1096(2200)
    sprite('null', 12)

@State
def rrb404MuzzleEff():

    def upon_IMMEDIATE():
        teleportRelativeX(145000)
        Unknown1007(5000)
        Unknown1072(90000)
    sprite('null', 20)
    GFX_0('rrbMuzzleEff', 0)
    GFX_0('rrb404Smoke', 0)

@State
def rrb404MuzzleEff_B():

    def upon_IMMEDIATE():
        teleportRelativeX(145000)
        Unknown1007(5000)
        Unknown1072(92000)
    sprite('null', 20)
    GFX_0('rrbMuzzleEff_B', 0)
    GFX_0('rrb404Smoke', 0)

@State
def rrb404Smoke():

    def upon_IMMEDIATE():
        callSubroutine('CommonSmoke')
        teleportRelativeY(-10000)
        Unknown1096(500)
        Unknown1064(400)
        Unknown1099(20)
        physicsXImpulse(-5000)
    sprite('vrrrbef_smokeb01', 2)
    sprite('vrrrbef_smokeb02', 2)
    sprite('vrrrbef_smokeb03', 2)
    sprite('vrrrbef_smokeb04', 3)
    sprite('vrrrbef_smokeb05', 3)
    Unknown3004(-28)
    sprite('vrrrbef_smokeb06', 3)
    sprite('vrrrbef_smokeb07', 3)

@State
def rrb405Eff():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)
    sprite('null', 2)
    GFX_0('rrb405_Particle', 0)
    GFX_0('rrb405_Smoke', 0)
    GFX_0('rrb405MuzzleEff', 0)

    def upon_IMMEDIATE():
        teleportRelativeX(-160000)
        Unknown1007(380000)
        Unknown1072(-60000)
    sprite('null', 20)
    sprite('null', 14)
    GFX_0('rrb405_Ani', 0)
    endState()

@State
def rrb405_Ani():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4011(3)
        Unknown4061(0)
        teleportRelativeX(100000)
        Unknown3032()
    sprite('vrrrbef405_01', 2)
    sprite('vrrrbef405_02', 2)
    sprite('vrrrbef405_03', 2)

@State
def rrb405_Particle():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown4011(3)
        Unknown2055(17)
        Unknown1007(200000)
    label(0)
    sprite('null', 1)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef_move_petal', 0)
    Unknown4045('rrbef_speed', 0)
    gotoLabel(0)

@State
def rrb405_Smoke():

    def upon_IMMEDIATE():
        teleportRelativeX(200000)
        Unknown4010(3)
        Unknown4011(3)
    sprite('null', 1)
    GFX_0('rrb405_RingSmokeB', 0)
    GFX_0('rrb405_DashSmoke', 0)
    sprite('null', 1)
    GFX_0('rrb405_RingSmokeA2', 0)
    sprite('null', 1)
    GFX_0('rrb405_RingSmokeA', 0)
    sprite('null', 1)
    GFX_0('rrb405_RingSmokeC', 0)
    sprite('null', 1)
    GFX_0('rrb405_RingSmokeB2', 0)

@State
def rrb405_DashSmoke():

    def upon_IMMEDIATE():
        callSubroutine('CommonSmoke')
        Unknown1096(400)
        Unknown1064(300)
        Unknown1099(15)
        teleportRelativeX(-100000)
        physicsXImpulse(-5000)
    sprite('vrrrbef_smoke01', 3)
    sprite('vrrrbef_smoke02', 3)
    sprite('vrrrbef_smoke03', 3)
    sprite('vrrrbef_smoke04', 3)
    sprite('vrrrbef_smoke05', 3)
    sprite('vrrrbef_smoke06', 3)

@State
def rrb405_RingSmokeA():

    def upon_IMMEDIATE():
        callSubroutine('CommonSmoke')
    sprite('vrrrbef_ringsmokea01', 1)
    Unknown1096(700)
    sprite('vrrrbef_ringsmokea01', 2)
    Unknown1096(780)
    Unknown1099(25)
    sprite('vrrrbef_ringsmokea02', 3)
    sprite('vrrrbef_ringsmokea03', 3)
    sprite('vrrrbef_ringsmokea04', 3)

@State
def rrb405_RingSmokeA2():

    def upon_IMMEDIATE():
        callSubroutine('CommonSmoke')
        teleportRelativeX(-180000)
        physicsXImpulse(-3000)
    sprite('vrrrbef_ringsmokea01', 1)
    Unknown1096(500)
    sprite('vrrrbef_ringsmokea01', 3)
    Unknown1096(600)
    Unknown1099(10)
    sprite('vrrrbef_ringsmokea02', 4)
    sprite('vrrrbef_ringsmokea03', 4)
    sprite('vrrrbef_ringsmokea04', 4)

@State
def rrb405_RingSmokeB():

    def upon_IMMEDIATE():
        callSubroutine('CommonSmoke')
        teleportRelativeX(-250000)
        physicsXImpulse(-5000)
    sprite('vrrrbef_ringsmokeb01', 1)
    Unknown1096(500)
    sprite('vrrrbef_ringsmokeb01', 2)
    Unknown1096(600)
    Unknown1099(15)
    sprite('vrrrbef_ringsmokeb02', 3)
    sprite('vrrrbef_ringsmokeb03', 3)
    sprite('vrrrbef_ringsmokeb04', 3)

@State
def rrb405_RingSmokeB2():

    def upon_IMMEDIATE():
        callSubroutine('CommonSmoke')
        teleportRelativeX(100000)
    sprite('vrrrbef_ringsmokeb01', 1)
    Unknown1096(450)
    sprite('vrrrbef_ringsmokeb01', 2)
    Unknown1096(550)
    Unknown1099(5)
    sprite('vrrrbef_ringsmokeb02', 3)
    sprite('vrrrbef_ringsmokeb03', 3)
    sprite('vrrrbef_ringsmokeb04', 3)

@State
def rrb405_RingSmokeC():

    def upon_IMMEDIATE():
        callSubroutine('CommonSmoke')
        Unknown1096(700)
        teleportRelativeX(100000)
    sprite('vrrrbef_ringsmokec01', 1)
    Unknown1096(600)
    sprite('vrrrbef_ringsmokec01', 3)
    Unknown1096(700)
    Unknown1099(10)
    sprite('vrrrbef_ringsmokec02', 4)
    sprite('vrrrbef_ringsmokec03', 4)
    sprite('vrrrbef_ringsmokec04', 4)

@State
def rrb405_Particle():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown4011(3)
        Unknown2055(17)
        Unknown1007(200000)
    label(0)
    sprite('null', 1)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef_move_petal', 0)
    Unknown4045('rrbef_speed', 0)
    gotoLabel(0)

@State
def rrb405MuzzleEff():

    def upon_IMMEDIATE():
        teleportRelativeX(-200000)
        Unknown1007(160000)
        Unknown1072(-90000)
    sprite('null', 20)
    GFX_0('rrbMuzzleEff_B', 0)

@State
def rrb405_Issen():

    def upon_IMMEDIATE():
        Unknown4009(3)
        Unknown6001(1)

        def upon_16():
            Unknown23032(50)
    sprite('null', 40)
    GFX_0('rrb405_Issen01', 0)
    GFX_0('rrb405_Issen02', 0)

@State
def rrb405_Issen01():

    def upon_IMMEDIATE():
        Unknown4022(2)
        Unknown1007(200000)
        Unknown4061(6)
    sprite('null', 1)
    Unknown4047(1, 1, 1)
    Unknown23067('rrbef405_issen')
    teleportRelativeX(-800000)
    Unknown3001(255)
    Unknown1064(3000)
    sprite('null', 1)
    teleportRelativeX(800000)
    Unknown1064(3500)
    sprite('null', 1)
    teleportRelativeX(400000)
    Unknown1056(1300)
    Unknown1064(4000)
    sprite('null', 2)
    Unknown1064(3000)
    sprite('null', 3)
    Unknown1067(-800)
    sprite('null', 3)
    Unknown1067(-100)
    sprite('null', 5)
    Unknown1067(-40)
    sprite('null', 1)
    Unknown1067(-10)
    sprite('null', 1)
    Unknown1064(100)
    Unknown1067(-1)
    sprite('null', 2)
    Unknown3001(0)
    sprite('null', 2)
    Unknown3001(255)
    sprite('null', 1)
    Unknown3001(0)
    sprite('null', 1)
    Unknown3001(255)
    sprite('null', 2)
    Unknown3001(0)
    sprite('null', 2)
    Unknown3001(255)
    sprite('null', 2)
    Unknown3001(0)
    sprite('null', 1)
    Unknown3001(255)
    sprite('null', 2)
    Unknown3001(0)
    sprite('null', 1)
    Unknown3001(255)
    sprite('null', 2)
    Unknown3001(0)
    sprite('null', 1)
    Unknown3001(255)

@State
def rrb405_Issen02():

    def upon_IMMEDIATE():
        Unknown4022(2)
        Unknown4061(6)
        Unknown1007(200000)
    sprite('null', 1)
    Unknown4047(17, 1, 1)
    Unknown23067('rrbef405_issenB')
    teleportRelativeX(-800000)
    Unknown3001(255)
    Unknown1064(3000)
    sprite('null', 1)
    teleportRelativeX(800000)
    Unknown1064(3500)
    sprite('null', 1)
    teleportRelativeX(400000)
    Unknown1056(1300)
    Unknown1064(4000)
    sprite('null', 2)
    Unknown1064(3000)
    sprite('null', 3)
    Unknown1067(-800)
    sprite('null', 3)
    Unknown1067(-100)
    sprite('null', 5)
    Unknown1067(-40)
    sprite('null', 1)
    Unknown1067(-10)
    sprite('null', 1)
    Unknown1064(100)
    Unknown1067(-1)
    sprite('null', 2)
    Unknown3001(0)
    sprite('null', 2)
    Unknown3001(255)
    sprite('null', 1)
    Unknown3001(0)
    sprite('null', 1)
    Unknown3001(255)
    sprite('null', 2)
    Unknown3001(0)
    sprite('null', 2)
    Unknown3001(255)
    sprite('null', 2)
    Unknown3001(0)
    sprite('null', 1)
    Unknown3001(255)
    sprite('null', 2)
    Unknown3001(0)
    sprite('null', 1)
    Unknown3001(255)
    sprite('null', 2)
    Unknown3001(0)
    sprite('null', 1)
    Unknown3001(255)

@State
def rrb406aEff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(30000)
        Unknown1007(220000)
        Unknown1096(3900)
        sendToLabelUpon(32, 1)
    sprite('null', 10)
    GFX_0('rrb406aEff_2', 0)
    GFX_0('rrb406aEff_1', 0)
    GFX_0('rrb406aEff_4', 0)
    GFX_0('rrb406aEff_3', 0)

@State
def rrb406aEff_1():

    def upon_IMMEDIATE():
        Unknown4003('rrbef406a_1.DIG', '')
        callSubroutine('NormalArts_Temp01')
        Unknown4013(2)
    sprite('null', 10)

@State
def rrb406aEff_2():

    def upon_IMMEDIATE():
        Unknown4003('rrbef406a_2.DIG', '')
        callSubroutine('NormalArts_Temp02')
        Unknown4013(2)
    sprite('null', 10)

@State
def rrb406aEff_3():

    def upon_IMMEDIATE():
        Unknown4003('rrbef406a_3.DIG', '')
        callSubroutine('NormalArts_Temp03')
        Unknown4013(2)
        Unknown3001(90)
    sprite('null', 2)
    sprite('null', 8)
    Unknown3004(-5)

@State
def rrb406aEff_4():

    def upon_IMMEDIATE():
        Unknown4003('rrbef406a_4.DIG', '')
        callSubroutine('NormalArts_Temp')
        Unknown3033()
        Unknown4013(2)
    sprite('null', 10)

@State
def rrb406bEff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(40000)
        Unknown1007(220000)
        Unknown1096(3700)
        Unknown1072(0)
    sprite('null', 10)
    GFX_0('rrb406bEff_2', 0)
    GFX_0('rrb406bEff_1', 0)
    GFX_0('rrb406bEff_4', 0)
    GFX_0('rrb406bEff_3', 0)

@State
def rrb406bEff_1():

    def upon_IMMEDIATE():
        Unknown4003('rrbef406b_1.DIG', '')
        callSubroutine('NormalArts_Temp01')
        Unknown4013(2)
    sprite('null', 10)

@State
def rrb406bEff_2():

    def upon_IMMEDIATE():
        Unknown4003('rrbef406b_2.DIG', '')
        callSubroutine('NormalArts_Temp02')
        Unknown4013(2)
    sprite('null', 10)

@State
def rrb406bEff_3():

    def upon_IMMEDIATE():
        Unknown4003('rrbef406b_3.DIG', '')
        callSubroutine('NormalArts_Temp03')
        Unknown4013(2)
        Unknown3001(70)
    sprite('null', 10)

@State
def rrb406bEff_4():

    def upon_IMMEDIATE():
        Unknown4003('rrbef406b_4.DIG', '')
        callSubroutine('NormalArts_Temp')
        Unknown3033()
        Unknown4013(2)
        Unknown4006(2)
    sprite('null', 10)

@State
def rrb406cEff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        Unknown4007(0)
        Unknown4022(3)
        teleportRelativeX(-250000)
        Unknown1007(-20000)
        Unknown1096(4200)
    sprite('null', 10)
    GFX_0('rrb406cEff_2', 0)
    GFX_0('rrb406cEff_1', 0)
    GFX_0('rrb406cEff_4', 0)
    GFX_0('rrb406cEff_3', 0)

@State
def rrb406cEff_1():

    def upon_IMMEDIATE():
        Unknown4003('rrbef406c_1.DIG', '')
        callSubroutine('NormalArts_Temp01')
        Unknown4013(2)
    sprite('null', 10)

@State
def rrb406cEff_2():

    def upon_IMMEDIATE():
        Unknown4003('rrbef406c_2.DIG', '')
        callSubroutine('NormalArts_Temp02')
        Unknown4013(2)
    sprite('null', 10)

@State
def rrb406cEff_3():

    def upon_IMMEDIATE():
        Unknown4003('rrbef406c_3.DIG', '')
        callSubroutine('NormalArts_Temp03')
        Unknown4013(2)
        Unknown3001(70)
    sprite('null', 10)

@State
def rrb406cEff_4():

    def upon_IMMEDIATE():
        Unknown4003('rrbef406c_4.DIG', '')
        callSubroutine('NormalArts_Temp')
        Unknown3033()
        Unknown4013(2)
        Unknown4006(2)
    sprite('null', 10)

@State
def rrb406MuzzleEff():

    def upon_IMMEDIATE():
        teleportRelativeX(340000)
        Unknown1007(250000)
        Unknown1072(85000)
    sprite('null', 20)
    GFX_0('rrbMuzzleEff_B', 0)

@State
def rrb407MuzzleEff():

    def upon_IMMEDIATE():
        teleportRelativeX(100000)
        Unknown1007(5000)
        Unknown1072(90000)
    sprite('null', 20)
    GFX_0('rrbMuzzleEff', 0)
    GFX_0('rrb404Smoke', 0)

@State
def rrb407EndEff():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4010(3)
        Unknown4011(3)
        Unknown1000(-65000)
        teleportRelativeY(285000)
        Unknown4061(6)
        Unknown21004(1)
        Unknown1096(2470)
    sprite('null', 4)
    Unknown4003('rrbef601_02.DIG', '')
    sprite('null', 4)
    Unknown4003('rrbef601_03.DIG', '')
    sprite('null', 4)
    Unknown4003('rrbef601_04.DIG', '')
    sprite('null', 2)
    Unknown4003('rrbef601_05.DIG', '')
    sprite('null', 2)
    Unknown4003('rrbef601_06.DIG', '')
    sprite('null', 2)
    Unknown4003('rrbef601_07.DIG', '')
    sprite('null', 2)
    Unknown4003('rrbef601_08.DIG', '')
    sprite('null', 2)
    Unknown4003('rrbef601_09.DIG', '')

@State
def rrb408Eff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(-30000)
        Unknown1007(320000)
    sprite('null', 12)
    GFX_0('rrb408Eff_2', 0)
    GFX_0('rrb408Eff_1', 0)
    GFX_0('rrb408Eff_4', 0)
    GFX_0('rrb408Eff_3', 0)

@State
def rrb408Eff_1():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp01')
        Unknown1096(3700)
    sprite('null', 4)
    Unknown4003('rrbef408_1_01.DIG', '')
    sprite('null', 4)
    Unknown4003('rrbef408_1_02.DIG', '')
    sprite('null', 4)
    Unknown4003('rrbef408_1_03.DIG', '')

@State
def rrb408Eff_2():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp02')
        Unknown1096(3700)
    sprite('null', 4)
    Unknown4003('rrbef408_2_01.DIG', '')
    sprite('null', 4)
    Unknown4003('rrbef408_2_02.DIG', '')
    sprite('null', 4)
    Unknown4003('rrbef408_2_03.DIG', '')

@State
def rrb408Eff_3():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp03')
        Unknown1096(4300)
        Unknown3001(70)
    sprite('null', 4)
    Unknown4003('rrbef408_3_01.DIG', '')
    sprite('null', 4)
    Unknown4003('rrbef408_3_02.DIG', '')
    sprite('null', 4)
    Unknown4003('rrbef408_3_03.DIG', '')

@State
def rrb408Eff_4():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        Unknown3033()
        Unknown1096(3700)
    sprite('null', 4)
    Unknown4003('rrbef408_4_01.DIG', '')
    sprite('null', 4)
    Unknown4003('rrbef408_4_02.DIG', '')
    sprite('null', 4)
    Unknown4003('rrbef408_4_03.DIG', '')

@State
def rrb408Eff_Assist():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(-30000)
        Unknown1007(320000)
    sprite('null', 12)
    GFX_0('rrb408Eff_2_Assist', 0)
    GFX_0('rrb408Eff_1_Assist', 0)
    GFX_0('rrb408Eff_4_Assist', 0)
    GFX_0('rrb408Eff_3_Assist', 0)

@State
def rrb408Eff_1_Assist():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp01')
        Unknown1096(3700)
    sprite('null', 2)
    Unknown4003('rrbef408_1_01.DIG', '')
    sprite('null', 2)
    Unknown4003('rrbef408_1_02.DIG', '')
    sprite('null', 2)
    Unknown4003('rrbef408_1_03.DIG', '')

@State
def rrb408Eff_2_Assist():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp02')
        Unknown1096(3700)
    sprite('null', 2)
    Unknown4003('rrbef408_2_01.DIG', '')
    sprite('null', 2)
    Unknown4003('rrbef408_2_02.DIG', '')
    sprite('null', 2)
    Unknown4003('rrbef408_2_03.DIG', '')

@State
def rrb408Eff_3_Assist():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp03')
        Unknown1096(4300)
        Unknown3001(70)
    sprite('null', 2)
    Unknown4003('rrbef408_3_01.DIG', '')
    sprite('null', 2)
    Unknown4003('rrbef408_3_02.DIG', '')
    sprite('null', 2)
    Unknown4003('rrbef408_3_03.DIG', '')

@State
def rrb408Eff_4_Assist():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        Unknown3033()
        Unknown1096(3700)
    sprite('null', 2)
    Unknown4003('rrbef408_4_01.DIG', '')
    sprite('null', 2)
    Unknown4003('rrbef408_4_02.DIG', '')
    sprite('null', 2)
    Unknown4003('rrbef408_4_03.DIG', '')

@State
def rrb408PetalEff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4011(3)
        Unknown4009(2)
        teleportRelativeX(90000)
        Unknown1007(240000)
        Unknown2055(90)
    label(0)
    sprite('null', 1)
    Unknown4047(9, 9, 9)
    Unknown4048(0)
    Unknown4045('rrbef408_petal', 0)
    gotoLabel(0)

@State
def rrb409Eff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        Unknown4008(3)
        teleportRelativeX(0)
        Unknown1007(245000)
        Unknown1096(3500)
    sprite('null', 10)
    Unknown26('rrb408Eff_2')
    Unknown26('rrb408Eff_1')
    Unknown26('rrb408Eff_4')
    Unknown26('rrb408Eff_3')
    GFX_0('rrb409Eff_2', 0)
    GFX_0('rrb409Eff_1', 0)
    GFX_0('rrb409Eff_4', 0)
    GFX_0('rrb409Eff_3', 0)
    GFX_0('rrbGroundEff', 0)

@State
def rrb409Eff_1():

    def upon_IMMEDIATE():
        Unknown4003('rrbef409_1.DIG', '')
        callSubroutine('NormalArts_Temp01')
        Unknown4013(2)
    sprite('null', 10)

@State
def rrb409Eff_2():

    def upon_IMMEDIATE():
        Unknown4003('rrbef409_2.DIG', '')
        callSubroutine('NormalArts_Temp02')
        Unknown4013(2)
    sprite('null', 10)

@State
def rrb409Eff_3():

    def upon_IMMEDIATE():
        Unknown4003('rrbef409_3.DIG', '')
        callSubroutine('NormalArts_Temp03')
        Unknown4013(2)
        Unknown3001(70)
    sprite('null', 10)

@State
def rrb409Eff_4():

    def upon_IMMEDIATE():
        Unknown4003('rrbef409_4.DIG', '')
        callSubroutine('NormalArts_Temp')
        Unknown4013(2)
        Unknown3033()
    sprite('null', 10)

@State
def rrb204MuzzleEff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        teleportRelativeX(205000)
        Unknown1007(95000)
        Unknown1072(140000)
    sprite('null', 20)
    GFX_0('rrbMuzzleEff', 0)

@State
def rrb320Eff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(-40000)
        Unknown1007(150000)
        Unknown1096(3700)
        Unknown1064(3600)
        Unknown1072(-10000)
    sprite('null', 12)
    GFX_0('rrb320PetalEff', 0)
    GFX_0('rrb320Eff_2', 0)
    GFX_0('rrb320Eff_1', 0)
    GFX_0('rrb320Eff_3', 0)

@State
def rrb320Eff_1():

    def upon_IMMEDIATE():
        Unknown4003('rrbef320_1.DIG', '')
        callSubroutine('NormalArts_Temp01')
        Unknown4013(2)
    sprite('null', 12)

@State
def rrb320Eff_2():

    def upon_IMMEDIATE():
        Unknown4003('rrbef320_2.DIG', '')
        callSubroutine('NormalArts_Temp02')
        Unknown4013(2)
    sprite('null', 12)

@State
def rrb320Eff_3():

    def upon_IMMEDIATE():
        Unknown4003('rrbef320_3.DIG', '')
        callSubroutine('NormalArts_Temp03')
        Unknown3032()
        Unknown1007(15000)
        teleportRelativeX(20000)
        Unknown1096(3200)
        Unknown1100(50)
        Unknown3001(120)
        Unknown3004(-12)
        Unknown1073(-10000)
    sprite('null', 12)

@State
def rrb320MuzzleEff():

    def upon_IMMEDIATE():
        teleportRelativeX(-140000)
        Unknown1007(30000)
        Unknown1072(-140000)
    sprite('null', 20)
    GFX_0('rrbMuzzleEff_B', 0)

@State
def rrb320PetalEff():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)
        teleportRelativeX(200000)
        Unknown1007(-50000)
    sprite('null', 2)
    Unknown1015(-5000)
    Unknown1021(18000)
    Unknown4047(9, 9, 9)
    Unknown4048(0)
    Unknown4045('rrbef320_petal', 0)
    sprite('null', 2)
    Unknown1015(-10000)
    Unknown1021(10000)
    Unknown4047(9, 9, 9)
    Unknown4048(0)
    Unknown4045('rrbef320_petal', 0)
    sprite('null', 2)
    Unknown1015(-15000)
    Unknown1021(2000)
    Unknown4047(9, 9, 9)
    Unknown4048(0)
    Unknown4045('rrbef320_petal', 0)
    sprite('null', 2)
    Unknown1015(-10000)
    Unknown1021(-7000)
    Unknown4047(9, 9, 9)
    Unknown4048(-20000)
    Unknown4045('rrbef320_petal', 0)
    sprite('null', 2)
    Unknown1015(-7500)
    Unknown1021(-15000)
    Unknown4047(9, 9, 9)
    Unknown4048(-50000)
    Unknown4045('rrbef320_petal', 0)
    sprite('null', 2)
    Unknown1015(-5000)
    Unknown1021(-30000)
    Unknown4047(9, 9, 9)
    Unknown4048(-70000)
    Unknown4045('rrbef320_petal', 0)
    sprite('null', 2)
    Unknown1015(3000)
    Unknown1021(-30000)
    Unknown4047(9, 9, 9)
    Unknown4048(-90000)
    Unknown4045('rrbef320_petal', 0)

@State
def rrb430Eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        sendToLabelUpon(32, 10)
        sendToLabelUpon(33, 20)
        sendToLabelUpon(41, 100)
        Unknown23022(1)
        Unknown3038(1)
    sprite('null', 16)
    GFX_0('rrb430aEff', 0)
    sprite('null', 4)
    GFX_0('rrb430bEff', 0)
    sprite('null', 6)
    GFX_0('rrb430cEff', 0)
    label(0)
    sprite('null', 2)
    GFX_0('rrb430dEff', 0)
    GFX_0('rrb430MuzzleEff_01', 0)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(1)
    sprite('rrb430_14', 5)
    GFX_0('rrbCaseEffC', 0)
    gotoLabel(2)
    label(1)
    sprite('rrb430_14', 5)
    GFX_0('rrbCaseEffD', 0)
    label(2)
    sprite('null', 4)
    GFX_0('rrb430eEff', 0)
    GFX_0('rrb430MuzzleEff_02', 0)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(3)
    sprite('rrb430_19', 3)
    GFX_0('rrbCaseEff', 0)
    gotoLabel(0)
    label(3)
    sprite('rrb430_19', 3)
    GFX_0('rrbCaseEffB', 0)
    gotoLabel(0)
    label(10)
    sprite('null', 3)
    sprite('rrb430_17', 2)
    GFX_0('rrbCaseEffB', 0)
    sprite('null', 200)
    Unknown26('rrb430eEff')
    GFX_0('rrb430fEff', 0)
    label(20)
    sprite('null', 60)
    GFX_0('rrb430MuzzleEff_03', 0)
    GFX_0('rrb430Ryuhai', 103)
    GFX_0('rrb430FinishHit', 103)
    sprite('null', 1)
    Unknown14()
    label(100)
    sprite('rrb430_17', 3)
    sprite('rrb430_17', 6)
    GFX_0('rrbCaseEffB', 0)
    Unknown26('rrb430eEff')
    GFX_0('rrb430fEff', 100)

@State
def rrb430aEff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(70000)
        Unknown1007(340000)
        Unknown1096(4000)
    sprite('null', 13)
    GFX_0('rrb430aEff_2', 0)
    GFX_0('rrb430aEff_1', 0)
    GFX_0('rrb430aEff_3', 0)
    GFX_0('rrb430aEff_4', 0)

@State
def rrb430aEff_1():

    def upon_IMMEDIATE():
        Unknown4003('rrbef430a_1.DIG', '')
        callSubroutine('NormalArts_Temp01')
        Unknown4013(2)
    sprite('null', 13)

@State
def rrb430aEff_2():

    def upon_IMMEDIATE():
        Unknown4003('rrbef430a_2.DIG', '')
        callSubroutine('NormalArts_Temp02')
        Unknown4013(2)
    sprite('null', 13)

@State
def rrb430aEff_3():

    def upon_IMMEDIATE():
        Unknown4003('rrbef430a_3.DIG', '')
        callSubroutine('NormalArts_Temp03')
        Unknown4013(2)
        Unknown3001(127)
    sprite('null', 4)
    sprite('null', 10)
    Unknown3004(-5)

@State
def rrb430aEff_4():

    def upon_IMMEDIATE():
        Unknown4003('rrbef430a_4.DIG', '')
        callSubroutine('NormalArts_Temp')
        Unknown3033()
        Unknown4013(2)
    sprite('null', 13)

@State
def rrb430bEff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(70000)
        Unknown1007(240000)
        Unknown1096(4000)
    sprite('null', 13)
    GFX_0('rrb430bEff_2', 0)
    GFX_0('rrb430bEff_1', 0)
    GFX_0('rrb430bEff_3', 0)
    GFX_0('rrb430bEff_4', 0)

@State
def rrb430bEff_1():

    def upon_IMMEDIATE():
        Unknown4003('rrbef430b_1.DIG', '')
        callSubroutine('NormalArts_Temp01')
        Unknown4013(2)
    sprite('null', 10)

@State
def rrb430bEff_2():

    def upon_IMMEDIATE():
        Unknown4003('rrbef430b_2.DIG', '')
        callSubroutine('NormalArts_Temp02')
        Unknown4013(2)
    sprite('null', 10)

@State
def rrb430bEff_3():

    def upon_IMMEDIATE():
        Unknown4003('rrbef430b_3.DIG', '')
        callSubroutine('NormalArts_Temp03')
        Unknown4013(2)
        Unknown3001(127)
    sprite('null', 3)
    sprite('null', 7)
    Unknown3004(-5)

@State
def rrb430bEff_4():

    def upon_IMMEDIATE():
        Unknown4003('rrbef430b_4.DIG', '')
        callSubroutine('NormalArts_Temp')
        Unknown3033()
        Unknown4013(2)
    sprite('null', 10)

@State
def rrb430cEff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(20000)
        Unknown1007(400000)
        Unknown1096(4500)
    sprite('null', 3)
    GFX_0('rrb430cEff_2', 0)
    GFX_0('rrb430cEff_1', 0)
    sprite('null', 3)
    Unknown1096(4000)
    teleportRelativeX(20000)
    Unknown1007(80000)

@State
def rrb430cEff_1():

    def upon_IMMEDIATE():
        Unknown4003('rrbef430c_1.DIG', '')
        callSubroutine('NormalArts_Temp01')
        Unknown4013(2)
    sprite('null', 6)

@State
def rrb430cEff_2():

    def upon_IMMEDIATE():
        Unknown4003('rrbef430c_2.DIG', '')
        callSubroutine('NormalArts_Temp02')
        Unknown4013(2)
    sprite('null', 6)

@State
def rrb430dEff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(-40000)
        Unknown1007(265000)
        Unknown1096(3900)
        Unknown1064(3400)
        Unknown1072(-15000)
    sprite('null', 10)
    GFX_0('rrb430dEff_2', 0)
    GFX_0('rrb430dEff_1', 0)
    GFX_0('rrb430dEff_3', 0)
    GFX_0('rrb430dEff_4', 0)

@State
def rrb430dEff_1():

    def upon_IMMEDIATE():
        Unknown4003('rrbef430d_1.DIG', '')
        callSubroutine('NormalArts_Temp01')
        Unknown23015(11)
        Unknown4013(2)
    sprite('null', 10)

@State
def rrb430dEff_2():

    def upon_IMMEDIATE():
        Unknown4003('rrbef430d_2.DIG', '')
        callSubroutine('NormalArts_Temp02')
        Unknown23015(11)
        Unknown4013(2)
    sprite('null', 10)

@State
def rrb430dEff_3():

    def upon_IMMEDIATE():
        Unknown4003('rrbef430d_3.DIG', '')
        callSubroutine('NormalArts_Temp03')
        Unknown23015(11)
        Unknown4013(2)
        Unknown3001(90)
    sprite('null', 10)

@State
def rrb430dEff_4():

    def upon_IMMEDIATE():
        Unknown4003('rrbef430d_4.DIG', '')
        callSubroutine('NormalArts_Temp')
        Unknown4006(2)
        Unknown23015(11)
        Unknown3033()
        Unknown4013(2)
    sprite('null', 10)

@State
def rrb430dEffB():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(-50000)
        Unknown1007(255000)
        Unknown1096(3900)
        Unknown1064(3700)
        Unknown1072(0)
    sprite('null', 10)
    GFX_0('rrb430dEff_2B', 0)
    GFX_0('rrb430dEff_1B', 0)
    GFX_0('rrb430dEff_3B', 0)
    GFX_0('rrb430dEff_4B', 0)

@State
def rrb430dEff_1B():

    def upon_IMMEDIATE():
        Unknown4003('rrbef430e_1.DIG', '')
        callSubroutine('NormalArts_Temp01')
        Unknown23015(11)
        Unknown4013(2)
    sprite('null', 10)

@State
def rrb430dEff_2B():

    def upon_IMMEDIATE():
        Unknown4003('rrbef430e_2.DIG', '')
        callSubroutine('NormalArts_Temp02')
        Unknown23015(11)
        Unknown4013(2)
    sprite('null', 10)

@State
def rrb430dEff_3B():

    def upon_IMMEDIATE():
        Unknown4003('rrbef430e_3.DIG', '')
        callSubroutine('NormalArts_Temp03')
        Unknown23015(11)
        Unknown4013(2)
        Unknown3001(90)
    sprite('null', 10)

@State
def rrb430dEff_4B():

    def upon_IMMEDIATE():
        Unknown4003('rrbef430e_4.DIG', '')
        callSubroutine('NormalArts_Temp')
        Unknown4006(2)
        Unknown23015(11)
        Unknown3033()
        Unknown4013(2)
    sprite('null', 10)

@State
def rrb430eEff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(-30000)
        Unknown1007(260000)
        Unknown1096(4400)
        Unknown1064(3700)
        Unknown1072(10000)
    sprite('null', 10)
    GFX_0('rrb430eEff_2', 0)
    GFX_0('rrb430eEff_1', 0)
    GFX_0('rrb430eEff_3', 0)
    GFX_0('rrb430eEff_4', 0)

@State
def rrb430eEff_1():

    def upon_IMMEDIATE():
        Unknown4003('rrbef430e_1.DIG', '')
        callSubroutine('NormalArts_Temp01')
        Unknown4013(2)
        Unknown4010(2)
    sprite('null', 10)

@State
def rrb430eEff_2():

    def upon_IMMEDIATE():
        Unknown4003('rrbef430e_2.DIG', '')
        callSubroutine('NormalArts_Temp02')
        Unknown4013(2)
        Unknown4010(2)
    sprite('null', 10)

@State
def rrb430eEff_3():

    def upon_IMMEDIATE():
        Unknown4003('rrbef430e_3.DIG', '')
        callSubroutine('NormalArts_Temp03')
        Unknown4013(2)
        Unknown4010(2)
        Unknown3001(90)
    sprite('null', 10)

@State
def rrb430eEff_4():

    def upon_IMMEDIATE():
        Unknown4003('rrbef430e_4.DIG', '')
        callSubroutine('NormalArts_Temp')
        Unknown3033()
        Unknown4006(2)
        Unknown4013(2)
        Unknown4010(2)
    sprite('null', 10)

@State
def rrb430eEffB():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(-45000)
        Unknown1007(260000)
        Unknown1096(4400)
        Unknown1064(4000)
        Unknown1072(5000)
    sprite('null', 10)
    GFX_0('rrb430eEff_2B', 0)
    GFX_0('rrb430eEff_1B', 0)
    GFX_0('rrb430eEff_3B', 0)
    GFX_0('rrb430eEff_4B', 0)

@State
def rrb430eEff_1B():

    def upon_IMMEDIATE():
        Unknown4003('rrbef430d_1.DIG', '')
        callSubroutine('NormalArts_Temp01')
        Unknown4013(2)
        Unknown4010(2)
    sprite('null', 10)

@State
def rrb430eEff_2B():

    def upon_IMMEDIATE():
        Unknown4003('rrbef430d_2.DIG', '')
        callSubroutine('NormalArts_Temp02')
        Unknown4013(2)
        Unknown4010(2)
    sprite('null', 10)

@State
def rrb430eEff_3B():

    def upon_IMMEDIATE():
        Unknown4003('rrbef430d_3.DIG', '')
        callSubroutine('NormalArts_Temp03')
        Unknown4013(2)
        Unknown4010(2)
        Unknown3001(90)
    sprite('null', 10)

@State
def rrb430eEff_4B():

    def upon_IMMEDIATE():
        Unknown4003('rrbef430d_4.DIG', '')
        callSubroutine('NormalArts_Temp')
        Unknown3033()
        Unknown4006(2)
        Unknown4013(2)
        Unknown4010(2)
    sprite('null', 10)

@State
def rrb430fEff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(-50000)
        Unknown1007(250000)
        Unknown1096(4100)
    sprite('null', 3)
    GFX_0('rrb430fEff_2', 0)
    GFX_0('rrb430fEff_1', 0)
    GFX_0('rrb430fEff_4', 0)

@State
def rrb430fEff_1():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp01')
        Unknown4013(2)
    sprite('null', 3)
    Unknown4003('rrbef430f_1.DIG', '')

@State
def rrb430fEff_2():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp02')
        Unknown4013(2)
    sprite('null', 3)
    Unknown4003('rrbef430f_2.DIG', '')

@State
def rrb430fEff_4():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        Unknown3033()
        Unknown4013(2)
    sprite('null', 3)
    Unknown4003('rrbef430f_4.DIG', '')

@State
def rrb430MuzzleEff_01():

    def upon_IMMEDIATE():
        Unknown4007(3)
        teleportRelativeX(280000)
        Unknown1007(420000)
        Unknown1072(30000)
    sprite('null', 20)
    GFX_0('rrbMuzzleEff_C', 0)

@State
def rrb430MuzzleEff_02():

    def upon_IMMEDIATE():
        Unknown4007(3)
        teleportRelativeX(300000)
        Unknown1007(400000)
        Unknown1072(45000)
    sprite('null', 20)
    GFX_0('rrbMuzzleEff', 0)

@State
def rrb430MuzzleEff_03():

    def upon_IMMEDIATE():
        Unknown4007(3)
        teleportRelativeX(480000)
        Unknown1007(370000)
        Unknown1072(67000)
    sprite('null', 20)
    GFX_0('rrbMuzzleEff_B', 0)

@State
def rrb430FinishHit():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown1056(4500)
        Unknown1064(3400)
        Unknown1059(100)
        physicsXImpulse(-15000)
        physicsYImpulse(-5000)
        teleportRelativeX(350000)
        Unknown1007(330000)
        Unknown1072(-23000)
    sprite('null', 24)
    GFX_0('rrb430FinishHit03', 0)
    GFX_0('rrb430FinishHit01', 0)
    GFX_0('rrb430FinishHit02', 0)
    GFX_0('rrb430HitRing', 0)
    Unknown4048(157000)
    Unknown4045('rrbef430_speed', 0)
    Unknown4048(157000)
    Unknown4047(1, 1, 1)
    Unknown4045('rrbef430_speedB', 0)
    GFX_0('rrb430FinishPetal', 0)

@State
def rrb430FinishPetal():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown1056(1000)
        Unknown1064(0)
        Unknown4061(0)
        Unknown3038(1)
    sprite('vrrrbef430_Hit', 1)
    Unknown4048(157000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_unique_petal', 100)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 25)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 24)
    sprite('vrrrbef430_Hit', 1)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 23)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 22)
    sprite('vrrrbef430_Hit', 1)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 21)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 20)
    sprite('vrrrbef430_Hit', 1)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 19)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 18)
    sprite('vrrrbef430_Hit', 1)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 17)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 16)
    SFX_3('rrbse_10')
    sprite('vrrrbef430_Hit', 1)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 15)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 14)
    sprite('vrrrbef430_Hit', 1)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 13)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 12)
    sprite('vrrrbef430_Hit', 1)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 11)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 10)
    sprite('vrrrbef430_Hit', 1)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 9)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 8)
    sprite('vrrrbef430_Hit', 1)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 7)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 6)
    sprite('vrrrbef430_Hit', 1)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 5)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 4)
    sprite('vrrrbef430_Hit', 1)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 3)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 2)
    sprite('vrrrbef430_Hit', 1)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 1)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 0)

@State
def rrb430FinishHit01():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown4061(6)
        Unknown3032()
        Unknown23015(10)
        Unknown23122(1)
    sprite('null', 3)
    Unknown4003('rrbef430_finish01', '')
    sprite('null', 4)
    Unknown4003('rrbef430_finish02', '')
    sprite('null', 3)
    Unknown4003('rrbef430_finish03', '')
    sprite('null', 3)
    Unknown4003('rrbef430_finish04', '')
    sprite('null', 3)
    Unknown4003('rrbef430_finish05', '')
    sprite('null', 3)
    Unknown4003('rrbef430_finish06', '')

@State
def rrb430FinishHit02():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown3033()
        Unknown23015(10)
    sprite('null', 3)
    Unknown4003('rrbef430_finish_BloomA01', '')
    sprite('null', 4)
    Unknown4003('rrbef430_finish_BloomA02', '')
    sprite('null', 3)
    Unknown4003('rrbef430_finish_BloomA03', '')
    sprite('null', 3)
    Unknown4003('rrbef430_finish_BloomA04', '')

@State
def rrb430FinishHit03():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown3033()
        Unknown4061(6)
        Unknown21004(1)
        Unknown23015(10)
    sprite('null', 3)
    Unknown4003('rrbef430_finish_BloomB01', '')
    sprite('null', 4)
    Unknown4003('rrbef430_finish_BloomB02', '')
    sprite('null', 3)
    Unknown4003('rrbef430_finish_BloomB03', '')
    sprite('null', 3)
    Unknown4003('rrbef430_finish_BloomB04', '')
    sprite('null', 3)
    Unknown4003('rrbef430_finish_BloomB05', '')
    sprite('null', 3)
    Unknown4003('rrbef430_finish_BloomB06', '')

@State
def rrb430HitRing():

    def upon_IMMEDIATE():
        Unknown4003('rrbef431_shockwave.DIG', '')
        Unknown2054(1)
        Unknown3032()
        Unknown1096(2500)
        Unknown1099(20)
        Unknown1072(-23000)
        Unknown4061(6)
        Unknown21004(1)
    sprite('null', 15)
    sprite('null', 3)
    Unknown3004(-90)

@State
def rrb430Ryuhai():

    def upon_IMMEDIATE():
        Unknown1072(-23000)
    sprite('null', 3)
    sprite('null', 300)
    GFX_0('rrb430Ryuhai_1', 0)
    GFX_0('rrb430Ryuhai_2', 0)
    GFX_0('rrb430Ryuhai_3', 0)

@State
def rrb430Ryuhai_1():

    def upon_IMMEDIATE():
        Unknown4003('rrbef431_ryuhai01.DIG', '')
        Unknown4022(2)
        Unknown4006(2)
        Unknown2054(1)
        Unknown3033()
        Unknown23015(2)
        teleportRelativeY(200000)
        Unknown1096(8000)
        Unknown1064(5000)
        Unknown4061(0)
        Unknown21004(9)
        Unknown3001(190)
    sprite('null', 1)
    sprite('null', 2)
    Unknown1064(7000)
    sprite('null', 1)
    Unknown1064(6000)
    sprite('null', 20)
    Unknown1067(-100)
    Unknown3004(-10)

@State
def rrb430Ryuhai_2():

    def upon_IMMEDIATE():
        Unknown4003('rrbef431_ryuhai01.DIG', '')
        Unknown4022(2)
        Unknown4006(2)
        Unknown2054(1)
        Unknown3033()
        Unknown23015(2)
        teleportRelativeY(200000)
        Unknown1096(8000)
        Unknown1064(3000)
        Unknown4061(6)
        Unknown21004(17)
        Unknown3001(190)
    sprite('null', 1)
    sprite('null', 2)
    Unknown1064(4000)
    sprite('null', 1)
    Unknown1064(3000)
    sprite('null', 20)
    Unknown1067(-100)
    Unknown3004(-10)

@State
def rrb430Ryuhai_3():

    def upon_IMMEDIATE():
        Unknown4003('rrbef431_ryuhai02.DIG', '')
        Unknown4022(2)
        Unknown4006(2)
        Unknown2054(1)
        Unknown3033()
        Unknown4061(6)
        Unknown21004(1)
        Unknown23015(2)
        teleportRelativeY(200000)
        Unknown1056(6000)
        Unknown1064(2000)
        Unknown3001(128)
    sprite('null', 1)
    sprite('null', 2)
    Unknown1064(3000)
    sprite('null', 1)
    Unknown1064(2000)
    sprite('null', 15)
    Unknown1067(-166)
    Unknown3004(-12)

@State
def rrb430EffOD():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        sendToLabelUpon(32, 10)
        sendToLabelUpon(33, 20)
        sendToLabelUpon(41, 100)
        Unknown23022(1)
        Unknown3038(1)
    sprite('null', 16)
    GFX_0('rrb430aEff', 0)
    GFX_0('rrb430aEff_5', 0)
    sprite('null', 4)
    GFX_0('rrb430bEff', 0)
    GFX_0('rrb430bEff_5', 0)
    sprite('null', 6)
    GFX_0('rrb430cEff', 0)
    label(0)
    sprite('null', 2)
    GFX_0('rrb430dEff', 0)
    GFX_0('rrb430dEff_5', 0)
    GFX_0('rrb430MuzzleEff_01', 0)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(1)
    sprite('rrb430_14', 5)
    GFX_0('rrbCaseEffC', 0)
    gotoLabel(2)
    label(1)
    sprite('rrb430_14', 5)
    GFX_0('rrbCaseEffD', 0)
    label(2)
    sprite('null', 4)
    GFX_0('rrb430eEff', 0)
    GFX_0('rrb430eEff_5', 0)
    GFX_0('rrb430MuzzleEff_02', 0)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(3)
    sprite('rrb430_19', 3)
    GFX_0('rrbCaseEff', 0)
    gotoLabel(4)
    label(3)
    sprite('rrb430_19', 3)
    GFX_0('rrbCaseEffB', 0)
    gotoLabel(4)
    label(4)
    sprite('null', 2)
    GFX_0('rrb430dEffB', 0)
    GFX_0('rrb430dEff_5', 0)
    GFX_0('rrb430MuzzleEff_01', 0)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(5)
    sprite('rrb430_14', 5)
    GFX_0('rrbCaseEffC', 0)
    gotoLabel(6)
    label(5)
    sprite('rrb430_14', 5)
    GFX_0('rrbCaseEffD', 0)
    label(6)
    sprite('null', 4)
    GFX_0('rrb430eEffB', 0)
    GFX_0('rrb430eEff_5', 0)
    GFX_0('rrb430MuzzleEff_02', 0)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(7)
    sprite('rrb430_19', 3)
    GFX_0('rrbCaseEff', 0)
    gotoLabel(0)
    label(7)
    sprite('rrb430_19', 3)
    GFX_0('rrbCaseEffB', 0)
    gotoLabel(0)
    label(10)
    sprite('null', 3)
    sprite('rrb430_17', 4)
    GFX_0('rrbCaseEffB', 0)
    sprite('null', 200)
    Unknown26('rrb430eEff')
    GFX_0('rrb430fEff', 0)
    label(20)
    sprite('null', 60)
    GFX_0('rrb430MuzzleEff_03', 0)
    GFX_0('rrb430Ryuhai', 103)
    GFX_0('rrb430FinishHit', 103)
    sprite('null', 1)
    Unknown14()
    label(100)
    sprite('rrb430_17', 10)
    GFX_0('rrbCaseEffB', 0)
    Unknown26('rrb430eEff')
    GFX_0('rrb430fEff', 100)

@State
def rrb430aEff_5():

    def upon_IMMEDIATE():
        Unknown4003('rrbef430a_5.DIG', '')
        callSubroutine('NormalArts_Temp')
        Unknown3033()
        Unknown4009(0)
        Unknown4061(6)
        Unknown21004(1)
        teleportRelativeX(70000)
        Unknown1007(340000)
    sprite('null', 2)
    Unknown1096(1)
    sprite('null', 3)
    Unknown4003('rrbef430a_5.DIG', '')
    Unknown1096(4000)
    Unknown1099(300)
    physicsXImpulse(3000)
    physicsYImpulse(-3000)
    sprite('null', 7)
    Unknown3004(-31)

@State
def rrb430bEff_5():

    def upon_IMMEDIATE():
        Unknown4003('rrbef430b_5.DIG', '')
        callSubroutine('NormalArts_Temp')
        Unknown3033()
        Unknown4009(0)
        Unknown4061(6)
        Unknown21004(1)
        teleportRelativeX(70000)
        Unknown1007(240000)
        Unknown1096(4600)
    sprite('null', 3)
    Unknown1099(300)
    physicsXImpulse(2000)
    physicsYImpulse(-5000)
    sprite('null', 10)
    Unknown3004(-23)

@State
def rrb430dEff_5():

    def upon_IMMEDIATE():
        Unknown4003('rrbef430d_5.DIG', '')
        callSubroutine('NormalArts_Temp')
        Unknown3033()
        Unknown4009(0)
        Unknown4061(6)
        Unknown21004(1)
        teleportRelativeX(-40000)
        Unknown1007(265000)
        Unknown1096(3900)
        Unknown1064(3400)
    sprite('null', 3)
    Unknown1099(200)
    physicsXImpulse(2000)
    physicsYImpulse(2000)
    sprite('null', 7)
    Unknown3004(-31)

@State
def rrb430eEff_5():

    def upon_IMMEDIATE():
        Unknown4003('rrbef430e_5.DIG', '')
        callSubroutine('NormalArts_Temp')
        Unknown3033()
        Unknown4009(0)
        Unknown4061(6)
        Unknown21004(1)
        teleportRelativeX(-40000)
        Unknown1007(265000)
        Unknown1096(3900)
        Unknown1064(3400)
    sprite('null', 3)
    Unknown1099(300)
    physicsXImpulse(2000)
    physicsYImpulse(-2000)
    sprite('null', 7)
    Unknown3004(-31)

@State
def rrb431Eff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        teleportRelativeX(-40000)
        Unknown1007(220000)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        sendToLabelUpon(34, 2)
        sendToLabelUpon(35, 10)
    sprite('null', 8)
    sprite('null', 20)
    GFX_0('rrb431Screen', 0)
    sprite('null', 50)
    GFX_0('rrb431Smoke', 0)
    GFX_0('rrb431Petal_First', 0)
    label(10)
    sprite('null', 50)
    GFX_0('rrb431Tornade', 0)
    GFX_0('rrb431Trail', 0)
    label(0)
    sprite('null', 120)
    Unknown21012('rrb431BlackIO', 32)
    Unknown21012('rrb431Trail', 32)
    Unknown21012('rrb431Petal_First', 33)
    Unknown26('rrb431Smoke')
    sprite('null', 1)
    Unknown14()
    label(1)
    sprite('null', 5)
    Unknown21012('rrb431Screen', 33)
    sprite('null', 5)
    Unknown26('rrb431Petal_First')
    Unknown21012('rrb431Tornade', 32)
    Unknown21012('rrb431Trail', 32)
    sprite('null', 10)
    Unknown26('rrb431Smoke')
    sprite('null', 120)
    sprite('null', 1)
    Unknown14()
    label(2)
    sprite('null', 5)
    Unknown21012('rrb431Screen', 34)
    sprite('null', 5)
    Unknown26('rrb431Petal_First')
    Unknown21012('rrb431Tornade', 32)
    Unknown21012('rrb431Trail', 32)
    sprite('null', 10)
    Unknown26('rrb431Smoke')
    sprite('null', 120)

@State
def rrb431Screen():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown6001(1)

        def upon_3():
            Unknown23032(50)
            Unknown23033(50)
        Unknown2055(150)
        sendToLabelUpon(33, 1)
        sendToLabelUpon(34, 2)
    sprite('null', 180)
    GFX_0('rrb431BlackIO', 0)
    sprite('null', 1)
    Unknown14()
    label(1)
    sprite('null', 120)
    GFX_0('rrb431Petal_Hit', 0)
    GFX_0('rrb431Ryuhai_1', 0)
    GFX_0('rrb431Ryuhai_2', 0)
    GFX_0('rrb431Ryuhai_3', 0)
    GFX_0('rrb431BGLine', 0)
    GFX_0('rrb431Wind', 0)
    sprite('null', 1)
    Unknown14()
    label(2)
    sprite('null', 120)
    GFX_0('rrb431Petal_Hit', 0)
    GFX_0('rrb431Ryuhai_1', 0)
    GFX_0('rrb431Ryuhai_2', 0)
    GFX_0('rrb431Ryuhai_3', 0)
    GFX_0('rrb431BGLine', 0)
    GFX_0('rrb431Wind', 0)
    GFX_0('rrb431Wind_OD', 0)
    sprite('null', 1)
    Unknown14()

@State
def rrb431BlackIO():

    def upon_IMMEDIATE():
        Unknown4003('rrbef_plane.DIG', '')
        Unknown4007(2)
        Unknown2054(1)
        Unknown3032()
        sendToLabelUpon(32, 0)
        Unknown23015(2)
        Unknown3007(0)
        Unknown3013(0)
        Unknown3019(0)
        Unknown3001(0)
        Unknown1096(6000)
    sprite('null', 20)
    Unknown3004(9)
    sprite('null', 60)
    Unknown3004(0)
    label(0)
    sprite('null', 40)
    Unknown3004(-4)

@State
def rrb431Ryuhai_1():

    def upon_IMMEDIATE():
        Unknown4003('rrbef431_ryuhai01.DIG', '')
        Unknown4022(2)
        Unknown2054(1)
        Unknown3033()
        Unknown23015(15)
        teleportRelativeY(200000)
        Unknown1096(6000)
        Unknown1064(2000)
        Unknown4061(0)
        Unknown21004(9)
        Unknown3001(0)
    sprite('null', 1)
    Unknown3001(255)
    sprite('null', 2)
    Unknown3001(255)
    Unknown1064(3500)
    sprite('null', 1)
    Unknown1064(3000)
    sprite('null', 22)
    Unknown1067(-136)
    Unknown3004(-5)

@State
def rrb431Ryuhai_2():

    def upon_IMMEDIATE():
        Unknown4003('rrbef431_ryuhai01.DIG', '')
        Unknown4022(2)
        Unknown2054(1)
        Unknown3033()
        Unknown23015(15)
        teleportRelativeY(200000)
        Unknown1096(6000)
        Unknown1064(1000)
        Unknown3001(0)
        Unknown4061(6)
        Unknown21004(17)
    sprite('null', 1)
    Unknown3001(204)
    sprite('null', 2)
    Unknown3001(204)
    Unknown1064(3000)
    sprite('null', 1)
    Unknown1064(2000)
    sprite('null', 20)
    Unknown1067(-100)
    Unknown3004(-7)

@State
def rrb431Ryuhai_3():

    def upon_IMMEDIATE():
        Unknown4003('rrbef431_ryuhai02.DIG', '')
        Unknown4022(2)
        Unknown2054(1)
        Unknown3033()
        Unknown23015(15)
        teleportRelativeY(200000)
        Unknown1056(6000)
        Unknown1064(1500)
        Unknown3001(0)
    sprite('null', 1)
    Unknown3001(127)
    sprite('null', 2)
    Unknown3001(127)
    Unknown1064(3500)
    sprite('null', 1)
    Unknown1064(2500)
    sprite('null', 15)
    Unknown3004(-5)
    Unknown1067(-166)

@State
def rrb431BGLine():

    def upon_IMMEDIATE():
        Unknown4022(2)
        Unknown2054(1)
        Unknown2055(14)
        teleportRelativeX(-200000)
        teleportRelativeY(200000)
    label(0)
    sprite('null', 2)
    GFX_1('rrbef431_speed03', 0)
    gotoLabel(0)

@State
def rrb431Hit():

    def upon_IMMEDIATE():
        Unknown4003('rrbef431_shockwave.DIG', '')
        Unknown2054(1)
        Unknown3032()
        Unknown1096(2500)
        Unknown1099(20)
        Unknown1007(150000)
        Unknown1072(-25000)
        Unknown4061(0)
        Unknown21004(9)
    sprite('null', 15)
    sprite('null', 3)
    Unknown3004(-90)

@State
def rrb431Petal_First():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4007(3)
        Unknown4010(3)
        Unknown2055(120)
        sendToLabelUpon(33, 1)
        teleportRelativeX(-10000)
    sprite('null', 2)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal', 0)
    sprite('null', 2)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal', 0)
    sprite('null', 2)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal', 0)
    label(0)
    sprite('null', 2)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal', 0)
    Unknown4047(9, 9, 9)
    Unknown4054(0)
    Unknown4045('rrbef431_speed04', 0)
    sprite('null', 2)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal', 0)
    gotoLabel(0)
    label(1)
    sprite('null', 2)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal', 0)
    SFX_3('rrbse_10')
    sprite('null', 2)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal', 0)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_speed04', 0)
    sprite('null', 2)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal', 0)
    sprite('null', 2)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal', 0)
    sprite('null', 2)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal', 0)
    sprite('null', 2)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal', 0)
    sprite('null', 2)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal', 0)

@State
def rrb431Petal_Hit():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4007(2)
    sprite('null', 5)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal_end', 0)
    Unknown4045('rrbef431_smoke_end', 0)
    SFX_3('rrbse_11')
    sprite('null', 5)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal_end', 0)
    Unknown4045('rrbef431_smoke_end', 0)
    sprite('null', 4)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal_end', 0)
    Unknown4045('rrbef431_smoke_end', 0)
    SFX_3('rrbse_10')
    sprite('null', 3)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal_end', 0)
    Unknown4045('rrbef431_smoke_end', 0)
    sprite('null', 5)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal_end', 0)
    Unknown4045('rrbef431_smoke_end', 0)
    sprite('null', 5)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal_end', 0)
    Unknown4045('rrbef431_smoke_end', 0)
    sprite('null', 5)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal_end', 0)
    Unknown4045('rrbef431_smoke_end', 0)
    sprite('null', 5)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal_end', 0)
    Unknown4045('rrbef431_smoke_end', 0)
    sprite('null', 6)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal_end', 0)
    Unknown4045('rrbef431_smoke_end', 0)
    sprite('null', 6)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal_end', 0)
    Unknown4045('rrbef431_smoke_end', 0)
    sprite('null', 7)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal_end', 0)
    Unknown4045('rrbef431_smoke_end', 0)
    sprite('null', 7)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal_end', 0)
    Unknown4045('rrbef431_smoke_end', 0)
    sprite('null', 8)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal_end', 0)
    Unknown4045('rrbef431_smoke_end', 0)
    sprite('null', 9)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal_end', 0)
    Unknown4045('rrbef431_smoke_end', 0)
    sprite('null', 10)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal_end01', 0)
    Unknown4045('rrbef431_smoke_end', 0)
    sprite('null', 12)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal_end01', 0)
    Unknown4045('rrbef431_smoke_end', 0)

@State
def rrb431Tornade():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown2054(1)
        Unknown3032()
        Unknown4061(0)
        Unknown1000(0)
        teleportRelativeY(0)
        sendToLabelUpon(32, 0)
    sprite('vrrrbef431_tornade01', 3)
    sprite('vrrrbef431_tornade02', 3)
    sprite('vrrrbef431_tornade03', 3)
    sprite('vrrrbef431_tornade01', 2)
    sprite('vrrrbef431_tornade02', 2)
    sprite('vrrrbef431_tornade03', 2)
    sprite('vrrrbef431_tornade01', 2)
    sprite('vrrrbef431_tornade02', 2)
    sprite('vrrrbef431_tornade03', 2)
    sprite('vrrrbef431_tornade01', 2)
    sprite('vrrrbef431_tornade02', 2)
    sprite('vrrrbef431_tornade03', 2)
    sprite('null', 19)
    Unknown14()
    label(0)
    sprite('vrrrbef431_tornade01', 2)
    Unknown3001(200)
    Unknown3004(-20)
    sprite('vrrrbef431_tornade02', 2)
    sprite('vrrrbef431_tornade03', 2)
    sprite('vrrrbef431_tornade01', 2)
    sprite('vrrrbef431_tornade02', 2)
    sprite('vrrrbef431_tornade03', 2)
    sprite('vrrrbef431_tornade01', 1)
    sprite('vrrrbef431_tornade02', 1)
    sprite('vrrrbef431_tornade03', 1)
    sprite('vrrrbef431_tornade01', 1)
    sprite('vrrrbef431_tornade02', 1)
    sprite('vrrrbef431_tornade03', 1)
    Unknown3004(-21)

@State
def rrb431Trail():

    def upon_IMMEDIATE():
        Unknown4003('rrbef431_trail.DIG', '')
        Unknown4022(3)
        Unknown2054(1)
        Unknown3033()
        Unknown23015(11)
        sendToLabelUpon(32, 0)
        Unknown1007(-30000)
        teleportRelativeX(-100000)
        Unknown1056(1000)
        Unknown1064(800)
        Unknown21004(9)
        Unknown3001(15)
    sprite('null', 5)
    GFX_0('rrb431Trail_2', 0)
    GFX_0('rrb431Trail_3', 0)
    Unknown1059(1000)
    Unknown1067(200)
    Unknown3004(30)
    sprite('null', 5)
    Unknown3004(0)
    Unknown1059(400)
    Unknown1067(50)
    sprite('null', 80)
    Unknown1059(100)
    Unknown1067(10)
    label(0)
    sprite('null', 5)
    Unknown21012('rrb431Trail_2', 32)
    Unknown21012('rrb431Trail_3', 32)
    Unknown1059(-900)
    Unknown1067(-150)
    Unknown3004(-12)
    sprite('null', 5)
    Unknown1059(-500)

@State
def rrb431Trail_2():

    def upon_IMMEDIATE():
        Unknown4003('rrbef_glow.DIG', '')
        Unknown4022(3)
        Unknown2054(1)
        Unknown23015(11)
        Unknown3033()
        sendToLabelUpon(32, 0)
        teleportRelativeX(100000)
        Unknown1056(15000)
        Unknown1064(4500)
        Unknown21004(9)
        Unknown3001(10)
    sprite('null', 10)
    Unknown3004(20)
    sprite('null', 10)
    Unknown3004(0)
    label(0)
    sprite('null', 5)
    sprite('null', 10)
    Unknown3004(-11)

@State
def rrb431Trail_3():

    def upon_IMMEDIATE():
        Unknown4003('rrbef_glow.DIG', '')
        Unknown4022(3)
        Unknown2054(1)
        Unknown23015(6)
        Unknown3033()
        sendToLabelUpon(32, 0)
        teleportRelativeX(100000)
        Unknown1056(15000)
        Unknown1064(4500)
        Unknown21004(9)
        Unknown3001(0)
    sprite('null', 5)
    Unknown3004(5)
    sprite('null', 90)
    Unknown3004(0)
    label(0)
    sprite('null', 10)
    sprite('null', 10)
    Unknown3004(-2)

@State
def rrb431Wind():

    def upon_IMMEDIATE():
        Unknown4022(22)
        Unknown2054(1)
        Unknown2055(75)
    sprite('null', 30)
    label(0)
    sprite('null', 4)
    Unknown4045('rrbef431_speed02', 0)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_speed01', 0)
    gotoLabel(0)

@State
def rrb431Wind_OD():

    def upon_IMMEDIATE():
        Unknown4022(22)
        Unknown2054(1)
        Unknown2055(75)
        Unknown4061(6)
    sprite('null', 30)
    label(0)
    sprite('null', 4)
    Unknown4047(1, 1, 1)
    Unknown4045('rrbef431_speed_OD', 0)
    gotoLabel(0)

@State
def rrb431Smoke():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4022(3)
        Unknown2055(60)
    sprite('null', 3)
    GFX_0('rrb431RingA', 0)
    GFX_0('rrb431Smoke_Start', 0)
    label(0)
    sprite('null', 3)
    GFX_0('rrb431RingA', 0)
    GFX_0('rrb431SmokeB1', 0)
    sprite('null', 3)
    GFX_0('rrb431RingB', 0)
    GFX_0('rrb431RingC2', 0)
    GFX_0('rrb431SmokeB1', 0)
    sprite('null', 3)
    GFX_0('rrb431RingA', 0)
    GFX_0('rrb431SmokeB1', 0)
    sprite('null', 3)
    GFX_0('rrb431RingC', 0)
    GFX_0('rrb431RingB2', 0)
    GFX_0('rrb431SmokeB1', 0)
    gotoLabel(0)

@State
def rrb431RingA():

    def upon_IMMEDIATE():
        callSubroutine('CommonSmoke')
        Unknown2054(1)
        Unknown1007(-250000)
        teleportRelativeX(-50000)
        Unknown1010(10000, -250000)
        physicsXImpulse(-5000)
    sprite('vrrrbef_ringsmokea01', 1)
    Unknown1096(500)
    sprite('vrrrbef_ringsmokea01', 3)
    Unknown1096(650)
    Unknown1099(40)
    sprite('vrrrbef_ringsmokea02', 4)
    sprite('vrrrbef_ringsmokea03', 4)
    sprite('vrrrbef_ringsmokea04', 4)

@State
def rrb431RingB():

    def upon_IMMEDIATE():
        callSubroutine('CommonSmoke')
        Unknown2054(1)
        Unknown1007(-250000)
        teleportRelativeX(-50000)
        Unknown1010(100000, -250000)
        physicsXImpulse(-5000)
    sprite('vrrrbef_ringsmokeb01', 1)
    Unknown1096(400)
    sprite('vrrrbef_ringsmokeb01', 3)
    Unknown1096(500)
    Unknown1099(30)
    sprite('vrrrbef_ringsmokeb02', 4)
    sprite('vrrrbef_ringsmokeb03', 4)
    sprite('vrrrbef_ringsmokeb04', 4)

@State
def rrb431RingC():

    def upon_IMMEDIATE():
        callSubroutine('CommonSmoke')
        Unknown2054(1)
        Unknown1007(-250000)
        teleportRelativeX(-50000)
        Unknown1010(100000, -150000)
        physicsXImpulse(-5000)
    sprite('vrrrbef_ringsmokec01', 1)
    Unknown1096(400)
    sprite('vrrrbef_ringsmokec01', 3)
    Unknown1096(550)
    Unknown1099(35)
    sprite('vrrrbef_ringsmokec02', 4)
    sprite('vrrrbef_ringsmokec03', 4)
    sprite('vrrrbef_ringsmokec04', 4)

@State
def rrb431RingB2():

    def upon_IMMEDIATE():
        callSubroutine('CommonSmoke')
        Unknown2054(1)
        Unknown1007(-250000)
        teleportRelativeX(200000)
        Unknown1010(100000, -250000)
        physicsXImpulse(-5000)
    sprite('vrrrbef_ringsmokeb01', 1)
    Unknown1096(600)
    sprite('vrrrbef_ringsmokeb01', 3)
    Unknown1096(700)
    Unknown1099(20)
    sprite('vrrrbef_ringsmokeb02', 4)
    sprite('vrrrbef_ringsmokeb03', 4)
    sprite('vrrrbef_ringsmokeb04', 4)

@State
def rrb431RingC2():

    def upon_IMMEDIATE():
        callSubroutine('CommonSmoke')
        Unknown2054(1)
        Unknown1007(-250000)
        teleportRelativeX(150000)
        Unknown1010(100000, -150000)
        physicsXImpulse(-5000)
    sprite('vrrrbef_ringsmokec01', 1)
    Unknown1096(600)
    sprite('vrrrbef_ringsmokec01', 3)
    Unknown1096(650)
    Unknown1099(25)
    sprite('vrrrbef_ringsmokec02', 4)
    sprite('vrrrbef_ringsmokec03', 4)
    sprite('vrrrbef_ringsmokec04', 4)

@State
def rrb431Smoke_Start():

    def upon_IMMEDIATE():
        callSubroutine('CommonSmoke')
        Unknown2054(1)
        Unknown1007(-250000)
        teleportRelativeX(150000)
        physicsXImpulse(-15000)
        Unknown1025(10000, 0)
        Unknown1096(500)
        Unknown1099(20)
    sprite('vrrrbef_smoke01', 3)
    sprite('vrrrbef_smoke02', 3)
    sprite('vrrrbef_smoke03', 3)
    sprite('vrrrbef_smoke04', 3)
    sprite('vrrrbef_smoke05', 3)
    Unknown3004(-20)
    sprite('vrrrbef_smoke06', 3)
    Unknown3004(-50)

@State
def rrb431SmokeB1():

    def upon_IMMEDIATE():
        callSubroutine('CommonSmoke')
        Unknown2054(1)
        Unknown1007(-250000)
        teleportRelativeX(50000)
        physicsXImpulse(-5000)
        Unknown1096(700)
        Unknown1102(100, -100)
        Unknown1099(20)
    sprite('vrrrbef_smokeb01', 2)
    GFX_0('rrb431SmokeB2', 0)
    sprite('vrrrbef_smokeb02', 2)
    sprite('vrrrbef_smokeb03', 2)
    sprite('vrrrbef_smokeb04', 3)
    sprite('vrrrbef_smokeb05', 3)
    Unknown3004(-28)
    sprite('vrrrbef_smokeb06', 3)
    sprite('vrrrbef_smokeb07', 3)

@State
def rrb431SmokeB2():

    def upon_IMMEDIATE():
        callSubroutine('CommonSmoke')
        Unknown2054(1)
        teleportRelativeX(-150000)
        physicsXImpulse(-15000)
        Unknown1096(1000)
        Unknown1102(100, -100)
        Unknown1099(20)
    sprite('vrrrbef_smokeb01', 2)
    sprite('vrrrbef_smokeb02', 2)
    sprite('vrrrbef_smokeb03', 2)
    sprite('vrrrbef_smokeb04', 3)
    Unknown1026(500, 0)
    sprite('vrrrbef_smokeb05', 3)
    Unknown3004(-28)
    sprite('vrrrbef_smokeb06', 3)
    sprite('vrrrbef_smokeb07', 3)

@State
def rrb431Petal_DDD():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown6001(1)

        def upon_3():
            Unknown23032(50)
            Unknown23033(50)
    sprite('null', 14)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal_end', 0)
    sprite('null', 14)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal_end', 0)
    sprite('null', 16)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal_end', 0)
    sprite('null', 16)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal_end', 0)
    sprite('null', 16)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal_end', 0)
    sprite('null', 16)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef431_petal_end01', 0)

@Subroutine
def DDSmokeColor():
    Unknown3019(225)
    Unknown3013(250)
    Unknown3001(255)

@State
def rrb450():

    def upon_IMMEDIATE():
        Unknown2054(1)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        sendToLabelUpon(34, 2)
        sendToLabelUpon(41, 100)
        Unknown4007(3)
        Unknown4011(3)
    sprite('null', 32767)
    GFX_0('RWBY_AHground', -1)
    label(0)
    sprite('null', 6)
    GFX_0('rrb450_WhiteOut', -1)
    sprite('null', 20)
    GFX_0('rrb450_Jump', -1)
    GFX_0('rrb450Ryuhai', -1)
    sprite('null', 32767)
    GFX_0('rrb450_TrailPetal', -1)
    label(1)
    sprite('null', 32767)
    Unknown21012('rrb450_WhiteOut', 32)
    GFX_0('rrb450Flare', -1)
    label(2)
    sprite('null', 8)
    sprite('null', 36)
    GFX_0('rrb450FinishHit', -1)
    GFX_0('rrb450_Petal', -1)
    sprite('null', 32767)
    GFX_0('rrb450_Transition', -1)
    label(100)
    sprite('null', 6)
    Unknown21012('RWBY_AHground', 32)

@State
def RWBY_AHground():

    def upon_IMMEDIATE():
        Unknown4003('RWBY_AHground.DIG', '')
        Unknown2054(1)
        Unknown3026(-16777216)
        Unknown1000(0)
        teleportRelativeY(-1000)
        Unknown3032()
        Unknown23015(2)
        sendToLabelUpon(32, 0)
        Unknown4011(3)
    sprite('null', 32767)
    label(0)
    sprite('null', 20)

@State
def rrb450_Jump():

    def upon_IMMEDIATE():
        Unknown2054(1)
        sendToLabelUpon(32, 0)
        Unknown4007(3)
        teleportRelativeX(50000)
        Unknown1007(20000)
        Unknown4061(0)
    sprite('null', 40)
    GFX_0('rrb450_JumpPetal', 0)
    GFX_0('rrb450_JumpSmoke', 0)

@State
def rrb450_JumpPetal():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4007(2)
        Unknown4061(0)
        Unknown4010(2)
    sprite('null', 120)
    Unknown4047(9, 9, 9)
    Unknown23067('rrbef450_jumppetal')

@State
def rrb450_JumpSmoke():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 120)
    Unknown23067('rrbef450_jumpsmoke')

@State
def rrb450_TrailPetal():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown2055(220)
        Unknown3038(1)
        Unknown1000(0)
        teleportRelativeY(1000000)
    sprite('vrrrbef450_petalex', 5)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef450_trailpetal', 6)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef450_trailpetal', 5)
    sprite('vrrrbef450_petalex', 5)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef450_trailpetal', 5)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef450_trailpetal', 4)
    sprite('vrrrbef450_petalex', 5)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef450_trailpetal', 4)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef450_trailpetal', 3)
    sprite('vrrrbef450_petalex', 5)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef450_trailpetal', 3)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef450_trailpetal', 2)
    sprite('vrrrbef450_petalex', 5)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef450_trailpetal', 2)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef450_trailpetal', 1)
    sprite('vrrrbef450_petalex', 5)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef450_trailpetal', 0)
    Unknown4007(3)
    Unknown1000(0)
    teleportRelativeY(0)
    label(0)
    sprite('vrrrbef450_petalex', 4)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef450_trailpetalB', 0)
    Unknown4048(45000)
    Unknown4045('rrbef450_trailspeed', 0)
    gotoLabel(0)

@State
def rrb450_WhiteOut():

    def upon_IMMEDIATE():
        Unknown3033()
        sendToLabelUpon(32, 0)
        Unknown23015(1)
        Unknown1096(6000)
        Unknown3000(0)
        Unknown4061(6)
        Unknown6001(1)

        def upon_3():
            Unknown23032(50)
            Unknown23033(50)
        Unknown1000(0)
        teleportRelativeY(0)
    sprite('null', 5)
    sprite('null', 5)
    GFX_0('rrb450_Speed', -1)
    sprite('null', 20)
    Unknown4003('rrbef450_white.DIG', '')
    Unknown3001(0)
    Unknown3004(13)
    sprite('null', 60)
    Unknown3004(0)
    label(0)
    sprite('null', 1)
    sprite('null', 15)
    clearUponHandler(3)
    Unknown4012(3)
    Unknown1000(0)
    teleportRelativeY(0)
    sprite('null', 40)
    Unknown3004(-7)
    sprite('null', 40)
    Unknown1096(0)
    Unknown21012('rrb450_Speed', 32)
    sprite('null', 40)

@State
def rrb450_Speed():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown2054(1)
        sendToLabelUpon(32, 1)
    Unknown2055(260)
    sprite('null', 2)
    Unknown4048(45000)
    Unknown4045('rrbef450_speed', -1)
    sprite('null', 3)
    Unknown4048(45000)
    Unknown4045('rrbef450_speed', -1)
    sprite('null', 3)
    Unknown4048(45000)
    Unknown4045('rrbef450_speed', -1)
    sprite('null', 5)
    Unknown4048(45000)
    Unknown4045('rrbef450_speed', -1)
    sprite('null', 5)
    Unknown4048(45000)
    Unknown4045('rrbef450_speed', -1)
    label(0)
    sprite('null', 5)
    Unknown4048(45000)
    Unknown4045('rrbef450_speedB', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    Unknown4048(45000)
    Unknown4045('rrbef450_speedC', -1)
    gotoLabel(1)

@State
def rrb450Ryuhai():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown1072(-45000)
        Unknown1000(0)
        teleportRelativeY(0)
    sprite('null', 3)
    Unknown4012(0)
    sprite('null', 40)
    GFX_0('rrb450Ryuhai_1', 0)
    GFX_0('rrb450Ryuhai_2', 0)
    GFX_0('rrb450Ryuhai_3', 0)

@State
def rrb450Ryuhai_1():

    def upon_IMMEDIATE():
        Unknown4003('rrbef431_ryuhai01.DIG', '')
        Unknown4007(2)
        Unknown4006(2)
        Unknown4010(2)
        Unknown2054(1)
        Unknown3033()
        Unknown23015(15)
        Unknown1096(8000)
        Unknown1064(5000)
        Unknown4061(0)
        Unknown21004(9)
        Unknown3001(190)
    sprite('null', 1)
    sprite('null', 2)
    Unknown1064(7000)
    sprite('null', 1)
    Unknown1064(6000)
    sprite('null', 30)
    Unknown1067(-66)
    Unknown3004(-10)

@State
def rrb450Ryuhai_2():

    def upon_IMMEDIATE():
        Unknown4003('rrbef431_ryuhai01.DIG', '')
        Unknown4007(2)
        Unknown4006(2)
        Unknown4010(2)
        Unknown2054(1)
        Unknown3033()
        Unknown23015(15)
        Unknown1096(8000)
        Unknown1064(3000)
        Unknown4061(6)
        Unknown21004(17)
        Unknown3001(190)
    sprite('null', 1)
    sprite('null', 2)
    Unknown1064(4000)
    sprite('null', 1)
    Unknown1064(3000)
    sprite('null', 30)
    Unknown1067(-66)
    Unknown3004(-10)

@State
def rrb450Ryuhai_3():

    def upon_IMMEDIATE():
        Unknown4003('rrbef431_ryuhai02.DIG', '')
        Unknown4007(2)
        Unknown4006(2)
        Unknown4010(2)
        Unknown2054(1)
        Unknown3033()
        Unknown23015(15)
        Unknown1056(6000)
        Unknown1064(2000)
        Unknown3001(64)
    sprite('null', 1)
    sprite('null', 2)
    Unknown1064(3000)
    sprite('null', 1)
    Unknown1064(2000)
    sprite('null', 25)
    Unknown1067(-100)
    Unknown3004(-12)

@State
def rrb450Flare():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown2054(1)
        Unknown21010(1)
        Unknown4061(6)
        Unknown1000(-230000)
        teleportRelativeY(60000)
        Unknown2055(380)
        GFX_0('rrb450FlareA', -1)
        GFX_0('rrb450FlareB', -1)
        Unknown1096(1000)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 6)
    Unknown1000(-220000)
    teleportRelativeY(58000)
    sprite('null', 6)
    Unknown1000(-219000)
    teleportRelativeY(56000)
    sprite('null', 3)
    Unknown1000(-225000)
    teleportRelativeY(52000)
    sprite('null', 3)
    Unknown1000(-230000)
    teleportRelativeY(48000)
    sprite('null', 4)
    Unknown1000(-233000)
    teleportRelativeY(46000)
    sprite('null', 10)
    sprite('null', 10)
    sprite('null', 10)
    sprite('null', 10)
    sprite('null', 32767)
    Unknown1096(0)
    Unknown14()
    Unknown1000(250000)
    teleportRelativeY(500000)

@State
def rrb450FlareA():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4025(2)
        Unknown4013(2)
        Unknown4061(6)
        Unknown4054(6)
        Unknown4047(17, 17, 17)
        Unknown23067('rrbef450_flareA')
    sprite('null', 32767)

@State
def rrb450FlareB():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4025(2)
        Unknown4013(2)
        Unknown4061(6)
        Unknown4054(6)
        Unknown4047(1, 1, 1)
        Unknown23067('rrbef450_flareB')
    sprite('null', 32767)

@State
def rrb450MuzzleEff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        Unknown1073(230000)
        teleportRelativeX(-230000)
        Unknown1007(-20000)
    sprite('null', 25)
    GFX_0('rrbMuzzleEff_450', 0)
    sprite('null', 25)
    GFX_0('rrbMuzzleEff_450', 0)
    SFX_3('rrbse_15')
    sprite('null', 25)
    GFX_0('rrbMuzzleEff_450', 0)
    SFX_3('rrbse_15')
    sprite('null', 25)
    GFX_0('rrbMuzzleEff_450', 0)
    SFX_3('rrbse_15')
    sprite('null', 25)
    GFX_0('rrbMuzzleEff_450', 0)
    SFX_3('rrbse_15')
    sprite('null', 25)
    GFX_0('rrbMuzzleEff_450', 0)
    SFX_3('rrbse_15')
    sprite('null', 25)
    GFX_0('rrbMuzzleEff_450', 0)
    SFX_3('rrbse_01')
    SFX_3('rrbse_02')
    sprite('null', 25)
    GFX_0('rrbMuzzleEff_450', 0)
    SFX_3('rrbse_01')
    SFX_3('rrbse_02')
    sprite('null', 58)
    GFX_0('rrbMuzzleEff_450', 0)
    SFX_3('rrbse_01')
    SFX_3('rrbse_02')
    sprite('null', 15)
    GFX_0('rrbMuzzleEff_450', 0)
    SFX_3('rrbse_02')

@State
def rrbMuzzleEff_450():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown4007(2)
        Unknown4006(2)
        teleportRelativeX(-50000)
        Unknown1072(-90000)
        Unknown1096(900)
        Unknown1088(-2000)
    sprite('null', 12)
    Unknown4048(-40000)
    Unknown4045('rrbef_muzzle', -1)
    GFX_0('rrbMuzzleEff_450_2', 0)
    GFX_0('rrbMuzzleEff_B3', 0)

@State
def rrbMuzzleEff_450_2():

    def upon_IMMEDIATE():
        Unknown4003('rrbef_muzzle01.DIG', '')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown3033()
        Unknown1056(4500)
        Unknown1064(4000)
        Unknown1088(-3000)
        Unknown1099(150)
        Unknown3007(160)
        Unknown3013(210)
        Unknown23015(1)
    sprite('null', 6)
    sprite('null', 1)
    Unknown3001(180)
    sprite('null', 1)
    Unknown3001(128)

@State
def rrb450FinishHit():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown1056(5000)
        Unknown1064(4000)
        Unknown1059(100)
        physicsXImpulse(15000)
        physicsYImpulse(9000)
        Unknown1000(-150000)
        teleportRelativeY(50000)
        Unknown1072(157000)
    sprite('null', 24)
    GFX_0('rrb430FinishHit03', 0)
    GFX_0('rrb430FinishHit01', 0)
    GFX_0('rrb430FinishHit02', 0)
    GFX_0('rrb450RyuhaiFinish', -1)
    GFX_0('rrb430HitRing', 0)
    Unknown4048(-23000)
    Unknown4045('rrbef430_speed', 0)
    Unknown4048(-23000)
    Unknown4047(1, 1, 1)
    Unknown4045('rrbef430_speedB', 0)
    GFX_0('rrb450FinishPetal', 0)

@State
def rrb450RyuhaiFinish():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown1072(-23000)
        Unknown1000(-150000)
        teleportRelativeY(50000)
        Unknown1056(4000)
        Unknown1064(3000)
    sprite('null', 3)
    Unknown4012(0)
    sprite('null', 70)
    GFX_0('rrb450Ryuhai_1_Finish', 0)
    GFX_0('rrb450Ryuhai_2_Finish', 0)
    GFX_0('rrb450Ryuhai_3_Finish', 0)
    sprite('null', 70)
    Unknown3001(0)

@State
def rrb450Ryuhai_1_Finish():

    def upon_IMMEDIATE():
        Unknown4003('rrbef431_ryuhai01.DIG', '')
        Unknown4007(2)
        Unknown4006(2)
        Unknown4010(2)
        Unknown2054(1)
        Unknown3033()
        Unknown1056(4000)
        Unknown23015(12)
        Unknown4061(0)
        Unknown21004(9)
        Unknown3001(192)
    sprite('null', 1)
    Unknown1064(5000)
    sprite('null', 2)
    Unknown1066(75)
    sprite('null', 10)

    def upon_16():
        Unknown1066(70)
    sprite('null', 13)

    def upon_16():
        Unknown1066(90)
    sprite('null', 2)
    clearUponHandler(16)
    Unknown3003(10)
    sprite('null', 2)
    Unknown3003(1000)
    sprite('null', 2)
    Unknown3003(10)
    sprite('null', 10)
    Unknown3003(1000)
    sprite('null', 2)
    Unknown3003(10)
    sprite('null', 6)
    Unknown3003(1000)
    sprite('null', 2)
    Unknown3003(10)
    sprite('null', 2)
    Unknown3003(1000)
    sprite('null', 2)
    Unknown3003(10)
    sprite('null', 2)
    Unknown3003(1000)

@State
def rrb450Ryuhai_2_Finish():

    def upon_IMMEDIATE():
        Unknown4003('rrbef431_ryuhai01.DIG', '')
        Unknown4007(2)
        Unknown4006(2)
        Unknown4010(2)
        Unknown2054(1)
        Unknown3033()
        Unknown23015(12)
        Unknown1056(4000)
        Unknown4061(6)
        Unknown21004(17)
        Unknown3001(160)
    sprite('null', 1)
    Unknown1064(4000)
    sprite('null', 2)
    Unknown1066(75)
    sprite('null', 10)

    def upon_16():
        Unknown1066(70)
    sprite('null', 13)

    def upon_16():
        Unknown1066(90)
    sprite('null', 2)
    clearUponHandler(16)
    Unknown3003(10)
    sprite('null', 2)
    Unknown3003(1000)
    sprite('null', 2)
    Unknown3003(10)
    sprite('null', 10)
    Unknown3003(1000)
    sprite('null', 2)
    Unknown3003(10)
    sprite('null', 6)
    Unknown3003(1000)
    sprite('null', 2)
    Unknown3003(10)
    sprite('null', 2)
    Unknown3003(1000)
    sprite('null', 2)
    Unknown3003(10)
    sprite('null', 2)
    Unknown3003(1000)

@State
def rrb450Ryuhai_3_Finish():

    def upon_IMMEDIATE():
        Unknown4003('rrbef431_ryuhai02.DIG', '')
        Unknown4007(2)
        Unknown4006(2)
        Unknown4010(2)
        Unknown2054(1)
        Unknown3033()
        Unknown23015(12)
        Unknown1056(4000)
        Unknown3001(128)
    sprite('null', 1)
    Unknown1064(2000)
    sprite('null', 2)
    Unknown1066(75)
    sprite('null', 10)

    def upon_16():
        Unknown1066(70)
    sprite('null', 13)

    def upon_16():
        Unknown1066(90)
    sprite('null', 2)
    clearUponHandler(16)
    Unknown3003(10)

@State
def rrb450FinishPetal():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown1056(1000)
        Unknown1064(0)
        Unknown4061(0)
        Unknown3038(1)
    sprite('vrrrbef430_Hit', 1)
    Unknown4048(-23000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_unique_petal', 100)
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 25)
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 24)
    sprite('vrrrbef430_Hit', 1)
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 23)
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 22)
    sprite('vrrrbef430_Hit', 1)
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 21)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 20)
    Unknown4048(180000)
    sprite('vrrrbef430_Hit', 1)
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 19)
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 18)
    sprite('vrrrbef430_Hit', 1)
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 17)
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 16)
    sprite('vrrrbef430_Hit', 1)
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 15)
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 14)
    sprite('vrrrbef430_Hit', 1)
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 13)
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 12)
    sprite('vrrrbef430_Hit', 1)
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 11)
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 10)
    sprite('vrrrbef430_Hit', 1)
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 9)
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 8)
    sprite('vrrrbef430_Hit', 1)
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 7)
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 6)
    sprite('vrrrbef430_Hit', 1)
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 5)
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 4)
    sprite('vrrrbef430_Hit', 1)
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 3)
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 2)
    sprite('vrrrbef430_Hit', 1)
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 1)
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef430_finish_petal', 0)

@State
def rrb450_Petal():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown1000(0)
        teleportRelativeY(0)
        Unknown1096(4000)
        Unknown6001(1)

        def upon_3():
            Unknown23032(50)
            Unknown23033(50)
    sprite('null', 110)
    Unknown4047(9, 9, 9)
    Unknown23067('rrbef450_petal')

@State
def rrb450_Transition():

    def upon_IMMEDIATE():
        Unknown21004(9)
        Unknown2054(1)
        Unknown1000(0)
        teleportRelativeY(0)

        def upon_3():
            Unknown23057(50)
            Unknown23058(50)
        Unknown2055(70)
    sprite('null', 46)
    GFX_0('rrb450_TransitionL', -1)
    GFX_0('rrb450_TransitionR', -1)
    sprite('null', 100)
    GFX_0('rrb450_Red', -1)

@State
def rrb450_TransitionL():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown1096(1210)
        Unknown23015(4)
        Unknown4061(4)
    sprite('rrbef450_transition00_l', 3)
    SFX_3('rrbse_10')
    sprite('rrbef450_transition01_l', 3)
    sprite('rrbef450_transition02_l', 3)
    sprite('rrbef450_transition03_l', 3)
    sprite('rrbef450_transition04_l', 3)
    sprite('rrbef450_transition05_l', 3)
    sprite('rrbef450_transition06_l', 3)
    sprite('rrbef450_transition07_l', 3)
    sprite('rrbef450_transition08_l', 3)
    sprite('rrbef450_transition09_l', 3)
    sprite('rrbef450_transition10_l', 3)
    sprite('rrbef450_transition11_l', 3)
    sprite('rrbef450_transition12_l', 3)
    sprite('rrbef450_transition13_l', 2)
    sprite('rrbef450_transition14_l', 3)
    sprite('rrbef450_transition15_l', 2)
    sprite('rrbef450_transition16_l', 3)
    sprite('rrbef450_transition17_l', 2)
    sprite('rrbef450_transition18_l', 3)
    sprite('rrbef450_transition19_l', 2)
    sprite('rrbef450_transition20_l', 3)
    sprite('rrbef450_transition21_l', 2)
    sprite('rrbef450_transition22_l', 3)
    sprite('rrbef450_transition23_l', 2)
    sprite('rrbef450_transition24_l', 2)
    sprite('rrbef450_transition25_l', 2)
    sprite('rrbef450_transition26_l', 2)
    sprite('rrbef450_transition27_l', 2)
    sprite('rrbef450_transition28_l', 2)

@State
def rrb450_TransitionR():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown1096(1210)
        Unknown23015(4)
        Unknown4061(4)
    sprite('rrbef450_transition00_r', 3)
    sprite('rrbef450_transition01_r', 3)
    sprite('rrbef450_transition02_r', 3)
    sprite('rrbef450_transition03_r', 3)
    sprite('rrbef450_transition04_r', 3)
    sprite('rrbef450_transition05_r', 3)
    sprite('rrbef450_transition06_r', 3)
    sprite('rrbef450_transition07_r', 3)
    sprite('rrbef450_transition08_r', 3)
    sprite('rrbef450_transition09_r', 3)
    sprite('rrbef450_transition10_r', 3)
    sprite('rrbef450_transition11_r', 3)
    sprite('rrbef450_transition12_r', 3)
    sprite('rrbef450_transition13_r', 2)
    sprite('rrbef450_transition14_r', 3)
    sprite('rrbef450_transition15_r', 2)
    sprite('rrbef450_transition16_r', 3)
    sprite('rrbef450_transition17_r', 2)
    sprite('rrbef450_transition18_r', 3)
    sprite('rrbef450_transition19_r', 2)
    sprite('rrbef450_transition20_r', 3)
    sprite('rrbef450_transition21_r', 2)
    sprite('rrbef450_transition22_r', 3)
    sprite('rrbef450_transition23_r', 2)
    sprite('rrbef450_transition24_r', 2)
    sprite('rrbef450_transition25_r', 2)
    sprite('rrbef450_transition26_r', 2)
    sprite('rrbef450_transition27_r', 2)
    sprite('rrbef450_transition28_r', 2)

@State
def rrb450_Red():

    def upon_IMMEDIATE():
        Unknown3032()
        sendToLabelUpon(32, 0)
        Unknown23015(4)
        Unknown1096(6000)
        Unknown4061(0)
        Unknown3001(0)
        Unknown3007(225)
        Unknown3013(225)
        Unknown3019(225)
    sprite('rrbef450_transition29', 20)
    Unknown3004(16)
    sprite('keep', 20)
    Unknown26('RWBY_AHground')
    Unknown3010(1)
    Unknown3016(1)
    Unknown3022(1)
    sprite('keep', 15)
    Unknown23102(1)
    Unknown23108(1)
    Unknown23114(1)
    sprite('keep', 10)
    Unknown23102(4)
    Unknown23108(4)
    Unknown23114(4)
    sprite('keep', 30)
    Unknown23102(12)
    Unknown23108(12)
    Unknown23114(12)
    sprite('keep', 40)
    Unknown3010(0)
    Unknown3016(0)
    Unknown3022(0)
    Unknown23102(0)
    Unknown23108(0)
    Unknown23114(0)
    Unknown23099(255)
    Unknown23105(255)
    Unknown23111(255)
    Unknown3004(-8)

@State
def rrb450WinPetal():

    def upon_IMMEDIATE():
        Unknown4061(0)
        Unknown4007(3)
    sprite('null', 180)
    Unknown4047(9, 9, 9)
    Unknown23067('rrbef610_petal_prewarm')

@State
def rrb600Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        teleportRelativeX(-150000)
        Unknown1007(100000)
        Unknown2055(120)
        sendToLabelUpon(32, 1)
    sprite('null', 2)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef600_petal', 0)
    Unknown4047(9, 9, 9)
    label(0)
    sprite('null', 2)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef600_petal', 0)
    sprite('null', 3)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef600_petal', 0)
    gotoLabel(0)
    label(1)
    teleportRelativeX(15000)
    Unknown1007(15000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef600_petal01', 0)
    sprite('null', 2)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef600_petal01', 0)
    sprite('null', 2)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef600_petal01', 0)
    sprite('null', 2)
    teleportRelativeX(30000)
    Unknown1007(25000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef600_petal01', 0)
    sprite('null', 2)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef600_petal01', 0)
    sprite('null', 2)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef600_petal01', 0)
    sprite('null', 2)
    teleportRelativeX(15000)
    Unknown1007(30000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef600_petal01', 0)
    sprite('null', 2)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef600_petal01', 0)
    sprite('null', 2)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef600_petal01', 0)
    sprite('null', 3)
    teleportRelativeX(5000)
    Unknown1007(5000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef600_petal01', 0)
    sprite('null', 3)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef600_petal01', 0)

@State
def rrb601Eff():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown1096(2470)
        Unknown1000(-65000)
        teleportRelativeY(285000)
        Unknown4061(6)
        Unknown21004(1)
    sprite('null', 6)
    Unknown4003('rrbef601_00.DIG', '')
    sprite('null', 6)
    Unknown4003('rrbef601_01.DIG', '')
    sprite('null', 6)
    Unknown4003('rrbef601_02.DIG', '')
    sprite('null', 6)
    Unknown4003('rrbef601_03.DIG', '')
    sprite('null', 6)
    Unknown4003('rrbef601_04.DIG', '')
    sprite('null', 3)
    Unknown4003('rrbef601_05.DIG', '')
    sprite('null', 3)
    Unknown4003('rrbef601_06.DIG', '')
    sprite('null', 3)
    Unknown4003('rrbef601_07.DIG', '')
    sprite('null', 3)
    Unknown4003('rrbef601_08.DIG', '')
    sprite('null', 2)
    Unknown4003('rrbef601_09.DIG', '')

@State
def rrb610Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        teleportRelativeX(-20000)
        Unknown1007(200000)
        Unknown2055(600)
    sprite('null', 10)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef610_petal', 0)
    sprite('null', 8)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef610_petal', 0)
    sprite('null', 6)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef610_petal', 0)
    label(0)
    sprite('null', 3)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef610_petal', 0)
    sprite('null', 2)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef610_petal', 0)
    gotoLabel(0)

@State
def rrb612Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        teleportRelativeX(130000)
        Unknown1007(200000)
    sprite('null', 3)
    sprite('null', 3)
    teleportRelativeX(-50000)
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef612_petal', 0)
    sprite('null', 3)
    teleportRelativeX(-70000)
    Unknown1007(3000)
    Unknown4048(270000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef612_petal', 0)
    sprite('null', 3)
    teleportRelativeX(-70000)
    Unknown1007(-80000)
    Unknown4048(-270000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef612_petal02', 0)
    sprite('null', 1)
    teleportRelativeX(-30000)
    Unknown1007(-50000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef612_petal02', 0)
    sprite('null', 2)
    teleportRelativeX(-70000)
    Unknown1007(70000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef612_petal02', 0)
    sprite('null', 1)
    teleportRelativeX(-70000)
    Unknown1007(50000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef612_petal02', 0)
    sprite('null', 2)
    teleportRelativeX(-70000)
    Unknown1007(40000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef612_petal02', 0)
    sprite('null', 1)
    teleportRelativeX(-70000)
    Unknown1007(40000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef612_petal', 0)
    sprite('null', 2)
    teleportRelativeX(-70000)
    Unknown1007(40000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef612_petal', 0)
    sprite('null', 2)
    teleportRelativeX(-70000)
    Unknown1007(30000)
    Unknown4047(9, 9, 9)
    Unknown4045('rrbef612_petal', 0)

@Subroutine
def NormalArts_Temp():
    Unknown4007(2)
    Unknown4009(2)
    Unknown4011(3)
    Unknown4010(3)

@Subroutine
def NormalArts_Temp01():
    Unknown4007(2)
    Unknown4006(2)
    Unknown4009(2)
    Unknown4011(3)
    Unknown4010(3)
    Unknown4061(6)
    Unknown21004(1)
    Unknown3032()

@Subroutine
def NormalArts_Temp02():
    Unknown4007(2)
    Unknown4006(2)
    Unknown4009(2)
    Unknown4011(3)
    Unknown4010(3)
    Unknown4061(6)
    Unknown21004(2)
    Unknown3032()

@Subroutine
def NormalArts_Temp03():
    Unknown4007(2)
    Unknown4006(2)
    Unknown4009(2)
    Unknown4011(3)
    Unknown4010(3)
    Unknown3032()

@Subroutine
def CommonSmoke():
    Unknown3000(0)
    Unknown4061(6)
    Unknown3032()
    Unknown13044(1)

@State
def rrbef_kakeai_brg():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        sendToLabelUpon(32, 0)
        Unknown2055(280)
    label(0)
    sprite('null', 10)
    Unknown4045('rrbef_kakeai_brg01', -1)
    teleportRelativeY(320000)
    gotoLabel(0)

@State
def rrbef_kakeai_brg_smoke01():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown1102(0, -300)
        teleportRelativeY(15000)
    sprite('null', 30)
    Unknown4054(11)
    Unknown23067('rrbef_kakeai_brg_smoke01')

@State
def rrbef_kakeai_brg_smoke02():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown1102(0, -300)
        Unknown2005()
        teleportRelativeY(15000)
    sprite('null', 30)
    Unknown4054(11)
    Unknown23067('rrbef_kakeai_brg_smoke01')

@State
def DDLight():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4003('ef_dd_light.DIG', '')
        Unknown1096(1300)
    sprite('null', 2)
    sprite('null', 10)
    Unknown23130(39935, 10, 1)
    sprite('null', 10)
    Unknown23130(33023, 10, 1)
    sprite('null', 10)