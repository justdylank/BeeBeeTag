@State
def EMB_OD():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('ef_emb_ma.DIG', '')
        Unknown23015(5)
        Unknown1007(280000)
        Unknown1096(1500)
    sprite('null', 8)
    Unknown3026(-16777216)
    Unknown3025(-1, 10)
    sprite('null', 8)
    Unknown3025(-8342273, 10)
    sprite('null', 8)
    Unknown3025(-16744193, 10)
    sprite('null', 8)
    Unknown3025(-16744193, 10)
    sprite('null', 80)

@Subroutine
def Zanzou_Color():
    Unknown3033()
    Unknown4061(1)
    Unknown3053(1)
    Unknown3040(2)
    Unknown3042(1)
    Unknown3043(128)
    Unknown3041(128)
    Unknown3044(1)

@Subroutine
def maef_color():
    Unknown4061(1)
    Unknown4047(128, 128, 128)
    Unknown21004(128)

@Subroutine
def maef_color2():
    Unknown4061(1)
    Unknown4047(64, 64, 64)
    Unknown21004(64)

@Subroutine
def maef_color3():
    Unknown4061(1)
    Unknown4047(1, 1, 1)
    Unknown21004(1)

@Subroutine
def __3d_color():
    Unknown4061(2)
    Unknown4047(1, 1, 1)
    Unknown21004(1)

@State
def maef_001_zanzou():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
    sprite('vrmaef001_00', 20)
    callSubroutine('Zanzou_Color')

@State
def maef_001_zanzou2():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4061(1)
        Unknown3033()
        Unknown3001(197)
    sprite('vrmaef001_10', 4)
    sprite('vrmaef001_11', 20)
    callSubroutine('Zanzou_Color')

@State
def maef_202():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4061(1)
        Unknown3033()
    sprite('vrmaef202_01', 2)
    sprite('vrmaef202_02', 2)
    sprite('vrmaef202_03', 2)
    teleportRelativeX(-23000)

@State
def maef_202_2():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef202_04', 4)
    teleportRelativeX(-64000)
    sprite('vrmaef202_05', 12)

@State
def maef_232():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef232_04', 4)
    sprite('vrmaef232_05', 12)

@State
def maef_231():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown3038(1)
        Unknown23022(1)
    sprite('ma231_03', 3)
    GFX_0('maef_231_3d', -1)
    sprite('keep', 3)
    sprite('keep', 3)
    sprite('keep', 3)
    sprite('keep', 3)

@State
def maef_231_3d():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown1096(1450)
        Unknown3001(200)
        Unknown3032()
        teleportRelativeX(60000)
        Unknown4003('maef_231slash', '')
    sprite('null', 15)

@State
def maef_540():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef540_03', 2)
    teleportRelativeX(-64000)
    sprite('vrmaef540_04', 16)
    teleportRelativeX(64000)
    teleportRelativeX(-128000)
    GFX_0('maef_540_Particle', 0)
    GFX_0('maef_540_Particle', 1)

@State
def maef_540_Particle():
    callSubroutine('maef_color')
    Unknown4045('maef_540dust', -1)

@State
def maef_252():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef252_04', 4)
    Unknown3004(-16)
    sprite('vrmaef252_05', 3)
    sprite('vrmaef252_06', 3)

@State
def maef_321():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef321_09', 7)

@State
def ThrowCamera():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown20000(1)
    sprite('null', 80)

@State
def maef_521_kick():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown4009(3)
        Unknown3033()
        teleportRelativeX(256000)
        Unknown1007(64000)
        Unknown3001(220)
    sprite('null', 3)
    Unknown4003('maef_521kick.DIG', '')
    sprite('null', 10)
    Unknown4003('maef_521kick2.DIG', '')
    Unknown4007(0)

@State
def maef_520_slash():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4003('maef_520slash.DIG', '')
        Unknown3033()
        Unknown3001(150)
        teleportRelativeX(4000)
        Unknown3038(1)
    sprite('vrmaef520_00', 2)
    Unknown4054(11)
    Unknown4045('maef_520smoke', 0)
    Unknown4054(11)
    Unknown4045('maef_520smoke', 1)
    GFX_1('maef_520smoke', 2)
    sprite('vrmaef520_00', 4)
    GFX_1('maef_520smoke', 3)
    GFX_1('maef_520smoke', 4)
    sprite('null', 10)
    Unknown4007(0)

@State
def maef_531():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4061(1)
        callSubroutine('Zanzou_Color')
        teleportRelativeX(64000)
    sprite('vrmaef531_00', 4)
    GFX_0('maef_531_smash', 0)
    sprite('vrmaef531_01', 20)

@State
def maef_531_smash():
    sprite('null', 1)
    teleportRelativeX(-32000)
    callSubroutine('maef_color')
    Unknown4045('maef_531smash', -1)

@State
def maef_500():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef500_03', 3)
    GFX_0('maef_500_Particle', 0)

@State
def maef_500_Particle():
    callSubroutine('maef_color')
    Unknown4045('maef_500dust', -1)

@State
def maef_503():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4061(1)
        Unknown3033()
    sprite('vrmaef503_00', 3)
    sprite('vrmaef503_01', 4)
    GFX_0('maef_503_particle', 0)
    sprite('vrmaef503_02', 4)

@State
def maef_503_particle():
    callSubroutine('maef_color')
    Unknown4045('maef_503dust', -1)

@State
def maef_503_wind():

    def upon_IMMEDIATE():
        Unknown4003('maef_503wind.DIG', '')
        Unknown3032()
        Unknown1059(5)
        teleportRelativeX(600000)
    sprite('null', 20)
    sprite('null', 8)
    Unknown3004(-32)

@State
def maef_340():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef340_00', 3)
    sprite('vrmaef340_01', 3)

@State
def maef_501_zanzou():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef501_00', 5)
    callSubroutine('Zanzou_Color')
    sprite('vrmaef501_01', 16)
    callSubroutine('Zanzou_Color')

@State
def maef_501_zanzou2():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef501_00', 7)
    callSubroutine('Zanzou_Color')
    sprite('vrmaef501_01', 16)
    callSubroutine('Zanzou_Color')

@State
def maef_502_zanzou():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef502_00', 20)

@State
def maef_501_atk():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(2)
        Damage(1500)
        Hitstop(5)
        hitstun(17)
        AirUntechableTime(19)
        PushbackX(30400)
        AirPushbackX(20000)
        AirPushbackY(20000)
        AirHitstunAnimation(13)
        physicsXImpulse(0)
        Unknown1096(2000)
        Unknown53(1)
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 1)
        sendToLabelUpon(54, 580)
    sprite('null', 3)
    sprite('vrmaef501atk', 3)
    StartMultihit()
    teleportRelativeX(50000)
    GFX_0('maef_501', -1)
    Unknown38(4, 1)
    SFX_3('mase_00')
    sprite('vrmaef501atk', 6)
    physicsXImpulse(60000)
    sprite('vrmaef501atk', 5)
    Unknown1019(60)
    sprite('vrmaef501atk', 5)
    Unknown1019(60)
    sprite('vrmaef501atk', 5)
    Unknown1019(60)
    Unknown23029(4, 5000, 0)
    DisableAttackRestOfMove()
    sprite('vrmaef501atk', 10)
    Unknown1019(20)
    label(580)
    sprite('vrmaef501atk', 10)
    clearUponHandler(54)
    Unknown13(4)
    Unknown1084(1)
    DisableAttackRestOfMove()

@State
def maef_501_atk1():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown11042(1)
        AttackLevel_(2)
        Damage(1700)
        AttackP1(70)
        Hitstop(5)
        hitstun(17)
        AirUntechableTime(19)
        PushbackX(30400)
        AirPushbackX(20000)
        AirPushbackY(20000)
        AirHitstunAnimation(13)
        physicsXImpulse(0)
        Unknown1096(2000)
        Unknown53(1)
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 1)
        sendToLabelUpon(54, 580)
    sprite('null', 3)
    sprite('vrmaef501atk', 3)
    StartMultihit()
    teleportRelativeX(50000)
    GFX_0('maef_501', -1)
    Unknown38(4, 1)
    SFX_3('mase_00')
    sprite('vrmaef501atk', 6)
    physicsXImpulse(60000)
    sprite('vrmaef501atk', 5)
    Unknown1019(60)
    sprite('vrmaef501atk', 5)
    Unknown1019(60)
    sprite('vrmaef501atk', 5)
    Unknown1019(60)
    Unknown23029(4, 5000, 0)
    DisableAttackRestOfMove()
    sprite('vrmaef501atk', 10)
    Unknown1019(20)
    label(580)
    sprite('vrmaef501atk', 10)
    clearUponHandler(54)
    Unknown13(4)
    Unknown1084(1)
    DisableAttackRestOfMove()

@State
def maef_501_atk2():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown11042(1)
        AttackLevel_(2)
        Damage(1700)
        AttackP1(70)
        Hitstop(5)
        hitstun(17)
        AirUntechableTime(19)
        PushbackX(30400)
        AirPushbackX(20000)
        AirPushbackY(20000)
        AirHitstunAnimation(13)
        physicsXImpulse(0)
        Unknown1096(2000)
        Unknown53(1)
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 1)
        sendToLabelUpon(54, 580)
    sprite('null', 3)
    sprite('vrmaef501atk', 3)
    StartMultihit()
    teleportRelativeX(50000)
    GFX_0('maef_501', -1)
    Unknown38(4, 1)
    SFX_3('mase_00')
    sprite('vrmaef501atk', 12)
    physicsXImpulse(60000)
    sprite('vrmaef501atk', 5)
    Unknown1019(60)
    sprite('vrmaef501atk', 5)
    Unknown1019(60)
    sprite('vrmaef501atk', 5)
    Unknown1019(60)
    Unknown23029(4, 5000, 0)
    DisableAttackRestOfMove()
    sprite('vrmaef501atk', 10)
    Unknown1019(20)
    label(580)
    sprite('vrmaef501atk', 10)
    clearUponHandler(54)
    Unknown13(4)
    Unknown1084(1)
    DisableAttackRestOfMove()

@State
def maef_501():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4061(1)
        Unknown3033()
        Unknown1064(600)
        Unknown1056(950)
        Unknown1096(1200)
        GFX_2('maef_shot_sub')

        def upon_43():
            if (SLOT_48 == 5000):
                Unknown3004(-10)
                Unknown3001(128)
                Unknown23029(4, 5000, 0)
    sprite('vrmaef_shot00', 2)
    GFX_0('maef_501_Shot', -1)
    Unknown38(4, 1)
    sprite('vrmaef_shot01', 2)
    sprite('vrmaef_shot02', 2)
    GFX_0('maef_501_Shot_aura', -1)
    label(0)
    sprite('vrmaef_shot00', 2)
    sprite('vrmaef_shot01', 2)
    sprite('vrmaef_shot02', 2)
    gotoLabel(0)

@State
def maef_501_Shot():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)

        def upon_43():
            if (SLOT_48 == 5000):
                Unknown3004(-10)
                Unknown3001(128)
        Unknown1096(1200)
    sprite('null', 32767)
    Unknown23067('maef_shot')

@State
def maef_501_Shot_aura():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown1096(1200)
    label(0)
    sprite('null', 2)
    callSubroutine('maef_color')
    Unknown4045('maef_shot_aura', -1)
    callSubroutine('maef_color2')
    Unknown4045('maef_shot_aura2', -1)
    callSubroutine('maef_color2')
    Unknown4045('maef_shot_dust', -1)
    gotoLabel(0)

@State
def maef_muzzle():
    sprite('null', 1)
    teleportRelativeX(60000)
    callSubroutine('maef_color')
    Unknown4045('maef_muzzle_blm', -1)
    callSubroutine('maef_color3')
    Unknown4045('maef_muzzle_add', -1)
    callSubroutine('maef_color')
    Unknown4045('maef_muzzle', -1)
    callSubroutine('maef_color2')
    Unknown4045('maef_muzzle_ring', -1)
    callSubroutine('maef_color2')
    Unknown4045('maef_muzzle_dust', -1)
    GFX_1('maef_muzzle_sub', -1)

@State
def maef_D_hold():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown4009(3)
        Unknown26('maef_D')
    sprite('null', 32767)
    GFX_0('maef_D', -1)

@State
def maef_203_up():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown4009(3)
        Unknown1072(-10000)
        Unknown26('maef_D')
    sprite('null', 32767)
    GFX_0('maef_D', -1)

@State
def maef_203_up2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown4009(3)
        Unknown1072(-20000)
        Unknown26('maef_D')
    sprite('null', 32767)
    GFX_0('maef_D', -1)

@State
def maef_203_down():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown4009(3)
        Unknown1072(10000)
        Unknown26('maef_D')
    sprite('null', 32767)
    GFX_0('maef_D', -1)

@State
def maef_203_down2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown4009(3)
        Unknown1072(20000)
        Unknown26('maef_D')
    sprite('null', 32767)
    GFX_0('maef_D', -1)

@State
def maef_AirD_hold():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown4009(3)
        Unknown1072(20000)
        Unknown26('maef_D')
    sprite('null', 32767)
    GFX_0('maef_D', -1)

@State
def maef_253_up():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown4009(3)
        Unknown1072(10000)
        Unknown26('maef_D')
    sprite('null', 32767)
    GFX_0('maef_D', -1)

@State
def maef_253_up2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown4009(3)
        Unknown26('maef_D')
    sprite('null', 32767)
    GFX_0('maef_D', -1)

@State
def maef_253_down():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown4009(3)
        Unknown1072(30000)
        Unknown26('maef_D')
    sprite('null', 32767)
    GFX_0('maef_D', -1)

@State
def maef_253_down2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown4009(3)
        Unknown1072(40000)
        Unknown26('maef_D')
    sprite('null', 32767)
    GFX_0('maef_D', -1)

@State
def maef_D():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4006(2)
    sprite('null', 32767)
    GFX_0('maef_D_particle_a', -1)
    GFX_0('maef_D_particle_b', -1)
    GFX_0('maef_D_particle_c', -1)
    GFX_0('maef_D_particle_d', -1)
    GFX_0('maef_D_particle_e', -1)
    GFX_0('maef_D_particle_f', -1)
    GFX_0('maef_D_3d', -1)

@State
def maef_D_particle_a():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4006(2)

        def upon_43():
            if (SLOT_48 == 1002):
                Unknown1096(2000)
        if SLOT_7:
            Unknown1096(2000)
    sprite('null', 32767)
    callSubroutine('maef_color')
    Unknown23067('maef_D_hold_a')

@State
def maef_D_particle_b():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4006(2)

        def upon_43():
            if (SLOT_48 == 1002):
                Unknown1096(2000)
        if SLOT_7:
            Unknown1096(2000)
    sprite('null', 32767)
    Unknown23067('maef_D_hold_b')

@State
def maef_D_particle_c():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4006(2)

        def upon_43():
            if (SLOT_48 == 1002):
                Unknown1096(2000)
        if SLOT_7:
            Unknown1096(2000)
    sprite('null', 32767)
    callSubroutine('maef_color2')
    Unknown23067('maef_D_hold_c')

@State
def maef_D_particle_d():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4006(2)
    sprite('null', 32767)
    callSubroutine('maef_color')
    Unknown23067('maef_D_hold_d')

@State
def maef_D_particle_e():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4006(2)
    sprite('null', 32767)
    Unknown23067('maef_D_hold_e')

@State
def maef_D_particle_f():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4006(2)
    sprite('null', 32767)
    callSubroutine('maef_color3')
    Unknown23067('maef_D_hold_f')

@State
def maef_D_3d():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4006(2)
        Unknown4003('maef_203wind.DIG', '')
        callSubroutine('3d_color')
        Unknown3033()
        Unknown1096(600)
    sprite('null', 32767)

@State
def maef_catch():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown4006(2)
        Unknown4009(3)
        SLOT_6 = 0
    sprite('vrmaef_catch', 1)
    callSubroutine('maef_color2')
    Unknown23067('maef_catch')
    callSubroutine('maef_color')
    Unknown4045('maef_catch_ring', 0)
    sprite('vrmaef_catch', 3)
    callSubroutine('maef_color2')
    Unknown4045('maef_catch_dust', 0)
    callSubroutine('maef_color2')
    Unknown4045('maef_catch_dust', 1)
    callSubroutine('maef_color2')
    Unknown4045('maef_catch_dust', 2)
    callSubroutine('maef_color2')
    Unknown4045('maef_catch_dust', 3)
    callSubroutine('maef_color2')
    Unknown4045('maef_catch_dust', 4)
    sprite('vrmaef_catch', 60)
    Unknown4007(0)

@State
def maef_530():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown3033()
        Unknown4061(3)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef530_00', 3)
    GFX_0('maef_530_Particle', 0)
    sprite('vrmaef530_01', 4)
    sprite('vrmaef530_02', 12)

@State
def maef_530_Particle():
    callSubroutine('maef_color')
    Unknown4045('maef_530slash', -1)
    Unknown4045('maef_530slash_add', -1)

@State
def maef_533():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        teleportRelativeX(600000)
        teleportRelativeX(150000)
    label(0)
    sprite('null', 2)
    GFX_0('maef_533_slash', -1)
    sprite('null', 2)
    GFX_0('maef_533_slash2', -1)
    sprite('null', 2)
    GFX_0('maef_533_slash3', -1)
    sprite('null', 2)
    GFX_0('maef_533_slash4', -1)
    sprite('null', 2)
    GFX_0('maef_533_slash5', -1)
    sprite('null', 2)
    GFX_0('maef_533_slash6', -1)
    gotoLabel(0)

@State
def maef_533_slash():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(3)
        Unknown4007(3)
        Unknown4003('maef_533slash.DIG', '')
        callSubroutine('3d_color')
        Unknown3033()
    sprite('null', 9)
    GFX_0('maef_533_slash_add', -1)
    GFX_0('maef_533_particle', -1)

@State
def maef_533_slash_add():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(3)
        Unknown4007(3)
        Unknown4003('maef_533slash_add.DIG', '')
        Unknown3033()
    sprite('null', 6)
    sprite('null', 3)
    Unknown3001(128)

@State
def maef_533_slash2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(3)
        Unknown4007(3)
        Unknown4003('maef_533slash2.DIG', '')
        callSubroutine('3d_color')
        Unknown3033()
    sprite('null', 9)
    GFX_0('maef_533_slash2_add', -1)
    GFX_0('maef_533_particle', -1)

@State
def maef_533_slash2_add():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(3)
        Unknown4007(3)
        Unknown4003('maef_533slash2_add.DIG', '')
        Unknown3033()
    sprite('null', 6)
    sprite('null', 3)
    Unknown3001(128)

@State
def maef_533_slash3():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(3)
        Unknown4007(3)
        Unknown4003('maef_533slash3.DIG', '')
        callSubroutine('3d_color')
        Unknown3033()
    sprite('null', 9)
    GFX_0('maef_533_slash3_add', -1)
    GFX_0('maef_533_particle', -1)

@State
def maef_533_slash3_add():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(3)
        Unknown4007(3)
        Unknown4003('maef_533slash3_add.DIG', '')
        Unknown3033()
    sprite('null', 6)
    sprite('null', 3)
    Unknown3001(128)

@State
def maef_533_slash4():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(3)
        Unknown4007(3)
        Unknown4003('maef_533slash4.DIG', '')
        callSubroutine('3d_color')
        Unknown3033()
    sprite('null', 9)
    GFX_0('maef_533_slash4_add', -1)
    GFX_0('maef_533_particle', -1)

@State
def maef_533_slash4_add():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(3)
        Unknown4007(3)
        Unknown4003('maef_533slash4_add.DIG', '')
        Unknown3033()
    sprite('null', 6)
    sprite('null', 3)
    Unknown3001(128)

@State
def maef_533_slash5():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(3)
        Unknown4007(3)
        Unknown4003('maef_533slash5.DIG', '')
        callSubroutine('3d_color')
        Unknown3033()
    sprite('null', 9)
    GFX_0('maef_533_slash5_add', -1)
    GFX_0('maef_533_particle', -1)

@State
def maef_533_slash5_add():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(3)
        Unknown4007(3)
        Unknown4003('maef_533slash5_add.DIG', '')
        Unknown3033()
    sprite('null', 6)
    sprite('null', 3)
    Unknown3001(128)

@State
def maef_533_slash6():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(3)
        Unknown4007(3)
        Unknown4003('maef_533slash6.DIG', '')
        callSubroutine('3d_color')
        Unknown3033()
    sprite('null', 9)
    GFX_0('maef_533_slash6_add', -1)
    GFX_0('maef_533_particle', -1)

@State
def maef_533_slash6_add():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(3)
        Unknown4007(3)
        Unknown4003('maef_533slash6_add.DIG', '')
        Unknown3033()
    sprite('null', 6)
    sprite('null', 3)
    Unknown3001(128)

@State
def maef_533_particle():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        Unknown1011(350000, 0)
        Unknown1010(-500000, -300000)
        Unknown1077(30000, -30000)
    sprite('null', 6)
    callSubroutine('maef_color')
    Unknown23067('maef_533slash')
    GFX_0('maef_533_particle_add', -1)

@State
def maef_533_particle_add():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        Unknown4006(2)
    sprite('null', 6)
    Unknown23067('maef_533slash_add')

@State
def maef_522():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        teleportRelativeX(100000)

        def upon_43():
            if (SLOT_48 == 1001):
                sendToLabel(0)
    sprite('null', 32767)
    GFX_0('maef_522_a', -1)
    GFX_0('maef_522_b', -1)
    GFX_0('maef_522_c', -1)
    GFX_0('maef_522_dust', -1)
    label(0)
    sprite('null', 4)
    Unknown26('maef_522_c')
    Unknown26('maef_522_dust')
    Unknown1099(-250)

@State
def maef_522_a():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4013(2)
    sprite('null', 32767)
    callSubroutine('maef_color')
    Unknown23067('maef_522a')

@State
def maef_522_b():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4013(2)
    sprite('null', 32767)
    Unknown23067('maef_522b')

@State
def maef_522_c():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        teleportRelativeX(-30000)
    label(0)
    sprite('null', 3)
    GFX_0('maef_522_c2', -1)
    gotoLabel(0)

@State
def maef_522_c2():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4009(3)
    sprite('null', 30)
    callSubroutine('maef_color')
    Unknown23067('maef_522c')

@State
def maef_522_dust():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        teleportRelativeX(-100000)
    label(0)
    sprite('null', 10)
    callSubroutine('maef_color')
    Unknown4045('maef_522dust', -1)
    gotoLabel(0)

@State
def maef_522_ribon():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef522_03', 16)

@State
def maef_311():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef311_08', 16)

@State
def maef_401():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown3033()
        Unknown4061(1)
    sprite('vrmaef401_00', 3)
    GFX_0('maef_401_aura', 0)
    GFX_0('maef_401_aura2', 0)
    GFX_0('maef_401_aura3', 0)
    GFX_0('maef_401_dust', 0)
    GFX_0('maef_401_ring', 0)
    GFX_0('maef_401_ring2', 0)
    label(0)
    sprite('vrmaef401_01', 3)
    GFX_0('maef_401_aura', 0)
    GFX_0('maef_401_aura2', 0)
    GFX_0('maef_401_aura3', 0)
    sprite('vrmaef401_00', 3)
    GFX_0('maef_401_aura', 0)
    GFX_0('maef_401_aura2', 0)
    GFX_0('maef_401_aura3', 0)
    gotoLabel(0)

@State
def maef_401C():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown3033()
        Unknown4061(1)
        Unknown1072(-30000)
    sprite('vrmaef401_00', 3)
    GFX_0('maef_401_aura', 0)
    GFX_0('maef_401_aura2', 0)
    GFX_0('maef_401_aura3', 0)
    GFX_0('maef_401_dust', 0)
    GFX_0('maef_401_ring', 0)
    GFX_0('maef_401_ring2', 0)
    label(0)
    sprite('vrmaef401_01', 3)
    GFX_0('maef_401_aura', 0)
    GFX_0('maef_401_aura2', 0)
    GFX_0('maef_401_aura3', 0)
    sprite('vrmaef401_00', 3)
    GFX_0('maef_401_aura', 0)
    GFX_0('maef_401_aura2', 0)
    GFX_0('maef_401_aura3', 0)
    gotoLabel(0)

@State
def maef_403():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown3033()
        Unknown4061(1)
        Unknown1072(90000)
        sendToLabelUpon(32, 1)
    sprite('vrmaef401_00', 3)
    GFX_0('maef_401_aura', 0)
    GFX_0('maef_401_aura2', 0)
    GFX_0('maef_401_aura3', 0)
    GFX_0('maef_401_dust', 0)
    GFX_0('maef_401_ring', 0)
    GFX_0('maef_401_ring2', 0)
    label(0)
    sprite('vrmaef401_01', 3)
    GFX_0('maef_401_aura', 0)
    GFX_0('maef_401_aura2', 0)
    GFX_0('maef_401_aura3', 0)
    sprite('vrmaef401_00', 3)
    GFX_0('maef_401_aura', 0)
    GFX_0('maef_401_aura2', 0)
    GFX_0('maef_401_aura3', 0)
    gotoLabel(0)
    label(1)
    sprite('keep', 1)
    Unknown3004(-128)
    loopRest()

@State
def maef_403B():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown3033()
        Unknown4061(1)
        Unknown1072(60000)
        sendToLabelUpon(32, 1)
    sprite('vrmaef401_00', 3)
    GFX_0('maef_401_aura', 0)
    GFX_0('maef_401_aura2', 0)
    GFX_0('maef_401_aura3', 0)
    GFX_0('maef_401_dust', 0)
    GFX_0('maef_401_ring', 0)
    GFX_0('maef_401_ring2', 0)
    label(0)
    sprite('vrmaef401_01', 3)
    GFX_0('maef_401_aura', 0)
    GFX_0('maef_401_aura2', 0)
    GFX_0('maef_401_aura3', 0)
    sprite('vrmaef401_00', 3)
    GFX_0('maef_401_aura', 0)
    GFX_0('maef_401_aura2', 0)
    GFX_0('maef_401_aura3', 0)
    gotoLabel(0)
    label(1)
    sprite('keep', 1)
    Unknown3004(-128)
    loopRest()

@State
def maef_403C():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown3033()
        Unknown4061(1)
        Unknown1072(30000)
        sendToLabelUpon(32, 1)
    sprite('vrmaef401_00', 3)
    GFX_0('maef_401_aura', 0)
    GFX_0('maef_401_aura2', 0)
    GFX_0('maef_401_aura3', 0)
    GFX_0('maef_401_dust', 0)
    GFX_0('maef_401_ring', 0)
    GFX_0('maef_401_ring2', 0)
    label(0)
    sprite('vrmaef401_01', 3)
    GFX_0('maef_401_aura', 0)
    GFX_0('maef_401_aura2', 0)
    GFX_0('maef_401_aura3', 0)
    sprite('vrmaef401_00', 3)
    GFX_0('maef_401_aura', 0)
    GFX_0('maef_401_aura2', 0)
    GFX_0('maef_401_aura3', 0)
    gotoLabel(0)
    label(1)
    sprite('keep', 1)
    Unknown3004(-128)
    loopRest()

@State
def maef_401_aura():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4006(2)
    sprite('null', 60)
    GFX_2('maef_401aura')

@State
def maef_401_aura2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4009(3)
        Unknown4006(2)
    sprite('null', 60)
    callSubroutine('maef_color2')
    Unknown23067('maef_401aura2')

@State
def maef_401_aura3():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4009(3)
        Unknown4006(2)
    sprite('null', 60)
    callSubroutine('maef_color')
    Unknown23067('maef_401aura3')

@State
def maef_401_dust():

    def upon_IMMEDIATE():
        Unknown4006(2)
    sprite('null', 60)
    callSubroutine('maef_color2')
    Unknown23067('maef_401dust')

@State
def maef_401_ring():

    def upon_IMMEDIATE():
        Unknown4006(2)
    sprite('null', 60)
    callSubroutine('maef_color2')
    Unknown23067('maef_401ring')

@State
def maef_401_ring2():

    def upon_IMMEDIATE():
        Unknown4006(2)
    sprite('null', 60)
    callSubroutine('maef_color2')
    Unknown23067('maef_401ring2')

@State
def maef_401_impact():

    def upon_IMMEDIATE():
        Unknown4007(3)
    sprite('null', 1)
    GFX_2('maef_401impact')
    sprite('null', 60)
    Unknown4007(0)

@State
def maef_401_hit():
    sprite('null', 1)
    GFX_1('maef_401hit', -1)

@State
def maef_403_landing():

    def upon_IMMEDIATE():
        Unknown4009(3)
    sprite('null', 60)
    GFX_1('maef_403smoke', -1)
    callSubroutine('maef_color2')
    Unknown4049(1500)
    Unknown4045('maef_403dust', -1)
    callSubroutine('maef_color')
    Unknown4049(1500)
    Unknown4045('maef_403aura', -1)

@State
def maef_311_shadow2():

    def upon_IMMEDIATE():
        teleportRelativeX(200000)
    sprite('null', 20)
    sprite('null', 14)
    sprite('null', 1)
    Unknown36(22)
    Unknown2035(0)
    Unknown35()

@State
def maef_311_shadow2_b():

    def upon_IMMEDIATE():
        teleportRelativeX(160000)
    sprite('null', 20)
    sprite('null', 14)
    sprite('null', 1)
    Unknown36(22)
    Unknown2035(0)
    Unknown35()

@State
def dmyCamera():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown20000(1)

        def upon_43():
            if (SLOT_48 == 3000):
                clearUponHandler(3)

        def upon_3():
            Unknown1086(23)
    sprite('null', 180)

@State
def maef431():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown3033()
        Unknown4061(1)
        Unknown3038(1)
        Unknown2055(15)
    sprite('vrmaef431_00', 30)
    GFX_0('maef431_aura', 0)
    GFX_0('maef431_aura2', 0)
    GFX_0('maef431_aura_add', 0)
    GFX_0('maef431_aura_add2', 0)
    GFX_0('maef431_aura_screw', 0)
    GFX_0('maef431_hold_dust', 0)
    GFX_0('maef431_bloom', -1)

@State
def maef431_aura():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        callSubroutine('maef_color')
        Unknown1073(-204000)
    sprite('null', 25)
    Unknown23067('maef_431aura')

@State
def maef431_aura2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        callSubroutine('maef_color')
        Unknown1073(-204000)
    sprite('null', 25)
    Unknown4054(11)
    Unknown23067('maef_431aura01')

@State
def maef431_aura_add():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown1073(-204000)
        Unknown3001(191)
    sprite('null', 25)
    Unknown23067('maef_431add')

@State
def maef431_aura_add2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown1073(-204000)
        callSubroutine('maef_color2')
    sprite('null', 25)
    Unknown23067('maef_431add00')

@State
def maef431_aura_screw():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4006(2)
        Unknown2005()
        Unknown4003('maef_431aura.DIG', '')
        callSubroutine('3d_color')
        Unknown3033()
        Unknown1073(24000)
    sprite('null', 32767)

@State
def maef431_hold_dust():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        teleportRelativeX(100000)
        Unknown1007(50000)
    sprite('null', 25)
    callSubroutine('maef_color3')
    Unknown4045('maef_431hold_flower', -1)

@State
def maef431_bloom():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        callSubroutine('maef_color')
    sprite('null', 25)
    Unknown23067('maef_431bloom')

@State
def maef431_jump():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown3033()
        Unknown4061(1)
        Unknown2019(100)
    sprite('vrmaef431_10', 3)
    GFX_0('maef431_jump1', 0)
    GFX_0('maef431_jump1add', 0)
    sprite('vrmaef431_11', 3)
    Unknown26('maef431_jump1')
    Unknown26('maef431_jump1add')
    GFX_0('maef431_jump2', 0)
    GFX_0('maef431_jump2add', 0)
    sprite('vrmaef431_12', 2)
    Unknown26('maef431_jump2')
    Unknown26('maef431_jump2add')
    GFX_0('maef431_jump3', 0)
    GFX_0('maef431_jump3add', 0)
    GFX_0('maef431_tornade', -1)
    GFX_0('maef431_dust', -1)
    label(0)
    sprite('vrmaef431_13', 2)
    sprite('vrmaef431_12', 2)
    gotoLabel(0)

@State
def maef431_jump_od():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown3033()
        Unknown4061(1)
        Unknown2019(100)
    sprite('vrmaef431_10', 3)
    GFX_0('maef431_jump1', 0)
    GFX_0('maef431_jump1add', 0)
    sprite('vrmaef431_11', 3)
    Unknown26('maef431_jump1')
    Unknown26('maef431_jump1add')
    GFX_0('maef431_jump2', 0)
    GFX_0('maef431_jump2add', 0)
    sprite('vrmaef431_12', 2)
    Unknown26('maef431_jump2')
    Unknown26('maef431_jump2add')
    GFX_0('maef431_jump3', 0)
    GFX_0('maef431_jump3add', 0)
    GFX_0('maef431_tornade', -1)
    GFX_0('maef431_dust_od', -1)
    label(0)
    sprite('vrmaef431_13', 2)
    sprite('vrmaef431_12', 2)
    gotoLabel(0)

@State
def maef431_jump1():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        callSubroutine('maef_color')
        Unknown1072(33000)
        Unknown1096(800)
    sprite('null', 32767)
    Unknown23067('maef_431lance')

@State
def maef431_jump1add():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown1072(33000)
        Unknown1096(800)
    sprite('null', 32767)
    Unknown23067('maef_431lance_add')

@State
def maef431_jump2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        callSubroutine('maef_color')
        Unknown1072(-3000)
        Unknown1096(950)
    sprite('null', 32767)
    Unknown23067('maef_431lance')

@State
def maef431_jump2add():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown1072(-3000)
        Unknown1096(950)
    sprite('null', 32767)
    Unknown23067('maef_431lance_add')

@State
def maef431_jump3():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        callSubroutine('maef_color')
        Unknown1072(180000)
    sprite('null', 32767)
    Unknown23067('maef_431lance')

@State
def maef431_jump3add():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown1072(180000)
    sprite('null', 32767)
    Unknown23067('maef_431lance_add')

@State
def maef431_tornade():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(1)
        Unknown1099(7)
    sprite('vrmaef431_30', 6)
    sprite('vrmaef431_31', 6)
    sprite('null', 1)
    GFX_0('maef431_tornade2', -1)

@State
def maef431_tornade2():

    def upon_IMMEDIATE():
        callSubroutine('Zanzou_Color')
        Unknown1097(84)
        Unknown1099(7)
    sprite('vrmaef431_32', 10)

@State
def maef431_dust():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
    label(0)
    sprite('null', 2)
    callSubroutine('maef_color')
    Unknown4045('maef_431dust', -1)
    gotoLabel(0)

@State
def maef431_dust_od():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
    label(0)
    sprite('null', 3)
    callSubroutine('maef_color')
    Unknown4045('maef_431dust', -1)
    callSubroutine('maef_color2')
    Unknown4045('maef_431flower', -1)
    gotoLabel(0)

@State
def maef431_fall():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown3033()
        Unknown4061(1)

        def upon_STATE_END():
            Unknown26('maef431_fall_lance')
            Unknown26('maef431_fall_lance_add')
            Unknown26('maef431_fall_bloom')
            Unknown26('maef431_fall_ribon')
            Unknown26('maef431_fall_dust')
    sprite('vrmaef431_20', 2)
    GFX_0('maef431_fall_lance', 0)
    GFX_0('maef431_fall_lance_add', 0)
    GFX_0('maef431_fall_bloom', 0)
    GFX_0('maef431_fall_ribon', 0)
    GFX_0('maef431_fall_dust', 0)
    label(0)
    sprite('vrmaef431_21', 2)
    sprite('vrmaef431_20', 2)
    gotoLabel(0)

@State
def maef431_fall_od():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(2)
        Unknown4009(2)
        Unknown3033()
        Unknown4061(1)

        def upon_STATE_END():
            Unknown26('maef431_fall_lance')
            Unknown26('maef431_fall_lance_add')
            Unknown26('maef431_fall_bloom')
            Unknown26('maef431_fall_ribon')
            Unknown26('maef431_fall_dust')
    sprite('vrmaef431_20', 2)
    GFX_0('maef431_fall_lance', 0)
    GFX_0('maef431_fall_lance_add', 0)
    GFX_0('maef431_fall_bloom', 0)
    GFX_0('maef431_fall_ribon', 0)
    GFX_0('maef431_fall_dust', 0)
    label(0)
    sprite('vrmaef431_21', 2)
    sprite('vrmaef431_20', 2)
    gotoLabel(0)

@State
def maef431_fall_lance():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown4009(2)
        callSubroutine('maef_color3')
    sprite('null', 32767)
    Unknown23067('maef_431fall')

@State
def maef431_fall_lance_add():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
    sprite('null', 32767)
    Unknown23067('maef_431fall_add')

@State
def maef431_fall_bloom():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown4009(2)
        callSubroutine('maef_color')
        Unknown1007(300000)
        Unknown3001(128)
    sprite('null', 32767)
    Unknown23067('maef_431fall_blm')

@State
def maef431_fall_ribon():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('maef_431ribon.DIG', '')
        callSubroutine('maef_color2')
        Unknown1007(18000)
    sprite('null', 32767)

@State
def maef431_fall_dust():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown4009(2)
        Unknown1007(305000)
    label(0)
    sprite('null', 2)
    callSubroutine('maef_color2')
    Unknown4045('maef_431fall_dust', -1)
    gotoLabel(0)

@State
def maef431_crash():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
    sprite('null', 100)
    ScreenShake(48000, 48000)
    callSubroutine('maef_color')
    Unknown4045('maef_431crash_wave', -1)
    GFX_0('maef431_crash_aura', -1)
    GFX_0('maef431_crash_yari', -1)
    GFX_0('maef431_crash_particle', -1)
    GFX_0('maef431_flower_3d', -1)
    GFX_0('maef431_flower_particle', -1)
    GFX_0('maef431_storm', -1)
    GFX_0('maef431_storm2', -1)
    GFX_0('maef431_rock', -1)

@State
def maef431_crash_od():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
    sprite('null', 100)
    ScreenShake(64000, 64000)
    callSubroutine('maef_color')
    Unknown4045('maef_431crash_wave_od', -1)
    GFX_0('maef431_crash_aura', -1)
    GFX_0('maef431_crash_yari_od', -1)
    GFX_0('maef431_crash_particle', -1)
    GFX_0('maef431_flower_3d', -1)
    GFX_0('maef431_flower_particle', -1)
    GFX_0('maef431_storm', -1)
    GFX_0('maef431_storm2', -1)
    GFX_0('maef431_rock', -1)

@State
def maef431_crash_particle():
    sprite('null', 1)
    callSubroutine('3d_color')
    Unknown4045('maef_431crash_blm', -1)
    callSubroutine('maef_color2')
    Unknown4045('maef_431crash_dust', -1)

@State
def maef431_crash_aura():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown3033()
        Unknown4061(1)
    sprite('vrmaef431_40', 6)
    sprite('vrmaef431_41', 6)
    sprite('vrmaef431_42', 6)
    sprite('vrmaef431_43', 6)

@State
def maef431_flower_3d():

    def upon_IMMEDIATE():
        Unknown4007(2)
    sprite('null', 5)
    GFX_0('maef431_flower3', -1)
    GFX_0('maef431_flower4', -1)
    GFX_0('maef431_flower', -1)
    sprite('null', 5)
    GFX_0('maef431_flower2', -1)
    sprite('null', 5)
    GFX_0('maef431_flower', -1)
    sprite('null', 5)
    GFX_0('maef431_flower2', -1)
    sprite('null', 5)
    GFX_0('maef431_flower', -1)
    sprite('null', 5)
    GFX_0('maef431_flower2', -1)
    sprite('null', 100)

@State
def maef431_flower():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown4003('maef_431flower.DIG', '')
        Unknown4015()
        callSubroutine('maef_color')
        Unknown3033()
        Unknown1102(-500, 250)
        Unknown1099(10)
        GFX_0('maef431_flower_b', -1)
    sprite('null', 6)
    sprite('null', 10)
    Unknown4007(0)
    sprite('null', 16)
    Unknown3004(-16)

@State
def maef431_flower_b():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('maef_431flower.DIG', '')
        Unknown4015()
        callSubroutine('maef_color3')
        Unknown3033()
        Unknown4013(2)
    sprite('null', 32)
    Unknown3004(-8)

@State
def maef431_flower2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown4003('maef_431flower2.DIG', '')
        Unknown4015()
        callSubroutine('maef_color')
        Unknown3033()
        Unknown1070(-250, -500)
        Unknown1062(1000, 800)
        Unknown1094(1000, 800)
        Unknown1099(10)
        Unknown3001(128)
        Unknown1011(160000, 80000)
        Unknown1010(-32000, 32000)
        GFX_0('maef431_flower2b', -1)
    sprite('null', 6)
    sprite('null', 10)
    Unknown4007(0)
    sprite('null', 16)
    Unknown4007(0)
    Unknown3004(-8)

@State
def maef431_flower2b():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('maef_431flower2.DIG', '')
        Unknown4015()
        Unknown4013(2)
        callSubroutine('maef_color3')
        Unknown3033()
    sprite('null', 16)
    Unknown3004(-8)
    sprite('null', 16)

@State
def maef431_flower3():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown4003('maef_431flower3.DIG', '')
        Unknown4015()
        callSubroutine('maef_color')
        Unknown3033()
        GFX_0('maef431_flower3b', -1)
    sprite('null', 60)
    Unknown1099(10)
    Unknown3004(-10)

@State
def maef431_flower3b():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('maef_431flower3.DIG', '')
        Unknown4015()
        callSubroutine('maef_color3')
        Unknown3033()
        Unknown4013(2)
    sprite('null', 60)
    Unknown1099(10)
    Unknown3004(-10)

@State
def maef431_flower4():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown4003('maef_431flower4.DIG', '')
        Unknown4015()
        callSubroutine('maef_color')
        Unknown3033()
        Unknown1064(800)
        Unknown1056(1600)
        Unknown1088(1600)
        Unknown1099(10)
        Unknown3001(128)
        Unknown1007(50000)
        GFX_0('maef431_flower4b', -1)
    sprite('null', 16)
    sprite('null', 16)
    Unknown3004(-8)

@State
def maef431_flower4b():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('maef_431flower4.DIG', '')
        Unknown4015()
        Unknown4013(2)
        Unknown4007(2)
        callSubroutine('maef_color3')
        Unknown3033()
    sprite('null', 16)
    Unknown3004(-16)

@State
def maef431_storm():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4003('maef_431storm.DIG', '')
        Unknown4015()
        callSubroutine('maef_color2')
        Unknown3033()
        Unknown1096(1100)
    sprite('null', 6)
    GFX_0('maef431_storm_add', -1)
    sprite('null', 26)
    Unknown4007(0)
    sprite('null', 16)
    Unknown3004(-16)

@State
def maef431_storm_add():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('maef_431storm.DIG', '')
        Unknown4015()
        Unknown4013(2)
        callSubroutine('maef_color3')
        Unknown3033()
    sprite('null', 32)
    Unknown3001(128)
    Unknown3004(-4)

@State
def maef431_storm2():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4003('maef_431storm2.DIG', '')
        Unknown4015()
        callSubroutine('maef_color2')
        Unknown3033()
    sprite('null', 6)
    GFX_0('maef431_storm2_add', -1)
    sprite('null', 10)
    Unknown4007(0)
    sprite('null', 16)
    Unknown3004(-16)

@State
def maef431_storm2_add():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('maef_431storm2.DIG', '')
        Unknown4015()
        Unknown4013(2)
        callSubroutine('maef_color3')
        Unknown3033()
    sprite('null', 16)
    Unknown3001(128)
    Unknown3004(-8)

@State
def maef431_flower_particle():
    sprite('null', 1)
    callSubroutine('maef_color3')
    Unknown4045('maef_431crash_flower', -1)

@State
def maef431_crash_yari():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
    sprite('null', 20)
    teleportRelativeX(17000)
    callSubroutine('maef_color2')
    Unknown23067('maef_431crash')
    GFX_0('maef431_crash_yari_add', -1)

@State
def maef431_crash_yari_add():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
    sprite('null', 20)
    teleportRelativeX(17000)
    GFX_2('maef_431crash_add')

@State
def maef431_crash_yari_od():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown1056(1750)
        Unknown1064(1250)
    sprite('null', 20)
    callSubroutine('maef_color2')
    Unknown23067('maef_431crash')
    GFX_0('maef431_crash_yari_add_od', -1)

@State
def maef431_crash_yari_add_od():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4013(2)
    sprite('null', 20)
    GFX_2('maef_431crash_add')

@State
def maef431_rock():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(3)
        Unknown4003('maef_431crack.DIG', '')
        Unknown3032()
        Unknown23015(2)
        Unknown1056(1750)
    sprite('null', 20)
    GFX_0('maef431_rock_bloom', -1)
    GFX_1('maef_431rock', -1)
    sprite('null', 40)
    Unknown4007(0)
    Unknown3004(-6)

@State
def maef431_rock_bloom():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(3)
    sprite('null', 20)
    Unknown1096(1255)
    callSubroutine('maef_color')
    Unknown4054(2)
    Unknown23067('maef_431rock_blm')
    sprite('null', 40)
    Unknown4007(0)

@State
def maef430_ex():
    sprite('null', 1)
    callSubroutine('maef_color')
    Unknown4045('maef_430ex_dust', -1)
    callSubroutine('maef_color3')
    Unknown4045('maef_430ex_flower', -1)

@State
def maef430():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
    sprite('null', 32767)
    GFX_0('maef430_bloom', -1)
    GFX_0('maef430_aura', -1)
    GFX_0('maef430_dust', -1)

@State
def maef430_aura():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown2054(1)
        Unknown4003('maef_430aura.DIG', '')
        callSubroutine('maef_color2')
        Unknown3033()
        teleportRelativeX(200000)
        Unknown1007(-40000)
    sprite('null', 16)
    Unknown3001(0)
    Unknown3004(64)
    sprite('null', 16)
    Unknown3004(-16)

@State
def maef430_bloom():

    def upon_IMMEDIATE():
        callSubroutine('maef_color')
        Unknown23067('maef_430bloom')
        teleportRelativeX(25000)
        Unknown1007(-20000)
        Unknown2054(1)
    sprite('null', 8)
    Unknown3001(0)
    Unknown3004(32)
    sprite('null', 24)
    sprite('null', 16)
    Unknown3004(-16)

@State
def maef430_dust():
    sprite('null', 1)
    callSubroutine('maef_color')
    Unknown4045('maef_430bloom00', -1)

@State
def maef430_lance():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4061(1)
        Unknown3033()
    sprite('vrmaef430_00', 2)
    sprite('vrmaef430_02', 3)
    sprite('vrmaef430_03', 3)
    sprite('vrmaef430_10', 2)
    sprite('vrmaef430_11', 2)

@State
def maef430_strike():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown1007(168000)
        teleportRelativeX(600000)
    sprite('null', 1)
    GFX_0('maef430_strike_aura', -1)
    GFX_0('maef430_strike_anm', -1)
    GFX_0('maef430_strike_3d', -1)
    GFX_0('maef430_strike_bg', -1)
    GFX_0('maef430_flower', -1)

@State
def maef430_strike_aura():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
    sprite('null', 1)
    GFX_1('maef_430strike_add', -1)
    callSubroutine('maef_color')
    Unknown4045('maef_430strike_blm', -1)
    callSubroutine('maef_color2')
    Unknown4045('maef_430strike_ring00', -1)
    callSubroutine('maef_color3')
    Unknown4045('maef_430strike_aura', -1)
    callSubroutine('maef_color2')
    Unknown4045('maef_430strike_dust', -1)

@State
def maef430_strike_anm():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4061(1)
        Unknown3033()
    sprite('vrmaef430_50', 6)
    sprite('vrmaef430_51', 20)
    Unknown3004(-12)
    Unknown1059(20)

@State
def maef430_strike_3d():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(3)
        Unknown2054(1)
        Unknown4003('maef_430lance.DIG', '')
        Unknown3033()
        Unknown1064(2000)
        Unknown1056(1750)
    sprite('null', 25)
    Unknown3004(-10)

@State
def maef430_strike_bg():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(3)
        Unknown2054(1)
        Unknown4003('maef_430bg.DIG', '')
        callSubroutine('maef_color3')
        Unknown3033()
    sprite('null', 25)
    Unknown1099(10)
    Unknown3004(-10)

@State
def maef430_bg():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
    sprite('null', 1)
    GFX_1('maef_430smoke', -1)
    GFX_0('maef430_bg_aura', -1)

@State
def maef430_bg_aura():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown2054(1)
        Unknown4003('maef_430aura2.DIG', '')
        Unknown3033()
    sprite('null', 32)
    Unknown1096(1500)
    Unknown3001(175)
    Unknown3004(-6)

@State
def maef430_flower():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown3033()
        Unknown4061(1)
    sprite('vrmaef430_60', 16)
    GFX_0('maef430_flower_particle', -1)
    Unknown1099(10)
    sprite('vrmaef430_61', 8)
    sprite('vrmaef430_62', 8)
    Unknown4007(0)
    sprite('vrmaef430_63', 10)
    Unknown3004(-25)

@State
def maef430_flower_dust():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('null', -1)
    callSubroutine('maef_color2')
    Unknown4045('maef_430flower_dust', -1)

@State
def maef430_flower_particle():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        teleportRelativeX(-130000)
    sprite('null', -1)
    callSubroutine('maef_color3')
    Unknown4045('maef_430flower', -1)

@State
def maef430_od():
    sprite('null', -1)
    Unknown1007(164000)
    teleportRelativeX(64000)
    callSubroutine('maef_color3')
    Unknown4045('maef_430_od', -1)

@State
def ma203Shot():

    def upon_IMMEDIATE():
        Unknown3038(1)
        GFX_0('ma203_Shot_poly', -1)
        GFX_0('ma203_Shot_poly_add', -1)
        GFX_0('ma203_Shot_poly2', -1)
        GFX_0('ma203_Shot_particle', -1)
        SLOT_6 = 1
        Unknown2009()
        AttackLevel_(3)
        Damage(2000)
        AttackP1(70)
        AirUntechableTime(24)
        hitstun(19)
        Hitstop(2)
        blockstun(13)
        PushbackX(30400)
        Unknown11001(1, 11, 13)
        Unknown9016(1)
        Unknown2055(300)

        def upon_43():
            if (SLOT_48 == 1003):
                sendToLabel(580)
            if (SLOT_48 == 1004):
                Unknown11056(0)
                sendToLabel(1)
            if (SLOT_48 == 1006):
                Unknown1072(0)
                AirHitstunAnimation(9)
                AirPushbackX(34000)
                AirPushbackY(18000)
                callSubroutine('maef_color3')
                Unknown4045('maef_D_mazzle', -1)
                callSubroutine('maef_color2')
                Unknown4045('maef_D_mazzle_ring', -1)
            if (SLOT_48 == 1007):
                Unknown1072(15000)
                AirHitstunAnimation(11)
                AirPushbackX(10000)
                AirPushbackY(13000)
                HitLow(2)
                callSubroutine('maef_color3')
                Unknown4048(15000)
                Unknown4045('maef_D_mazzle', -1)
                callSubroutine('maef_color2')
                Unknown4048(15000)
                Unknown4045('maef_D_mazzle_ring', -1)
            if (SLOT_48 == 1008):
                Unknown1072(-15000)
                AirHitstunAnimation(9)
                AirPushbackX(34000)
                AirPushbackY(30000)
                callSubroutine('maef_color3')
                Unknown4048(-15000)
                Unknown4045('maef_D_mazzle', -1)
                callSubroutine('maef_color2')
                Unknown4048(-15000)
                Unknown4045('maef_D_mazzle_ring', -1)
            if (SLOT_48 == 1009):
                Unknown1072(20000)
                GroundedHitstunAnimation(18)
                AirHitstunAnimation(18)
                AirPushbackX(37000)
                AirPushbackY(5000)
                Unknown9310(1)
                Unknown11065(1)
                SLOT_57 = 1
                callSubroutine('maef_color3')
                Unknown4048(20000)
                Unknown4045('maef_D_mazzle', -1)
                callSubroutine('maef_color2')
                Unknown4048(20000)
                Unknown4045('maef_D_mazzle_ring', -1)
            if (SLOT_48 == 1011):
                Unknown1072(0)
                GroundedHitstunAnimation(9)
                AirHitstunAnimation(9)
                AirPushbackX(34000)
                AirPushbackY(18000)
                Unknown9310(1)
                Unknown11065(1)
                SLOT_57 = 1
                callSubroutine('maef_color3')
                Unknown4045('maef_D_mazzle', -1)
                callSubroutine('maef_color2')
                Unknown4045('maef_D_mazzle_ring', -1)
            if (SLOT_48 == 1010):
                Unknown1072(40000)
                GroundedHitstunAnimation(9)
                AirHitstunAnimation(9)
                AirPushbackX(34000)
                AirPushbackY(-15000)
                Unknown9310(1)
                SLOT_56 = 1
                SLOT_57 = 1
                callSubroutine('maef_color3')
                Unknown4048(40000)
                Unknown4045('maef_D_mazzle', -1)
                callSubroutine('maef_color2')
                Unknown4048(40000)
                Unknown4045('maef_D_mazzle_ring', -1)
            Unknown1110(70000, 0)
        if SLOT_7:
            AttackLevel_(4)
            Damage(2400)
            ProjectileDurabilityLvl(2)
            AirUntechableTime(60)
            PushbackX(39900)
            blockstun(16)
            Unknown11001(11, 11, 13)
            if (not SLOT_57):
                GroundedHitstunAnimation(9)
                AirHitstunAnimation(9)
            Unknown1096(1500)

        def upon_3():
            if (SLOT_23 < 60000):
                Unknown21015('NmlAtk5B', 1005, 0)
                Unknown21015('NmlAtkAIR5B', 1005, 0)
            if SLOT_56:
                if (SLOT_23 < 180000):
                    Unknown21015('NmlAtk5B', 1005, 0)
                    Unknown21015('NmlAtkAIR5B', 1005, 0)

        def upon_ON_HIT_OR_BLOCK():
            Unknown21015('NmlAtk5B', 1000, 0)
            Unknown21015('NmlAtkAIR5B', 1000, 0)
            GFX_0('ma203_Shot_hit', -1)

        def upon_ON_HIT_OR_BLOCK():
            Unknown21015('NmlAtk5B2nd', 1001, 0)
            Unknown21015('NmlAtkAIR5B2nd', 1001, 0)

        def upon_56():
            Unknown48(25, 2, 62, 3, 2, 62)
            if (not SLOT_62):
                sendToLabel(580)

        def upon_14():
            sendToLabel(580)
    sprite('ma203atk_dummy', 1)
    sprite('ma203atk_dummy', 1)
    if SLOT_7:
        Unknown1019(150)
        YAccel(150)
    label(0)
    sprite('ma203atk_dummy', 1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    clearUponHandler(10)
    Unknown1084(1)
    Unknown2006()
    GFX_0('maef_D_turn', -1)
    SFX_3('mase_03')
    sprite('ma203atk_dummy', 1)
    Unknown1111(70000, 22)
    RefreshMultihit()
    Unknown11001(11, 11, 13)
    AirPushbackX(1000)
    AirPushbackY(28000)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    HitLow(0)
    Unknown9311()
    if SLOT_7:
        Unknown1019(150)
        YAccel(150)

    def upon_ON_HIT_OR_BLOCK():
        Unknown21015('NmlAtk5B2nd', 1001, 0)

    def upon_ON_HIT_OR_BLOCK():
        Unknown21015('NmlAtkAIR5B2nd', 1001, 0)
    label(2)
    sprite('ma203atk_dummy', 1)
    Unknown1019(105)
    YAccel(105)
    loopRest()
    gotoLabel(2)
    label(580)
    sprite('ma203atk_dummy', 1)
    clearUponHandler(43)
    clearUponHandler(3)
    clearUponHandler(10)
    clearUponHandler(11)
    SLOT_7 = 0
    Unknown21015('NmlAtk5B', 1005, 0)
    Unknown21015('NmlAtkAIR5B', 1005, 0)
    Unknown1084(1)
    DisableAttackRestOfMove()

@State
def ma203_Shot_poly():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4008(2)
        if SLOT_7:
            Unknown1096(1500)
    sprite('null', 32767)
    callSubroutine('maef_color3')
    Unknown23067('maef_lance3')
    Unknown3033()
    Unknown4061(1)
    Unknown21004(1)
    Unknown23048('01000000')
    Unknown23051('76726d6165665f6c616e63656c61792e686970000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown23050('1400000000000000')
    Unknown23052('28000000')
    Unknown23049('ffffffffffffff00')

@State
def ma203_Shot_poly_add():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4008(2)
    sprite('null', 32767)
    GFX_2('maef_lance')

@State
def ma203_Shot_poly2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4008(2)
        if SLOT_7:
            Unknown1096(1500)
    sprite('null', 32767)
    callSubroutine('maef_color')
    Unknown23067('maef_lance2')
    Unknown3033()
    callSubroutine('maef_color')
    Unknown23048('01000000')
    Unknown23051('76726d6165665f6c616e63656c61792e686970000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown23050('1400000000000000')
    Unknown23052('3c000000')
    Unknown23049('ffffffffffffffff')

@State
def ma203_Shot_particle():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
    label(0)
    sprite('null', 2)
    callSubroutine('maef_color')
    Unknown4045('maef_lance_smoke', -1)
    callSubroutine('maef_color2')
    Unknown4045('maef_lance_dust', -1)
    gotoLabel(0)

@State
def ma203_Shot_hit():
    sprite('null', 1)
    callSubroutine('maef_color3')
    Unknown4045('maef_D_hit', -1)

@State
def maef_D_turn():
    sprite('null', 1)
    GFX_1('maef_D_turn_add', -1)
    callSubroutine('maef_color2')
    Unknown4049(1500)
    Unknown4045('maef_D_turn00', -1)
    callSubroutine('maef_color2')
    Unknown4049(1500)
    Unknown4045('maef_D_turn_ring', -1)

@State
def EMB_MA_AH():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown2054(1)
        Unknown4003('ef_emb_ma.DIG', '')
        Unknown23015(5)
        Unknown1007(280000)
        Unknown1096(1500)
    sprite('null', 10)
    Unknown3026(-16777216)
    Unknown3025(-65536, 10)
    sprite('null', 10)
    Unknown3025(-55256, 10)
    sprite('null', 10)
    Unknown3025(-19276, 10)
    sprite('null', 10)
    Unknown3025(-65536, 10)
    sprite('null', 80)

@State
def AstralCamera():

    def upon_IMMEDIATE():
        Unknown20000(1)
        Unknown20002(1)
        Unknown20003(1)
        Unknown20004(1)

        def upon_43():
            if (SLOT_48 == 4000):
                sendToLabel(0)
            if (SLOT_48 == 4001):
                sendToLabel(1)
            if (SLOT_48 == 4002):
                sendToLabel(2)
            if (SLOT_48 == 4003):
                sendToLabel(3)
            if (SLOT_48 == 4004):
                sendToLabel(4)
            if (SLOT_48 == 4005):
                sendToLabel(5)
    sprite('null', 32767)
    label(0)
    sprite('null', 32767)
    label(1)
    sprite('null', 20)
    physicsYImpulse(90000)
    sprite('null', 32767)
    Unknown1084(1)
    label(2)
    sprite('null', 5)
    Unknown1000(0)
    teleportRelativeY(0)
    Unknown1084(1)
    Unknown20001(1)
    Unknown20009(900)
    sprite('null', 10)
    Unknown23024(3)
    Unknown20001(0)
    Unknown1086(3)
    Unknown1007(250000)
    Unknown1084(1)
    sprite('null', 32767)
    GFX_0('maef_ah_Ryuhai', -1)
    SFX_0('000_airdash_0')
    label(3)
    sprite('null', 10)
    sprite('null', 5)
    Unknown23024(2)
    sprite('null', 10)
    Unknown23024(3)
    sprite('null', 32767)
    teleportRelativeY(2930000)
    Unknown20001(1)
    label(4)
    sprite('null', 50)
    physicsYImpulse(-50000)
    GFX_0('maef450_yari', -1)
    SFX_3('mase_10')
    SFX_3('mase_10')
    sprite('null', 10)
    physicsYImpulse(-4000)
    sprite('null', 10)
    physicsYImpulse(-2000)
    sprite('null', 40)
    physicsYImpulse(-1000)
    sprite('null', 40)
    Unknown1084(1)
    sprite('null', 30)
    SLOT_11 = 1
    sprite('null', 40)
    GFX_0('maef450_bomb', -1)
    sprite('null', 5)
    GFX_0('maef450_bomb2', -1)
    SFX_3('mase_11')
    SFX_0('016_explode_2')
    SFX_0('016_explode_2')
    sprite('null', 32767)
    GFX_0('maef450_cloud2', -1)
    GFX_0('maef450_cloud', -1)
    label(5)
    sprite('null', 30)
    Unknown1000(0)
    teleportRelativeY(0)
    GFX_0('maef_ah_killwhite', -1)
    Unknown23013(0)
    clearUponHandler(2)
    sprite('null', 32767)
    Unknown20010(0, 700, 0)

@State
def maef450():
    sprite('null', 1)
    Unknown2054(1)
    GFX_0('maef450_circle', -1)
    GFX_0('maef450_lance', -1)
    GFX_0('maef450_aura', -1)
    GFX_0('maef450_wind', -1)

@State
def maef450_circle():
    sprite('null', 1)
    callSubroutine('maef_color')
    Unknown4045('maef_450circle', -1)
    GFX_1('maef_450circle_add', -1)

@State
def maef450_lance():
    sprite('null', 1)
    teleportRelativeX(5000)
    Unknown1007(-10000)
    callSubroutine('maef_color')
    Unknown4045('maef_450lance', -1)
    GFX_1('maef_450lance_add', -1)

@State
def maef450_aura():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown2054(1)
        Unknown4003('maef_450aura.DIG', '')
        callSubroutine('3d_color')
        Unknown3033()
    sprite('null', 30)
    Unknown1056(500)
    Unknown1059(25)
    Unknown3001(0)
    Unknown3004(8)
    sprite('null', 15)
    Unknown1059(0)
    sprite('null', 30)
    Unknown3004(-8)

@State
def maef450_wind():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown2054(1)
        Unknown4003('maef_450wind.DIG', '')
        Unknown23015(11)
        Unknown3032()
    sprite('null', 30)
    Unknown1096(500)
    Unknown1065(250)
    Unknown1099(16)
    Unknown3001(0)
    Unknown3004(8)
    sprite('null', 30)
    Unknown1099(0)
    Unknown3004(0)
    sprite('null', 30)
    Unknown3004(-8)

@State
def maef450_slash():
    sprite('null', 1)
    GFX_0('maef450_zanzou', -1)
    GFX_0('maef450_aura2', -1)
    GFX_0('maef450_wind2', -1)
    GFX_0('maef450_dust', -1)
    GFX_0('maef450_smoke', -1)

@State
def maef450_zanzou():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(3)
        Unknown4009(3)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef450_00', 3)
    sprite('vrmaef450_01', 16)

@State
def maef450_aura2():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(3)
        Unknown4003('maef_450slash.DIG', '')
        callSubroutine('3d_color')
        Unknown3033()
        Unknown1007(256000)
        Unknown1099(15)
    sprite('null', 15)

@State
def maef450_wind2():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(3)
        Unknown2054(1)
        Unknown4003('maef_450wind2.DIG', '')
        Unknown23015(2)
        Unknown1065(1250)
        Unknown3032()
    sprite('null', 32)
    Unknown1099(25)
    Unknown3004(-8)

@State
def maef450_dust():
    sprite('null', 1)
    callSubroutine('maef_color')
    Unknown4045('maef_450dust2', -1)

@State
def maef450_smoke():
    sprite('null', 1)
    teleportRelativeX(90000)
    Unknown4045('maef_450smoke', -1)

@State
def maef450_upper():
    sprite('null', 1)
    teleportRelativeX(-128000)
    GFX_0('maef450_zanzou2', -1)
    GFX_0('maef450_particle', -1)
    GFX_0('maef450_aura3', -1)

@State
def maef450_zanzou2():
    sprite('vrmaef450_10', 20)
    callSubroutine('Zanzou_Color')

@State
def maef450_particle():
    sprite('null', 1)
    callSubroutine('maef_color')
    Unknown4048(40000)
    Unknown4045('maef_450upper', -1)

@State
def maef450_aura3():

    def upon_IMMEDIATE():
        Unknown4003('maef_450upper.DIG', '')
        callSubroutine('3d_color')
        Unknown3033()
        Unknown1072(40000)
    sprite('null', 30)
    Unknown1059(-33)
    Unknown3004(-8)

@State
def maef450_charge():
    sprite('null', 32767)
    Unknown4013(2)
    GFX_0('maef450_charge_lance', -1)
    GFX_0('maef450_charge_lance_add', -1)
    GFX_0('maef450_charge_lance_sub', -1)
    GFX_0('maef450_charge_aura', -1)
    GFX_0('maef450_charge_aura2', -1)
    GFX_0('maef450_charge_bloom', -1)
    GFX_0('maef450_charge_flower', -1)

@State
def maef450_charge_flower():
    sprite('null', 32767)
    Unknown4010(2)
    Unknown4049(2)
    callSubroutine('maef_color2')
    Unknown23067('maef_450charge_flower')

@State
def maef450_charge_lance():
    sprite('null', 32767)
    Unknown4010(2)
    callSubroutine('3d_color')
    Unknown4049(2)
    Unknown23067('maef_450charge')

@State
def maef450_charge_lance_add():
    sprite('null', 32767)
    Unknown4010(2)
    Unknown4049(2)
    GFX_2('maef_450charge_add')

@State
def maef450_charge_lance_sub():
    sprite('null', 32767)
    Unknown4010(2)
    Unknown1007(200000)
    Unknown4049(2)
    GFX_2('maef_450charge_sub')

@State
def maef450_charge_aura():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2007()
        callSubroutine('maef_color2')
        Unknown4003('maef_450charge.DIG', '')
        Unknown3033()
        Unknown1007(-25000)
        Unknown1056(750)
        Unknown1064(1250)
    sprite('null', 32767)

@State
def maef450_charge_aura2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2007()
        callSubroutine('3d_color')
        Unknown4003('maef_450charge2.DIG', '')
        Unknown3032()
        Unknown3001(128)
        Unknown1007(-100000)
        Unknown1064(1000)
        Unknown1056(1500)
    sprite('null', 32767)

@State
def maef450_charge_bloom():

    def upon_IMMEDIATE():
        Unknown4010(2)
        callSubroutine('maef_color')
        Unknown4003('maef_450bloom.DIG', '')
        Unknown3033()
        Unknown3001(64)
        Unknown1007(-25000)
        Unknown1056(1000)
    sprite('null', 32767)

@State
def maef450_throw():
    sprite('null', 3)
    GFX_2('maef_450throw_sub')
    GFX_1('maef_450throw_speed', -1)
    callSubroutine('maef_color2')
    Unknown4045('maef_450throw_dust', -1)
    GFX_0('maef_450_throw_flower', -1)
    callSubroutine('3d_color')
    Unknown4045('maef_450throw', -1)
    callSubroutine('maef_color2')
    Unknown4045('maef_450throw_add', -1)
    callSubroutine('maef_color2')
    Unknown4045('maef_450throw_yari', -1)
    sprite('null', 32767)
    GFX_1('maef_450throw_yari2', -1)

@State
def maef_450_throw_flower():
    sprite('null', 1)
    Unknown1007(60000)
    callSubroutine('maef_color2')
    Unknown4045('maef_450throw_flower', -1)

@State
def maef450_yari():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown4061(0)
        Unknown3032()
        Unknown13044(1)
        Unknown23032(50)
        Unknown23033(50)
        Unknown1086(2)
        Unknown1007(98000)
        Unknown4007(2)
    sprite('maef450_90', 6)
    sprite('maef450_91', 6)
    sprite('maef450_92', 6)
    GFX_0('maef450_yari_dust', -1)
    sprite('maef450_93', 7)
    sprite('maef450_94', 8)
    sprite('maef450_95', 6)
    GFX_0('maef450_yari2_dust', -1)
    sprite('maef450_96', 4)
    sprite('maef450_97', 3)
    sprite('maef450_98', 3)
    sprite('null', 20)
    physicsYImpulse(-4000)
    sprite('null', 10)
    physicsYImpulse(-1000)
    sprite('null', 70)
    GFX_0('maef450_yari2', -1)
    sprite('null', 60)

@State
def maef450_yari2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        GFX_0('maef450_yari2_add', -1)
    sprite('null', 60)
    callSubroutine('maef_color')
    Unknown23067('maef_450kira')
    Unknown1096(1100)
    Unknown1099(-18)

@State
def maef450_yari2_add():

    def upon_IMMEDIATE():
        Unknown4007(2)
    sprite('null', 60)
    Unknown23067('maef_450kira')
    Unknown1096(775)
    Unknown1099(-12)

@State
def maef450_yari_dust():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown1007(-128000)
    sprite('null', 8)
    callSubroutine('maef_color2')
    Unknown4045('maef_450yari_dust', -1)
    GFX_0('maef450_yari_speed', -1)
    sprite('null', 9)
    callSubroutine('maef_color2')
    Unknown4045('maef_450yari_dust', -1)
    sprite('null', 10)
    callSubroutine('maef_color2')
    Unknown4045('maef_450yari_dust', -1)
    sprite('null', 1)
    callSubroutine('maef_color2')
    Unknown4045('maef_450yari_dust', -1)

@State
def maef450_yari2_dust():

    def upon_IMMEDIATE():
        Unknown4007(2)
    sprite('null', 6)
    callSubroutine('maef_color2')
    Unknown4049(1000)
    Unknown4045('maef_450yari2_dust', -1)
    GFX_0('maef450_yari2_speed', -1)
    sprite('null', 6)
    callSubroutine('maef_color2')
    Unknown4049(800)
    Unknown4045('maef_450yari2_dust', -1)
    sprite('null', 6)
    callSubroutine('maef_color2')
    Unknown4049(600)
    Unknown4045('maef_450yari2_dust', -1)
    sprite('null', 6)
    callSubroutine('maef_color2')
    Unknown4049(400)
    Unknown4045('maef_450yari2_dust', -1)
    GFX_0('maef450_yari2_speed2', -1)
    sprite('null', 6)
    callSubroutine('maef_color2')
    Unknown4049(200)
    Unknown4045('maef_450yari2_dust', -1)
    sprite('null', 3)
    sprite('null', 6)
    callSubroutine('maef_color2')
    Unknown4049(150)
    Unknown4045('maef_450yari2_dust', -1)
    sprite('null', 6)
    sprite('null', 6)
    callSubroutine('maef_color2')
    Unknown4049(120)
    Unknown4045('maef_450yari2_dust', -1)
    sprite('null', 6)
    callSubroutine('maef_color2')
    Unknown4049(90)
    Unknown4045('maef_450yari2_dust', -1)

@State
def maef450_yari_speed():

    def upon_IMMEDIATE():
        Unknown4007(2)
    sprite('null', 6)
    GFX_1('maef_450yari_speed', -1)
    sprite('null', 6)
    GFX_1('maef_450yari_speed', -1)
    sprite('null', 6)
    GFX_1('maef_450yari_speed', -1)
    sprite('null', 6)
    GFX_1('maef_450yari_speed', -1)

@State
def maef450_yari2_speed():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown1007(-192000)
    sprite('null', 6)
    GFX_1('maef_450yari_speed2', -1)
    sprite('null', 6)
    GFX_1('maef_450yari_speed2', -1)
    sprite('null', 6)
    GFX_1('maef_450yari_speed2', -1)

@State
def maef450_yari2_speed2():

    def upon_IMMEDIATE():
        Unknown1007(-110000)
    sprite('null', 30)
    GFX_2('maef_450yari_speed3')
    sprite('null', 5)
    Unknown1007(-50000)
    sprite('null', 60)
    Unknown3004(-4)

@State
def maef450_bomb():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown23032(50)
        Unknown23033(50)
        Unknown1086(2)
        Unknown1007(-32000)
    sprite('null', 1)
    GFX_1('maef_450bomb_ring', -1)

@State
def maef450_bomb2():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown23032(50)
        Unknown23033(50)
        Unknown4003('maef_450bomb.DIG', '')
        Unknown3033()
        Unknown1086(2)
        Unknown1007(-32000)
        Unknown2055(120)
    sprite('null', 6)
    Unknown1099(100)
    GFX_1('maef_450bomb', -1)
    sprite('null', 10)
    Unknown1099(10)
    ScreenShake(10000, 10000)
    sprite('null', 10)
    ScreenShake(10000, 10000)
    sprite('null', 10)
    ScreenShake(10000, 10000)
    label(0)
    sprite('null', 10)
    ScreenShake(10000, 10000)
    Unknown1099(4)
    gotoLabel(0)

@State
def maef450_cloud():

    def upon_IMMEDIATE():
        Unknown23015(2)
        Unknown2007()
        Unknown23032(50)
        Unknown23033(50)
        Unknown4003('maef_astral_whirl.DIG', '')
        Unknown3032()
        Unknown1086(2)
        Unknown1007(-150000)
        Unknown2055(120)
    sprite('null', 32767)

@State
def maef450_cloud2():

    def upon_IMMEDIATE():
        Unknown23015(2)
        Unknown2007()
        Unknown23032(50)
        Unknown23033(50)
        Unknown4003('maef_astral_black.DIG', '')
        Unknown1086(2)
        Unknown1007(-225000)
        Unknown2055(120)
        Unknown3032()
    sprite('null', 10)
    Unknown3001(0)
    Unknown3004(12)
    sprite('null', 32767)
    Unknown3004(0)
    Unknown3001(128)

@State
def maef_ah_Ryuhai():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23015(4)
        Unknown6001(1)
        Unknown4007(2)
        Unknown3032()
        Unknown4003('maef_450kirikae', '')
        Unknown1064(-1000)
    sprite('null', 20)

@State
def maef_ah_killwhite():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23015(4)
        Unknown4007(2)
        Unknown23032(50)
        Unknown1096(10000)
        Unknown3033()
        Unknown3001(0)
    sprite('vr_white', 5)
    Unknown3004(51)
    sprite('vr_white', 120)
    sprite('vr_white', 5)
    Unknown3004(-51)

@State
def ma450yari_dummy():

    def upon_IMMEDIATE():
        Unknown4013(2)
        Unknown1000(0)
        teleportRelativeY(0)
    sprite('ma450yari_dummy', 32767)

@State
def maef_440():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef312_00', 3)
    sprite('vrmaef312_01', 15)

@State
def maef_440_slash_3d():

    def upon_IMMEDIATE():
        Unknown4003('maef_440slash.DIG', '')
        callSubroutine('3d_color')
        Unknown3032()
        Unknown1097(500)
        Unknown1079()
        teleportRelativeX(256000)
        Unknown1007(256000)
    sprite('null', 15)
    GFX_0('maef_440_slash_3d_add', -1)
    Unknown1099(50)
    Unknown3004(-16)

@State
def maef_440_slash_3d_add():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4006(2)
        Unknown4025(2)
        Unknown4013(2)
        Unknown4003('maef_440slash.DIG', '')
        Unknown3033()
    sprite('null', 15)

@State
def maef_440_slash1():

    def upon_IMMEDIATE():
        Unknown4007(2)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef440_00', 4)
    sprite('vrmaef440_01', 10)

@State
def maef_440_slash2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef440_10', 4)
    sprite('vrmaef440_11', 10)

@State
def maef_440_slash3():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef440_20', 4)
    sprite('vrmaef440_21', 4)
    sprite('vrmaef440_22', 10)

@State
def maef_440_slash4():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef440_30', 4)
    sprite('vrmaef440_31', 4)

@State
def maef_440_slash5():

    def upon_IMMEDIATE():
        Unknown4007(2)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef440_40', 4)
    sprite('vrmaef440_41', 10)

@State
def maef_440_finish():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        callSubroutine('Zanzou_Color')
        Unknown1057(250)
        teleportRelativeX(-192000)
    sprite('vrmaef440_90', 20)

@State
def maef_440_finish2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        callSubroutine('Zanzou_Color')
        Unknown1057(250)
    sprite('vrmaef440_80', 20)

@State
def BurstDD_Camera():

    def upon_IMMEDIATE():
        Unknown20000(1)
        Unknown20003(1)
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(3)
        Unknown4008(3)
        teleportRelativeX(280000)
    sprite('null', 32767)

@State
def maef_311_shadow2():

    def upon_IMMEDIATE():
        teleportRelativeX(200000)
    sprite('null', 20)
    GFX_1('maef_311shadow2', -1)
    sprite('null', 14)
    sprite('null', 1)
    Unknown36(22)
    Unknown2035(0)
    Unknown35()

@State
def maef_311_shadow2_b():

    def upon_IMMEDIATE():
        teleportRelativeX(160000)
    sprite('null', 20)
    GFX_1('maef_311shadow2', -1)
    sprite('null', 14)
    sprite('null', 1)
    Unknown36(22)
    Unknown2035(0)
    Unknown35()

@State
def maef_601():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(0)
        Unknown1007(704000)
    sprite('null', 30)
    sprite('maef601_00', 2)
    physicsYImpulse(-64000)
    GFX_0('maef_601_dust', -1)
    sprite('maef601_00', 2)
    GFX_0('maef_601_dust', -1)
    sprite('maef601_00', 2)
    GFX_0('maef_601_dust', -1)
    sprite('maef601_00', 2)
    GFX_0('maef_601_dust', -1)
    sprite('maef601_00', 2)
    GFX_0('maef_601_dust', -1)

@State
def maef_601_dust():
    sprite('null', 1)
    callSubroutine('maef_color2')
    Unknown4045('maef_601dust', -1)

@State
def maef_600():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(0)
        Unknown1007(250000)
    sprite('vrmaef600m_00', 30)
    physicsXImpulse(-35000)
    physicsYImpulse(18000)
    setGravity(500)
    Unknown1028(500)