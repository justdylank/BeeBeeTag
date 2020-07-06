@State
def EMB_PH():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown2054(1)
        Unknown3038(1)
        Unknown23015(5)
        Unknown4003('ef_emb_ph.DIG', '')
        Unknown1007(315000)
        Unknown1096(1300)
    sprite('null', 10)
    Unknown3026(-16777216)
    Unknown3025(-16776961, 10)
    sprite('null', 10)
    Unknown3025(-8342273, 10)
    sprite('null', 10)
    Unknown3025(-1, 10)
    sprite('null', 10)
    Unknown3025(-8342273, 10)
    sprite('null', 80)

@State
def EMB_PH_OD():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown2054(1)
        Unknown3038(1)
        Unknown23015(5)
        Unknown4003('ef_emb_ph.DIG', '')
        Unknown1007(315000)
        Unknown1096(1300)
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

@State
def EMB_PH_AH():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown2054(1)
        Unknown23015(5)
        Unknown4003('ef_emb_ph.DIG', '')
        Unknown1007(315000)
        Unknown1096(1300)
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
def ph333_arm():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4011(2)
        Unknown4009(2)
        Unknown23015(8)

        def upon_43():
            if (SLOT_48 == 3331):
                sendToLabel(1)
            if (SLOT_48 == 3332):
                Unknown14()
    sprite('ph333_cutin00', 3)
    GFX_0('ph333_arm_eff_L', 0)
    GFX_0('ph333_arm_eff_R', 1)
    sprite('ph333_cutin01', 32767)
    label(1)
    sprite('ph333_cutin02', 3)
    GFX_0('ph333_arm_eff2_L', 0)
    GFX_0('ph333_arm_eff2_R', 1)
    sprite('ph333_cutin03', 32767)
    Unknown4054(9)
    Unknown4045('phef_333arm_fire3', 2)
    Unknown4054(9)
    Unknown4045('phef_333arm_fire3', 3)

@State
def ph333_arm_eff_L():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4054(6)
        Unknown23067('phef_333arm_circle')
    label(0)
    sprite('null', 3)
    Unknown4054(9)
    Unknown4045('phef_333arm_fire', 100)
    gotoLabel(0)

@State
def ph333_arm_eff_R():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4054(6)
        Unknown23067('phef_333arm_circle')
    label(0)
    sprite('null', 3)
    Unknown4054(9)
    Unknown4045('phef_333arm_fire', 100)
    gotoLabel(0)

@State
def ph333_arm_eff2_L():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown23015(7)
        GFX_2('phef_333arm')
    sprite('null', 60)
    Unknown4054(9)
    Unknown4045('phef_333arm_fire2', 100)

@State
def ph333_arm_eff2_R():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown23015(7)
        GFX_2('phef_333arm')
    sprite('null', 60)
    Unknown4054(9)
    Unknown4045('phef_333arm_fire2', 100)

@State
def Eff_402Fire_PL():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)
        Unknown3033()
        Unknown4061(2)
        Unknown3001(255)
        Unknown1096(2000)
        Unknown23015(3)
    sprite('vr_ph402_10', 3)
    GFX_2('phef402_mcadd_g')
    sprite('vr_ph402_10', 3)
    Unknown1096(1700)
    sprite('vr_ph402_11', 3)
    sprite('vr_ph402_12', 3)
    sprite('vr_ph402_13', 3)

@State
def MidAssault_Atk():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4010(3)
        Unknown4011(3)
        DisableAttackRestOfMove()
        Unknown1056(6000)
        Unknown1064(15000)
        Unknown1007(80000)
        if (SLOT_19 < 450000):
            Unknown1008()
            Unknown1086(22)
            Unknown1009()
        else:
            teleportRelativeX(450000)
        Unknown2053(1)
    sprite('null', 9)
    sprite('null', 4)
    GFX_0('Eff_402', -1)
    SFX_0('016_explode_1')
    sprite('vr_ph_magictest', 5)
    Unknown8003(104, 1, 1)

@State
def Eff_402():

    def upon_IMMEDIATE():
        GFX_2('phef402_mc')
        Unknown4011(3)
        Unknown4009(2)
        Unknown4061(5)
        Unknown1007(-60000)
        Unknown2007()
    sprite('ph402_cutin_a', 2)
    sprite('ph402_cutin_b', 1)
    Unknown3032()
    sprite('ph402_cutin_c', 1)
    sprite('ph402_cutin', 3)
    GFX_0('Eff_402Fire', -1)
    sprite('ph402_cutin', 6)
    Unknown4009(0)
    GFX_1('phef_402_end_g', -1)
    sprite('ph402_cutin', 2)
    Unknown3004(-26)
    GFX_1('phef402_end_sita', -1)
    GFX_1('phef402_end', 0)
    sprite('ph402_cutin', 2)
    GFX_1('phef402_end', 1)
    sprite('ph402_cutin', 2)
    GFX_1('phef402_end', 2)
    sprite('ph402_cutin', 2)
    GFX_1('phef402_end', 3)

@State
def Eff_402Fire():

    def upon_IMMEDIATE():
        GFX_2('phef402_sub')
        Unknown4010(3)
        Unknown4011(3)
        Unknown4009(2)
        Unknown3033()
        Unknown4061(2)
        Unknown3001(160)
        Unknown23015(3)
    sprite('vr_ph402_00', 3)
    Unknown1096(1200)
    sprite('vr_ph402_00', 2)
    Unknown4009(0)
    sprite('vr_ph402_01', 2)
    sprite('vr_ph402_02', 2)
    sprite('vr_ph402_03', 2)
    Unknown3001(255)
    Unknown1096(1200)
    sprite('vr_ph402_04', 1)
    Unknown1096(1100)
    sprite('vr_ph402_05', 5)
    Unknown1096(1000)
    Unknown3004(-51)

@State
def Eff_401():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4061(5)
        Unknown23015(13)
        teleportRelativeX(-140000)
        Unknown3032()
        Unknown3001(0)
        AttackLevel_(4)
        Damage(2000)
        AirUntechableTime(35)
        AirPushbackX(5000)
        AirPushbackY(37500)
        AttackP1(90)
        GroundedHitstunAnimation(9)
        Unknown9266(1)

        def upon_43():
            if (SLOT_48 == 4101):
                AttackLevel_(4)
                Damage(1800)
                AirUntechableTime(60)
                AirPushbackX(2500)
                AirPushbackY(45000)
                AttackP1(70)
                Unknown11042(1)
            if (SLOT_48 == 4102):
                Damage(1900)
                AirUntechableTime(60)
                AirPushbackX(15000)
                AirPushbackY(25000)

                def upon_11():
                    Unknown23029(3, 4103, 0)
    sprite('null', 3)
    GFX_0('Eff_401Fire', -1)
    sprite('null', 3)
    sprite('ph401_cutin', 6)
    Unknown3001(255)
    sprite('ph401_cutin', 3)
    Unknown2001()
    Unknown4009(0)
    Unknown4007(0)
    sprite('ph401_cutin', 10)
    Unknown3004(-51)

@State
def Eff_401Fire():

    def upon_IMMEDIATE():
        GFX_2('phef401_sub')
        Unknown4010(3)
        Unknown4011(3)
        Unknown4009(2)
        Unknown3033()
        Unknown4061(2)
        Unknown23015(14)
        Unknown1096(1300)
        teleportRelativeX(35000)
    sprite('vr_ph401_00', 3)
    sprite('vr_ph401_01', 3)
    teleportRelativeX(22500)
    sprite('vr_ph401_02', 5)
    teleportRelativeX(22500)
    sprite('vr_ph401_03', 3)
    Unknown4009(0)
    sprite('vr_ph401_04', 3)
    sprite('vr_ph401_05', 3)
    GFX_1('phef401_hinoko', -1)
    sprite('vr_ph401_06', 3)
    GFX_1('phef402_end', 0)
    GFX_1('phef402_end', 1)
    GFX_1('phef402_end', 2)
    GFX_1('phef402_end', 3)
    GFX_1('phef402_end', 4)
    sprite('vr_ph401_07', 3)
    sprite('null', 10)

@State
def BurstDDMaster():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        Unknown3038(1)
        Unknown2053(1)
        Unknown1086(3)
        teleportRelativeX(180000)
        Unknown1007(200000)

        def upon_43():
            if (SLOT_48 == 4402):
                if (SLOT_163 > 600000):
                    Unknown1086(22)
                    Unknown1007(200000)
                else:
                    teleportRelativeX(600000)

                def upon_3():
                    if Unknown2065(25):
                        clearUponHandler(3)
                        Unknown23029(3, 4407, 0)
                AttackLevel_(5)
                AttackP1(90)
                AttackP2(90)
                Damage(2000)
                Unknown11064(1)
                MinimumDamagePct(10)
                Unknown30065(0)
                AirUntechableTime(60)
                AirPushbackY(30000)
                YImpluseBeforeWallbounce(1000)
                GroundedHitstunAnimation(9)
                Unknown9266(1)
                Unknown11044(1)
                Unknown2037(1)
                Unknown11069('BurstDDBomb')
                sendToLabel(1)
            if (SLOT_48 == 4404):
                if (SLOT_163 > 600000):
                    Unknown1086(22)
                    Unknown1007(200000)
                else:
                    teleportRelativeY(200000)
                    teleportRelativeX(600000)
                AttackLevel_(5)
                AttackP1(90)
                AttackP2(90)
                Damage(2500)
                MinimumDamagePct(10)
                Unknown30065(0)
                AirUntechableTime(60)
                AirPushbackY(35000)
                GroundedHitstunAnimation(9)
                Unknown9266(1)
                sendToLabel(1)
            if (SLOT_48 == 4401):
                if (SLOT_163 > 600000):
                    Unknown1086(22)
                    teleportRelativeY(200000)
                else:
                    teleportRelativeX(600000)
                AttackLevel_(5)
                Damage(2300)
                AirUntechableTime(60)
                AttackP1(70)
                GroundedHitstunAnimation(9)
                Unknown11042(1)
                Unknown9266(1)
                sendToLabel(2)

        def upon_78():
            if SLOT_2:
                clearUponHandler(78)
                Unknown23029(3, 4403, 0)
    sprite('null', 1)
    sprite('null', 4)
    GFX_0('BurstDDEff', -1)
    GFX_0('BurstDDRevEff', -1)
    sprite('ph402_cutinRev', 6)
    sprite('ph402_cutinRev', 4)
    StartMultihit()
    ExitState()
    label(1)
    sprite('null', 14)
    sprite('null', 4)
    GFX_0('BurstDDEff', -1)
    GFX_0('BurstDDRevEff', -1)
    sprite('ph402_cutinRevex', 2)
    sprite('ph402_cutinRev', 4)
    sprite('ph402_cutinRev', 4)
    Unknown23029(3, 4405, 0)
    StartMultihit()
    ExitState()
    label(2)
    sprite('null', 14)
    sprite('null', 4)
    GFX_0('BurstDDEff', -1)
    GFX_0('BurstDDRevEff', -1)
    sprite('ph402_cutinRevex', 2)
    sprite('ph402_cutinRev', 4)
    sprite('ph402_cutinRev', 4)
    Unknown23029(3, 4406, 0)
    StartMultihit()
    ExitState()

@State
def BurstDDMasterCrushFinish():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        Unknown3038(1)
        Unknown2053(1)
        Unknown1086(3)
        teleportRelativeX(180000)
        Unknown1007(200000)
    sprite('null', 3)
    sprite('null', 4)
    GFX_0('BurstDDEff', -1)
    GFX_0('BurstDDRevEff', -1)
    sprite('ph402_cutinRev', 6)
    sprite('ph402_cutinRev', 4)
    StartMultihit()

@State
def BurstDDEff():

    def upon_IMMEDIATE():
        GFX_2('phef402_mc3')
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(5)
        Unknown1007(100000)
        Unknown1072(90000)
        Unknown2035(1)
    sprite('ph402_cutin_a', 2)
    SFX_0('005_swing_grap_2_2')
    sprite('ph402_cutin_b', 1)
    SFX_0('016_explode_2')
    sprite('ph402_cutin_c', 1)
    sprite('ph402_cutin', 3)
    GFX_0('Eff_402Fire', -1)
    Unknown36(1)
    Unknown1072(90000)
    teleportRelativeX(28000)
    Unknown35()
    sprite('ph402_cutin', 6)
    Unknown4010(0)
    Unknown4009(0)
    sprite('ph402_cutin', 2)
    Unknown3004(-26)
    GFX_1('phef402_end_sita', -1)
    GFX_1('phef402_end', 0)
    sprite('ph402_cutin', 2)
    GFX_1('phef402_end', 1)
    sprite('ph402_cutin', 2)
    GFX_1('phef402_end', 2)
    sprite('ph402_cutin', 2)
    GFX_1('phef402_end', 3)

@State
def BurstDDRevEff():

    def upon_IMMEDIATE():
        GFX_2('phef402_mc2')
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(5)
        Unknown1007(100000)
        Unknown1072(-90000)
        Unknown2035(1)
    sprite('ph402_cutin_aRev', 2)
    sprite('ph402_cutin_bRev', 1)
    sprite('ph402_cutin_cRev', 1)
    sprite('ph402_cutinRev', 3)
    GFX_0('Eff_402Fire', -1)
    Unknown36(1)
    Unknown1072(-90000)
    Unknown1007(-45000)
    teleportRelativeX(-28000)
    Unknown35()
    sprite('ph402_cutinRev', 6)
    Unknown4010(0)
    Unknown4009(0)
    sprite('ph402_cutinRev', 2)
    Unknown3004(-26)
    GFX_1('phef402_end_sita', -1)
    GFX_1('phef402_end', 0)
    sprite('ph402_cutinRev', 2)
    GFX_1('phef402_end', 1)
    sprite('ph402_cutinRev', 2)
    GFX_1('phef402_end', 2)
    sprite('ph402_cutinRev', 2)
    GFX_1('phef402_end', 3)

@State
def BurstDDBomb():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown2010()
        Unknown4011(3)
        Unknown1096(12500)
        AttackLevel_(5)
        Damage(1500)
        AirPushbackX(40000)
        AirPushbackY(20000)
        AirUntechableTime(60)
        Unknown9178(1)
        WallbounceReboundTime(25)
        AirHitstunAfterWallbounce(60)
        MinimumDamagePct(10)
        Unknown30065(0)
        Unknown11066(1)
        Unknown11084(1)
        Unknown3038(1)

        def upon_11():
            Unknown11108(3)
    sprite('null', 40)
    sprite('null', 5)
    Unknown1086(22)
    GFX_0('BurstDDBomb2', -1)
    Unknown36(1)
    Unknown1097(400)
    Unknown1007(-150000)
    Unknown35()
    sprite('vr_ph_magictest', 3)
    ScreenShake(25000, 100000)
    sprite('null', 5)

@State
def BurstDDBomb2():

    def upon_IMMEDIATE():
        Unknown4061(3)
        Unknown4011(3)
        Unknown1096(800)
    sprite('vr_ph400_04', 2)
    Unknown21010(1)
    sprite('vr_ph400_05', 3)
    Unknown1007(200000)
    ScreenShake(10000, 10000)
    Unknown1099(15)
    GFX_0('pheff_400sub2', 1)
    Unknown36(1)
    Unknown1077(-40000, 40000)
    Unknown21010(1)
    Unknown35()
    GFX_1('phef_400_bom', 1)
    GFX_1('phef_400_blm', 1)
    sprite('vr_ph400_07', 2)
    sprite('vr_ph400_08', 2)
    GFX_1('phef321_shock2', -1)
    sprite('vr_ph400_09', 2)
    sprite('vr_ph400_06', 3)
    GFX_0('ph320BombEff_Circle', -1)
    Unknown36(1)
    Unknown21010(1)
    Unknown1077(20000, 30000)
    Unknown1097(-600)
    Unknown35()
    GFX_0('phEff400_corebom', 0)
    Unknown3004(-51)

@State
def phef_340_fire():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(2)
        Unknown3033()
        teleportRelativeX(-32000)
        Unknown1007(8000)
    sprite('vr_ph340_07', 3)
    GFX_1('phef_340fire_ground', 0)
    sprite('vr_ph340_08', 4)
    Unknown4049(1250)
    Unknown4045('phef_340fire', 0)
    Unknown4049(1000)
    Unknown4045('phef_340fire', 1)
    sprite('vr_ph340_10', 2)
    Unknown4049(750)
    Unknown4045('phef_340fire', 0)
    Unknown4049(500)
    Unknown4045('phef_340fire', 1)
    sprite('vr_ph340_11', 2)
    Unknown4049(250)
    Unknown4045('phef_340fire', 0)
    GFX_1('phef_340fire_add', 1)
    sprite('vr_ph340_12', 2)
    sprite('vr_ph340_13', 4)
    sprite('vr_ph340_14', 4)
    sprite('vr_ph340_15', 4)

@State
def CrossBurst_Bomb():

    def upon_IMMEDIATE():
        Unknown4061(3)
        Unknown4011(3)
        Unknown21010(1)
        Unknown1096(1200)
        teleportRelativeX(250000)
        Unknown1007(100000)
    sprite('vr_ph400_04', 2)
    sprite('vr_ph400_05', 3)
    Unknown1007(150000)
    ScreenShake(10000, 10000)
    Unknown1099(15)
    GFX_0('pheff_400sub2', 1)
    Unknown36(1)
    Unknown21010(1)
    Unknown1077(-40000, 40000)
    Unknown35()
    GFX_1('phef_400_bom', 1)
    GFX_1('phef_400_blm', 1)
    sprite('vr_ph400_07', 2)
    sprite('vr_ph400_08', 2)
    GFX_1('phef321_shock2', -1)
    sprite('vr_ph400_09', 2)
    sprite('vr_ph400_06', 3)
    GFX_0('ph320BombEff_Circle', -1)
    Unknown36(1)
    Unknown21010(1)
    Unknown1077(20000, 30000)
    Unknown1097(-600)
    Unknown35()
    GFX_0('phEff400_corebom', 0)
    Unknown3004(-51)

@State
def ph001Eff():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('pheff001_fire00', '')
        Unknown1096(450)
        Unknown3001(180)
        Unknown1007(275000)
        teleportRelativeX(-65000)
        Unknown2008()
        GFX_2('phef001_hinoko')
    sprite('null', 5)
    Unknown3001(0)
    Unknown3004(30)
    label(0)
    sprite('null', 25)
    physicsYImpulse(300)
    Unknown3004(0)
    Unknown1099(-2)
    sprite('null', 5)
    Unknown1099(-1)
    physicsYImpulse(150)
    sprite('null', 25)
    physicsYImpulse(-300)
    Unknown1099(2)
    sprite('null', 5)
    Unknown1099(1)
    physicsYImpulse(-150)
    gotoLabel(0)

@State
def ph032FireEff():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2054(1)
        Unknown3032()
        Unknown4061(2)
        Unknown3033()
        teleportRelativeX(50000)
    sprite('vr_ph32_00', 3)
    GFX_0('ph032FireEffSub', -1)
    GFX_1('phef_dash_aura', 0)
    GFX_1('phef_dash_aura', 1)
    GFX_1('phef_dash_aura', 2)
    GFX_1('phef_dash_aura', 3)
    GFX_1('phef_dash_aura', 4)
    GFX_1('phef_dash_aura', 5)
    GFX_1('phef_dash_aura', 6)
    sprite('vr_ph32_01', 3)
    sprite('vr_ph32_02', 3)
    sprite('vr_ph32_03', 3)
    sprite('vr_ph32_04', 3)
    sprite('vr_ph32_05', 3)
    Unknown3004(-25)
    sprite('vr_ph32_06', 3)
    sprite('vr_ph32_07', 3)

@State
def ph032FireEffSub():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2054(1)
        Unknown3032()
        Unknown4061(0)
    sprite('vr_ph32_10', 3)
    Unknown3025(0, 16)
    sprite('vr_ph32_11', 3)
    sprite('vr_ph32_12', 3)
    sprite('vr_ph32_13', 3)
    Unknown3004(-25)
    sprite('vr_ph32_14', 3)
    sprite('vr_ph32_15', 3)

@State
def ph032FireEff2():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2054(1)
        Unknown3032()
        Unknown4061(2)
        Unknown3033()
        teleportRelativeX(50000)
    sprite('vr_ph32_00', 3)
    sprite('vr_ph32_01', 3)
    sprite('vr_ph32_02', 3)
    sprite('vr_ph32_03', 3)
    sprite('vr_ph32_04', 3)
    sprite('vr_ph32_05', 3)
    Unknown3004(-25)
    sprite('vr_ph32_06', 3)
    sprite('vr_ph32_07', 3)

@State
def ph035FireEff():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2054(1)
        Unknown3032()
        Unknown4061(2)
        Unknown3033()
    sprite('vr_ph35_00', 3)
    GFX_0('ph035FireEffSub', -1)
    GFX_1('phef_dash_aura', 0)
    GFX_1('phef_dash_aura', 1)
    GFX_1('phef_dash_aura', 2)
    GFX_1('phef_dash_aura', 3)
    GFX_1('phef_dash_aura', 4)
    GFX_1('phef_dash_aura', 5)
    GFX_1('phef_dash_aura', 6)
    sprite('vr_ph35_01', 3)
    sprite('vr_ph35_02', 3)
    sprite('vr_ph35_04', 3)
    sprite('vr_ph35_05', 2)
    sprite('vr_ph35_06', 2)
    sprite('vr_ph35_07', 2)

@State
def ph035FireEffSub():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2054(1)
        Unknown3032()
        Unknown4061(0)
    sprite('vr_ph035_10', 3)
    Unknown3025(0, 16)
    sprite('vr_ph035_11', 3)
    sprite('vr_ph035_12', 3)
    Unknown3004(-25)
    sprite('vr_ph035_13', 3)
    sprite('vr_ph035_14', 3)

@State
def ph035FireEff2():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2054(1)
        Unknown3032()
        Unknown4061(2)
        Unknown3033()
    sprite('vr_ph35_00', 3)
    sprite('vr_ph35_02', 3)
    sprite('vr_ph35_05', 3)
    Unknown3004(-25)
    sprite('vr_ph35_06', 3)
    sprite('vr_ph35_07', 3)

@State
def phChangeFireEff():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2054(1)
        Unknown3032()
        Unknown4061(2)
        Unknown3033()
        teleportRelativeX(50000)
    sprite('vr_ph32_00', 3)
    GFX_0('ph032FireEffSub', -1)
    GFX_1('phef_dash_aura', 0)
    GFX_1('phef_dash_aura', 1)
    GFX_1('phef_dash_aura', 2)
    GFX_1('phef_dash_aura', 3)
    GFX_1('phef_dash_aura', 4)
    GFX_1('phef_dash_aura', 5)
    GFX_1('phef_dash_aura', 6)
    sprite('vr_ph32_01', 3)
    sprite('vr_ph32_02', 3)
    sprite('vr_ph32_03', 3)
    sprite('vr_ph32_04', 3)
    sprite('vr_ph32_05', 3)
    Unknown3004(-25)
    sprite('vr_ph32_06', 3)
    sprite('vr_ph32_07', 3)

@State
def phChangeFireEff2():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2054(1)
        Unknown3032()
        Unknown4061(2)
        Unknown3033()
        teleportRelativeX(100000)
    sprite('vr_ph32_00', 3)
    sprite('vr_ph32_01', 3)
    sprite('vr_ph32_02', 3)
    sprite('vr_ph32_03', 3)
    sprite('vr_ph32_04', 3)
    sprite('vr_ph32_05', 3)
    Unknown3004(-25)
    sprite('vr_ph32_06', 3)
    sprite('vr_ph32_07', 3)

@State
def ph216_eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown2054(1)
        Unknown3033()
        Unknown1007(130000)
        teleportRelativeX(235000)
        Unknown1056(1400)
        Unknown1064(1200)
        Unknown4061(2)
        Unknown23015(1)
    sprite('vr_ph216_00', 4)
    GFX_0('ph216_effBG', -1)
    SFX_0('015_blaze_0')
    sprite('vr_ph216_01', 4)
    GFX_1('phef216_smoke', -1)
    Unknown4007(0)
    sprite('vr_ph216_02', 3)
    sprite('vr_ph216_03', 3)
    sprite('vr_ph216_04', 2)
    sprite('vr_ph216_05', 2)

@State
def ph216_effBG():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown1096(2000)
    sprite('vr_ph216bloom_00', 15)
    sprite('vr_ph216bloom_00', 10)
    Unknown3004(-26)

@State
def ph202_eff():

    def upon_IMMEDIATE():
        Unknown4003('ph202eff_00.DIG', '')
        Unknown4007(2)
        Unknown2054(1)
        Unknown3032()
        Unknown1007(210000)
        teleportRelativeX(205000)
        Unknown1056(700)
        Unknown1064(600)
    sprite('null', 3)
    GFX_1('phef202_patchin', -1)
    SFX_0('015_blaze_0')
    sprite('null', 3)
    Unknown4007(0)
    sprite('null', 5)
    GFX_1('phef202_hinoko', -1)
    GFX_0('ph202_effSub', -1)

@State
def ph202_effSub():

    def upon_IMMEDIATE():
        Unknown3038(1)
        teleportRelativeX(20000)
    sprite('vr_ph202effpos_00', 3)
    GFX_0('phCmnFireEff', 0)
    Unknown36(1)
    Unknown2005()
    Unknown1096(700)
    Unknown1007(-25000)
    Unknown35()
    sprite('vr_ph202effpos_00', 3)
    GFX_0('phCmnFireEff', 1)
    Unknown36(1)
    Unknown1056(900)
    Unknown1064(-700)
    Unknown1007(32500)
    Unknown35()
    sprite('vr_ph202effpos_00', 3)
    GFX_0('phCmnFireEff', 2)
    Unknown36(1)
    Unknown2005()
    Unknown1096(700)
    Unknown1007(-22000)
    Unknown35()

@State
def ph200_eff():

    def upon_IMMEDIATE():
        Unknown4003('ph200eff_00.DIG', '')
        Unknown4007(2)
        Unknown2054(1)
        Unknown3032()
        Unknown3038(1)
        Unknown1007(300000)
        teleportRelativeX(100000)
        Unknown1056(1400)
        Unknown1064(950)
        Unknown1073(20000)
    sprite('null', 3)
    sprite('null', 3)
    Unknown4007(0)
    sprite('null', 16)
    GFX_0('ph200_effSub', -1)

@State
def ph200_effSub():

    def upon_IMMEDIATE():
        Unknown3038(1)
        teleportRelativeX(20000)
    sprite('vr_ph200effpos_00', 2)
    GFX_1('phefcmn_fallwater', 0)
    sprite('vr_ph200effpos_00', 2)
    GFX_1('phefcmn_fallwater', 1)
    sprite('vr_ph200effpos_00', 2)
    GFX_1('phefcmn_fallwater', 2)

@State
def ph210_eff():

    def upon_IMMEDIATE():
        Unknown4003('ph210eff_00.DIG', '')
        Unknown2054(1)
        Unknown3032()
        Unknown1007(324000)
        teleportRelativeX(-40000)
        Unknown1096(900)
        Unknown1072(-15000)
        Unknown4007(2)
        Unknown3038(1)
    sprite('null', 3)
    GFX_0('ph210_effSub', -1)
    sprite('null', 11)
    Unknown4007(0)
    sprite('null', 8)

@State
def ph210_effSub():

    def upon_IMMEDIATE():
        Unknown3038(1)
    sprite('vr_ph210effpos_00', 1)
    GFX_1('phefcmn_fallwater', 0)
    sprite('vr_ph210effpos_00', 1)
    GFX_1('phefcmn_fallwater', 1)
    sprite('vr_ph210effpos_00', 1)
    GFX_1('phefcmn_fallwater', 2)
    sprite('vr_ph210effpos_00', 1)
    GFX_1('phefcmn_fallwater', 3)
    sprite('vr_ph210effpos_00', 1)
    GFX_1('phefcmn_fallwater', 4)

@State
def ph212_eff():

    def upon_IMMEDIATE():
        Unknown4003('ph202eff_00.DIG', '')
        Unknown4007(2)
        Unknown2054(1)
        Unknown3032()
        Unknown1007(330000)
        teleportRelativeX(175000)
        Unknown1056(900)
        Unknown1064(750)
        Unknown1072(-14500)
    sprite('null', 3)
    GFX_1('phef202_patchin', -1)
    SFX_0('015_blaze_0')
    sprite('null', 3)
    Unknown4007(0)
    sprite('null', 5)
    GFX_1('phef202_hinoko', -1)
    GFX_0('ph212_effSub', -1)

@State
def ph212_effSub():

    def upon_IMMEDIATE():
        Unknown3038(1)
    sprite('vr_ph212effpos_00', 2)
    GFX_0('phCmnFireEff', 0)
    Unknown36(1)
    Unknown2005()
    Unknown1096(800)
    Unknown1007(-60000)
    Unknown35()
    sprite('vr_ph212effpos_00', 2)
    GFX_0('phCmnFireEff', 1)
    Unknown36(1)
    Unknown1096(800)
    Unknown1064(-700)
    teleportRelativeX(40000)
    Unknown1072(7500)
    Unknown35()
    sprite('vr_ph212effpos_00', 2)
    GFX_0('phCmnFireEff', 2)
    Unknown36(1)
    Unknown2005()
    Unknown1096(900)
    teleportRelativeX(-100000)
    Unknown1007(-100000)
    Unknown35()

@State
def ph201_eff():

    def upon_IMMEDIATE():
        Unknown4003('ph201eff_00.DIG', '')
        Unknown4007(2)
        Unknown2054(1)
        Unknown3032()
        Unknown1007(270000)
        teleportRelativeX(100000)
        Unknown3038(1)
    sprite('null', 3)
    Unknown1096(700)
    sprite('null', 9)
    Unknown4007(0)
    GFX_0('ph201_effSub', -1)
    Unknown1096(850)
    sprite('null', 4)
    sprite('null', 10)
    Unknown3004(-26)

@State
def ph201_effSub():

    def upon_IMMEDIATE():
        Unknown3038(1)
        teleportRelativeX(75000)
        Unknown1007(-50000)
    sprite('vr_ph201effpos_00', 2)
    GFX_1('phef201_kira', 0)
    sprite('vr_ph201effpos_00', 2)
    GFX_1('phef201_kira', 1)
    sprite('vr_ph201effpos_00', 2)
    GFX_1('phef201_kira', 2)
    sprite('vr_ph201effpos_00', 2)
    GFX_1('phef201_kira', 3)
    sprite('vr_ph201effpos_00', 2)
    GFX_1('phef201_kira', 4)
    sprite('vr_ph201effpos_00', 2)
    GFX_1('phef201_kira', 5)

@State
def ph230_eff():

    def upon_IMMEDIATE():
        Unknown4003('ph230eff_00.DIG', '')
        Unknown4007(2)
        Unknown2054(1)
        Unknown3032()
        teleportRelativeX(20000)
        Unknown1007(50000)
        Unknown1064(700)
        Unknown1056(600)
        Unknown1072(15000)
        Unknown3038(1)
    sprite('vr_ph202effpos_00', 4)
    GFX_1('phef230_sibuki', -1)
    sprite('vr_ph202effpos_00', 2)
    Unknown4007(0)
    Unknown1097(50)
    sprite('vr_ph202effpos_00', 2)
    GFX_1('phef230_sibuki', -1)
    Unknown1097(50)
    sprite('vr_ph202effpos_00', 16)

@State
def ph231_eff():

    def upon_IMMEDIATE():
        Unknown4003('ph201eff_00.DIG', '')
        Unknown4007(2)
        Unknown2054(1)
        Unknown3032()
        teleportRelativeX(120000)
        Unknown1007(150000)
        Unknown1072(10000)
        Unknown3038(1)
    sprite('null', 3)
    Unknown1096(400)
    sprite('null', 3)
    GFX_0('ph231_effSub', -1)
    Unknown1096(550)
    sprite('null', 6)
    Unknown4007(0)
    sprite('null', 4)
    sprite('null', 10)
    Unknown3004(-26)

@State
def ph231_effSub():

    def upon_IMMEDIATE():
        Unknown3038(1)
        teleportRelativeX(75000)
        Unknown1007(-50000)
    sprite('vr_ph201effpos_00', 2)
    GFX_1('phef201_kira', 0)
    sprite('vr_ph201effpos_00', 2)
    GFX_1('phef201_kira', 1)
    sprite('vr_ph201effpos_00', 2)
    GFX_1('phef201_kira', 2)
    sprite('vr_ph201effpos_00', 2)
    GFX_1('phef201_kira', 3)

@State
def ph235_eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4061(2)
        Unknown3033()
        Unknown1096(1900)
        teleportRelativeX(275000)
        Unknown1007(-10000)
        Unknown2005()
    sprite('vr_ph235_10', 4)
    SFX_0('015_blaze_0')
    GFX_1('phef232_sub', 0)
    GFX_1('phef232_sub', 1)
    GFX_1('phef232_sub', 2)
    GFX_1('phef232_sub', 3)
    GFX_1('phef232_sub', 4)
    GFX_1('phef232_sub', 5)
    GFX_1('phef232_sub', 6)
    sprite('vr_ph235_11', 4)
    Unknown4007(0)
    sprite('vr_ph235_12', 4)
    sprite('vr_ph235_13', 4)
    sprite('vr_ph235_14', 4)
    sprite('vr_ph235_15', 4)
    sprite('vr_ph235_16', 4)

@State
def ph250_eff():

    def upon_IMMEDIATE():
        Unknown4003('ph250eff_00.DIG', '')
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        Unknown3032()
        Unknown1007(217000)
        teleportRelativeX(75000)
        Unknown1096(850)
        Unknown3038(1)
    sprite('null', 3)
    sprite('null', 19)
    GFX_0('ph250_effSub', -1)
    Unknown4007(0)
    Unknown4010(0)

@State
def ph250_effSub():

    def upon_IMMEDIATE():
        Unknown3038(1)
        teleportRelativeX(20000)
        Unknown1007(100000)
    sprite('vr_ph200effpos_00', 2)
    GFX_0('phCmnWaterEff', 0)
    Unknown36(1)
    Unknown1096(450)
    Unknown1007(-25000)
    Unknown1073(-5000)
    Unknown35()
    sprite('vr_ph200effpos_00', 2)
    GFX_0('phCmnWaterEff', 1)
    Unknown36(1)
    Unknown1056(550)
    Unknown1064(-750)
    Unknown1007(40000)
    Unknown35()

@State
def ph252_eff():

    def upon_IMMEDIATE():
        Unknown4003('ph202eff_00.DIG', '')
        Unknown4007(2)
        Unknown2054(1)
        Unknown3032()
        Unknown1007(270000)
        teleportRelativeX(175000)
        Unknown1056(600)
        Unknown1064(700)
    sprite('null', 3)
    Unknown4010(2)
    GFX_1('phef202_patchin', -1)
    SFX_0('015_blaze_0')
    sprite('null', 3)
    Unknown4007(0)
    Unknown4010(0)
    sprite('null', 5)
    GFX_1('phef202_hinoko', -1)
    GFX_0('ph252_effSub', -1)

@State
def ph252_effSub():

    def upon_IMMEDIATE():
        Unknown3038(1)
        teleportRelativeX(20000)
    sprite('vr_ph202effpos_00', 3)
    GFX_0('phCmnFireEff', 0)
    Unknown36(1)
    Unknown2005()
    Unknown1096(600)
    Unknown1007(-25000)
    Unknown35()
    sprite('vr_ph202effpos_00', 3)
    GFX_0('phCmnFireEff', 1)
    Unknown36(1)
    Unknown1056(800)
    Unknown1064(-600)
    Unknown1007(32500)
    Unknown35()
    sprite('vr_ph202effpos_00', 3)
    GFX_0('phCmnFireEff', 2)
    Unknown36(1)
    Unknown2005()
    Unknown1096(600)
    Unknown1007(-22000)
    teleportRelativeX(-22000)
    Unknown35()

@State
def ph253_eff():

    def upon_IMMEDIATE():
        Unknown4003('ph253eff_00.DIG', '')
        Unknown4007(2)
        Unknown2054(1)
        Unknown3032()
        Unknown1007(270000)
        teleportRelativeX(-90000)
        teleportRelativeX(100000)
        Unknown1007(50000)
        Unknown1073(-20000)
        Unknown3038(1)
    sprite('null', 3)
    GFX_0('ph253_effSub', -1)
    sprite('null', 12)
    Unknown4007(0)

@State
def ph253_effSub():

    def upon_IMMEDIATE():
        Unknown3038(1)
        Unknown1007(-100000)
    sprite('vr_ph200effpos_00', 2)
    GFX_1('phefcmn_fallwater', 0)
    GFX_1('phefcmn_fallwater', 1)
    GFX_1('phefcmn_fallwater', 2)

@State
def ph255_eff():

    def upon_IMMEDIATE():
        Unknown4003('ph202eff_00.DIG', '')
        Unknown4007(2)
        Unknown2054(1)
        Unknown3032()
        Unknown1007(210000)
        teleportRelativeX(125000)
        Unknown1056(700)
        Unknown1064(800)
        Unknown1072(40000)
    sprite('null', 3)
    GFX_1('phef202_patchin', -1)
    SFX_0('015_blaze_0')
    sprite('null', 3)
    Unknown4007(0)
    sprite('null', 5)
    GFX_1('phef202_hinoko', -1)
    GFX_0('ph255_effSub', -1)

@State
def ph255_effSub():

    def upon_IMMEDIATE():
        Unknown3038(1)
        teleportRelativeX(20000)
    sprite('vr_ph202effpos_00', 3)
    GFX_0('phCmnFireEff', 0)
    Unknown36(1)
    Unknown2005()
    Unknown1096(700)
    Unknown1007(-100000)
    Unknown1072(-40000)
    Unknown35()
    sprite('vr_ph202effpos_00', 3)
    GFX_0('phCmnFireEff', 1)
    Unknown36(1)
    Unknown1056(700)
    Unknown1064(-700)
    Unknown1072(20000)
    teleportRelativeX(-50000)
    Unknown1007(-140000)
    Unknown35()
    sprite('vr_ph202effpos_00', 3)
    GFX_0('phCmnFireEff', 2)
    Unknown36(1)
    Unknown2005()
    Unknown1096(800)
    Unknown1007(-300000)
    teleportRelativeX(100000)
    Unknown1072(-40000)
    Unknown35()

@State
def ph251_eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        Unknown3032()
        Unknown1007(289800)
        teleportRelativeX(20000)
    sprite('vr_ph254_00', 2)
    GFX_1('phef201_kira', 0)
    GFX_1('phef201_kira', 1)
    GFX_1('phef201_kira', 2)
    GFX_1('phef201_kira', 3)
    GFX_1('phef201_kira', 4)
    GFX_1('phef201_kira', 5)
    GFX_1('phef201_kira', 6)
    Unknown1099(3)
    sprite('vr_ph254_00', 1)
    sprite('vr_ph254_00', 1)
    Unknown1097(300)
    sprite('vr_ph254_01', 3)
    sprite('vr_ph254_02', 3)
    Unknown3004(-22)
    Unknown4010(0)
    Unknown4007(0)
    sprite('vr_ph254_03', 3)
    sprite('vr_ph254_04', 3)

@State
def ph251_effSub():

    def upon_IMMEDIATE():
        Unknown3038(1)
        teleportRelativeX(75000)
        Unknown1007(-50000)
    sprite('vr_ph201effpos_00', 2)
    GFX_1('phef201_kira', 0)
    sprite('vr_ph201effpos_00', 2)
    GFX_1('phef201_kira', 1)
    sprite('vr_ph201effpos_00', 2)
    GFX_1('phef201_kira', 2)
    sprite('vr_ph201effpos_00', 2)
    GFX_1('phef201_kira', 3)

@State
def phCmnWaterEff():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2054(1)
        Unknown3032()
    sprite('null', 10)
    Unknown1099(1)
    GFX_1('phefcmn_fallwater', -1)
    Unknown3004(-8)
    sprite('null', 6)
    Unknown1099(15)

@State
def phCmnFireEff():

    def upon_IMMEDIATE():
        Unknown4003('phCmneff_fire00', '')
        Unknown21010(1)
        Unknown2054(1)
        Unknown3032()
    sprite('null', 7)
    sprite('null', 5)
    Unknown3004(-51)

@State
def DriveAtk_RRB():

    def upon_IMMEDIATE():
        Unknown2009()
        Unknown4011(3)
        JumpCancel_(0)
        Unknown1056(6000)
        Unknown1064(10000)
        Unknown1007(375000)
        Unknown2053(1)
        if (SLOT_163 > 150000):
            if (SLOT_163 < 450000):
                Unknown1008()
                Unknown1086(22)
                Unknown1009()
            else:
                teleportRelativeX(450000)
        else:
            teleportRelativeX(150000)
        AttackLevel_(5)
        Damage(1700)
        AttackP1(100)
        AttackP2(90)
        AirPushbackX(1500)
        AirPushbackY(50000)
        Hitstop(6)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirUntechableTime(60)
        Unknown9190(1)
        Unknown9118(30)
        AirPushbackX(3500)
        AirPushbackY(-80000)
        HitOverhead(2)
        Unknown3038(1)
        Unknown23013(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)

        def upon_43():
            if (SLOT_48 == 9001):
                clearUponHandler(43)
                clearUponHandler(2)
                sendToLabel(2)
    sprite('vr_ph_magictest', 17)
    GFX_0('phEff_RRB', -1)
    Unknown38(4, 1)
    SFX_3('phse_04')
    SFX_0('019_quake_1')
    StartMultihit()
    physicsYImpulse(5000)
    setGravity(500)
    sprite('vr_ph_magictest', 32767)
    physicsYImpulse(-150000)
    label(1)
    sprite('vr_ph_magictest', 5)
    Unknown21007(4, 32)
    GFX_0('Eff_RRNsub2', -1)
    Unknown36(1)
    Unknown1007(180000)
    Unknown1073(25000)
    Unknown1097(500)
    Unknown35()
    StartMultihit()
    SFX_0('016_explode_2')
    Unknown23029(3, 6003, 0)
    sprite('vr_ph_magictest', 5)
    GFX_0('Eff_RRNsub2', -1)
    Unknown36(1)
    Unknown1007(60000)
    Unknown1073(15000)
    Unknown1099(30)
    Unknown35()
    ExitState()
    label(2)
    sprite('null', 10)
    Unknown3004(-23)
    ExitState()

@State
def DriveAtk_RRB_Lv2():

    def upon_IMMEDIATE():
        Unknown2009()
        Unknown4011(3)
        JumpCancel_(0)
        Unknown1056(6000)
        Unknown1064(10000)
        Unknown1007(375000)
        Unknown2053(1)
        if (SLOT_163 > 150000):
            if (SLOT_163 < 450000):
                Unknown1008()
                Unknown1086(22)
                Unknown1009()
            else:
                teleportRelativeX(450000)
        else:
            teleportRelativeX(150000)
        AttackLevel_(5)
        Damage(1900)
        AttackP1(100)
        AttackP2(90)
        AirPushbackX(1500)
        AirPushbackY(50000)
        Hitstop(6)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirUntechableTime(60)
        Unknown9190(1)
        Unknown9118(30)
        AirPushbackX(3500)
        AirPushbackY(-80000)
        HitOverhead(2)
        Unknown3038(1)
        Unknown23013(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)

        def upon_43():
            if (SLOT_48 == 9001):
                clearUponHandler(43)
                clearUponHandler(2)
                sendToLabel(2)
    sprite('vr_ph_magictest', 17)
    GFX_0('phEff_RRB', -1)
    Unknown38(4, 1)
    SFX_3('phse_04')
    SFX_0('019_quake_1')
    StartMultihit()
    physicsYImpulse(5000)
    setGravity(500)
    sprite('vr_ph_magictest', 32767)
    physicsYImpulse(-150000)
    label(1)
    sprite('vr_ph_magictest', 5)
    Unknown21007(4, 32)
    GFX_0('Eff_RRNsub2', -1)
    Unknown36(1)
    Unknown1007(180000)
    Unknown1073(25000)
    Unknown1097(500)
    Unknown35()
    StartMultihit()
    SFX_0('016_explode_2')
    Unknown23029(3, 6003, 0)
    sprite('vr_ph_magictest', 5)
    GFX_0('Eff_RRNsub2', -1)
    Unknown36(1)
    Unknown1007(60000)
    Unknown1073(15000)
    Unknown1099(30)
    Unknown35()
    ExitState()
    label(2)
    sprite('null', 10)
    Unknown3004(-23)
    ExitState()

@State
def DriveAtk_RRB_Lv3():

    def upon_IMMEDIATE():
        Unknown2009()
        Unknown4011(3)
        JumpCancel_(0)
        Unknown1056(6000)
        Unknown1064(10000)
        Unknown1007(375000)
        Unknown2053(1)
        if (SLOT_163 > 150000):
            if (SLOT_163 < 450000):
                Unknown1008()
                Unknown1086(22)
                Unknown1009()
            else:
                teleportRelativeX(450000)
        else:
            teleportRelativeX(150000)
        AttackLevel_(4)
        Damage(2000)
        AttackP1(90)
        AttackP2(90)
        AirPushbackX(1500)
        AirPushbackY(50000)
        Hitstop(6)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirUntechableTime(60)
        Unknown9190(1)
        Unknown9118(30)
        AirPushbackX(3500)
        AirPushbackY(-80000)
        HitOverhead(2)
        Unknown3038(1)
        Unknown23013(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)

        def upon_43():
            if (SLOT_48 == 9001):
                clearUponHandler(43)
                clearUponHandler(2)
                sendToLabel(2)
    sprite('vr_ph_magictest', 17)
    GFX_0('phEff_RRB', -1)
    Unknown38(4, 1)
    SFX_3('phse_04')
    SFX_0('019_quake_1')
    StartMultihit()
    physicsYImpulse(5000)
    setGravity(500)
    sprite('vr_ph_magictest', 32767)
    physicsYImpulse(-150000)
    label(1)
    sprite('vr_ph_magictest', 5)
    Unknown21007(4, 32)
    GFX_0('Eff_RRNsub2', -1)
    Unknown36(1)
    Unknown1007(180000)
    Unknown1073(25000)
    Unknown1097(500)
    Unknown35()
    StartMultihit()
    SFX_0('016_explode_2')
    Unknown23029(3, 6003, 0)
    sprite('vr_ph_magictest', 5)
    GFX_0('Eff_RRNsub2', -1)
    Unknown36(1)
    Unknown1007(60000)
    Unknown1073(15000)
    Unknown1099(30)
    Unknown35()
    ExitState()
    label(2)
    sprite('null', 10)
    Unknown3004(-23)
    ExitState()

@State
def phEff_RRB():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4061(2)
        Unknown1096(1150)
        Unknown1007(100000)
        sendToLabelUpon(32, 1)
    sprite('vr_phrrb_01', 2)
    GFX_0('phEff_RRBSub', -1)
    sprite('vr_phrrb_02', 2)
    sprite('vr_phrrb_03', 2)
    sprite('vr_phrrb_04', 2)
    GFX_2('phef_rrb_jizoku')
    sprite('vr_phrrb_05', 2)
    sprite('vr_phrrb_00', 4)
    label(0)
    sprite('vr_phrrb_00', 2)
    Unknown3029(1)
    Unknown3069(2)
    AfterimageCount(3)
    AfterimageSize_1(1200)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_phrrb_00', 3)
    Unknown1099(30)
    sprite('null', 10)
    GFX_1('phef_rrb_end', -1)
    Unknown3004(-26)
    ScreenShake(10000, 10000)
    loopRest()

@State
def phEff_RRBSub():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4013(2)
    sprite('null', 30)
    GFX_2('phef_rrb_start')

@State
def ph211_eff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown1007(308000)
        teleportRelativeX(50000)
        Unknown3032()
        Unknown1072(-30000)
        Unknown1064(-1000)
        Unknown1056(1000)
        Unknown4007(2)
    sprite('vr_ph254_00', 1)
    GFX_1('phef201_kira', 0)
    GFX_1('phef201_kira', 1)
    GFX_1('phef201_kira', 2)
    GFX_1('phef201_kira', 3)
    GFX_1('phef201_kira', 4)
    GFX_1('phef201_kira', 5)
    GFX_1('phef201_kira', 6)
    sprite('vr_ph254_00', 3)
    Unknown1057(300)
    Unknown1065(-300)
    sprite('vr_ph254_01', 2)
    sprite('vr_ph254_01', 2)
    Unknown4007(0)
    sprite('vr_ph254_02', 4)
    Unknown3004(-22)
    sprite('vr_ph254_03', 3)
    sprite('vr_ph254_04', 3)

@State
def Eff_DriveMagicCircle():

    def upon_IMMEDIATE():
        GFX_2('phef_magicAir_mc')

        def upon_3():
            Unknown2071('03000000b03cffffc0f2fcff6400000001000000')
    sprite('null', 20)

@State
def pheff_BufWaterMato():

    def upon_IMMEDIATE():
        Unknown2054(1)

        def upon_16():
            Unknown2071('0300000000000000e80300006400000001000000')
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 2)
    GFX_0('pheff_BufWater', -1)
    sprite('null', 2)
    GFX_0('pheff_BufWater', -1)
    Unknown36(1)
    Unknown2005()
    Unknown35()
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    Unknown21012('pheff_BufWater', 32)

@State
def pheff_BufWater():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2054(1)
        Unknown3033()
        Unknown4061(4)
        Unknown1096(600)
        Unknown1102(-100, 400)
        Unknown1010(-130000, 130000)
        Unknown1011(-125000, 60000)
        Unknown3001(200)
        Unknown23015(11)
        Unknown4007(2)
        Unknown4025(3)
        sendToLabelUpon(32, 0)
    sprite('vrpheff_buffw00', 5)
    Unknown1067(40)
    Unknown1059(20)
    sprite('vrpheff_buffw01', 2)
    sprite('vrpheff_buffw02', 3)
    GFX_2('pheff404_sub2')
    Unknown4007(0)
    sprite('vrpheff_buffw03', 3)
    sprite('vrpheff_buffw04', 3)
    Unknown3004(-22)
    sprite('vrpheff_buffw05', 2)
    sprite('vrpheff_buffw06', 2)
    sprite('vrpheff_buffw07', 2)
    gotoLabel(1)
    label(0)
    sprite('keep', 9)
    Unknown3004(-25)
    gotoLabel(1)
    label(1)
    sprite('null', 1)

@State
def pheff_BufFireMato():

    def upon_IMMEDIATE():
        Unknown2054(1)

        def upon_16():
            Unknown2071('0300000000000000e80300006400000001000000')
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 2)
    GFX_0('pheff_BufFire', -1)
    sprite('null', 2)
    GFX_0('pheff_BufFire', -1)
    Unknown36(1)
    Unknown2005()
    Unknown35()
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    Unknown21012('pheff_BufFire', 32)

@State
def pheff_BufFire():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown3029(1)
        AfterimageCount(2)
        Unknown4061(4)
        Unknown3001(200)
        Unknown1096(825)
        Unknown1102(-100, 400)
        Unknown1062(0, 200)
        Unknown1010(-130000, 130000)
        Unknown1011(-125000, 60000)
        Unknown23015(11)
        Unknown4007(2)
        Unknown4025(3)
        Unknown21010(1)
        Unknown2054(1)
        sendToLabelUpon(32, 0)
    sprite('vrpheff_bufff00', 3)
    sprite('vrpheff_bufff01', 3)
    sprite('vrpheff_bufff02', 3)
    Unknown4007(0)
    GFX_2('pheff404_sub')
    sprite('vrpheff_bufff03', 3)
    sprite('vrpheff_bufff04', 3)
    Unknown3004(-16)
    sprite('vrpheff_bufff05', 3)
    sprite('vrpheff_bufff06', 3)
    sprite('vrpheff_bufff07', 3)
    gotoLabel(1)
    label(0)
    sprite('keep', 9)
    Unknown3004(-25)
    gotoLabel(1)
    label(1)
    sprite('null', 1)

@State
def pheff_BufWindMato():

    def upon_IMMEDIATE():
        Unknown2054(1)

        def upon_16():
            Unknown2071('0300000000000000e80300006400000001000000')
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 3)
    GFX_0('pheff_BufWind', -1)
    sprite('null', 3)
    GFX_0('pheff_BufWind', -1)
    Unknown36(1)
    Unknown2005()
    Unknown35()
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    Unknown21012('pheff_BufWind', 32)

@State
def pheff_BufWind():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(4)
        Unknown3001(200)
        Unknown1096(800)
        Unknown1102(-100, 400)
        Unknown1010(-130000, 130000)
        Unknown1011(-125000, 60000)
        Unknown3029(1)
        AfterimageCount(2)
        Unknown23015(11)
        Unknown4007(2)
        Unknown4025(3)
        Unknown21010(1)
        Unknown2054(1)
        sendToLabelUpon(32, 0)
    sprite('vrpheff_buffk00', 3)
    Unknown1067(35)
    Unknown1059(-7)
    sprite('vrpheff_buffk01', 3)
    sprite('vrpheff_buffk02', 3)
    Unknown4007(0)
    GFX_2('pheff404_sub3')
    physicsYImpulse(1500)
    sprite('vrpheff_buffk03', 3)
    sprite('vrpheff_buffk04', 3)
    Unknown3004(-16)
    sprite('vrpheff_buffk05', 3)
    sprite('vrpheff_buffk06', 3)
    sprite('vrpheff_buffk07', 3)
    gotoLabel(1)
    label(0)
    sprite('keep', 9)
    Unknown3004(-25)
    gotoLabel(1)
    label(1)
    sprite('null', 1)

@State
def Eff_BuffAtkR():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2054(1)
        Unknown1007(200000)
        Unknown4010(2)
        Unknown4007(3)
    sprite('null', 7)
    sprite('null', 24)
    GFX_0('Eff_BuffAtkRSub', -1)

@State
def Eff_BuffAtkRSub():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(3)
        Unknown4003('pheff_buffatk00', '')
        GFX_2('pheff_buffatkR')
        Unknown1096(500)
    sprite('null', 9)
    Unknown21010(1)
    sprite('null', 10)
    Unknown21010(0)
    sprite('null', 4)
    Unknown1099(10)

@State
def Eff_BuffAtkB():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2054(1)
        Unknown1007(200000)
        Unknown4010(2)
        Unknown4007(3)
    sprite('null', 7)
    sprite('null', 24)
    GFX_0('Eff_BuffAtkBSub', -1)

@State
def Eff_BuffAtkBSub():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(3)
        Unknown4003('pheff_buffatk01', '')
        GFX_2('pheff_buffatkB')
        Unknown1096(500)
    sprite('null', 9)
    Unknown21010(1)
    sprite('null', 10)
    Unknown21010(0)
    sprite('null', 4)
    Unknown1099(10)

@State
def Eff_BuffAtkG():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2054(1)
        Unknown1007(200000)
        Unknown4010(2)
        Unknown4007(3)
    sprite('null', 7)
    sprite('null', 24)
    GFX_0('Eff_BuffAtkGSub', -1)

@State
def Eff_BuffAtkGSub():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(3)
        Unknown4003('pheff_buffatk02', '')
        GFX_2('pheff_buffatkG')
        Unknown1096(500)
    sprite('null', 9)
    Unknown21010(1)
    sprite('null', 10)
    Unknown21010(0)
    sprite('null', 4)
    Unknown1099(10)

@State
def pheff_400():

    def upon_IMMEDIATE():
        Unknown4061(3)
        Unknown4007(2)
        Unknown4010(2)

        def upon_43():
            if (SLOT_48 == 4001):
                sendToLabel(1)
            if (SLOT_48 == 4002):
                sendToLabel(2)
    sprite('vr_ph400_00', 2)
    Unknown3001(0)
    Unknown3004(51)
    GFX_1('phef400_nokosi', 0)
    GFX_0('pheff_400Fire', 0)
    GFX_1('phef400_nokosi', 1)
    GFX_0('pheff_400Fire', 1)
    GFX_1('phef400_nokosi', 2)
    GFX_0('pheff_400Fire', 2)
    GFX_1('phef400_nokosi', 3)
    label(0)
    sprite('vr_ph400_00', 2)
    GFX_1('phef400_nokosi', 0)
    GFX_1('phef400_nokosi', 1)
    GFX_1('phef400_nokosi', 2)
    GFX_1('phef400_nokosi', 3)
    sprite('vr_ph400_01', 2)
    GFX_1('phef400_nokosi', 0)
    GFX_1('phef400_nokosi', 1)
    GFX_1('phef400_nokosi', 2)
    GFX_1('phef400_nokosi', 3)
    gotoLabel(0)
    label(1)
    sprite('vr_ph400_00', 2)
    Unknown21012('pheff_400Fire', 32)
    sprite('vr_ph400_01', 2)
    sprite('vr_ph400_02', 4)
    sprite('vr_ph400_03', 4)
    sprite('vr_ph400_04', 2)
    Unknown1096(1000)
    Unknown3029(0)
    sprite('vr_ph400_04', 2)
    Unknown1096(1500)
    teleportRelativeX(-40000)
    Unknown1007(-50000)
    Unknown4007(0)
    sprite('vr_ph400_05', 7)
    Unknown1096(1150)
    Unknown1007(50000)
    Unknown1007(200000)
    teleportRelativeX(40000)
    ScreenShake(10000, 10000)
    Unknown1099(15)
    GFX_0('pheff_400sub', 0)
    GFX_1('phef_400_bom', 1)
    GFX_1('phef_400_blm', 1)
    GFX_1('phef_400_bom_ground', 1)
    sprite('vr_ph400_07', 3)
    sprite('vr_ph400_08', 3)
    sprite('vr_ph400_09', 3)
    GFX_0('pheff_400sub3', 0)
    sprite('vr_ph400_06', 5)
    GFX_0('phEff400_corebom', 0)
    Unknown3004(-51)
    ExitState()
    label(2)
    sprite('vr_ph400_00', 1)
    Unknown21012('pheff_400Fire', 32)
    sprite('vr_ph400_01', 2)
    sprite('vr_ph400_02', 2)
    sprite('vr_ph400_03', 2)
    sprite('vr_ph400_04', 2)
    Unknown1096(1000)
    Unknown3029(0)
    Unknown1096(1500)
    teleportRelativeX(-40000)
    Unknown1007(-50000)
    Unknown4007(0)
    sprite('vr_ph400_05', 3)
    Unknown1096(1150)
    Unknown1007(50000)
    Unknown1007(200000)
    teleportRelativeX(40000)
    ScreenShake(10000, 10000)
    Unknown1099(15)
    GFX_0('pheff_400sub', 0)
    GFX_1('phef_400_bom', 1)
    GFX_1('phef_400_blm', 1)
    GFX_1('phef_400_bom_ground', 1)
    sprite('vr_ph400_07', 3)
    sprite('vr_ph400_08', 3)
    sprite('vr_ph400_09', 3)
    GFX_0('pheff_400sub3', 0)
    sprite('vr_ph400_06', 5)
    GFX_0('phEff400_corebom', 0)
    Unknown3004(-51)
    ExitState()

@State
def pheff_400Fire():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4003('ph400eff_jizoku00', '')
        Unknown3032()
        Unknown1062(-50, 200)
        sendToLabelUpon(32, 0)
    sprite('null', 10)
    Unknown3001(0)
    Unknown3004(13)
    sprite('null', 32767)
    Unknown3004(0)
    label(0)
    sprite('null', 5)
    Unknown3004(51)
    Unknown1067(-30)
    sprite('null', 5)
    Unknown3004(-51)

@State
def pheff_400Air():

    def upon_IMMEDIATE():
        Unknown4061(3)
        Unknown4007(2)
        Unknown4010(2)

        def upon_43():
            if (SLOT_48 == 4001):
                sendToLabel(1)
            if (SLOT_48 == 4003):
                Unknown1072(22500)
            if (SLOT_48 == 4004):
                Unknown1072(-22500)
            if (SLOT_48 == 4005):
                Unknown1072(0)
    sprite('vr_ph400_00', 2)
    Unknown3001(0)
    Unknown3004(51)
    GFX_1('phef400_nokosi', 0)
    GFX_0('pheff_400Fire', 0)
    GFX_1('phef400_nokosi', 1)
    GFX_0('pheff_400Fire', 1)
    GFX_1('phef400_nokosi', 2)
    GFX_0('pheff_400Fire', 2)
    GFX_1('phef400_nokosi', 3)
    label(0)
    sprite('vr_ph400_00', 2)
    GFX_1('phef400_nokosi', 0)
    GFX_1('phef400_nokosi', 1)
    GFX_1('phef400_nokosi', 2)
    GFX_1('phef400_nokosi', 3)
    sprite('vr_ph400_01', 2)
    GFX_1('phef400_nokosi', 0)
    GFX_1('phef400_nokosi', 1)
    GFX_1('phef400_nokosi', 2)
    GFX_1('phef400_nokosi', 3)
    gotoLabel(0)
    label(1)
    sprite('vr_ph400_00', 2)
    Unknown21012('pheff_400Fire', 32)
    sprite('vr_ph400_01', 2)
    sprite('vr_ph400_02', 4)
    sprite('vr_ph400_03', 4)
    sprite('vr_ph400_04', 2)
    Unknown3029(0)
    sprite('vr_ph400_04', 2)
    Unknown1072(0)
    Unknown1096(1500)
    teleportRelativeX(-40000)
    Unknown1007(-50000)
    Unknown4007(0)
    sprite('vr_ph400_05', 7)
    Unknown1096(1150)
    teleportRelativeX(40000)
    Unknown1007(50000)
    Unknown1007(200000)
    ScreenShake(10000, 10000)
    Unknown1099(15)
    GFX_0('pheff_400sub2', 1)
    GFX_1('phef_400_bom', 1)
    GFX_1('phef_400_blm', 1)
    sprite('vr_ph400_07', 3)
    sprite('vr_ph400_08', 3)
    GFX_1('phef321_shock2', -1)
    sprite('vr_ph400_09', 3)
    sprite('vr_ph400_06', 5)
    GFX_0('pheff_400sub3', 0)
    GFX_0('phEff400_corebom', 0)
    Unknown3004(-51)

@State
def phEff400_corebom():

    def upon_IMMEDIATE():
        Unknown1096(1300)
        Unknown3033()
        Unknown4061(2)
        Unknown23015(1)
    sprite('vr_ph216_03', 4)
    Unknown1099(15)
    sprite('vr_ph216_04', 4)
    sprite('vr_ph216_05', 4)

@State
def pheff_400sub():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('ph240eff_00', '')
        Unknown1064(450)
        Unknown1056(600)
        Unknown2054(1)
    sprite('null', 19)
    sprite('null', 5)
    Unknown3004(-51)

@State
def pheff_400sub2():

    def upon_IMMEDIATE():
        Unknown4003('ph240eff_01', '')
        Unknown3032()
        Unknown1096(300)
        Unknown3001(200)
        teleportRelativeX(25000)
    sprite('null', 23)
    Unknown1099(4)

@State
def pheff_400sub3():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('ph240eff_02', '')
        Unknown1007(-100000)
        Unknown1096(500)
        Unknown2054(1)
    sprite('null', 13)
    sprite('null', 10)
    Unknown3004(-26)

@Subroutine
def MagicInit():
    Unknown2009()
    Unknown4011(3)
    Unknown9021(1)

@Subroutine
def BlueMagicInit():
    Unknown23078(1)
    AirPushbackY(12000)
    FreezeCount(1)
    FreezeDuration(20)
    
@Subroutine
def BlueMagic_Lv2_Init():
    Unknown23078(1)
    AirPushbackY(12000)
    FreezeCount(1)
    FreezeDuration(35)
    
@Subroutine
def BlueMagic_Lv3_Init():
    Unknown23078(1)
    AirPushbackY(12000)
    FreezeCount(1)
    FreezeDuration(85)

@State
def DriveAtk_BNN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(14500)
        Unknown1064(4000)
        teleportRelativeX(330000)
        Unknown1007(180000)
        callSubroutine('BlueMagicInit')
        AttackLevel_(3)
        Damage(2000)
        Unknown3038(1)
    sprite('vr_ph_magictest', 3)
    GFX_0('Eff_BNN', -1)

@State
def DriveAirAtk_BNN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(14500)
        Unknown1064(4000)
        teleportRelativeX(330000)
        Unknown1007(180000)
        callSubroutine('BlueMagicInit')
        AttackLevel_(3)
        Damage(1200)
        Unknown3038(1)
    sprite('vr_ph_magictest', 3)
    GFX_0('Eff_BNN', -1)

@State
def Eff_BNN():

    def upon_IMMEDIATE():
        Unknown4003('pheff_bnn00', '')
        Unknown3032()
        Unknown1096(1000)
        teleportRelativeX(-100000)
        Unknown1007(35000)
    sprite('null', 5)
    GFX_0('Eff_BNNsub', -1)
    sprite('null', 4)
    Unknown1097(100)
    sprite('null', 3)
    Unknown1097(-50)
    Unknown3001(200)
    sprite('null', 3)
    Unknown1097(-50)
    Unknown3001(100)
    GFX_1('phef_bnn_moya', -1)

@State
def Eff_BNNsub():

    def upon_IMMEDIATE():
        Unknown4003('pheff_bnn01', '')
        GFX_1('phef_bnn_mc', -1)
        Unknown3032()
        Unknown1096(750)
    sprite('null', 5)
    SFX_0('017_freeze_1')
    Unknown1097(200)
    sprite('null', 5)
    Unknown1097(200)
    sprite('null', 2)
    Unknown1097(-200)
    sprite('null', 2)
    SFX_0('018_ice_break_1')
    Unknown1097(-200)

@State
def DriveAtk_BBN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(16000)
        Unknown1064(4000)
        teleportRelativeX(305000)
        Unknown1007(180000)
        callSubroutine('BlueMagicInit')
        AttackLevel_(4)
        Damage(2500)
        Unknown3038(1)
    sprite('vr_ph_magictest', 3)
    GFX_0('Eff_BBN', -1)
    
@State
def DriveAirAtk_BBN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(16000)
        Unknown1064(4000)
        teleportRelativeX(305000)
        Unknown1007(180000)
        callSubroutine('BlueMagic_Lv2_Init')
        AttackLevel_(4)
        Damage(1500)
        Unknown3038(1)
    sprite('vr_ph_magictest', 3)
    GFX_0('Eff_BBN', -1)

@State
def Eff_BBN():

    def upon_IMMEDIATE():
        Unknown4003('pheff_bbn00', '')
        Unknown3032()
        Unknown1096(1000)
        Unknown1057(100)
        teleportRelativeX(-125000)
        Unknown1007(25000)
    sprite('null', 5)
    GFX_0('Eff_BNNsub', -1)
    Unknown36(1)
    Unknown1097(150)
    Unknown35()
    SFX_0('017_freeze_1')
    sprite('null', 4)
    Unknown1097(100)
    sprite('null', 3)
    Unknown1097(-50)
    Unknown3001(200)
    sprite('null', 3)
    Unknown1097(-50)
    Unknown3001(100)
    Unknown3033()
    GFX_1('phef_bbb', -1)
    SFX_0('018_ice_break_1')

@State
def DriveAtk_BBB():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(17500)
        Unknown1064(5000)
        teleportRelativeX(280000)
        Unknown1007(170000)
        callSubroutine('BlueMagicInit')
        AttackLevel_(5)
        Damage(3000)
        Unknown3038(1)
    sprite('vr_ph_magictest', 3)
    GFX_0('Eff_BBB', -1)

@State
def DriveAirAtk_BBB():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(17500)
        Unknown1064(5000)
        teleportRelativeX(280000)
        Unknown1007(170000)
        callSubroutine('BlueMagic_Lv3_Init')
        AttackLevel_(5)
        AttackP1(100)
        AttackP2(100)
        Damage(2000)
        Unknown3038(1)
    sprite('vr_ph_magictest', 3)
    GFX_0('Eff_BBB', -1)

@State
def Eff_BBB():

    def upon_IMMEDIATE():
        Unknown4003('pheff_bbb00', '')
        Unknown3032()
        Unknown1096(675)
        teleportRelativeX(-100000)
        Unknown1007(70000)
    sprite('null', 4)
    GFX_0('Eff_BNNsub', -1)
    Unknown36(1)
    Unknown1097(225)
    Unknown35()
    SFX_0('017_freeze_0')
    SFX_0('017_freeze_0')
    sprite('null', 4)
    Unknown1097(100)
    sprite('null', 3)
    Unknown1097(-50)
    Unknown3001(200)
    GFX_1('phef_bbb', -1)
    SFX_0('018_ice_break_0')
    SFX_0('018_ice_break_0')
    sprite('null', 4)
    Unknown1097(-50)
    Unknown1099(7)
    Unknown3004(-51)

@Subroutine
def RedMagicInit():
    if (SLOT_19 < 400000):
        Unknown1008()
        Unknown1086(22)
        Unknown1009()
    else:
        teleportRelativeX(400000)

    Unknown23078(1)
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    AirPushbackX(7500)
    AirPushbackY(-50000)
    PushbackX(4000)
    Unknown9190(1)
    Unknown9118(10)
    Unknown2053(1)

@Subroutine
def RedMagicInit_Lv2():
    if (SLOT_19 < 400000):
        Unknown1008()
        Unknown1086(22)
        Unknown1009()
    else:
        teleportRelativeX(400000)

    Unknown23078(1)
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    AirPushbackX(7500)
    AirPushbackY(35000)
    PushbackX(6000)
    Unknown2053(1)

@Subroutine
def RedMagicInit_Lv3():
    if (SLOT_19 < 400000):
        Unknown1008()
        Unknown1086(22)
        Unknown1009()
    else:
        teleportRelativeX(400000)

    Unknown23078(1)
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    AirPushbackX(7500)
    AirPushbackY(45000)
    PushbackX(6000)
    Unknown2053(1)

@State
def DriveAtk_RNN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(6000)
        Unknown1064(11000)
        callSubroutine('RedMagicInit')
        AttackLevel_(3)
        Damage(1600)
        AirUntechableTime(22)
        Unknown3038(1)
    sprite('vr_ph_magictest', 3)
    GFX_0('Eff_RNN', -1)

@State
def DriveAirAtk_RNN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(6000)
        Unknown1064(11000)
        callSubroutine('RedMagicInit')
        AttackLevel_(3)
        Damage(1800)
        AirUntechableTime(35)
        Unknown3038(1)
    sprite('vr_ph_magictest', 3)
    GFX_0('Eff_RNN', -1)

@State
def Eff_RNN():

    def upon_IMMEDIATE():
        Unknown4003('pheff_rnn00', '')
        Unknown2053(1)
        Unknown3032()
        Unknown1096(1200)
        Unknown1007(50000)
    sprite('null', 8)
    GFX_0('Eff_RNNsub', -1)
    SFX_0('016_explode_0')
    sprite('null', 3)
    Unknown1065(50)
    sprite('null', 3)
    Unknown1065(50)
    sprite('null', 8)
    Unknown1065(50)
    Unknown3033()
    GFX_0('Eff_RNNsub2', -1)

@State
def Eff_RNNsub2():

    def upon_IMMEDIATE():
        Unknown4003('pheff_rnn01', '')
        Unknown4007(2)
        Unknown3032()
        Unknown1096(1200)
    sprite('null', 16)
    Unknown3004(-10)

@State
def Eff_RNNsub():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown3032()
        Unknown1096(800)
    sprite('null', 60)
    GFX_2('phef_rnn_mc')

@State
def DriveAtk_RRN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(6000)
        Unknown1064(13000)
        callSubroutine('RedMagicInit')
        AttackLevel_(4)
        Damage(1800)
        AirUntechableTime(24)
        Unknown3038(1)
    sprite('vr_ph_magictest', 3)
    GFX_0('Eff_RRN', -1)

@State
def DriveAirAtk_RRN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(6000)
        Unknown1064(13000)
        callSubroutine('RedMagicInit_Lv2')
        AttackLevel_(4)
        Damage(2000)
        AirUntechableTime(45)
        Unknown3038(1)
    sprite('vr_ph_magictest', 3)
    GFX_0('Eff_RRN', -1)

@State
def Eff_RRN():

    def upon_IMMEDIATE():
        Unknown4003('pheff_rnn00', '')
        Unknown2053(1)
        Unknown3032()
        Unknown1096(1350)
        Unknown1007(50000)
    sprite('null', 8)
    GFX_0('Eff_RNNsub', -1)
    GFX_0('Eff_RRNsub2Mato', -1)
    SFX_0('016_explode_1')
    sprite('null', 3)
    Unknown1065(50)
    sprite('null', 3)
    Unknown1065(50)
    sprite('null', 8)
    Unknown1065(50)
    Unknown3033()
    GFX_0('Eff_RRNsub', -1)

@State
def Eff_RRNsub():

    def upon_IMMEDIATE():
        Unknown4003('pheff_rnn01', '')
        Unknown4007(2)
        Unknown3032()
        Unknown1096(1350)
    sprite('null', 16)
    Unknown3004(-10)

@State
def Eff_RRNsub2Mato():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown3032()
    sprite('null', 4)
    GFX_1('phef_rrn_bg', -1)
    GFX_0('Eff_RRNsub2', -1)
    Unknown36(1)
    Unknown1072(25500)
    Unknown35()
    sprite('null', 4)
    GFX_0('Eff_RRNsub2', -1)
    Unknown36(1)
    Unknown1007(100000)
    Unknown1097(-125)
    Unknown2005()
    Unknown1072(-25500)
    Unknown35()
    sprite('null', 4)
    GFX_0('Eff_RRNsub2', -1)
    Unknown36(1)
    Unknown1007(200000)
    Unknown1097(-125)
    Unknown1072(25500)
    Unknown35()

@State
def Eff_RRNsub2():

    def upon_IMMEDIATE():
        Unknown4003('pheff_rrn00', '')
        Unknown3032()
        Unknown1096(1450)
        Unknown3001(255)
    sprite('null', 15)
    Unknown1099(20)
    sprite('null', 4)
    Unknown3004(-51)

@State
def DriveAtk_RRR():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(6000)
        Unknown1064(15000)
        callSubroutine('RedMagicInit')
        AttackLevel_(5)
        Damage(2000)
        AirUntechableTime(26)
        Unknown3038(1)
    sprite('vr_ph_magictest', 3)
    GFX_0('Eff_RRR', -1)

@State
def DriveAirAtk_RRR():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(6000)
        Unknown1064(15000)
        callSubroutine('RedMagicInit_Lv3')
        AttackLevel_(5)
        Damage(2500)
        AttackP2(130)
        AirUntechableTime(55)
        Unknown3038(1)
    sprite('vr_ph_magictest', 3)
    GFX_0('Eff_RRR', -1)

@State
def Eff_RRR():

    def upon_IMMEDIATE():
        Unknown4003('pheff_rrr01', '')
        Unknown2053(1)
        Unknown3032()
        Unknown1064(1750)
        Unknown1056(1500)
        Unknown1007(50000)
    sprite('null', 8)
    GFX_0('Eff_RNNsub', -1)
    GFX_0('Eff_RRRsub2Mato', -1)
    SFX_0('016_explode_2')
    ScreenShake(5000, 5000)
    sprite('null', 3)
    Unknown1065(25)
    sprite('null', 3)
    Unknown1065(25)
    sprite('null', 8)
    Unknown1065(25)
    Unknown3033()
    GFX_0('Eff_RRRsub', -1)

@State
def Eff_RRRsub():

    def upon_IMMEDIATE():
        Unknown4003('pheff_rnn01', '')
        Unknown4007(2)
        Unknown3032()
        Unknown1096(1350)
    sprite('null', 16)
    Unknown3004(-10)

@State
def Eff_RRRsub2Mato():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
    sprite('null', 6)
    GFX_1('phef_rrr_bg', -1)
    GFX_0('Eff_RRRsub2', -1)
    Unknown36(1)
    Unknown1072(25500)
    Unknown35()
    sprite('null', 6)
    GFX_0('Eff_RRRsub2', -1)
    Unknown36(1)
    Unknown1007(100000)
    Unknown1097(-125)
    Unknown2005()
    Unknown1072(-25500)
    Unknown35()
    sprite('null', 6)
    GFX_0('Eff_RRRsub2', -1)
    Unknown36(1)
    Unknown1007(200000)
    Unknown1097(100)
    Unknown1072(25500)
    Unknown35()
    sprite('null', 12)

@State
def Eff_RRRsub2():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4003('pheff_rrr00', '')
        Unknown1096(1450)
        Unknown3001(255)
    sprite('null', 14)
    Unknown1099(20)
    sprite('null', 4)
    Unknown3004(-51)

@Subroutine
def GreenMagicInit():
    Unknown23078(1)
    Unknown11092(1)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirPushbackX(60000)
    AirPushbackY(6000)
    Unknown9202(40)
    Unknown9178(1)
    WallbounceReboundTime(20)
    Unknown11001(0, 0, 0)
    Unknown11057(500)
    Unknown9016(1)
    Unknown23182(3)

@Subroutine
def GreenMagic_Lv1_Lv2Init():
    Unknown23078(1)
    Unknown11092(1)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirPushbackX(50000)
    AirPushbackY(5000)
    Unknown9202(40)
    Unknown11001(0, 0, 0)
    Unknown11057(500)
    Unknown9016(1)
    Unknown23182(3)

@Subroutine
def GreenMagicInit_Lv3():
    Unknown23078(1)
    Unknown11092(1)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirPushbackX(100000)
    AirPushbackY(16000)
    Unknown9202(40)
    Unknown9178(1)
    WallbounceReboundTime(24)
    Unknown11001(0, 0, 0)
    Unknown11057(500)
    Unknown9016(1)
    Unknown23182(3)

@State
def DriveAtk_GNN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown4010(3)
        Unknown1056(20000)
        Unknown1064(2500)
        teleportRelativeX(650000)
        Unknown1007(210000)
        callSubroutine('GreenMagicInit')
        AttackLevel_(3)
        Damage(1500)
        AirUntechableTime(26)
        PushbackX(39800)
        Unknown3038(1)

        def upon_STATE_END():
            Unknown23029(3, 6001, 0)
    sprite('vr_ph_magictest', 3)
    GFX_0('Eff_GNN', -1)
    GFX_0('Eff_GNN', -1)
    Unknown21007(1, 32)
    GFX_0('Eff_GNN', -1)
    Unknown21007(1, 33)
    SFX_0('011_spin_0')
    SFX_0('011_spin_0')
    SFX_0('011_spin_1')
    SFX_3('phse_01')
    Unknown1056(15000)
    teleportRelativeX(-400000)
    Unknown1064(5000)
    Unknown1007(-10000)
    sprite('vr_ph_magictest', 3)
    Unknown1056(25000)
    teleportRelativeX(160000)
    Unknown1064(5000)
    sprite('vr_ph_magictest', 3)
    Unknown1056(40000)
    teleportRelativeX(240000)
    Unknown1064(5000)
    ExitState()

@State
def DriveAirAtk_GNN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown4010(3)
        Unknown1056(20000)
        Unknown1064(2500)
        teleportRelativeX(650000)
        Unknown1007(210000)
        callSubroutine('GreenMagic_Lv1_Lv2Init')
        AttackLevel_(3)
        Damage(1500)
        AirUntechableTime(26)
        PushbackX(39800)
        Unknown3038(1)

        def upon_STATE_END():
            Unknown23029(3, 6001, 0)
    sprite('vr_ph_magictest', 3)
    GFX_0('Eff_GNN', -1)
    GFX_0('Eff_GNN', -1)
    Unknown21007(1, 32)
    GFX_0('Eff_GNN', -1)
    Unknown21007(1, 33)
    SFX_0('011_spin_0')
    SFX_0('011_spin_0')
    SFX_0('011_spin_1')
    SFX_3('phse_01')
    Unknown1056(15000)
    teleportRelativeX(-400000)
    Unknown1064(5000)
    Unknown1007(-10000)
    sprite('vr_ph_magictest', 3)
    Unknown1056(25000)
    teleportRelativeX(160000)
    Unknown1064(5000)
    sprite('vr_ph_magictest', 3)
    Unknown1056(40000)
    teleportRelativeX(240000)
    Unknown1064(5000)
    ExitState()

@State
def Eff_GNN():

    def upon_IMMEDIATE():
        Unknown4003('pheff_gnn00', '')
        Unknown3032()
        teleportRelativeX(-500000)
        Unknown1007(40000)
        Unknown1096(700)
        Unknown1065(-200)

        def upon_32():
            Unknown3001(0)
            Unknown2037(3)
            teleportRelativeX(350000)

        def upon_33():
            Unknown3001(0)
            Unknown2037(6)
            teleportRelativeX(700000)

        def upon_34():
            Unknown3001(255)

        def upon_3():
            if SLOT_2:
                Unknown2038(-1)
                if (not SLOT_2):
                    Unknown3001(255)
    sprite('null', 1)
    sprite('null', 1)
    GFX_1('phef_gnn_moya02', -1)
    if (not SLOT_2):
        GFX_1('phef_gnn_mc', -1)
    GFX_0('Eff_GNNsub', -1)
    sprite('null', 2)
    GFX_0('Eff_GNNsub', -1)
    Unknown36(1)
    teleportRelativeX(200000)
    Unknown35()
    sprite('null', 12)
    ExitState()

@State
def Eff_GNNsub():

    def upon_IMMEDIATE():
        Unknown4003('pheff_gnn01', '')
        Unknown3032()
    sprite('null', 8)
    Unknown1099(15)
    sprite('null', 10)
    Unknown3004(-26)

@State
def DriveAtk_GGN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown4010(3)
        Unknown1056(40000)
        Unknown1064(2500)
        teleportRelativeX(650000)
        Unknown1007(210000)
        callSubroutine('GreenMagicInit')
        AttackLevel_(4)
        Damage(800)
        AirUntechableTime(28)
        PushbackX(60800)
        Hitstop(4)
        Unknown3038(1)

        def upon_STATE_END():
            Unknown23029(3, 6001, 0)
    sprite('vr_ph_magictest', 3)
    GFX_0('Eff_GGN', -1)
    GFX_0('Eff_GGN', -1)
    Unknown21007(1, 32)
    GFX_0('Eff_GGN', -1)
    Unknown21007(1, 33)
    SFX_0('011_spin_2')
    SFX_0('011_spin_2')
    SFX_0('006_swing_blade_2')
    SFX_0('022_magiccircle_b')
    Unknown1056(15000)
    teleportRelativeX(-400000)
    Unknown1064(5000)
    Unknown1007(-10000)
    sprite('vr_ph_magictest', 3)
    Unknown1056(25000)
    teleportRelativeX(160000)
    Unknown1064(5000)
    sprite('vr_ph_magictest', 3)
    Unknown1056(40000)
    teleportRelativeX(240000)
    Unknown1064(5000)
    RefreshMultihit()
    Damage(1200)
    Hitstop(12)
    ExitState()

@State
def DriveAirAtk_GGN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown4010(3)
        Unknown1056(40000)
        Unknown1064(2500)
        teleportRelativeX(650000)
        Unknown1007(210000)
        callSubroutine('GreenMagic_Lv1_Lv2Init')
        AttackLevel_(4)
        Damage(800)
        AirUntechableTime(28)
        PushbackX(60800)
        Hitstop(4)
        Unknown3038(1)

        def upon_STATE_END():
            Unknown23029(3, 6001, 0)
    sprite('vr_ph_magictest', 3)
    GFX_0('Eff_GGN', -1)
    GFX_0('Eff_GGN', -1)
    Unknown21007(1, 32)
    GFX_0('Eff_GGN', -1)
    Unknown21007(1, 33)
    SFX_0('011_spin_2')
    SFX_0('011_spin_2')
    SFX_0('006_swing_blade_2')
    SFX_0('022_magiccircle_b')
    Unknown1056(15000)
    teleportRelativeX(-400000)
    Unknown1064(5000)
    Unknown1007(-10000)
    sprite('vr_ph_magictest', 3)
    Unknown1056(25000)
    teleportRelativeX(160000)
    Unknown1064(5000)
    sprite('vr_ph_magictest', 3)
    Unknown1056(40000)
    teleportRelativeX(240000)
    Unknown1064(5000)
    RefreshMultihit()
    Damage(1200)
    Hitstop(12)
    ExitState()

@State
def Eff_GGN():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff_ggn00', '')
        teleportRelativeX(-500000)
        Unknown1007(40000)
        Unknown1096(700)
        Unknown1065(-150)
        Unknown1072(2000)

        def upon_32():
            Unknown3001(0)
            Unknown2037(3)
            teleportRelativeX(350000)

        def upon_33():
            Unknown3001(0)
            Unknown2037(6)
            teleportRelativeX(700000)

        def upon_34():
            Unknown3001(255)

        def upon_3():
            if SLOT_2:
                Unknown2038(-1)
                if (not SLOT_2):
                    Unknown3001(255)
    sprite('null', 1)
    sprite('null', 1)
    GFX_1('phef_ggn_moya02', -1)
    if (not SLOT_2):
        GFX_0('Eff_GNNmc', -1)
    GFX_0('Eff_GGNsub', -1)
    sprite('null', 2)
    GFX_0('Eff_GGNsub', -1)
    Unknown36(1)
    teleportRelativeX(200000)
    Unknown35()
    sprite('null', 12)
    ExitState()

@State
def Eff_GGNsub():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff_gnn01', '')
    sprite('null', 8)
    Unknown1099(30)
    sprite('null', 10)
    Unknown3004(-26)

@State
def DriveAtk_GGG():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown4010(3)
        Unknown1056(40000)
        Unknown1064(2500)
        teleportRelativeX(650000)
        Unknown1007(210000)
        callSubroutine('GreenMagicInit')
        AttackLevel_(5)
        Damage(300)
        AirUntechableTime(30)
        PushbackX(79800)
        Hitstop(2)
        Unknown3038(1)

        def upon_STATE_END():
            Unknown23029(3, 6001, 0)
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    GFX_0('Eff_GGG', -1)
    GFX_0('Eff_GGG', -1)
    Unknown21007(1, 32)
    GFX_0('Eff_GGG', -1)
    Unknown21007(1, 33)
    SFX_3('phse_03')
    ScreenShake(5000, 5000)
    Unknown1056(15000)
    teleportRelativeX(-400000)
    Unknown1064(5000)
    Unknown1007(-10000)
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    Damage(600)
    Unknown1056(25000)
    teleportRelativeX(160000)
    Unknown1064(5000)
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    Damage(1500)
    Hitstop(13)
    Unknown1056(40000)
    teleportRelativeX(240000)
    Unknown1064(5000)
    ExitState()

@State
def DriveAirAtk_GGG():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown4010(3)
        Unknown1056(40000)
        Unknown1064(2500)
        teleportRelativeX(650000)
        Unknown1007(210000)
        callSubroutine('GreenMagicInit_Lv3')
        AttackLevel_(5)
        AttackP1(100)
        AttackP2(100)
        Damage(350)
        AirUntechableTime(50)
        PushbackX(90000)
        Hitstop(2)
        Unknown3038(1)

        def upon_STATE_END():
            Unknown23029(3, 6001, 0)
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    GFX_0('Eff_GGG', -1)
    GFX_0('Eff_GGG', -1)
    Unknown21007(1, 32)
    GFX_0('Eff_GGG', -1)
    Unknown21007(1, 33)
    SFX_3('phse_03')
    ScreenShake(5000, 5000)
    Unknown1056(15000)
    teleportRelativeX(-400000)
    Unknown1064(5000)
    Unknown1007(-10000)
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    Damage(600)
    Unknown1056(25000)
    teleportRelativeX(160000)
    Unknown1064(5000)
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    Damage(1500)
    Hitstop(13)
    Unknown1056(40000)
    teleportRelativeX(240000)
    Unknown1064(5000)
    ExitState()

@State
def Eff_GGG():

    def upon_IMMEDIATE():
        Unknown4003('pheff_ggg00', '')
        Unknown3032()
        teleportRelativeX(-500000)
        Unknown1007(40000)
        Unknown1096(750)
        Unknown1065(-300)
        Unknown1072(2000)

        def upon_32():
            Unknown3001(0)
            Unknown2037(3)
            teleportRelativeX(350000)

        def upon_33():
            Unknown3001(0)
            Unknown2037(6)
            teleportRelativeX(700000)

        def upon_34():
            Unknown3001(255)

        def upon_3():
            if SLOT_2:
                Unknown2038(-1)
                if (not SLOT_2):
                    Unknown3001(255)
    sprite('null', 1)
    sprite('null', 1)
    if (not SLOT_2):
        GFX_0('Eff_GNNmc', -1)
    GFX_1('phef_ggg_moya03', -1)
    GFX_0('Eff_GGGsub', -1)
    Unknown1065(50)
    sprite('null', 2)
    GFX_0('Eff_GGGsub', -1)
    Unknown36(1)
    teleportRelativeX(200000)
    Unknown35()
    Unknown1065(-50)
    sprite('null', 2)
    Unknown1065(50)
    sprite('null', 2)
    Unknown1065(-50)
    sprite('null', 2)
    Unknown1065(50)
    sprite('null', 1)
    sprite('null', 5)
    ExitState()

@State
def Eff_GGGsub():

    def upon_IMMEDIATE():
        Unknown4003('pheff_gnn01', '')
        Unknown3032()
    sprite('null', 8)
    Unknown1099(45)
    sprite('null', 10)
    Unknown3004(-26)

@State
def Eff_GNNmc():

    def upon_IMMEDIATE():
        GFX_2('phef_gnn_mc')
        Unknown3032()
    sprite('null', 20)

@State
def Wind_Herald():

    def upon_IMMEDIATE():
        GFX_2('phef_g_yotyou')
        Unknown1007(260000)
        Unknown1056(700)
    sprite('null', 7)
    sprite('null', 4)
    Unknown3004(-51)

@Subroutine
def SpecialMagicInit():
    Unknown2010()
    Unknown4011(3)
    Unknown9021(1)

@State
def DriveAtk_NNN():

    def upon_IMMEDIATE():
        callSubroutine('SpecialMagicInit')
        Unknown1064(4000)
        teleportRelativeX(250000)
        Unknown1007(200000)
        AttackLevel_(1)
        Damage(1500)
        AttackP1(80)
        GroundedHitstunAnimation(9)
        Unknown9016(1)
        Unknown11057(700)
        AirUntechableTime(35)
        AirPushbackX(15000)
        AirPushbackY(12000)
        Unknown3038(1)
    sprite('vr_ph_magictest', 3)
    GFX_0('Eff_NNN', -1)
    Unknown1056(7500)
    teleportRelativeX(-120000)
    sprite('vr_ph_magictest', 2)
    Unknown1056(15000)
    teleportRelativeX(120000)

@State
def Eff_NNN():

    def upon_IMMEDIATE():
        Unknown4061(2)
        teleportRelativeX(-300000)
        Unknown1007(70000)
        Unknown1096(1000)
    sprite('vr_ph5d_00', 2)
    physicsXImpulse(32000)
    GFX_0('Eff_NNNsub', -1)
    SFX_3('phse_04')
    sprite('vr_ph5d_00', 1)
    physicsXImpulse(1000)
    GFX_1('phef_nnn_nokosi', 0)
    sprite('vr_ph5d_01', 2)
    GFX_1('phef_nnn_nokosi', 0)
    sprite('vr_ph5d_02', 2)
    GFX_1('phef_nnn_nokosi', 0)
    sprite('vr_ph5d_03', 2)
    physicsXImpulse(-1000)
    GFX_1('phef_nnn_nokosi', 0)
    sprite('vr_ph5d_04', 2)
    GFX_1('phef_nnn_nokosi', 0)
    sprite('vr_ph5d_05', 2)
    GFX_1('phef_nnn_nokosi', 0)

@State
def Eff_NNNsub():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown23015(1)
    sprite('null', 60)
    GFX_2('phef_nnn')
    GFX_0('Eff_NNNsub2', -1)

@State
def Eff_NNNsub2():

    def upon_IMMEDIATE():
        Unknown4003('phef_nnn00', '')
        Unknown3032()
        Unknown23015(1)
        Unknown3001(200)
    sprite('null', 8)
    sprite('null', 2)
    Unknown3004(-26)
    Unknown1056(600)
    Unknown1064(900)
    sprite('null', 2)
    Unknown1056(450)
    Unknown1064(700)
    sprite('null', 5)

@State
def DriveAtk_BRN():

    def upon_IMMEDIATE():
        callSubroutine('SpecialMagicInit')
        Unknown1056(6000)
        Unknown1064(6000)
        teleportRelativeX(300000)
        Unknown1007(150000)
        AttackLevel_(4)
        Damage(1800)
        Hitstop(0)
        Unknown11001(10, 10, 15)
        ProjectileDurabilityLvl(1)
        AirPushbackX(2500)
        AirPushbackY(20000)
        AirUntechableTime(40)
        AttackP1(80)
        AttackP2(80)
        AirHitstunAnimation(14)
        GroundedHitstunAnimation(14)
        Unknown9266(4)
        Unknown53(1)
        Unknown3038(1)
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 1)
        sendToLabelUpon(54, 1)

        def upon_43():
            if (SLOT_48 == 5001):
                clearUponHandler(43)
                clearUponHandler(10)
                Unknown2037(0)
                sendToLabel(1)
    sprite('vr_ph_magictest_ex', 14)
    Unknown2037(18)
    GFX_0('Eff_BRN', -1)
    SFX_3('phse_04')
    GFX_1('phef_rbn_mc', 0)
    teleportRelativeX(-100000)
    label(0)
    sprite('vr_ph_magictest_ex', 13)
    RefreshMultihit()
    GFX_0('Eff_BRN', -1)
    teleportRelativeX(20000)
    if (SLOT_2 <= 16):
        teleportRelativeX(30000)
    if (SLOT_2 <= 16):
        teleportRelativeX(30000)
    if (SLOT_2 <= 13):
        teleportRelativeX(80000)
    sprite('vr_ph_magictest_ex', 1)
    if SLOT_2:
        Unknown2038(-1)
        sendToLabel(0)
    label(1)
    sprite('null', 10)
    clearUponHandler(54)
    clearUponHandler(32)

@State
def Eff_BRN():

    def upon_IMMEDIATE():
        Unknown4003('pheff_brn00', '')
        GFX_2('phef_brn_00')
        Unknown4007(2)
        Unknown3032()
        Unknown1007(75000)
    sprite('null', 2)
    Unknown3001(255)
    GFX_1('phef_brn_00a2', -1)
    GFX_0('Eff_BRNsub', -1)
    SFX_0('014_electric_sl')
    sprite('null', 2)
    Unknown1077(-90000, 90000)
    Unknown3001(255)
    GFX_0('Eff_BRNsub', -1)
    sprite('null', 2)
    GFX_0('Eff_BRNsub', -1)
    sprite('null', 2)
    Unknown1077(-90000, 90000)
    sprite('null', 2)
    sprite('null', 2)
    Unknown3033()
    Unknown1096(1075)
    Unknown1077(-90000, 90000)
    sprite('null', 2)
    sprite('null', 3)
    Unknown1096(1100)

@State
def Eff_BRNsub():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4003('pheff_brn01', '')
        Unknown1096(750)
        Unknown1102(-50, 250)
        Unknown1077(-360000, 360000)
    sprite('null', 2)
    sprite('null', 1)
    Unknown3001(0)
    sprite('null', 2)
    Unknown3001(128)
    sprite('null', 1)
    Unknown3001(0)
    sprite('null', 2)
    Unknown3001(128)
    sprite('null', 1)
    Unknown3001(0)
    sprite('null', 2)
    Unknown3001(128)

@State
def DriveAtk_GRN():

    def upon_IMMEDIATE():
        callSubroutine('SpecialMagicInit')
        Unknown3038(1)
        teleportRelativeX(100000)
        AttackLevel_(2)
        Damage(1500)
        GroundedHitstunAnimation(9)
        AirPushbackX(25000)
        AirPushbackY(-30000)
        AirUntechableTime(22)
        Unknown9202(30)
        AttackP1(80)
        Unknown11066(1)
        Unknown11032(150000, -150000, 250000, -250000)
        Hitstop(6)
        Unknown11001(4, 4, 5)
        Unknown11056(1)
        setInvincible(1)
        Unknown22024(3000)
        GuardPoint_(1)
        Unknown22019(0, 0, 0, 1, 0)
        Unknown22026(0)
        Unknown23013(1)
        Unknown2053(1)
        EnableCollision(1)
        Unknown2015(150)
        Unknown23087(-100000)

        def upon_43():
            if (SLOT_48 == 5101):
                clearUponHandler(43)
                EnableCollision(0)
                sendToLabel(1)

        def upon_11():
            EnableCollision(0)
            Unknown1019(50)
            sendToLabel(1)
        Unknown23021(1)

        def upon_14():
            EnableCollision(0)
            sendToLabel(1)
        Unknown2037(0)

        def upon_42():
            Unknown21015('MagicActivateB_Lv1', 5102, 0)
            if (SLOT_163 > 0):
                if (SLOT_2 == 0):
                    GFX_0('RefShotAtk_GRN', 0)
                    GFX_0('Eff_GRNatk', -1)
                if (SLOT_2 == 1):
                    GFX_0('RefShotAtk_GRN', 1)
                    GFX_0('Eff_GRNatk', -1)
                if (SLOT_2 == 2):
                    GFX_0('RefShotAtk_GRN', 2)
                    GFX_0('Eff_GRNatk', -1)
                Unknown2038(1)
                if (SLOT_2 >= 3):
                    Unknown2037(0)
                sendToLabel(0)

        def upon_3():
            Unknown1019(87)
    sprite('null', 1)
    GFX_0('Eff_GRN', -1)
    Unknown38(4, 1)
    SFX_3('phse_04')
    sprite('phdrivecol_grn', 3)
    Unknown3001(128)
    physicsXImpulse(10000)
    sprite('phdrivecol_grn', 80)
    EnableCollision(0)
    label(0)
    sprite('phdrivecol_grn', 20)
    label(1)
    sprite('null', 10)
    clearUponHandler(42)
    clearUponHandler(14)
    clearUponHandler(11)
    clearUponHandler(43)
    Unknown21007(4, 32)
    ExitState()

@State
def RefShotAtk_GRN():

    def upon_IMMEDIATE():
        callSubroutine('SpecialMagicInit')
        Unknown1056(4000)
        Unknown1064(2000)
        AttackLevel_(3)
        Damage(1500)
        ProjectileDurabilityLvl(2)
        Unknown9016(1)
        Hitstop(3)
        Unknown11084(1)
        Unknown11057(300)
        Unknown11001(8, 8, 10)
        AttackP1(80)
        AttackP2(60)
        Unknown11089(-1)
        GroundedHitstunAnimation(2)
        StarterRating(2)
        Unknown3032()
        Unknown4003('pheff_grn02', '')
        Unknown4061(2)
        Unknown21004(1)
        Unknown3038(1)
    sprite('null', 10)
    Unknown3001(0)
    Unknown3004(51)
    Unknown21012('Eff_GRNmc', 32)
    GFX_0('Eff_GRNmc', -1)
    sprite('vr_ph_magictest', 30)
    physicsXImpulse(120000)
    GFX_0('Eff_GRNnokosi', -1)

@State
def Eff_GRN():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff_grn00', '')
        Unknown4007(2)
        Unknown4010(2)
        Unknown1096(500)
        Unknown3001(0)
        Unknown1007(200000)
        Unknown4061(2)
        Unknown21004(1)
        sendToLabelUpon(32, 1)
    sprite('null', 5)
    Unknown4045('phef_rnn_start', -1)
    GFX_0('Eff_GRNsub', -1)
    Unknown1056(0)
    Unknown1059(100)
    Unknown3004(51)
    gotoLabel(0)
    label(0)
    sprite('null', 20)
    Unknown1059(0)
    physicsYImpulse(400)
    Unknown3004(-2)
    Unknown4047(1, 1, 1)
    Unknown4045('phef_rnn_jizoku', -1)
    sprite('null', 10)
    physicsYImpulse(200)
    sprite('null', 20)
    Unknown4047(1, 1, 1)
    Unknown4045('phef_rnn_jizoku', -1)
    Unknown3004(2)
    physicsYImpulse(-400)
    sprite('null', 10)
    physicsYImpulse(-200)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    Unknown4047(1, 1, 1)
    Unknown4045('phef_rnn_end', -1)
    Unknown3004(-51)
    Unknown1059(-60)
    Unknown1067(60)
    loopRest()

@State
def Eff_GRNsub():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff_grn01', '')
        Unknown4007(2)
        Unknown4010(2)
        Unknown4025(2)
        Unknown4013(2)
    sprite('null', 32767)

@State
def Eff_GRNatk():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(2)
        Unknown21004(1)
        Unknown4003('pheff_grn01', '')
        Unknown1096(650)
        Unknown1007(200000)
    sprite('null', 5)
    Unknown1067(7)
    Unknown1059(15)
    sprite('null', 5)
    Unknown3004(-51)

@State
def Eff_GRNmc():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown4047(1, 1, 1)
        Unknown23067('phef_grn_atk00')

        def upon_32():
            clearUponHandler(32)
            sendToLabel(1)
    sprite('null', 55)
    label(1)
    sprite('null', 5)

@State
def Eff_GRNnokosi():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4061(2)
    label(0)
    sprite('null', 2)
    Unknown4047(1, 1, 1)
    Unknown4045('phef_grn_nokosi', -1)
    gotoLabel(0)

@State
def DriveAtk_GGB():

    def upon_IMMEDIATE():
        callSubroutine('SpecialMagicInit')
        AttackLevel_(3)
        Damage(400)
        Hitstop(0)
        Unknown11001(11, 11, 13)
        AirPushbackY(20000)
        AirUntechableTime(40)
        Unknown11032(150000, -150000, 250000, -250000)
        Unknown1056(4000)
        Unknown1064(4000)
        teleportRelativeX(150000)
        Unknown1007(125000)
        Unknown2053(1)
        Unknown23013(1)
        Unknown2015(50)
        Unknown3038(1)
        Unknown2003(1)
        loopRelated(17, 7)

        def upon_17():
            clearUponHandler(17)
            Unknown2003(0)
        Unknown2037(0)

        def upon_3():
            Unknown1019(95)
            YAccel(95)
            if SLOT_2:
                if SLOT_51:
                    Unknown1028(0)
                    Unknown2037(0)
                    sendToLabel(1)
                if (not SLOT_51):
                    if CheckInput(0x93):
                        Unknown1021(1500)
                    if CheckInput(0x45):
                        Unknown1021(-1500)

        def upon_43():
            if (SLOT_48 == 5012):
                clearUponHandler(43)
                clearUponHandler(3)
                clearUponHandler(54)
                Unknown2003(1)
                sendToLabel(0)
            if (SLOT_48 == 5013):
                clearUponHandler(54)
                Unknown2003(1)
                SLOT_51 = 1
            if (SLOT_48 == 5014):
                clearUponHandler(54)
                Unknown2003(1)
                SLOT_51 = 1

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            clearUponHandler(43)
            clearUponHandler(3)
            clearUponHandler(54)
            Unknown23029(3, 5015, 0)
            sendToLabel(100)
        Unknown23089(1, 0, 0, 0, 0, 0, 1, 0)

        def upon_54():
            clearUponHandler(10)
            clearUponHandler(43)
            clearUponHandler(3)
            clearUponHandler(54)
            clearUponHandler(17)
            sendToLabel(0)
    sprite('vr_ph_magictest', 3)
    physicsXImpulse(60000)
    Unknown1028(3000)
    SFX_3('phse_04')
    GFX_0('DriveDef_GGB', -1)
    GFX_0('Eff_GGB', -1)
    Unknown38(4, 1)
    Unknown2037(1)
    sprite('vr_ph_magictest', 3)
    Unknown1019(50)
    sprite('vr_ph_magictest', 3)
    Unknown1019(50)
    sprite('vr_ph_magictest', 60)
    label(1)
    sprite('vr_ph_magictest', 15)
    Unknown1019(25)
    sprite('vr_ph_magictest', 5)
    Unknown1084(1)
    Unknown21007(4, 34)
    Unknown21012('DriveDef_GGB', 32)
    sprite('vr_ph_magictest', 10)
    clearUponHandler(43)
    clearUponHandler(3)
    Unknown21007(4, 32)
    Unknown2003(1)
    sprite('vr_ph_magictest', 60)
    GFX_0('DriveAtk_GGB_ATKMaster', -1)
    SFX_0('013_thunder_0')
    sprite('vr_ph_magictest', 10)
    ExitState()
    label(2)
    sprite('vr_ph_magictest', 40)
    Unknown1084(1)
    sprite('vr_ph_magictest', 20)
    Unknown21007(4, 34)
    Unknown21012('DriveDef_GGB', 32)
    sprite('vr_ph_magictest', 10)
    clearUponHandler(43)
    clearUponHandler(3)
    Unknown21007(4, 32)
    Unknown2003(1)
    sprite('vr_ph_magictest', 60)
    GFX_0('DriveAtk_GGB_ATKMaster', -1)
    SFX_0('013_thunder_0')
    sprite('vr_ph_magictest', 10)
    ExitState()
    label(0)
    sprite('null', 11)
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown21012('DriveDef_GGB', 32)
    Unknown21007(4, 33)
    Unknown3004(-25)
    ExitState()
    label(100)
    sprite('vr_ph_magictest', 4)
    StartMultihit()
    sprite('vr_ph_magictest', 5)
    Unknown1019(25)
    Unknown21007(4, 34)
    Unknown21012('DriveDef_GGB', 32)
    sprite('vr_ph_magictest', 5)
    Unknown1084(1)
    clearUponHandler(43)
    clearUponHandler(3)
    Unknown21007(4, 32)
    Unknown2003(1)
    sprite('vr_ph_magictest', 60)
    GFX_0('DriveAtk_GGB_ATKMaster', -1)
    SFX_0('013_thunder_0')
    sprite('vr_ph_magictest', 10)
    ExitState()

@State
def DriveDef_GGB():

    def upon_IMMEDIATE():
        callSubroutine('SpecialMagicInit')
        Unknown3038(1)
        Unknown4007(2)

        def upon_14():
            clearUponHandler(32)
            clearUponHandler(14)
            Unknown23029(2, 5012, 0)
            sendToLabel(1)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(14)
            Unknown23022(1)
            sendToLabel(1)
    sprite('phdrivecol_ggb', 300)
    label(1)
    sprite('null', 10)

@State
def DriveAtk_GGB_ATKMaster():

    def upon_IMMEDIATE():
        Unknown2037(6)

        def upon_43():
            if (SLOT_48 == 5011):
                clearUponHandler(43)
                sendToLabel(1)
    sprite('null', 3)
    GFX_0('Eff_GGBatk', -1)
    Unknown38(4, 1)
    GFX_0('DriveAtk_GGB_ATKU', -1)
    Unknown38(5, 1)
    GFX_0('DriveAtk_GGB_ATKH', -1)
    Unknown38(6, 1)
    Unknown21007(5, 33)
    Unknown21007(6, 33)
    label(0)
    sprite('null', 2)
    Unknown21007(5, 33)
    Unknown21007(6, 33)
    sprite('null', 1)
    if (SLOT_2 == 0):
        sendToLabel(1)
    else:
        Unknown2038(-1)
        sendToLabel(0)
    label(1)
    sprite('null', 10)
    Unknown21007(4, 32)
    Unknown21007(5, 32)
    Unknown21007(6, 32)

@Subroutine
def DriveAtk_GGB_Init():
    AttackLevel_(3)
    Damage(250)
    ChipDamagePct(15)
    AttackP2(80)
    Unknown11092(1)
    Hitstop(0)
    blockstun(20)
    Unknown11001(2, 2, 4)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    AirPushbackX(25000)
    AirPushbackY(15000)
    PushbackX(39900)
    AirUntechableTime(40)
    Unknown11110(85)
    Unknown11057(200)
    Unknown11084(1)
    Unknown11056(1)

@State
def DriveAtk_GGB_ATKU():

    def upon_IMMEDIATE():
        callSubroutine('SpecialMagicInit')
        Unknown1056(120000)
        Unknown1064(1000)
        Unknown1007(25000)
        callSubroutine('DriveAtk_GGB_Init')
        Unknown3038(1)

        def upon_12():
            Damage(300)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        DisableAttackRestOfMove()
    sprite('null', 10)
    label(1)
    sprite('vr_ph_magictest', 4)
    RefreshMultihit()
    sprite('null', 60)
    label(0)
    sprite('null', 5)

@State
def DriveAtk_GGB_ATKH():

    def upon_IMMEDIATE():
        callSubroutine('SpecialMagicInit')
        Unknown1056(1000)
        Unknown1064(100000)
        Unknown1007(-600000)
        callSubroutine('DriveAtk_GGB_Init')
        Unknown3038(1)

        def upon_12():
            Damage(400)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
    sprite('null', 10)
    label(1)
    sprite('vr_ph_magictest', 4)
    RefreshMultihit()
    sprite('null', 60)
    label(0)
    sprite('null', 5)

@State
def Eff_GGB():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4010(2)
        Unknown4003('pheff_ggb01', '')
        Unknown4015()
        Unknown1096(1100)
        Unknown1007(50000)
        GFX_2('phef_ggb_add')
        sendToLabelUpon(32, 1)
        sendToLabelUpon(33, 2)
        sendToLabelUpon(34, 100)
        Unknown3001(0)
        Unknown3004(63)
    label(0)
    sprite('null', 2)
    Unknown1096(1100)
    GFX_0('Eff_GGBMoya', -1)
    sprite('null', 2)
    Unknown1096(1000)
    sprite('null', 2)
    Unknown1096(1100)
    sprite('null', 2)
    Unknown1096(1000)
    SFX_0('014_electric_s')
    gotoLabel(0)
    label(100)
    clearUponHandler(34)
    sprite('null', 5)
    Unknown3001(255)
    Unknown3004(-23)
    Unknown1096(1000)
    Unknown1099(-90)
    Unknown21012('Eff_GGBMoya', 32)
    sprite('null', 5)
    GFX_0('Eff_GGBPre', -1)
    sprite('null', 10)
    Unknown3001(0)
    Unknown3004(0)
    Unknown1096(0)
    Unknown1099(0)
    label(1)
    clearUponHandler(32)
    clearUponHandler(33)
    sprite('null', 7)
    ScreenShake(20000, 20000)
    Unknown3001(255)
    Unknown1096(1000)
    Unknown1099(200)
    GFX_1('phef_ggb_start', -1)
    Unknown21012('Eff_GGBMoya', 32)
    loopRest()
    label(2)
    clearUponHandler(32)
    clearUponHandler(33)
    sprite('null', 10)
    Unknown3001(255)
    Unknown3004(-23)
    Unknown21012('Eff_GGBMoya', 32)
    loopRest()

@State
def Eff_GGBPre():

    def upon_IMMEDIATE():
        Unknown1096(250)
        GFX_2('phef_ggb_end')
    sprite('null', 60)

@State
def Eff_DriveMagicCircle():

    def upon_IMMEDIATE():
        GFX_2('phef_magicAir_mc')

        def upon_3():
            Unknown2071('03000000b03cffffc0f2fcff6400000001000000')
    sprite('null', 20)

@State
def Eff_GGBMoya():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4007(2)
        sendToLabelUpon(32, 1)
        Unknown4061(2)
        Unknown4047(1, 1, 1)
        Unknown23067('phef_rrb_moya')
        Unknown1096(700)
    sprite('null', 32767)
    label(1)
    sprite('null', 10)
    Unknown1099(-25)
    Unknown3004(-31)

@State
def Eff_GGBatk():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4010(2)
        Unknown4003('pheff_ggb00', '')
        Unknown4015()
        Unknown1007(50000)
        sendToLabelUpon(32, 1)
        GFX_2('phef_ggb_jizoku')
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 2)
    Unknown1096(1300)
    ScreenShake(1000, 1000)
    sprite('null', 2)
    Unknown1096(1250)
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    Unknown1099(-25)
    GFX_1('phef_ggb_end', -1)
    loopRest()

@State
def DriveAtk_BBR():

    def upon_IMMEDIATE():
        callSubroutine('SpecialMagicInit')
        Unknown3032()
        Unknown4011(2)
        Unknown1096(550)
        Unknown3001(0)
        GFX_2('phef_rrb_add')
        teleportRelativeX(150000)
        Unknown1007(200000)
        Unknown3038(1)
        Unknown2003(1)
        Unknown23089(1, 0, 0, 0, 0, 0, 1, 0)

        def upon_54():
            clearUponHandler(43)
            clearUponHandler(54)
            sendToLabel(1)

        def upon_43():
            if (SLOT_48 == 5021):
                clearUponHandler(43)
                clearUponHandler(54)
                sendToLabel(1)
    sprite('null', 10)
    physicsXImpulse(2000)
    GFX_0('Eff_BBRSub', -1)
    GFX_0('ParticleMaster_BBR', -1)
    Unknown4003('pheff_bbr00', '')
    Unknown3001(0)
    Unknown3004(51)
    SFX_3('phse_04')
    sprite('null', 20)
    sprite('null', 4)
    Unknown1019(2500)
    Unknown3001(255)
    Unknown3004(-63)
    SFX_0('000_airdash_0')
    sprite('null', 20)
    Unknown3001(0)
    Unknown3004(0)
    sprite('null', 5)
    Unknown1086(22)
    Unknown1007(200000)
    Unknown1019(0)
    YAccel(0)
    sprite('null', 4)
    Unknown3001(0)
    Unknown3004(51)
    physicsXImpulse(-60000)
    physicsYImpulse(50000)
    sprite('null', 6)
    Unknown3001(255)
    Unknown3004(0)
    Unknown1019(10)
    YAccel(10)
    sprite('null', 6)
    Unknown1019(10)
    YAccel(10)
    sprite('null', 2)
    Unknown1019(0)
    YAccel(0)
    Unknown4003('pheff_bbr01', '')
    sprite('null', 3)
    GFX_0('DriveAtk_BBR_ATK', -1)
    Unknown21007(1, 32)
    physicsXImpulse(-8000)
    physicsYImpulse(8000)
    sprite('null', 3)
    Unknown1019(25)
    YAccel(25)
    sprite('null', 3)
    Unknown1019(25)
    YAccel(25)
    sprite('null', 6)
    Unknown1019(0)
    YAccel(0)
    sprite('null', 6)
    physicsXImpulse(5000)
    physicsYImpulse(-1500)
    Unknown4003('pheff_bbr00', '')
    sprite('null', 4)
    Unknown1019(2500)
    YAccel(2500)
    Unknown3001(255)
    Unknown3004(-63)
    SFX_0('000_airdash_0')
    sprite('null', 10)
    Unknown3001(0)
    Unknown3004(0)
    Unknown1019(0)
    YAccel(0)
    sprite('null', 5)
    Unknown1086(22)
    Unknown1007(200000)
    sprite('null', 4)
    Unknown3001(0)
    Unknown3004(51)
    physicsXImpulse(80000)
    sprite('null', 6)
    Unknown3001(255)
    Unknown3004(0)
    Unknown1019(5)
    YAccel(5)
    Unknown2006()
    sprite('null', 6)
    Unknown1019(5)
    YAccel(5)
    sprite('null', 2)
    Unknown1019(0)
    YAccel(0)
    Unknown1072(15000)
    Unknown4003('pheff_bbr01', '')
    sprite('null', 3)
    GFX_0('DriveAtk_BBR_ATK', -1)
    Unknown21007(1, 33)
    physicsXImpulse(-8000)
    sprite('null', 3)
    Unknown1019(25)
    sprite('null', 3)
    Unknown1019(25)
    sprite('null', 6)
    Unknown1019(0)
    sprite('null', 6)
    physicsXImpulse(6000)
    Unknown4003('pheff_bbr00', '')
    sprite('null', 4)
    Unknown1072(0)
    Unknown1019(2500)
    YAccel(2500)
    Unknown3001(255)
    Unknown3004(-63)
    SFX_0('000_airdash_0')
    sprite('null', 10)
    Unknown3004(-63)
    Unknown3001(0)
    Unknown3004(0)
    Unknown1019(0)
    YAccel(0)
    sprite('null', 5)
    Unknown1086(22)
    teleportRelativeX(-30000)
    Unknown1007(200000)
    sprite('null', 4)
    Unknown3001(0)
    Unknown3004(51)
    physicsYImpulse(75000)
    sprite('null', 6)
    Unknown3001(255)
    Unknown3004(0)
    Unknown1019(5)
    YAccel(5)
    sprite('null', 6)
    Unknown1019(5)
    YAccel(5)
    sprite('null', 2)
    Unknown1019(0)
    YAccel(0)
    Unknown2006()
    sprite('null', 3)
    Unknown4003('pheff_bbr01', '')
    Unknown1072(35000)
    GFX_0('DriveAtk_BBR_ATK', -1)
    Unknown21007(1, 34)
    physicsYImpulse(8000)
    sprite('null', 5)
    YAccel(25)
    sprite('null', 5)
    YAccel(25)
    sprite('null', 10)
    YAccel(0)
    sprite('null', 5)
    Unknown4003('pheff_bbr00', '')
    physicsXImpulse(-20000)
    physicsYImpulse(2000)
    sprite('null', 5)
    Unknown1019(50)
    YAccel(50)
    sprite('null', 5)
    physicsYImpulse(-5000)
    sprite('null', 5)
    Unknown1019(50)
    YAccel(200)
    sprite('null', 5)
    physicsXImpulse(10000)
    YAccel(200)
    sprite('null', 8)
    Unknown1072(0)
    Unknown1019(1500)
    YAccel(150)
    Unknown3001(255)
    Unknown3004(-15)
    SFX_0('000_airdash_0')
    sprite('null', 30)
    Unknown3001(0)
    Unknown3004(0)
    ExitState()
    label(1)
    sprite('null', 10)
    Unknown4003('pheff_bbr00', '')
    Unknown1019(0)
    YAccel(0)
    Unknown3004(-28)

@State
def DriveAtk_BBR_PreAtk():

    def upon_IMMEDIATE():
        callSubroutine('SpecialMagicInit')
        Unknown1056(4000)
        Unknown1064(4000)
        AttackLevel_(2)
        Damage(300)
        AirPushbackX(20000)
        AirPushbackY(10000)
        AirUntechableTime(26)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        Unknown11107(1)
        Unknown3038(1)

        def upon_3():
            Unknown2071('02000000e0b1ffffc063ffff6400000001000000')
    sprite('vr_ph_magictest', 10)

@State
def ParticleMaster_BBR():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(3)
        Unknown4007(2)
    label(0)
    sprite('null', 4)
    GFX_1('phef_rrb_tb', -1)
    gotoLabel(0)

@State
def DriveAtk_BBR_ATK():

    def upon_IMMEDIATE():
        callSubroutine('SpecialMagicInit')
        Unknown1056(1500)
        Unknown1064(1500)
        AttackLevel_(2)
        Damage(1500)
        AttackP1(80)
        AirPushbackX(250)
        AirPushbackY(25000)
        AirUntechableTime(20)
        Unknown11001(0, 10, 11)
        Unknown11057(500)
        Unknown23182(2)
        Unknown3038(1)
        Unknown53(1)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            Unknown2001()

        def upon_32():
            Unknown1072(45000)
            physicsXImpulse(60000)
            physicsYImpulse(-60000)

        def upon_33():
            physicsXImpulse(60000)

        def upon_34():
            AirPushbackX(0)
            AirPushbackY(-40000)
            Unknown11056(3)
            Unknown9190(1)
            Unknown9118(25)
            Unknown1072(90000)
            physicsYImpulse(-60000)
    sprite('vr_ph_magictest', 120)
    GFX_0('Eff_BBRmc', -1)
    GFX_0('Eff_BBRAtk', -1)
    SFX_3('phse_07')
    label(1)
    sprite('null', 10)
    Unknown3004(-23)

@State
def Eff_BBRSub():

    def upon_IMMEDIATE():
        Unknown4047(1, 1, 1)
        Unknown23067('phef_rrb_moya')
        Unknown4010(2)
        Unknown4007(2)
        Unknown4025(2)
        Unknown3032()
        Unknown4061(2)
    sprite('null', 32767)

@State
def Eff_BBRAtk():

    def upon_IMMEDIATE():
        Unknown4054(7)
        Unknown23067('phef_rrbatk_add')
        Unknown4010(2)
        Unknown4007(2)
        Unknown4025(2)
        Unknown4006(2)
        Unknown3032()
        Unknown4061(3)
        Unknown23015(8)
        Unknown3029(1)
        Unknown3069(2)
        Unknown1096(1000)
    label(0)
    sprite('vr_phbbr_00', 2)
    GFX_1('phef_rrbatk_bgnokosi', -1)
    GFX_1('phef_rrbatk_tb', -1)
    GFX_1('phef_rrbatk_tb2', -1)
    GFX_0('Eff_BBRBlack', -1)
    sprite('vr_phbbr_01', 2)
    GFX_1('phef_rrbatk_bgnokosi', -1)
    sprite('vr_phbbr_02', 2)
    GFX_1('phef_rrbatk_bgnokosi', -1)
    GFX_1('phef_rrbatk_tb', -1)
    GFX_1('phef_rrbatk_tb2', -1)
    GFX_0('Eff_BBRBlack', -1)
    sprite('vr_phbbr_03', 2)
    GFX_1('phef_rrbatk_bgnokosi', -1)
    gotoLabel(0)

@State
def Eff_BBRBlack():

    def upon_IMMEDIATE():
        Unknown4003('pheff_bbrAtk', '')
        Unknown4006(2)
        Unknown3032()
    sprite('null', 5)
    sprite('null', 10)
    Unknown3004(-26)

@State
def Eff_BBRmc():

    def upon_IMMEDIATE():
        GFX_2('phef_bbr_entermc')
        Unknown4006(2)
        Unknown3032()
    sprite('null', 30)

@State
def DriveAtk_RRG():

    def upon_IMMEDIATE():
        callSubroutine('SpecialMagicInit')
        Unknown3038(1)
        Unknown1056(4500)
        Unknown1064(3000)
        teleportRelativeX(100000)
        Unknown1007(270000)
        AttackLevel_(3)
        Damage(400)
        Hitstop(6)
        Unknown11001(5, 5, 7)
        AirUntechableTime(30)
        AirPushbackX(10000)
        AirPushbackY(-20000)
        Unknown11032(150000, -150000, 250000, -250000)
        Unknown23013(1)
        Unknown23089(1, 0, 0, 0, 0, 0, 1, 0)

        def upon_54():
            clearUponHandler(32)
            clearUponHandler(54)
            sendToLabel(2)

        def upon_4():
            clearUponHandler(4)
            sendToLabel(0)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)

        def upon_43():
            if (SLOT_48 == 5111):
                clearUponHandler(43)
                sendToLabel(2)
    sprite('vr_ph_magictest', 6)
    StartMultihit()
    physicsXImpulse(8500)
    physicsYImpulse(10000)
    Unknown1043()
    GFX_0('phEff_RRGseed', -1)
    Unknown36(1)
    Unknown1007(30000)
    Unknown35()
    SFX_3('phse_04')
    sprite('vr_ph_magictest', 32767)
    label(0)
    sprite('vr_ph_magictest', 32767)
    label(1)
    sprite('vr_ph_magictest', 10)
    AttackLevel_(5)
    Damage(1500)
    HitLow(2)
    AirPushbackX(20000)
    AirPushbackY(-20000)
    AttackP1(80)
    Hitstop(0)
    PushbackX(19950)
    Unknown11001(6, 6, 8)
    Unknown9202(17)

    def upon_11():
        Unknown2038(1)

    def upon_3():
        if (not SLOT_158):
            HitLow(0)
        if (SLOT_2 >= 1):
            HitLow(0)
    Unknown26('phEff_RRGseed')
    GFX_1('phef_rrb_umore', -1)
    Unknown1059(500)
    Unknown1067(150)
    StartMultihit()
    Unknown1084(1)
    Unknown2006()
    SFX_0('012_stab_deep')
    sprite('vr_ph_magictest', 15)
    GFX_0('phEff_RRGmoguri', -1)
    Unknown1056(7500)
    Unknown1064(4000)
    Unknown1059(0)
    Unknown1067(0)
    StartMultihit()
    physicsXImpulse(1000)
    SFX_0('019_quake_1')
    sprite('vr_ph_magictest', 10)
    RefreshMultihit()
    GroundedHitstunAnimation(2)
    Unknown9130(40)
    Unknown9142(30)
    Unknown2006()
    physicsXImpulse(45000)
    GFX_0('phEff_RRG', -1)
    SFX_0('005_swing_grap_2_2')
    SFX_3('phse_05')
    sprite('vr_ph_magictest', 13)
    StartMultihit()
    Unknown1019(5)
    sprite('vr_ph_magictest', 10)
    RefreshMultihit()
    Unknown2006()
    PushbackX(50000)
    GroundedHitstunAnimation(9)
    AirPushbackX(20000)
    Unknown9202(12)
    Unknown9310(20)
    physicsXImpulse(45000)
    GFX_0('phEff_RRG', -1)
    SFX_0('005_swing_grap_2_2')
    SFX_3('phse_05')
    sprite('vr_ph_magictest', 20)
    StartMultihit()
    Unknown1019(5)
    ExitState()
    label(2)
    sprite('null', 10)
    Unknown3004(-23)
    ExitState()

@State
def phEff_RRG():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3032()
        Unknown1096(1000)
        Unknown2005()
        GFX_2('phef_rrb_kusa')
    sprite('null', 7)
    Unknown4003('pheff_rrg_start', '')
    ScreenShake(4000, 4000)
    GFX_1('phef_rrb_kusa', -1)
    GFX_0('phEff_RRG_moya', -1)
    sprite('null', 10)
    Unknown4003('pheff_rrg_jizoku', '')
    sprite('null', 5)
    Unknown4007(0)
    sprite('null', 40)
    Unknown3001(0)
    GFX_0('phEff_RRGend', -1)
    Unknown21012('phEff_RRG_moya', 32)

@State
def phEff_RRG_moya():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3032()
        Unknown1096(1000)
        Unknown4061(2)
        Unknown4047(1, 1, 1)
        Unknown23067('phef_rrg_moya')
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    Unknown3004(-26)
    Unknown4047(1, 1, 1)
    Unknown4045('phef_rrg_tb', -1)

@State
def phEff_RRGseed():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4061(2)
        Unknown1096(1200)
        Unknown1074(1250)
        Unknown23015(8)
        Unknown4054(7)
        Unknown23067('phef_rrb_seed')
        Unknown3029(1)
    sprite('vr_phrrg_00', 10)
    Unknown1074(1250)
    sprite('vr_phrrg_00', 10)
    Unknown1074(625)
    sprite('vr_phrrg_00', 32767)
    Unknown1074(416)

@State
def phEff_RRGend():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1096(1200)
    sprite('null', 15)
    GFX_1('phef_rrb_kusa', -1)
    Unknown4003('pheff_rrg_end', '')

@State
def phEff_RRGmoguri():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4007(2)
    label(0)
    sprite('null', 4)
    GFX_1('phef_rrb_umore2', -1)
    gotoLabel(0)

@State
def DriveAtk_GGR():

    def upon_IMMEDIATE():
        callSubroutine('SpecialMagicInit')
        Unknown4011(3)
        Unknown1096(200)
        teleportRelativeX(150000)
        Unknown1007(225000)
        Unknown2053(1)
        Unknown2003(1)
        Unknown3038(1)
        Unknown3032()
        Unknown4003('pheff_ggr00', '')
        Unknown4015()
        Unknown4061(2)
        Unknown4047(1, 1, 1)
        Unknown23067('phef_ggr_jizoku')
        Unknown2037(0)

        def upon_3():
            if SLOT_2:
                YAccel(95)

        def upon_43():
            if (SLOT_48 == 5121):
                clearUponHandler(43)
                clearUponHandler(3)
                sendToLabel(0)
    sprite('null', 10)
    GFX_1('phef_ggr_mc', -1)
    Unknown3001(0)
    Unknown3004(28)
    Unknown1099(30)
    SFX_3('phse_04')
    physicsXImpulse(5000)
    physicsYImpulse(5000)
    sprite('null', 10)
    Unknown3001(255)
    Unknown3004(0)
    Unknown1099(0)
    sprite('null', 5)
    Unknown2037(1)
    Unknown1019(1200)
    YAccel(1800)
    sprite('null', 2)
    Unknown2037(0)
    Unknown1019(40)
    YAccel(40)
    sprite('null', 2)
    Unknown1019(40)
    YAccel(40)
    sprite('null', 2)
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown1099(100)
    sprite('null', 10)
    clearUponHandler(3)

    def upon_3():
        Unknown48(25, 2, 52, 22, 2, 22)
        Unknown47('01000000020000001600000002000000340000000200000034000000')
        if SLOT_38:
            Unknown47('030000000200000034000000000000003c000000020000000c000000')
        else:
            Unknown47('03000000020000003400000000000000c4ffffff020000000c000000')
    GFX_0('phEff_GGRYotyouMC', -1)
    Unknown1099(0)
    sprite('null', 5)
    clearUponHandler(3)
    Unknown1019(80)
    GFX_0('phEff_GGRatk', -1)
    sprite('null', 5)
    Unknown1019(80)
    sprite('null', 5)
    Unknown1019(80)
    sprite('null', 5)
    Unknown1019(80)
    sprite('null', 5)
    Unknown1019(80)
    sprite('null', 5)
    physicsXImpulse(0)
    sprite('null', 3)
    Unknown21012('phEff_GGRYotyouMC', 32)
    GFX_0('DriveAtk_GGR_C', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_R', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_L', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_RR', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_LL', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_C', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_R', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_L', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_RR', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_LL', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_C', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_R', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_L', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_RR', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_LL', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_C', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_R', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_L', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_RR', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_LL', -1)
    sprite('null', 60)
    Unknown21012('phEff_GGRatk', 32)
    Unknown21012('phEff_GGRYotyouMC', 33)
    Unknown3004(-25)
    ExitState()
    label(0)
    sprite('null', 15)
    Unknown21012('phEff_GGRatk', 32)
    Unknown3004(-15)
    ExitState()

@State
def phEff_GGRatk():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1096(200)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('pheff_ggr01', '')
        Unknown4015()

        def upon_32():
            clearUponHandler(32)
            sendToLabel(0)
    sprite('null', 10)
    ScreenShake(10000, 10000)
    Unknown3001(0)
    Unknown3004(20)
    physicsYImpulse(-16000)
    Unknown1099(20)
    SFX_0('016_explode_0')
    SFX_0('019_quake_1')
    sprite('null', 100)
    Unknown3004(0)
    Unknown1099(0)
    physicsYImpulse(0)
    Unknown1099(0)
    Unknown4061(2)
    Unknown4047(1, 1, 1)
    Unknown23067('phef_ggr_ray')
    label(0)
    sprite('null', 10)
    Unknown3004(-23)
    loopRest()

@State
def phEff_GGRtama():

    def upon_IMMEDIATE():
        Unknown4061(3)
        Unknown3032()
        Unknown4010(2)
        Unknown4007(2)
        Unknown23015(8)
        Unknown4054(7)
        Unknown4047(1, 1, 1)
        Unknown23067('phef_ggr_tamacolor')
        Unknown1056(1000)
    sprite('vr_phbbr_00', 2)
    Unknown1007(150000)
    label(0)
    sprite('vr_phbbr_00', 2)
    GFX_0('Eff_GGRfire', -1)
    sprite('vr_phbbr_01', 2)
    sprite('vr_phbbr_02', 2)
    GFX_0('Eff_GGRfire2', -1)
    sprite('vr_phbbr_03', 2)
    gotoLabel(0)

@State
def Eff_GGRfire():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4006(2)
        Unknown4003('pheff_ggrAtk00', '')
        Unknown1064(500)
        Unknown1056(600)
        Unknown1102(-100, 100)
    sprite('null', 3)
    sprite('null', 5)
    Unknown3004(-51)

@State
def Eff_GGRfire2():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4006(2)
        Unknown4003('pheff_ggrAtk00', '')
        Unknown1064(500)
        Unknown1056(-600)
        Unknown1062(0, 200)
    sprite('null', 3)
    sprite('null', 5)
    Unknown1102(-100, 100)

@State
def phEff_GGRgshock():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown1096(400)
        Unknown3033()
        Unknown4061(2)
        Unknown23015(1)
        Unknown1077(-360000, 360000)
        Unknown1011(50000, 100000)
        Unknown1010(-25000, 25000)
        Unknown1102(0, 300)
    sprite('vr_ph216_00', 2)
    Unknown1099(30)
    sprite('vr_ph216_01', 2)
    sprite('vr_ph216_02', 2)
    sprite('vr_ph216_03', 2)
    sprite('vr_ph216_04', 2)
    sprite('vr_ph216_05', 5)

@Subroutine
def DriveAtk_GGR_Init():
    AttackLevel_(3)
    Damage(350)
    AirHitstunAnimation(10)
    AttackP1(80)
    AttackP2(100)
    Unknown11092(1)
    Unknown23182(2)
    AirUntechableTime(25)
    AirPushbackX(0)
    AirPushbackY(12000)
    Hitstop(0)
    Unknown11001(2, 2, 4)
    PushbackX(0)
    Unknown11057(300)
    Unknown11084(1)

@State
def DriveAtk_GGR_C():

    def upon_IMMEDIATE():
        callSubroutine('SpecialMagicInit')
        callSubroutine('DriveAtk_GGR_Init')
        Unknown1056(1500)
        Unknown1064(1500)
        Unknown1007(-100000)
        Unknown3038(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(3)
            sendToLabel(2)
    sprite('vr_ph_magictest', 32767)
    SFX_0('015_blaze_0')
    GFX_0('phEff_GGRtama', -1)
    Unknown36(1)
    Unknown1072(90000)
    Unknown35()
    physicsYImpulse(-60000)
    label(1)
    sprite('null', 1)
    SFX_0('016_explode_1')
    GFX_0('phEff_GGRgshock', -1)
    GFX_1('phef_ggr_gshock', -1)
    Unknown1084(1)
    ScreenShake(1000, 1000)
    loopRest()
    ExitState()
    label(2)
    sprite('null', 4)
    Unknown3001(255)
    Unknown3004(-51)
    ExitState()

@State
def DriveAtk_GGR_L():

    def upon_IMMEDIATE():
        callSubroutine('SpecialMagicInit')
        callSubroutine('DriveAtk_GGR_Init')
        teleportRelativeX(-25000)
        Unknown1007(-100000)
        Unknown1056(1500)
        Unknown1064(1500)
        Unknown3038(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(3)
            sendToLabel(2)
    sprite('vr_ph_magictest', 32767)
    physicsXImpulse(-11000)
    physicsYImpulse(-60000)
    GFX_0('phEff_GGRtama', -1)
    Unknown36(1)
    Unknown1072(90000)
    Unknown35()
    label(1)
    sprite('null', 1)
    GFX_0('phEff_GGRgshock', -1)
    GFX_1('phef_ggr_gshock', -1)
    Unknown1084(1)
    ScreenShake(1000, 1000)
    loopRest()
    label(2)
    sprite('null', 4)
    Unknown3001(255)
    Unknown3004(-51)
    ExitState()

@State
def DriveAtk_GGR_LL():

    def upon_IMMEDIATE():
        callSubroutine('SpecialMagicInit')
        callSubroutine('DriveAtk_GGR_Init')
        teleportRelativeX(-50000)
        Unknown1007(-100000)
        Unknown1056(1500)
        Unknown1064(1500)
        Unknown3038(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(3)
            sendToLabel(2)
    sprite('vr_ph_magictest', 32767)
    physicsXImpulse(-22000)
    physicsYImpulse(-60000)
    GFX_0('phEff_GGRtama', -1)
    Unknown36(1)
    Unknown1072(100000)
    Unknown35()
    label(1)
    sprite('null', 1)
    GFX_0('phEff_GGRgshock', -1)
    GFX_1('phef_ggr_gshock', -1)
    Unknown1084(1)
    ScreenShake(1000, 1000)
    loopRest()
    label(2)
    sprite('null', 4)
    Unknown3001(255)
    Unknown3004(-51)
    ExitState()

@State
def DriveAtk_GGR_R():

    def upon_IMMEDIATE():
        callSubroutine('SpecialMagicInit')
        callSubroutine('DriveAtk_GGR_Init')
        teleportRelativeX(25000)
        Unknown1007(-100000)
        Unknown1056(1500)
        Unknown1064(1500)
        Unknown3038(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(3)
            sendToLabel(2)
    sprite('vr_ph_magictest', 32767)
    physicsXImpulse(11000)
    physicsYImpulse(-60000)
    GFX_0('phEff_GGRtama', -1)
    Unknown36(1)
    Unknown1072(85000)
    Unknown35()
    label(1)
    sprite('null', 1)
    GFX_0('phEff_GGRgshock', -1)
    GFX_1('phef_ggr_gshock', -1)
    Unknown1084(1)
    ScreenShake(1000, 1000)
    loopRest()
    ExitState()
    label(2)
    sprite('null', 4)
    Unknown3001(255)
    Unknown3004(-51)
    ExitState()

@State
def DriveAtk_GGR_RR():

    def upon_IMMEDIATE():
        callSubroutine('SpecialMagicInit')
        callSubroutine('DriveAtk_GGR_Init')
        teleportRelativeX(50000)
        Unknown1007(-100000)
        Unknown1056(1500)
        Unknown1064(1500)
        Unknown3038(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(3)
            sendToLabel(2)
    sprite('vr_ph_magictest', 32767)
    physicsXImpulse(22000)
    physicsYImpulse(-60000)
    GFX_0('phEff_GGRtama', -1)
    Unknown36(1)
    Unknown1072(75000)
    Unknown35()
    label(1)
    sprite('null', 1)
    GFX_0('phEff_GGRgshock', -1)
    GFX_1('phef_ggr_gshock', -1)
    Unknown1084(1)
    ScreenShake(1000, 1000)
    loopRest()
    ExitState()
    label(2)
    sprite('null', 4)
    Unknown3001(255)
    Unknown3004(-51)
    ExitState()

@State
def phEff_GGRYotyouMC():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown23015(5)
        Unknown4003('pheff_ggr00_yotyou', '')
        Unknown1086(2)
        teleportRelativeY(0)
        Unknown1056(900)
        Unknown1064(600)
        Unknown3001(160)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        Unknown48(25, 2, 51, 2, 2, 23)
        Unknown47('03000000020000003300000000000000200300000200000067000000')
        if (SLOT_103 > 2000):
            SLOT_103 = 2000

        def upon_3():
            Unknown1086(2)
            teleportRelativeY(0)
    sprite('null', 32767)
    GFX_0('phEff_GGRYotyouMCcolor', -1)
    GFX_0('phEff_GGRYotyouMCcore', -1)
    label(0)
    sprite('null', 32767)
    Unknown21012('phEff_GGRYotyouMCcolor', 32)
    label(1)
    sprite('null', 5)
    Unknown21012('phEff_GGRYotyouMCcore', 32)
    sprite('null', 5)
    Unknown3004(-51)

@State
def phEff_GGRYotyouMCcore():

    def upon_IMMEDIATE():
        Unknown4010(2)
        GFX_2('phef_rgg_yotei_mc')
        Unknown1056(900)
        Unknown1064(600)
        sendToLabelUpon(32, 0)

        def upon_3():
            Unknown1086(2)
            teleportRelativeY(0)
    sprite('null', 32767)
    label(0)
    sprite('null', 5)
    Unknown1099(80)
    sprite('null', 5)
    Unknown3004(-51)

@State
def phEff_GGRYotyouMCcolor():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown4010(2)
        Unknown4047(1, 1, 1)
        Unknown23067('phef_rgg_yotei_color')
        Unknown1096(700)
        sendToLabelUpon(32, 0)

        def upon_3():
            Unknown1086(2)
            teleportRelativeY(0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    Unknown3004(-26)

@State
def DriveAtk_BGR():

    def upon_IMMEDIATE():
        callSubroutine('SpecialMagicInit')
        Unknown2011()
        Unknown1096(20000)
        AttackP1(80)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(0)
        AirPushbackY(100000)
        AirUntechableTime(180)
        Hitstop(2)
        Unknown11001(0, 0, 1)
        Unknown11069('DriveAtk_BGR')
        ChipDamagePct(25)
        Unknown11056(3)
        Unknown11044(1)
        Unknown2008()
        Unknown30065(0)
        Unknown3038(1)
        MinimumDamagePct(35)
        ProjectileDurabilityLvl(1)

        def upon_3():
            Unknown48(25, 2, 2, 22, 2, 170)
            if SLOT_2:
                clearUponHandler(3)
                sendToLabel(1)

        def upon_43():
            if (SLOT_48 == 5201):
                clearUponHandler(43)
                sendToLabel(1)
            if (SLOT_48 == 5202):
                AttackLevel_(3)
                Damage(1500)
                AttackP1(75)
                AttackP2(70)
                ChipDamagePct(20)
                Unknown11110(70)
            if (SLOT_48 == 5203):
                AttackLevel_(4)
                Damage(1750)
                AttackP1(65)
                AttackP2(75)
                ChipDamagePct(20)
                Unknown11110(70)
            if (SLOT_48 == 5204):
                AttackLevel_(5)
                Damage(2000)
                AttackP1(55)
                AttackP2(80)
                ChipDamagePct(20)
                Unknown11110(70)
            if (SLOT_48 == 5205):
                SLOT_7 = 1
                sendToLabel(100)

        def upon_STATE_END():
            if SLOT_7:
                SLOT_7 = 0
    sprite('null', 10)
    SFX_3('phse_04')
    GFX_0('Eff_BGRcount', -1)
    Unknown38(4, 1)
    sprite('null', 600)
    label(0)
    sprite('null', 64)
    SLOT_7 = 1
    clearUponHandler(43)
    Unknown1086(22)
    Unknown21007(4, 32)
    Unknown2036(63, -1, 2)
    Unknown48(25, 2, 2, 2, 2, 158)
    if SLOT_2:
        GFX_0('Eff_BGRCamera', -1)
    GFX_0('Eff_BGRstart', -1)
    GFX_0('Eff_BGRbg', -1)
    Unknown38(5, 1)
    SFX_0('302_spsys_drivemotion')
    SFX_0('303_supercancel')
    sprite('vr_ph_magictestex02', 1)
    Unknown21007(4, 33)
    GFX_0('Eff_BGRmato', -1)
    ScreenShake(0, 20000)
    sprite('vr_ph_magictestex02', 1)
    RefreshMultihit()
    Unknown11087(0, 0)
    sprite('vr_ph_magictestex02', 1)
    RefreshMultihit()
    sprite('vr_ph_magictestex02', 1)
    RefreshMultihit()
    sprite('vr_ph_magictestex02', 1)
    RefreshMultihit()
    Unknown11069('')
    sprite('vr_ph_magictest', 25)
    Unknown2001()
    sprite('vr_ph_magictest', 10)
    Unknown21007(5, 32)
    ExitState()
    label(1)
    sprite('null', 10)
    clearUponHandler(3)
    clearUponHandler(43)
    Unknown21007(4, 33)
    Unknown21007(5, 32)
    ExitState()
    label(100)
    sprite('null', 19)
    Unknown13(4)
    GFX_0('Eff_BGRcountFast', -1)
    Unknown38(4, 1)
    sprite('null', 10)
    sendToLabel(0)
    ExitState()

@State
def Eff_BGRcountFast():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown1096(50)
        Unknown23015(6)
        Unknown1086(22)
        Unknown1007(240000)

        def upon_3():
            Unknown2071('160000000000000050c300003200000001000000')
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
    sprite('vr_phbgr_00', 10)
    GFX_0('Eff_BGRhariFast', -1)
    Unknown1096(800)
    Unknown1099(0)
    Unknown1074(36000)
    sprite('vr_phbgr_00', 1)
    Unknown1074(0)
    sprite('vr_phbgr_00', 2)
    GFX_0('Eff_BGRcountSub1', 2)
    Unknown38(4, 1)
    sprite('vr_phbgr_00', 2)
    GFX_0('Eff_BGRcountSub2', 3)
    Unknown38(5, 1)
    sprite('vr_phbgr_00', 2)
    GFX_0('Eff_BGRcountSub3', 1)
    Unknown38(6, 1)
    sprite('vr_phbgr_00', 1)
    GFX_0('Eff_BGRcountSub4', 0)
    Unknown38(7, 1)
    sprite('vr_phbgr_00', 32767)
    label(0)
    sprite('vr_phbgr_00', 32767)
    clearUponHandler(3)
    Unknown1096(1300)
    Unknown1086(22)
    Unknown1007(200000)
    Unknown21007(4, 32)
    Unknown21007(5, 32)
    Unknown21007(6, 32)
    Unknown21007(7, 32)
    label(1)
    sprite('null', 1)

@State
def Eff_BGRhariFast():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1096(1200)
        Unknown23015(8)
        Unknown4011(3)
        Unknown4010(2)
        Unknown4007(2)
    sprite('vr_phbgr_01', 10)
    Unknown1074(36000)
    sprite('vr_phbgr_01', 32767)
    Unknown3001(255)
    Unknown3004(0)
    Unknown1099(0)
    Unknown1074(36000)

@State
def Eff_BGRcount():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown1096(50)
        Unknown23015(6)
        Unknown1086(22)
        Unknown1007(240000)

        def upon_3():
            Unknown2071('160000000000000050c300003200000001000000')
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
    sprite('vr_phbgr_00', 10)
    SFX_0('022_magiccircle_b')
    GFX_0('Eff_BGRhari', -1)
    Unknown1099(75)
    sprite('vr_phbgr_00', 78)
    Unknown1096(800)
    Unknown1099(0)
    sprite('vr_phbgr_00', 138)
    GFX_0('Eff_BGRcountSub1', 2)
    Unknown38(4, 1)
    sprite('vr_phbgr_00', 162)
    GFX_0('Eff_BGRcountSub2', 3)
    Unknown38(5, 1)
    sprite('vr_phbgr_00', 138)
    GFX_0('Eff_BGRcountSub3', 1)
    Unknown38(6, 1)
    sprite('vr_phbgr_00', 1)
    GFX_0('Eff_BGRcountSub4', 0)
    Unknown38(7, 1)
    sprite('vr_phbgr_00', 32767)
    label(0)
    sprite('vr_phbgr_00', 32767)
    clearUponHandler(3)
    Unknown1096(1300)
    Unknown1086(22)
    Unknown1007(200000)
    Unknown21007(4, 32)
    Unknown21007(5, 32)
    Unknown21007(6, 32)
    Unknown21007(7, 32)
    label(1)
    sprite('null', 1)

@State
def Eff_BGRhari():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1096(1200)
        Unknown23015(8)
        Unknown4011(3)
        Unknown4010(2)
        Unknown4007(2)
    sprite('vr_phbgr_01', 10)
    Unknown3001(0)
    Unknown3004(28)
    sprite('vr_phbgr_01', 32767)
    Unknown3001(255)
    Unknown3004(0)
    Unknown1074(600)

@Subroutine
def CountDownFrameInit():
    Unknown4007(2)
    Unknown4010(2)
    Unknown4011(3)
    Unknown3032()
    Unknown4054(7)
    SFX_0('015_blaze_0')

@State
def Eff_BGRcountSub1():

    def upon_IMMEDIATE():
        callSubroutine('CountDownFrameInit')
        Unknown23067('phef_bgr_count1')
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 20)
    Unknown1099(20)
    physicsXImpulse(3000)
    physicsYImpulse(3000)
    sprite('null', 32767)
    Unknown1099(0)
    physicsXImpulse(0)
    physicsYImpulse(0)

@State
def Eff_BGRcountSub2():

    def upon_IMMEDIATE():
        callSubroutine('CountDownFrameInit')
        Unknown23067('phef_bgr_count2')
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 20)
    Unknown1099(20)
    physicsXImpulse(3000)
    physicsYImpulse(-3000)
    sprite('null', 32767)
    Unknown1099(0)
    physicsXImpulse(0)
    physicsYImpulse(0)

@State
def Eff_BGRcountSub3():

    def upon_IMMEDIATE():
        callSubroutine('CountDownFrameInit')
        GFX_2('phef_bgr_count3')
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 20)
    Unknown1099(20)
    physicsXImpulse(-3000)
    physicsYImpulse(-3000)
    sprite('null', 32767)
    Unknown1099(0)
    physicsXImpulse(0)
    physicsYImpulse(0)

@State
def Eff_BGRcountSub4():

    def upon_IMMEDIATE():
        callSubroutine('CountDownFrameInit')
        Unknown23067('phef_bgr_count4')
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 20)
    Unknown1099(20)
    physicsXImpulse(-3000)
    physicsYImpulse(3000)
    sprite('null', 32767)
    Unknown1099(0)
    physicsXImpulse(0)
    physicsYImpulse(0)

@State
def Eff_BGRCamera():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown21010(1)
        Unknown2054(1)
        Unknown4010(2)
    sprite('null', 30)
    Unknown20009(1250)
    Unknown20000(1)
    Unknown20002(1)
    Unknown20003(1)
    Unknown20004(1)
    sprite('null', 30)
    Unknown20000(0)
    sprite('null', 32767)
    Unknown1007(300000)
    Unknown20009(1000)

@State
def Eff_BGRstart():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff_bgr_start', '')
        Unknown21010(1)
        Unknown2054(1)
        Unknown1011(-10000, 10000)
        Unknown2054(1)
    sprite('null', 60)
    GFX_1('phef_ggr_start', -1)
    sprite('null', 5)
    physicsYImpulse(-1000)
    Unknown1067(50)

@State
def Eff_BGRmato():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown21010(1)
        Unknown2054(1)
        teleportRelativeY(0)
    sprite('null', 3)
    GFX_0('Eff_BGRatk', -1)
    SFX_0('013_thunder_0')
    SFX_0('016_explode_2')
    sprite('null', 3)
    GFX_0('Eff_BGRatk', -1)
    Unknown36(1)
    teleportRelativeX(300000)
    Unknown35()
    sprite('null', 3)
    GFX_0('Eff_BGRatk', -1)
    Unknown36(1)
    teleportRelativeX(-300000)
    Unknown35()
    SFX_0('013_thunder_0')
    SFX_0('016_explode_2')
    sprite('null', 3)
    GFX_0('Eff_BGRatk', -1)
    Unknown36(1)
    teleportRelativeX(-600000)
    Unknown35()
    sprite('null', 3)
    GFX_0('Eff_BGRatk', -1)
    Unknown36(1)
    teleportRelativeX(600000)
    Unknown35()
    SFX_0('013_thunder_0')
    SFX_0('016_explode_2')
    sprite('null', 3)
    GFX_0('Eff_BGRatk', -1)
    sprite('null', 3)
    GFX_0('Eff_BGRatk', -1)
    Unknown36(1)
    teleportRelativeX(300000)
    Unknown35()
    SFX_0('013_thunder_0')
    SFX_0('016_explode_2')
    sprite('null', 3)
    GFX_0('Eff_BGRatk', -1)
    Unknown36(1)
    teleportRelativeX(-300000)
    Unknown35()
    sprite('null', 3)
    GFX_0('Eff_BGRatk', -1)
    Unknown36(1)
    teleportRelativeX(-600000)
    Unknown35()
    SFX_0('013_thunder_0')
    SFX_0('016_explode_2')
    sprite('null', 3)
    GFX_0('Eff_BGRatk', -1)
    Unknown36(1)
    teleportRelativeX(600000)
    Unknown35()

@State
def Eff_BGRatk():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff_bgr_water00', '')
        Unknown21010(1)
        Unknown2054(1)
        Unknown1056(300)
        Unknown1064(800)
        Unknown1011(-10000, 10000)
    sprite('null', 10)
    ScreenShake(2500, 2500)
    sprite('null', 10)
    Unknown1059(-13)
    GFX_1('phef_bgr_atk_end', -1)
    GFX_0('Eff_BGRatkEnd', -1)

@State
def Eff_BGRatkEnd():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff_bgr_water01', '')
        Unknown21010(1)
        Unknown2054(1)
        Unknown1056(300)
        Unknown1064(800)
        Unknown1011(-5000, 5000)
    sprite('null', 30)
    sprite('null', 10)
    Unknown3004(-26)

@State
def Eff_BGRbg():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff_bgr_bg', '')
        Unknown21010(1)
        Unknown2054(1)
        Unknown4010(2)
        Unknown1056(1000)
        Unknown1064(600)
        sendToLabelUpon(32, 0)

        def upon_3():
            Unknown1086(22)
            teleportRelativeY(600000)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    Unknown3004(-26)

@State
def Eff_MagicConv():

    def upon_IMMEDIATE():
        Unknown4007(3)
        GFX_2('phef403_flash')
    sprite('null', 60)

@State
def Eff_430_cap():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        Unknown3032()
        Unknown3029(1)
    sprite('vr_ph430_cap', 6)
    sprite('vr_ph430_cap', 5)
    physicsYImpulse(30000)
    physicsXImpulse(-7500)
    Unknown1074(3000)
    sprite('vr_ph430_cap', 5)
    Unknown3004(-51)

@State
def Eff_430_capFire():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3033()
        Unknown4061(2)
        Unknown1007(20000)
    sprite('vr_ph430_00', 4)
    sprite('vr_ph430_01', 4)
    sprite('vr_ph430_02', 4)
    sprite('vr_ph430_03', 4)
    sprite('vr_ph430_04', 4)
    sprite('vr_ph430_06', 4)
    sprite('vr_ph430_07', 4)

@State
def UltimateShotAtk1st():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056()
        Unknown4011(3)
        Unknown1056(45000)
        Unknown1064(3500)
        teleportRelativeX(850000)
        Unknown1007(180000)
        AttackLevel_(3)
        Damage(600)
        MinimumDamagePct(10)
        AttackP1(80)
        AttackP2(60)
        Unknown11092(1)
        GroundedHitstunAnimation(9)
        AirUntechableTime(30)
        AirPushbackX(15000)
        AirPushbackY(4000)
        PushbackX(12000)
        Unknown9190(1)
        Unknown9118(85)
        Hitstop(0)
        Unknown11001(3, 3, 5)
        Unknown11057(500)
        Unknown9021(1)
        Unknown9266(8)
        Unknown23182(3)
        Unknown3038(1)

        def upon_43():
            if (SLOT_48 == 4304):

                def upon_78():
                    Unknown11064(1)
                    Unknown23029(3, 4305, 0)

        def upon_3():
            if Unknown2065(25):
                clearUponHandler(3)
                Unknown23029(3, 4309, 0)
    sprite('vr_ph_magictest', 8)
    GFX_0('Eff_430_Beam00', -1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 8)
    RefreshMultihit()
    sprite('vr_ph_magictest', 8)
    RefreshMultihit()
    sprite('vr_ph_magictest', 8)
    RefreshMultihit()
    sprite('vr_ph_magictest', 8)
    RefreshMultihit()
    sprite('null', 1)
    Unknown21012('Eff_430_Beam00', 32)

@State
def UltimateShotAtk2nd():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056()
        Unknown4011(3)
        Unknown1056(45000)
        Unknown1064(7000)
        teleportRelativeX(850000)
        Unknown1007(130000)
        AttackLevel_(4)
        Damage(900)
        MinimumDamagePct(10)
        AttackP1(80)
        AttackP2(60)
        Unknown11092(1)
        GroundedHitstunAnimation(9)
        AirUntechableTime(30)
        AirPushbackX(35000)
        AirPushbackY(4500)
        PushbackX(19800)
        Unknown9178(1)
        WallbounceReboundTime(55)
        AirHitstunAfterWallbounce(60)
        Hitstop(0)
        Unknown11001(3, 3, 5)
        Unknown11057(500)
        Unknown9021(1)
        Unknown9266(8)
        Unknown11108(3)
        Unknown23182(3)

        def upon_43():
            if (SLOT_48 == 4304):

                def upon_78():
                    Unknown11064(1)
                    Unknown23029(3, 4305, 0)
        Unknown3038(1)
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    GFX_0('Eff_430_Beam00', -1)
    Unknown36(1)
    Unknown1097(150)
    Unknown1007(30000)
    Unknown35()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('null', 1)
    Unknown21012('Eff_430_Beam00', 32)

@State
def Eff_430_Beam00():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4003('ph430eff_00', '')
        GFX_2('phef430_mc')
        Unknown3032()
        teleportRelativeX(-800000)
        Unknown1007(45000)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 2)
    Unknown1065(-75)
    SFX_0('014_electric_ll')
    SFX_3('phse_11')
    sprite('null', 2)
    Unknown1065(75)
    SFX_0('014_electric_l')
    SFX_3('phse_11')
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    GFX_1('phef430_beamend_00', -1)
    GFX_0('Eff_430_Beam01', -1)

@State
def Eff_430_Beam01():

    def upon_IMMEDIATE():
        Unknown4003('ph430eff_01', '')
        Unknown3032()
        Unknown2054(1)
        Unknown21010(1)
    sprite('null', 3)
    sprite('null', 3)
    Unknown1065(25)
    sprite('null', 3)
    Unknown1065(25)
    sprite('null', 3)
    Unknown1065(25)
    sprite('null', 4)

@State
def UltimateShotHinokagutsuchi():

    def upon_IMMEDIATE():
        Unknown23056()
        Unknown4010(3)
        Unknown4011(3)
        Unknown2054(1)
        Unknown3032()
        Unknown23015(11)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(1)
    sprite('ph430cutin_00', 15)
    Unknown3001(0)
    GFX_0('Eff_430_hinoEnter', 0)
    sprite('ph430cutin_00', 27)
    Unknown3004(51)
    ScreenShake(10000, 10000)
    GFX_0('Eff_430_hinoNemoto', 0)
    GFX_1('phef430_end', 1)
    GFX_1('phef430_end', 2)
    GFX_1('phef430_end', 3)
    GFX_1('phef430_end', 4)
    GFX_1('phef430_end', 5)
    GFX_1('phef430_end', 6)
    GFX_0('Eff_430_TameEff', -1)
    sprite('ph430cutin_01', 3)
    Unknown3026(-4934476)
    sprite('ph430cutin_02', 3)
    Unknown3026(-6250336)
    sprite('ph430cutin_03', 3)
    Unknown3026(-10197916)
    GFX_0('UltimateShotAtk3rd', -1)
    Unknown21012('Eff_430_TameEff', 32)
    Unknown1045(-20000)
    sprite('ph430cutin_03', 300)
    label(1)
    sprite('ph430cutin_02', 3)
    Unknown3004(-31)
    sprite('ph430cutin_01', 3)
    Unknown21012('Eff_430_hinoNemoto', 32)
    sprite('ph430cutin_00', 3)
    GFX_1('phef402_end', 1)
    GFX_1('phef402_end', 2)
    GFX_1('phef402_end', 3)
    GFX_1('phef402_end', 4)
    GFX_1('phef402_end', 5)
    GFX_1('phef402_end', 6)
    sprite('null', 2)

@State
def UltimateShotAtk3rd():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown4011(3)
        Unknown23056()
        Unknown1056(45000)
        Unknown1064(20000)
        teleportRelativeX(850000)
        Unknown1007(140000)
        AttackLevel_(5)
        Damage(200)
        MinimumDamagePct(10)
        AttackP1(80)
        AttackP2(60)
        Unknown11092(1)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirUntechableTime(60)
        AirPushbackX(40000)
        AirPushbackY(33000)
        Hitstop(0)
        Unknown11001(4, 4, 6)
        Unknown11057(500)
        Unknown9266(1)
        Unknown11108(3)
        Unknown23182(3)
        Unknown3038(1)
    sprite('vr_ph_magictest', 5)
    GFX_0('Eff_430_HinoBeamEff', -1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('null', 10)
    Unknown21012('Eff_430_HinoBeamEff', 32)
    Unknown21012('UltimateShotHinokagutsuchi', 32)

@State
def Eff_430_hinoEnter():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('pheff430od_01', '')
        Unknown2054(1)
        Unknown3032()
    sprite('null', 5)
    Unknown1096(1200)
    sprite('null', 5)
    Unknown1096(1700)
    sprite('null', 5)
    Unknown3004(-17)
    sprite('null', 4)
    GFX_0('Eff_430_hinoEnterEnd', -1)

@State
def Eff_430_hinoEnterEnd():

    def upon_IMMEDIATE():
        Unknown4003('pheff430od_02', '')
        Unknown2054(1)
        Unknown21010(1)
        Unknown3032()
        Unknown1096(1000)
        teleportRelativeX(300000)
        physicsXImpulse(7500)
    sprite('null', 20)
    Unknown1099(30)

@State
def Eff_430_hinoNemoto():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('pheff430od_00', '')
        GFX_2('phef430_hngate')
        Unknown2054(1)
        Unknown3032()
        Unknown1096(1400)
        sendToLabelUpon(32, 1)
    sprite('null', 32767)
    label(1)
    sprite('null', 3)
    sprite('null', 6)
    Unknown3004(-42)

@State
def Eff_430_TameEff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('pheff430odbeam_00', '')
        GFX_2('phef430_beamtame')
        Unknown2054(1)
        Unknown3032()
        Unknown1096(60)
        Unknown1007(240000)
        teleportRelativeX(380000)
        sendToLabelUpon(32, 1)
    sprite('null', 5)
    Unknown1099(300)
    sprite('null', 5)
    Unknown1099(0)
    label(0)
    sprite('null', 1)
    Unknown1097(200)
    ScreenShake(2500, 2500)
    sprite('null', 1)
    Unknown1097(-100)
    sprite('null', 1)
    Unknown1097(200)
    sprite('null', 1)
    Unknown1097(-100)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    ScreenShake(10000, 10000)
    Unknown1096(1000)
    Unknown3001(0)

@State
def Eff_430_HinoBeamEff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('pheff430odbeam_01', '')
        Unknown2054(1)
        Unknown3032()
        Unknown1096(1000)
        Unknown1065(1200)
        teleportRelativeX(-650000)
        Unknown1007(250000)
        Unknown3038(1)
        sendToLabelUpon(32, 1)
    sprite('vr_ph430_effpos', 5)
    Unknown1067(80)
    Unknown1064(120)
    SFX_0('016_explode_2')
    sprite('vr_ph430_effpos', 5)
    SFX_3('phse_02')
    sprite('vr_ph430_effpos', 5)
    Unknown1067(10)
    sprite('vr_ph430_effpos', 5)
    Unknown1067(0)
    GFX_1('phef_430_shock', 0)
    GFX_1('phef_430_shock', 2)
    label(0)
    sprite('vr_ph430_effpos', 1)
    Unknown1057(-50)
    Unknown1065(50)
    GFX_1('phef_430_shock', 0)
    GFX_1('phef_430_shock', 2)
    SFX_3('phse_02')
    sprite('vr_ph430_effpos', 1)
    Unknown1065(-50)
    Unknown1057(50)
    sprite('vr_ph430_effpos', 1)
    Unknown1057(-50)
    Unknown1065(50)
    sprite('vr_ph430_effpos', 1)
    Unknown1065(-50)
    Unknown1057(50)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    GFX_0('Eff_430_HinoBeamEffEnd', -1)

@State
def Eff_430_HinoBeamEffEnd():

    def upon_IMMEDIATE():
        Unknown4003('pheff430odbeam_02', '')
        Unknown2054(1)
        Unknown21010(1)
        Unknown3032()
    sprite('null', 10)
    Unknown4003('pheff430odbeam_02', '')
    sprite('vr_ph430odbeam_expos', 1)
    Unknown3038(1)
    GFX_1('phef430_beamend', 0)
    GFX_1('phef430_beamend', 1)
    GFX_1('phef430_beamend', 2)
    GFX_1('phef430_beamend', 3)
    GFX_1('phef430_beamend', 4)
    GFX_1('phef430_beamend', 5)

@State
def Eff_432_AtkFire():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2054(1)
        Unknown4061(2)
        Unknown2005()
        Unknown1056(900)
        Unknown1064(1200)
        Unknown1007(-25000)
    sprite('vr_ph432_00', 6)
    GFX_0('Eff_432_AtkFireSub', -1)
    sprite('vr_ph432_01', 6)
    sprite('vr_ph432_02', 5)
    sprite('vr_ph432_03', 4)
    sprite('vr_ph432_04', 4)
    sprite('vr_ph432_05', 2)

@State
def Eff_432_AtkFireSub():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2054(1)
        Unknown4061(2)
        Unknown1056(-700)
        Unknown1064(700)
    sprite('vr_ph432_00', 4)
    sprite('vr_ph432_01', 4)
    sprite('vr_ph432_02', 4)
    sprite('vr_ph432_03', 4)
    sprite('vr_ph432_04', 4)
    sprite('vr_ph432_05', 4)

@Subroutine
def UltimateLock_Atk1stInit():
    AttackLevel_(3)
    Damage(250)
    MinimumDamagePct(10)
    Hitstop(3)
    Unknown11057(500)
    Unknown11083(1)
    Unknown11001(60, 60, 60)
    AttackP2(100)
    Unknown9017(1)
    Unknown11072(1, 0, 50000)
    Unknown11064(1)
    Unknown11108(3)
    Unknown11050(5, '')

@State
def UltimateLock_Atk1stLv1():

    def upon_IMMEDIATE():
        Unknown17011('UltimateLock_Atk1stLv1Exe', 3, 0, 0)
        Unknown2018(0, 80)
        Unknown11032(-1, -1, -1, -1)
        Unknown11054(-1)
        Unknown11002(-1)
        Unknown30061(1)
        Unknown1056(10000)
        Unknown1064(15000)
        Unknown1086(22)
        teleportRelativeY(0)
        Unknown3038(1)
    sprite('vr_ph_magictest', 5)
    StartMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    GFX_0('Eff_432_yariLv1', -1)

@State
def Eff_432_yariLv1():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff432_yari00', '')
        Unknown2054(1)
        Unknown1096(1750)
    sprite('null', 20)
    GFX_0('Eff_432_Boya', -1)
    sprite('null', 50)
    sprite('null', 10)
    Unknown3004(-26)
    Unknown21012('Eff_432_Boya', 32)

@State
def Eff_432_Boya():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown2054(1)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 8)
    GFX_1('phef432_fire00', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 1)

@State
def UltimateLock_Atk1stLv1Exe():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown1056(10000)
        Unknown1064(25000)
        Unknown1086(22)
        teleportRelativeY(0)
        Unknown3038(1)
        callSubroutine('UltimateLock_Atk1stInit')
    sprite('vr_ph_magictest', 1)
    Unknown5000(24, 0)
    Unknown5001(0, 5, 5, 0, 0)
    DisableAttackRestOfMove()
    Unknown36(22)
    teleportRelativeY(50000)
    Unknown35()
    sprite('vr_ph_magictest', 3)
    Unknown5000(24, 0)
    Unknown5001(0, 5, 5, 0, 0)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()

@State
def UltimateLock_Atk1stLv2():

    def upon_IMMEDIATE():
        Unknown17011('UltimateLock_Atk1stLv2Exe', 3, 0, 0)
        Unknown2018(0, 80)
        Unknown11032(-1, -1, -1, -1)
        Unknown11054(-1)
        Unknown11002(-1)
        Unknown30061(1)
        Unknown1056(10000)
        Unknown1064(15000)
        Unknown1086(22)
        teleportRelativeY(0)
        Unknown3038(1)
    sprite('vr_ph_magictest', 5)
    StartMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    GFX_0('Eff_432_yariLv2', -1)

@State
def Eff_432_yariLv2():

    def upon_IMMEDIATE():
        Unknown4003('pheff432_yari00', '')
        Unknown3032()
        Unknown2054(1)
        Unknown1096(1750)
    sprite('null', 5)
    sprite('null', 45)
    GFX_0('Eff_432_yariLv2sub', -1)
    sprite('null', 10)
    Unknown3004(-26)
    Unknown21012('Eff_432_yariLv2sub', 32)

@State
def Eff_432_yariLv2sub():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff432_yari04', '')
        Unknown2054(1)
        Unknown1056(1200)
        Unknown1064(1400)
        Unknown1007(-20000)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 8)
    GFX_1('phef432_fire00', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    Unknown3004(-26)
    Unknown1067(80)

@State
def UltimateLock_Atk1stLv2Exe():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown1056(10000)
        Unknown1064(25000)
        Unknown1086(22)
        teleportRelativeY(0)
        Unknown3038(1)
        callSubroutine('UltimateLock_Atk1stInit')
    sprite('vr_ph_magictest', 1)
    Unknown5000(24, 0)
    Unknown5001(0, 5, 5, 0, 0)
    DisableAttackRestOfMove()
    Unknown36(22)
    teleportRelativeY(50000)
    Unknown35()
    SFX_0('015_blaze_0')
    sprite('vr_ph_magictest', 3)
    Unknown5000(24, 0)
    Unknown5001(0, 5, 5, 0, 0)
    RefreshMultihit()
    SFX_0('015_blaze_0')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    SFX_0('015_blaze_0')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    SFX_0('015_blaze_0')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    SFX_0('015_blaze_0')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    SFX_0('015_blaze_0')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    SFX_0('015_blaze_0')

@State
def UltimateLock_Atk1stLv3():

    def upon_IMMEDIATE():
        Unknown17011('UltimateLock_Atk1stLv3Exe', 3, 0, 0)
        Unknown2018(0, 80)
        Unknown11032(-1, -1, -1, -1)
        Unknown11054(-1)
        Unknown11002(-1)
        Unknown30061(1)
        Unknown1056(10000)
        Unknown1064(15000)
        Unknown1086(22)
        teleportRelativeY(0)
        Unknown3038(1)
    sprite('vr_ph_magictest', 5)
    StartMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    GFX_0('Eff_432_yari', -1)

@State
def Eff_432_yari():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff432_yari00', '')
        Unknown2054(1)
        Unknown1096(1750)
    sprite('null', 4)
    GFX_0('Eff_432_Boya', -1)
    GFX_0('Eff_432_yari_sub2', -1)
    GFX_0('Eff_432_yari_sub1', -1)
    Unknown36(1)
    Unknown1007(50000)
    Unknown35()
    sprite('null', 4)
    GFX_0('Eff_432_yari_sub1', -1)
    Unknown36(1)
    Unknown1007(250000)
    Unknown1097(-300)
    Unknown35()
    sprite('null', 4)
    GFX_0('Eff_432_yari_sub1', -1)
    Unknown36(1)
    Unknown1007(435000)
    Unknown1097(-600)
    Unknown35()
    sprite('null', 14)
    GFX_0('Eff_432_yari_sub1', -1)
    Unknown36(1)
    Unknown1007(640000)
    Unknown1097(-900)
    Unknown35()
    sprite('null', 50)
    Unknown21012('Eff_432_yari_sub2', 32)
    Unknown21012('Eff_432_yari_sub1', 32)
    sprite('null', 10)
    Unknown21012('Eff_432_Boya', 32)
    Unknown3004(-26)

@State
def Eff_432_yari_sub1():

    def upon_IMMEDIATE():
        Unknown4003('pheff432_yari01', '')
        Unknown3032()
        Unknown2054(1)
        Unknown1096(4000)
        teleportRelativeX(50000)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    Unknown3004(-26)
    Unknown1099(-120)

@State
def Eff_432_yari_sub2():

    def upon_IMMEDIATE():
        Unknown4003('pheff432_yari02', '')
        Unknown3032()
        Unknown2054(1)
        Unknown1056(500)
        Unknown1064(2000)
        teleportRelativeX(50000)
        sendToLabelUpon(32, 0)
    sprite('null', 5)
    Unknown3001(0)
    Unknown3004(51)
    ScreenShake(15000, 15000)
    Unknown1059(300)
    sprite('null', 32767)
    Unknown1059(0)
    label(0)
    sprite('null', 5)
    Unknown3004(-26)
    Unknown1099(-120)
    sprite('null', 5)
    GFX_0('Eff_432_yari_sub3', -1)

@State
def Eff_432_yari_sub3():

    def upon_IMMEDIATE():
        Unknown4003('pheff432_yari03', '')
        Unknown3033()
        Unknown2054(1)
        Unknown1096(2000)
    sprite('null', 15)

@State
def UltimateLock_Atk1stLv3Exe():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown1056(10000)
        Unknown1064(25000)
        Unknown1086(22)
        teleportRelativeY(0)
        Unknown3038(1)
        callSubroutine('UltimateLock_Atk1stInit')
    sprite('vr_ph_magictest', 1)
    Unknown5000(24, 0)
    Unknown5001(0, 5, 5, 0, 0)
    DisableAttackRestOfMove()
    Unknown36(22)
    teleportRelativeY(50000)
    Unknown35()
    SFX_3('phse_02')
    sprite('vr_ph_magictest', 3)
    Unknown5000(24, 0)
    Unknown5001(0, 5, 5, 0, 0)
    RefreshMultihit()
    SFX_0('019_quake_1')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    SFX_3('phse_02')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    SFX_0('019_quake_1')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    SFX_3('phse_02')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    SFX_0('019_quake_1')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    SFX_0('019_quake_1')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()

@Subroutine
def UltimateLock_Atk2ndInit():
    MinimumDamagePct(10)
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    AirUntechableTime(60)
    hitstun(60)
    AttackP2(100)
    AirPushbackX(55000)
    AirPushbackY(15000)
    Unknown11057(400)
    Unknown9266(8)
    Unknown11108(3)
    Unknown30048(1)
    Unknown9178(1)
    WallbounceReboundTime(0)
    Hitstop(1)
    Unknown11001(10, 10, 10)

@Subroutine
def UltimateLock_Atk2ndODInit():
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirPushbackX(7500)
    AirPushbackY(25000)
    Unknown11064(1)
    Unknown9179()

@State
def UltimateLock_Atk2ndLv1():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056()
        Unknown4011(3)
        Unknown1056(45000)
        Unknown1064(12000)
        teleportRelativeX(850000)
        Unknown1007(140000)
        callSubroutine('UltimateLock_Atk2ndInit')

        def upon_43():
            if (SLOT_48 == 4321):
                clearUponHandler(43)
                callSubroutine('UltimateLock_Atk2ndODInit')
                MinimumDamagePct(8)
        AttackLevel_(2)
        Damage(1250)
        MinimumDamagePct(8)
        DisableAttackRestOfMove()
        Unknown3038(1)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash_SS', -1)
    SFX_3('phse_07')
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash2_SS', -1)
    SFX_3('phse_07')
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash3_SS', -1)
    SFX_3('phse_07')
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash_SS', -1)
    SFX_3('phse_07')
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash2_SS', -1)
    SFX_3('phse_07')
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()

@State
def Eff_432_mgSlash_SS():

    def upon_IMMEDIATE():
        Unknown4003('pheff432_slash00', '')
        GFX_2('phef432_aura')
        Unknown3032()
        Unknown2054(1)
        Unknown1096(1000)
        teleportRelativeX(-1100000)
        Unknown1010(0, 100000)
    sprite('null', 10)
    ScreenShake(0, 5000)
    sprite('null', 6)
    physicsXImpulse(60000)
    sprite('null', 2)
    GFX_1('phef432_hinoko00', -1)

@State
def Eff_432_mgSlash2_SS():

    def upon_IMMEDIATE():
        Unknown4003('pheff432_slash00', '')
        GFX_2('phef432_aura')
        Unknown3032()
        Unknown2054(1)
        Unknown1096(1000)
        teleportRelativeX(-900000)
        Unknown1007(150000)
        Unknown1010(0, 100000)
        Unknown1011(-50000, 50000)
    sprite('null', 10)
    ScreenShake(0, 5000)
    sprite('null', 6)
    physicsXImpulse(60000)
    sprite('null', 2)
    GFX_1('phef432_hinoko00', -1)

@State
def Eff_432_mgSlash3_SS():

    def upon_IMMEDIATE():
        GFX_2('phef432_aura')
        Unknown4003('pheff432_slash00', '')
        Unknown3032()
        Unknown2054(1)
        Unknown1096(1000)
        teleportRelativeX(-900000)
        Unknown1007(-100000)
        Unknown1010(0, 100000)
        Unknown1011(-50000, 50000)
    sprite('null', 10)
    ScreenShake(0, 5000)
    sprite('null', 6)
    physicsXImpulse(60000)
    sprite('null', 2)
    GFX_1('phef432_hinoko00', -1)

@State
def UltimateLock_Atk2ndLv2():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056()
        Unknown4011(3)
        Unknown1056(45000)
        Unknown1064(12000)
        teleportRelativeX(850000)
        Unknown1007(140000)
        callSubroutine('UltimateLock_Atk2ndInit')

        def upon_43():
            if (SLOT_48 == 4321):
                clearUponHandler(43)
                callSubroutine('UltimateLock_Atk2ndODInit')
        AttackLevel_(3)
        Damage(2050)
        MinimumDamagePct(14)
        DisableAttackRestOfMove()
        Unknown3038(1)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash_S', -1)
    SFX_3('phse_07')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('null', 5)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash2_S', -1)
    SFX_3('phse_07')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('null', 5)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash3_S', -1)
    SFX_3('phse_07')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()

@State
def Eff_432_mgSlash_S():

    def upon_IMMEDIATE():
        GFX_2('phef432_aura')
        Unknown4003('pheff432_slash00', '')
        Unknown3032()
        Unknown2054(1)
        Unknown1096(2000)
        teleportRelativeX(-1100000)
        Unknown1010(0, 50000)
    sprite('null', 17)
    ScreenShake(0, 15000)
    sprite('null', 1)
    GFX_1('phef432_hinoko00', -1)

@State
def Eff_432_mgSlash2_S():

    def upon_IMMEDIATE():
        GFX_2('phef432_aura')
        Unknown4003('pheff432_slash00', '')
        Unknown3032()
        Unknown2054(1)
        Unknown1096(1700)
        teleportRelativeX(-900000)
        Unknown1007(150000)
        Unknown1010(0, 50000)
    sprite('null', 17)
    ScreenShake(0, 15000)
    sprite('null', 1)
    GFX_1('phef432_hinoko00', -1)

@State
def Eff_432_mgSlash3_S():

    def upon_IMMEDIATE():
        GFX_2('phef432_aura')
        Unknown4003('pheff432_slash00', '')
        Unknown3032()
        Unknown2054(1)
        Unknown1096(1700)
        teleportRelativeX(-900000)
        Unknown1007(-100000)
        Unknown1010(0, 50000)
    sprite('null', 17)
    ScreenShake(0, 15000)
    sprite('null', 1)
    GFX_1('phef432_hinoko00', -1)

@State
def UltimateLock_Atk2ndLv3():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056()
        Unknown4011(3)
        Unknown1056(45000)
        Unknown1064(12000)
        teleportRelativeX(850000)
        Unknown1007(140000)
        callSubroutine('UltimateLock_Atk2ndInit')

        def upon_43():
            if (SLOT_48 == 4321):
                clearUponHandler(43)
                callSubroutine('UltimateLock_Atk2ndODInit')
        AttackLevel_(4)
        Damage(1050)
        MinimumDamagePct(14)
        DisableAttackRestOfMove()
        Unknown3038(1)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash_S', -1)
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('null', 2)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash2_S', -1)
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('null', 2)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash3_S', -1)
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('null', 2)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash_S', -1)
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('null', 2)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash2_S', -1)
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('null', 2)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash3_S', -1)
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()

@State
def UltimateLock_Atk2ndLv4():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056()
        Unknown4011(3)
        Unknown1056(45000)
        Unknown1064(12000)
        teleportRelativeX(850000)
        Unknown1007(140000)
        callSubroutine('UltimateLock_Atk2ndInit')

        def upon_43():
            if (SLOT_48 == 4321):
                clearUponHandler(43)
                callSubroutine('UltimateLock_Atk2ndODInit')
        AttackLevel_(5)
        Damage(720)
        MinimumDamagePct(14)
        DisableAttackRestOfMove()
        Unknown3038(1)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash', -1)
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('null', 2)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash2', -1)
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('null', 2)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash3', -1)
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('null', 2)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash', -1)
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('null', 2)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash2', -1)
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('null', 2)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash3', -1)
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('null', 8)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash', -1)
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()

@State
def Eff_432_mgSlash():

    def upon_IMMEDIATE():
        GFX_2('phef432_aura')
        Unknown4003('pheff432_slash00', '')
        Unknown3032()
        Unknown2054(1)
        Unknown1096(2200)
        teleportRelativeX(-1100000)
        Unknown1010(0, 50000)
    sprite('null', 17)
    ScreenShake(0, 20000)
    sprite('null', 1)
    Unknown4045('phef432_hinoko00', -1)

@State
def Eff_432_mgSlash2():

    def upon_IMMEDIATE():
        GFX_2('phef432_aura')
        Unknown4003('pheff432_slash00', '')
        Unknown3032()
        Unknown2054(1)
        Unknown1096(1700)
        teleportRelativeX(-900000)
        Unknown1007(300000)
        Unknown1073(15000)
        Unknown1010(0, 50000)
    sprite('null', 17)
    ScreenShake(0, 20000)
    sprite('null', 1)
    Unknown4048(15000)
    Unknown4045('phef432_hinoko00', -1)

@State
def Eff_432_mgSlash3():

    def upon_IMMEDIATE():
        GFX_2('phef432_aura')
        Unknown4003('pheff432_slash00', '')
        Unknown3032()
        Unknown2054(1)
        Unknown1096(1700)
        teleportRelativeX(-900000)
        Unknown1007(-300000)
        Unknown1073(-15000)
        Unknown1010(0, 50000)
    sprite('null', 17)
    ScreenShake(0, 20000)
    sprite('null', 1)
    Unknown4048(15000)
    Unknown4045('phef432_hinoko00', -1)

@State
def UltimateLock_AtkSPAdd():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056()
        Unknown4011(3)
        Unknown1096(20000)
        AttackLevel_(5)
        Damage(270)
        MinimumDamagePct(9)
        AttackP2(100)
        Unknown11092(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(0)
        AirPushbackY(25000)
        AirUntechableTime(120)
        Hitstop(1)
        Unknown11001(21, 21, 29)
        Unknown11050(5, '')
        Unknown11108(3)
        Unknown9266(8)
        Unknown30048(1)
        Unknown3038(1)
    sprite('vr_ph_magictest', 1)
    Unknown1086(22)
    teleportRelativeY(0)
    GFX_0('Eff_BGRmato', -1)
    ScreenShake(0, 20000)
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 10)
    StartMultihit()
    ExitState()

@State
def Eff_431_obi():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('pheff431_obi00', '')
        Unknown2054(1)
        Unknown3033()
        Unknown1096(2700)
        Unknown1007(-10000)
        teleportRelativeX(-38000)
    sprite('null', 6)
    Unknown4003('pheff431_obi00', '')
    sprite('null', 6)
    Unknown4003('pheff431_obi01', '')
    sprite('null', 6)
    Unknown4003('pheff431_obi02', '')
    sprite('null', 8)
    Unknown4003('pheff431_obi03', '')
    sprite('null', 6)
    Unknown4003('pheff431_obi04', '')
    sprite('null', 6)
    Unknown4003('pheff431_obi05', '')
    sprite('null', 6)
    Unknown4003('pheff431_obi06', '')
    sprite('null', 6)
    Unknown4003('pheff431_obi07', '')
    sprite('null', 6)
    Unknown4003('pheff431_obi08', '')
    sprite('null', 6)
    Unknown4003('pheff431_obi09', '')
    Unknown3004(-18)
    sprite('null', 6)
    Unknown4003('pheff431_obi10', '')

@State
def Eff_431_mc():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('pheff431_mc00', '')
        Unknown2054(1)
        Unknown3033()
        Unknown3001(160)
        Unknown1096(1500)
        Unknown1007(250000)
        teleportRelativeX(-38000)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 5)
    Unknown1099(150)
    Unknown3004(-26)
    physicsXImpulse(42500)

@State
def Eff_431_mc_sub1():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('pheff431_mc01', '')
        Unknown2054(1)
        Unknown3032()
        Unknown1096(3000)
        Unknown1007(250000)
        teleportRelativeX(-38000)
        sendToLabelUpon(32, 0)
    sprite('null', 20)
    Unknown3001(0)
    Unknown3004(10)
    sprite('null', 32767)
    Unknown3004(0)
    label(0)
    sprite('null', 5)
    Unknown3004(-26)
    Unknown1099(-200)
    physicsXImpulse(42500)

@State
def Eff_431_BomBall():

    def upon_IMMEDIATE():
        Unknown4010(2)
        GFX_2('pheff431_tameball')
        Unknown4003('pheff431_tameball00', '')
        Unknown2054(1)
        Unknown3033()
        Unknown1056(1400)
        Unknown1064(1200)
        Unknown1007(280000)
        teleportRelativeX(100000)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        sendToLabelUpon(34, 2)
    sprite('null', 10)
    Unknown3001(0)
    Unknown1099(-75)
    Unknown3004(26)
    label(0)
    sprite('null', 5)
    physicsXImpulse(10000)
    Unknown1099(5)
    sprite('null', 32767)
    physicsXImpulse(0)
    label(1)
    sprite('null', 5)
    physicsXImpulse(-5000)
    Unknown1099(10)
    sprite('null', 32767)
    physicsXImpulse(0)
    label(2)
    sprite('null', 1)
    teleportRelativeX(22500)
    Unknown1007(-10000)
    Unknown1057(200)
    Unknown1065(300)
    sprite('null', 1)
    Unknown1057(200)
    Unknown1065(300)
    teleportRelativeX(10000)
    Unknown1007(-10000)
    sprite('null', 1)
    Unknown1057(200)
    Unknown1065(300)
    teleportRelativeX(10000)
    Unknown1007(-10000)

@State
def Eff5AAAAA():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4003('pheff431_bomb00', '')
        Unknown3032()
        Unknown2053(1)
        Unknown1096(450)
        Unknown1007(100000)
    sprite('null', 1)
    ScreenShake(5000, 25000)
    SFX_0('016_explode_2')
    sprite('null', 1)
    Unknown1097(150)
    Unknown1007(10000)
    sprite('null', 1)
    Unknown1007(10000)
    sprite('null', 1)
    GFX_0('Eff5AAAAABombEnd', -1)
    Unknown1097(50)
    Unknown1007(25000)
    Unknown3004(-51)
    GFX_1('phef_400_bom', -1)
    GFX_1('phef_400_blm', -1)
    sprite('null', 10)

@State
def Atk5AAAAA_Lv1():

    def upon_IMMEDIATE():
        Unknown2009()
        Unknown4011(3)
        AttackLevel_(4)
        Damage(2000)
        AttackP1(80)
        AirUntechableTime(60)
        AirPushbackX(2500)
        AirPushbackY(25000)
        GroundedHitstunAnimation(10)
        Unknown9017(1)
        Unknown1056(10000)
        Unknown1064(10000)
        teleportRelativeX(500000)
        Unknown1007(100000)
        Unknown2053(1)
        Unknown23078(1)
        Unknown3038(1)
        Unknown11044(1)
        Unknown30088(1)
    sprite('vr_ph_magictest', 6)
    GFX_0('Eff5AAAAA', -1)
    RefreshMultihit()
    sprite('null', 20)

@State
def Atk5AAAAA_Lv2():

    def upon_IMMEDIATE():
        Unknown2009()
        Unknown4011(3)
        AttackLevel_(4)
        Damage(2200)
        AttackP1(80)
        AirUntechableTime(60)
        AirPushbackX(2500)
        AirPushbackY(25000)
        GroundedHitstunAnimation(10)
        Unknown9017(1)
        Unknown1056(10000)
        Unknown1064(10000)
        teleportRelativeX(500000)
        Unknown1007(100000)
        Unknown2053(1)
        Unknown23078(1)
        Unknown3038(1)
        Unknown11044(1)
        Unknown30088(1)
    sprite('vr_ph_magictest', 6)
    GFX_0('Eff5AAAAA', -1)
    RefreshMultihit()
    sprite('null', 20)

@State
def Atk5AAAAA_Lv3():

    def upon_IMMEDIATE():
        Unknown2009()
        Unknown4011(3)
        AttackLevel_(4)
        Damage(2400)
        AttackP1(80)
        AirUntechableTime(60)
        AirPushbackX(2500)
        AirPushbackY(25000)
        GroundedHitstunAnimation(10)
        Unknown9017(1)
        Unknown1056(10000)
        Unknown1064(10000)
        teleportRelativeX(500000)
        Unknown1007(100000)
        Unknown2053(1)
        Unknown23078(1)
        Unknown3038(1)
        Unknown11044(1)
        Unknown30088(1)
    sprite('vr_ph_magictest', 6)
    GFX_0('Eff5AAAAA', -1)
    RefreshMultihit()
    sprite('null', 20)

@State
def Eff5AAAAABombEnd():

    def upon_IMMEDIATE():
        Unknown4003('pheff431_bomb01', '')
        Unknown3032()
        Unknown2054(1)
        Unknown1096(200)
        Unknown1007(-260000)
    sprite('null', 14)
    GFX_1('phef_402_end_g', -1)
    sprite('null', 9)
    GFX_1('pheff431_gsmoke_pos', -1)
    Unknown3004(-26)

@State
def Eff_431_bomb():

    def upon_IMMEDIATE():
        Unknown4010(2)
        GFX_2('phef431_blm')
        Unknown4003('pheff431_bomb00', '')
        Unknown3032()
        Unknown1096(600)
        Unknown1007(200000)
        teleportRelativeX(100000)
    sprite('null', 2)
    ScreenShake(20000, 20000)
    sprite('null', 2)
    Unknown1097(200)
    Unknown1007(25000)
    sprite('null', 2)
    Unknown1007(25000)
    sprite('null', 1)
    GFX_0('ph320BombEff_Circle', -1)
    GFX_0('Eff_431_bombEnd', -1)
    Unknown1097(100)
    Unknown1007(25000)
    Unknown3004(-51)
    GFX_1('phef_400_bom', -1)
    GFX_1('phef_400_blm', -1)
    sprite('null', 10)
    GFX_0('Entry_Fire', -1)
    Unknown36(1)
    Unknown1007(-105000)
    Unknown1097(900)
    Unknown35()
    GFX_0('Entry_Fire', -1)
    Unknown36(1)
    Unknown1007(-205000)
    teleportRelativeX(200000)
    Unknown1097(550)
    Unknown1073(20000)
    Unknown35()
    GFX_0('Entry_Fire', -1)
    Unknown36(1)
    Unknown1007(-205000)
    teleportRelativeX(-200000)
    Unknown1097(550)
    Unknown1073(-20000)
    Unknown35()

@State
def Eff_431_bombEnd():

    def upon_IMMEDIATE():
        Unknown4003('pheff431_bomb01', '')
        Unknown3032()
        Unknown2054(1)
        Unknown1096(250)
        Unknown1007(-260000)
    sprite('null', 14)
    GFX_1('phef_402_end_g', -1)
    sprite('null', 9)
    GFX_1('pheff431_gsmoke_pos', -1)
    Unknown3004(-26)

@State
def ph320BombEff_Circle():

    def upon_IMMEDIATE():
        Unknown4003('pheff450_AddCircle', '')
        Unknown2054(1)
        Unknown3033()
        Unknown1096(650)
    sprite('null', 5)
    Unknown1099(300)
    sprite('null', 5)
    Unknown3004(-51)

@State
def Entry_Fire():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown1096(1000)
        Unknown1067(15)
        Unknown2054(1)
        Unknown21010(1)
        Unknown1010(-25000, 25000)
        Unknown1007(-50000)
    sprite('vr_phcmn_00', 3)
    sprite('vr_phcmn_01', 3)
    sprite('vr_phcmn_02', 3)
    sprite('vr_phcmn_03', 3)
    sprite('vr_phcmn_04', 3)
    sprite('vr_phcmn_05', 3)
    Unknown3004(-26)
    GFX_1('phef450_hinoko', 2)
    sprite('vr_phcmn_06', 3)
    sprite('vr_phcmn_07', 3)

@State
def UltimateChargeAtk():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown4011(3)
        AttackLevel_(5)
        ProjectileDurabilityLvl(2)
        Damage(2000)
        MinimumDamagePct(100)
        AttackP1(100)
        AttackP2(100)
        AirUntechableTime(60)
        AirPushbackX(20000)
        AirPushbackY(35000)
        GroundedHitstunAnimation(10)
        Unknown9017(1)
        Unknown1056(11000)
        Unknown1064(11000)
        teleportRelativeX(150000)
        Unknown1007(100000)
        Unknown3038(1)

        def upon_78():
            Unknown23029(3, 4311, 0)
    sprite('vr_ph_magictest', 10)
    RefreshMultihit()

@State
def UltimateChargeSPAddAtk():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(5)
        ProjectileDurabilityLvl(2)
        Damage(100)
        MinimumDamagePct(100)
        AttackP1(100)
        AttackP2(100)
        AirUntechableTime(60)
        AirPushbackX(25000)
        AirPushbackY(20000)
        GroundedHitstunAnimation(9)
        Unknown9017(1)
        Unknown1056(11000)
        Unknown1064(11000)
        Unknown3038(1)
    sprite('null', 17)
    sprite('vr_ph_magictest', 3)
    Unknown1086(22)
    teleportRelativeX(50000)
    Unknown2006()
    GFX_0('UltimateChargeSPAddAtk_Bomb', -1)
    RefreshMultihit()
    sprite('null', 5)
    sprite('vr_ph_magictest', 3)
    Unknown1086(22)
    teleportRelativeX(50000)
    Unknown2006()
    GFX_0('UltimateChargeSPAddAtk_Bomb', -1)
    RefreshMultihit()
    Damage(150)
    sprite('null', 3)
    sprite('vr_ph_magictest', 3)
    Unknown1086(22)
    teleportRelativeX(-50000)
    Unknown2006()
    GFX_0('UltimateChargeSPAddAtk_Bomb', -1)
    RefreshMultihit()
    Damage(250)
    AirPushbackX(30000)
    AirPushbackY(28000)
    sprite('null', 30)

@State
def UltimateChargeSPAddAtk_Bomb():

    def upon_IMMEDIATE():
        Unknown4061(3)
        Unknown4011(3)
        Unknown21010(1)
        Unknown1096(800)
    sprite('vr_ph400_04', 2)
    sprite('vr_ph400_05', 3)
    Unknown1007(200000)
    ScreenShake(10000, 10000)
    Unknown1099(15)
    GFX_0('pheff_400sub2', 1)
    Unknown36(1)
    Unknown21010(1)
    Unknown1077(-40000, 40000)
    Unknown35()
    GFX_1('phef_400_bom', 1)
    GFX_1('phef_400_blm', 1)
    sprite('vr_ph400_07', 2)
    sprite('vr_ph400_08', 2)
    GFX_1('phef321_shock2', -1)
    sprite('vr_ph400_09', 2)
    sprite('vr_ph400_06', 3)
    GFX_0('ph320BombEff_Circle', -1)
    Unknown36(1)
    Unknown21010(1)
    Unknown1077(20000, 30000)
    Unknown1097(-600)
    Unknown35()
    GFX_0('phEff400_corebom', 0)
    Unknown3004(-51)

@State
def AstralHeatAtk():

    def upon_IMMEDIATE():
        Unknown2012()
        Unknown1056(8000)
        Unknown1064(10000)
        AttackLevel_(3)
        Damage(0)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(810)
        Unknown9142(800)
        AirUntechableTime(600)
        Unknown9016(1)
        PushbackX(0)
        Unknown11072(1, 0, 0)
        Unknown11064(1)
        Unknown11056(0)
        Unknown2053(1)
        Unknown3038(1)

        def upon_12():
            Unknown23029(3, 4501, 0)
    sprite('vr_ph_magictest', 8)
    if (SLOT_19 > 450000):
        Unknown1086(22)
        teleportRelativeY(0)
    else:
        teleportRelativeX(500000)
    GFX_1('phef450_ahatk', -1)
    SFX_0('022_magiccircle_c')
    SFX_0('014_electric_ll')

@State
def AstralHeatAtk2nd():

    def upon_IMMEDIATE():
        Unknown2012()
        Unknown1056(8000)
        Unknown1064(10000)
        AttackLevel_(5)
        Damage(5000)
        MinimumDamagePct(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(600)
        Unknown9016(1)
        PushbackX(0)
        Unknown11072(1, 0, 0)
        Unknown11056(0)
        Unknown3038(1)
    sprite('vr_ph_magictest', 3)
    Unknown1086(22)
    teleportRelativeY(0)

@State
def AstralHeatLastAtk():

    def upon_IMMEDIATE():
        Unknown2012()
        Unknown1056(8000)
        Unknown1064(8000)
        AttackLevel_(5)
        Damage(30000)
        MinimumDamagePct(100)
        Unknown11064(3)
        AirPushbackY(-50000)
        GroundedHitstunAnimation(11)
        Unknown1086(22)
        Unknown11050(9, '')
        Unknown11072(1, 2500000, 0)
    sprite('vr_ph_magictest', 5)

@State
def Eff_450_EyeBurning():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        Unknown3033()
        Unknown4061(2)
    label(0)
    sprite('vr_ph450_00', 3)
    sprite('vr_ph450_01', 3)
    sprite('vr_ph450_02', 3)
    sprite('vr_ph450_03', 3)
    sprite('vr_ph450_04', 3)
    gotoLabel(0)

@State
def AstralHeat_Hinokagutsuchi():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1086(22)
        teleportRelativeY(0)
        Unknown4061(5)
        teleportRelativeX(-25000)
    sprite('null', 40)
    GFX_0('AstralHeat_Hibi', -1)
    SFX_0('019_quake_1')
    sprite('ph450_cutin00', 10)
    ScreenShake(80000, 80000)
    SFX_0('019_quake_1')
    SFX_0('016_explode_2')
    GFX_0('AstralHeatEff_SetugouFire', 0)
    GFX_0('AstralHeatEff_SetugouFire', 1)
    GFX_0('AstralHeatEff_SetugouFire', 2)
    GFX_0('AstralHeatEff_SetugouFire', 3)
    GFX_0('AstralHeatEff_SetugouFire', 4)
    sprite('ph450_cutin01', 6)
    SFX_0('019_quake_0')
    sprite('ph450_cutin02', 6)
    SFX_0('019_quake_0')
    sprite('ph450_cutin03', 6)
    SFX_0('019_quake_1')
    sprite('ph450_cutin04', 6)
    ScreenShake(20000, 20000)
    SFX_0('019_quake_1')
    Unknown36(22)
    Unknown3038(1)
    Unknown35()
    sprite('ph450_cutin05', 6)
    SFX_0('019_quake_1')
    sprite('ph450_cutin06', 6)
    sprite('ph450_cutin07', 6)
    sprite('ph450_cutin08', 6)
    sprite('ph450_cutin09', 6)
    sprite('ph450_cutin10', 6)
    GFX_0('AstralHeatEff_HinoAdd', -1)
    SFX_0('016_explode_1')
    SFX_0('015_blaze_2')
    SFX_0('015_blaze_2')
    sprite('ph450_cutin10', 1)
    GFX_0('AstralHeatEff_DelFire', 0)
    SFX_0('019_quake_1')
    sprite('ph450_cutin10', 1)
    GFX_0('AstralHeatEff_DelFire2', 1)
    sprite('ph450_cutin10', 1)
    GFX_0('AstralHeatEff_DelFire', 2)
    SFX_0('019_quake_0')
    sprite('ph450_cutin10', 1)
    sprite('ph450_cutin10', 1)
    SFX_0('015_blaze_2')
    SFX_0('019_quake_1')
    sprite('ph450_cutin10', 1)
    sprite('ph450_cutin10', 10)
    Unknown3004(-26)
    SFX_0('019_quake_0')
    sprite('ph450_cutin10', 10)
    GFX_0('AstralHeatEff_Rougoku', -1)
    Unknown3038(1)
    Unknown36(22)
    Unknown3038(0)
    Unknown35()
    SFX_0('019_quake_1')
    SFX_0('015_blaze_2')
    sprite('ph450_cutin10', 2)
    GFX_0('AstralHeatEff_DelFire', 0)
    sprite('ph450_cutin10', 2)
    GFX_0('AstralHeatEff_DelFire2', 1)
    sprite('ph450_cutin10', 2)
    GFX_0('AstralHeatEff_DelFire', 2)
    sprite('ph450_cutin10', 2)
    sprite('ph450_cutin10', 2)
    sprite('ph450_cutin10', 2)
    sprite('ph450_cutin10', 20)
    SFX_0('019_quake_1')
    sprite('ph450_cutin10', 2)
    GFX_0('AstralHeatEff_DelFire', 0)
    sprite('ph450_cutin10', 2)
    GFX_0('AstralHeatEff_DelFire2', 1)
    SFX_0('015_blaze_2')
    sprite('ph450_cutin10', 2)
    GFX_0('AstralHeatEff_DelFire', 2)
    sprite('ph450_cutin10', 2)
    sprite('ph450_cutin10', 2)
    SFX_0('019_quake_1')
    sprite('ph450_cutin10', 2)

@State
def AstralHeat_Hibi():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown1096(1350)
    sprite('vr_ph450_20', 4)
    Unknown23015(2)
    sprite('vr_ph450_21', 4)
    Unknown23015(0)
    sprite('vr_ph450_22', 4)
    ScreenShake(10000, 10000)
    sprite('vr_ph450_22', 4)
    ScreenShake(10000, 10000)
    GFX_1('phef450_groundray', 0)
    GFX_1('phef450_groundsmoke_R', 5)
    GFX_1('phef450_groundsmoke_L', 6)
    sprite('vr_ph450_22', 4)
    ScreenShake(10000, 10000)
    GFX_1('phef450_groundray', 1)
    GFX_1('phef450_groundray', 2)
    GFX_1('phef450_groundsmoke_R', 5)
    GFX_1('phef450_groundsmoke_L', 6)
    sprite('vr_ph450_22', 10)
    ScreenShake(10000, 10000)
    GFX_1('phef450_groundray', 3)
    GFX_1('phef450_groundray', 4)
    GFX_1('phef450_groundsmoke_R', 5)
    GFX_1('phef450_groundsmoke_L', 6)
    sprite('vr_ph450_22', 4)
    ScreenShake(10000, 10000)
    GFX_1('phef450_groundray', 0)
    GFX_1('phef450_groundsmoke_R', 5)
    GFX_1('phef450_groundsmoke_L', 6)
    sprite('vr_ph450_22', 4)
    ScreenShake(10000, 10000)
    GFX_1('phef450_groundray', 1)
    GFX_1('phef450_groundray', 2)
    GFX_1('phef450_groundsmoke_R', 5)
    GFX_1('phef450_groundsmoke_L', 6)
    sprite('null', 8)
    GFX_1('phef_450_groundstone', -1)
    endState()

@State
def AstralHeatEff_SetugouFire():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown21010(1)
        Unknown2054(1)
        EnableCollision(0)
        Unknown2053(0)
        Unknown2034(0)
    label(0)
    sprite('null', 25)
    GFX_0('AstralHeatEff_DelFire', -1)
    gotoLabel(0)

@State
def AstralHeatEff_HinoAdd():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2054(1)
        Unknown3033()
        Unknown4061(2)
        Unknown3001(0)
        Unknown23015(3)
    sprite('vrph450_30', 10)
    Unknown3004(26)
    sprite('vrph450_30', 10)
    Unknown3004(0)
    sprite('vrph450_30', 20)
    Unknown3004(-13)

@State
def AstralHeatEff_DelFire():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2054(1)
        Unknown4061(2)
        Unknown1096(1600)
        Unknown1099(7)
    sprite('vr_phcmn_00', 4)
    sprite('vr_phcmn_01', 4)
    sprite('vr_phcmn_02', 4)
    sprite('vr_phcmn_03', 4)
    sprite('vr_phcmn_04', 3)
    sprite('vr_phcmn_05', 3)
    GFX_1('phef450_hinoko', 0)
    GFX_1('phef450_hinoko', 1)
    GFX_1('phef450_hinoko', 2)
    sprite('vr_phcmn_06', 3)
    sprite('vr_phcmn_07', 3)

@State
def AstralHeatEff_DelFire2():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown1096(1800)
        Unknown1099(7)
        Unknown1007(-30000)
    sprite('vr_phcmn_00', 3)
    sprite('vr_phcmn_01', 3)
    sprite('vr_phcmn_02', 3)
    sprite('vr_phcmn_03', 3)
    sprite('vr_phcmn_04', 3)
    sprite('vr_phcmn_05', 3)
    GFX_1('phef450_hinoko', 0)
    GFX_1('phef450_hinoko', 1)
    GFX_1('phef450_hinoko', 2)
    sprite('vr_phcmn_06', 3)
    sprite('vr_phcmn_07', 3)

@State
def AstralHeatEff_Rougoku():

    def upon_IMMEDIATE():
        Unknown4003('pheff450_ori00', '')
        Unknown3032()
        Unknown2054(1)
        Unknown1096(825)
        Unknown1007(-3000)
    sprite('null', 10)
    Unknown3001(0)
    Unknown3004(26)
    sprite('null', 100)

@State
def AstralHeatEff_Rougoku2():

    def upon_IMMEDIATE():
        Unknown4003('pheff450_ori00', '')
        GFX_2('phef450_rou_jizoku')
        Unknown2054(1)
        Unknown3032()
        Unknown1096(600)
        Unknown1007(300000)
        Unknown3038(1)
    sprite('null', 160)
    GFX_0('AstralHeatEff_Rougoku2Sub', -1)

@State
def AstralHeatEff_Rougoku2Sub():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        Unknown1096(700)
        Unknown3001(0)
    label(0)
    sprite('null', 2)
    GFX_0('AstralHeatEff_DelFire', 0)
    Unknown36(1)
    Unknown1097(-450)
    Unknown3001(180)
    Unknown35()
    sprite('null', 2)
    GFX_0('AstralHeatEff_DelFire2', 1)
    Unknown36(1)
    Unknown1097(-450)
    Unknown3001(180)
    Unknown35()
    sprite('null', 2)
    GFX_0('AstralHeatEff_DelFire', 2)
    Unknown36(1)
    Unknown1097(-450)
    Unknown3001(180)
    Unknown35()
    sprite('null', 2)
    GFX_0('AstralHeatEff_DelFire2', 3)
    Unknown36(1)
    Unknown1097(-450)
    Unknown3001(180)
    teleportRelativeX(30000)
    Unknown35()
    sprite('null', 2)
    GFX_0('AstralHeatEff_DelFire', 4)
    Unknown36(1)
    Unknown1097(-450)
    teleportRelativeX(-30000)
    Unknown3001(180)
    Unknown35()
    sprite('null', 2)
    GFX_0('AstralHeatEff_DelFire2', 5)
    Unknown36(1)
    Unknown1097(-200)
    Unknown1007(60000)
    Unknown3001(180)
    Unknown35()
    sprite('null', 13)
    gotoLabel(0)

@State
def Eff_450_Terepo():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2054(1)
        Unknown4061(2)
    sprite('vr_ph450_10', 6)
    sprite('vr_ph450_11', 3)
    sprite('vr_ph450_12', 3)
    GFX_1('phef450_terepo', -1)
    sprite('vr_ph450_12', 10)
    physicsYImpulse(25000)
    Unknown1067(2400)
    GFX_0('Eff_450_circle', -1)
    GFX_0('Eff_450_circle2', -1)

@State
def Eff_450_circle():

    def upon_IMMEDIATE():
        Unknown4003('pheff450_AddCircle', '')
        Unknown2054(1)
        Unknown3033()
        Unknown1007(300000)
    sprite('null', 5)
    Unknown1099(300)
    sprite('null', 5)
    Unknown3004(-51)

@State
def Eff_450_circle2():

    def upon_IMMEDIATE():
        Unknown4003('pheff450_AddCircle', '')
        Unknown2054(1)
        Unknown3033()
    sprite('null', 5)
    Unknown1099(300)
    Unknown3004(-51)

@State
def phAst_ShaSha00():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4003('pheff450_shasha00', '')
        Unknown2054(1)
        Unknown3032()
        Unknown23015(1)
        Unknown1007(-400000)
    sprite('null', 39)

@State
def AstralHeat_Camera():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown20000(1)
        Unknown20003(1)
        Unknown20004(1)
        EnableCollision(0)
        Unknown2053(0)
        Unknown2034(0)
        Unknown20001(1)
    sprite('null', 7)
    teleportRelativeX(400000)
    Unknown1007(-800000)
    physicsYImpulse(48000)
    sprite('null', 30)
    Unknown20001(0)
    physicsYImpulse(18000)
    GFX_2('phef_shashaend')
    sprite('null', 10)
    physicsYImpulse(3000)
    sprite('null', 5)
    physicsYImpulse(1500)
    sprite('null', 210)
    physicsYImpulse(0)
    sprite('null', 10)
    Unknown20001(1)
    Unknown1007(-1200000)
    Unknown1000(0)
    Unknown36(22)
    Unknown3038(0)
    Unknown35()
    GFX_0('AstralHeatEff_Rougoku2', -1)
    sprite('null', 32767)
    Unknown20001(0)
    Unknown20009(1300)

@State
def AstralHeatEff_MeteoMato():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown1000(-800000)
        teleportRelativeY(0)
        Unknown1007(500000)
        sendToLabelUpon(2, 0)
    sprite('null', 8)
    GFX_0('AstralHeatEff_Meteo', -1)
    SFX_0('016_explode_2')
    SFX_0('016_explode_2')
    sprite('null', 8)
    GFX_0('AstralHeatEff_Meteo', -1)
    Unknown36(1)
    teleportRelativeX(1000000)
    Unknown1097(400)
    Unknown35()
    SFX_0('016_explode_2')
    SFX_0('213_bound_1')
    sprite('null', 8)
    GFX_0('AstralHeatEff_Meteo', -1)
    Unknown36(1)
    teleportRelativeX(500000)
    Unknown1097(500)
    Unknown35()
    SFX_0('016_explode_2')
    SFX_0('016_explode_2')
    sprite('null', 8)
    GFX_0('AstralHeatEff_Meteo', -1)
    Unknown36(1)
    teleportRelativeX(-1000000)
    Unknown1097(600)
    Unknown35()
    SFX_0('016_explode_2')
    SFX_0('213_bound_1')
    sprite('null', 6)
    GFX_0('AstralHeatEff_Meteo', -1)
    Unknown36(1)
    teleportRelativeX(-500000)
    Unknown1097(700)
    Unknown35()
    SFX_0('016_explode_2')
    SFX_0('016_explode_2')
    sprite('null', 6)
    GFX_0('AstralHeatEff_Meteo', -1)
    Unknown36(1)
    teleportRelativeX(750000)
    Unknown1097(800)
    Unknown35()
    SFX_0('016_explode_2')
    SFX_0('213_bound_0')
    sprite('null', 4)
    GFX_0('AstralHeatEff_Meteo', -1)
    Unknown36(1)
    teleportRelativeX(250000)
    Unknown1097(900)
    Unknown35()
    SFX_0('016_explode_2')
    SFX_0('016_explode_2')
    sprite('null', 15)
    GFX_0('AstralHeatEff_Meteo', -1)
    Unknown36(1)
    teleportRelativeX(-250000)
    Unknown1097(1000)
    Unknown35()
    SFX_0('016_explode_2')
    SFX_0('213_bound_0')
    sprite('null', 15)
    GFX_0('AstralHeatEff_MeteoLast', -1)
    SFX_0('016_explode_2')
    SFX_0('016_explode_2')
    sprite('null', 15)
    sprite('null', 10)
    GFX_0('Eff_450_Lastbomb', -1)
    Unknown26('AstralHeatEff_Meteo')
    SFX_0('016_explode_2')
    SFX_0('016_explode_2')
    SFX_0('213_bound_1')
    sprite('null', 4)
    GFX_0('Eff_450_Burning', -1)

@State
def AstralHeatEff_Meteo():

    def upon_IMMEDIATE():
        Unknown4003('pheff450_meteo00', '')
        Unknown2054(1)
        Unknown3032()
        physicsYImpulse(-48000)
        physicsXImpulse(48000)
        Unknown1073(-45000)
        sendToLabelUpon(2, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 32767)
    GFX_1('phef_bgr_atk_end', -1)
    Unknown3001(0)
    physicsYImpulse(0)
    physicsXImpulse(0)
    GFX_0('AstralHeatEff_MeteoMag', -1)
    ScreenShake(0, 10000)

@State
def AstralHeatEff_MeteoMag():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4013(2)
        Unknown2054(1)
        Unknown3032()
        Unknown1096(1000)
        Unknown1062(-300, 0)
    sprite('null', 10)
    GFX_0('Eff_450_bomb', -1)
    Unknown3001(0)
    ScreenShake(10000, 10000)
    sprite('null', 10)
    Unknown3001(255)
    Unknown1067(75)
    label(0)
    sprite('null', 2)
    Unknown1067(0)
    Unknown1057(-300)
    teleportRelativeX(10000)
    sprite('null', 2)
    Unknown1057(300)
    teleportRelativeX(-10000)
    gotoLabel(0)

@State
def Eff_450_bomb():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4003('pheff431_bomb00', '')
        GFX_2('phef431_blm')
        Unknown3032()
        Unknown1007(200000)
        teleportRelativeX(100000)
        Unknown1096(600)
    sprite('null', 2)
    sprite('null', 2)
    Unknown1097(200)
    Unknown1007(25000)
    sprite('null', 2)
    Unknown1007(25000)
    sprite('null', 5)
    GFX_0('Eff_450_bombEnd', -1)
    Unknown1097(100)
    Unknown1007(25000)
    Unknown3004(-51)
    GFX_1('phef_400_bom', -1)
    GFX_1('phef_400_blm', -1)

@State
def Eff_450_bombEnd():

    def upon_IMMEDIATE():
        Unknown4003('pheff431_bomb01', '')
        Unknown2054(1)
        Unknown3032()
        Unknown1096(250)
        Unknown1007(-250000)
    sprite('null', 14)
    GFX_1('phef_402_end_g', -1)
    sprite('null', 9)
    GFX_1('pheff431_gsmoke_pos', -1)
    Unknown3004(-26)

@State
def AstralHeatEff_MeteoLast():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown4003('pheff450_meteo01', '')
        Unknown1073(-45000)
        Unknown1056(3500)
        Unknown1064(3500)
        teleportRelativeX(650000)
        Unknown23015(1)
        EnableCollision(0)
        Unknown2053(0)
        Unknown2034(0)
    sprite('null', 7)
    physicsYImpulse(-40000)
    physicsXImpulse(28000)
    GFX_0('AstralHeat_ShakeFallMeteo', -1)
    sprite('null', 7)
    physicsYImpulse(-30000)
    physicsXImpulse(21000)
    sprite('null', 15)
    physicsYImpulse(-20000)
    physicsXImpulse(14000)
    sprite('null', 6)
    physicsYImpulse(-20000)
    physicsXImpulse(14000)

@State
def AstralHeat_ShakeFallMeteo():

    def upon_IMMEDIATE():
        Unknown2054(1)
        teleportRelativeX(-400000)
        Unknown1007(-800000)
    label(0)
    sprite('null', 5)
    ScreenShake(5000, 5000)
    gotoLabel(0)

@State
def Eff_450_Lastbomb():

    def upon_IMMEDIATE():
        Unknown4003('pheff450_lastbomb00', '')
        Unknown3032()
        Unknown1096(1200)
        teleportRelativeY(0)
        Unknown1000(0)
        Unknown23015(1)
    sprite('null', 2)
    sprite('null', 2)
    Unknown1097(200)
    Unknown1007(25000)
    sprite('null', 2)
    Unknown1007(25000)
    sprite('null', 5)
    GFX_0('Eff_450_LastbombEnd', -1)
    Unknown1097(100)
    Unknown1007(25000)
    Unknown3004(-51)

@State
def Eff_450_LastbombEnd():

    def upon_IMMEDIATE():
        Unknown4003('pheff450_lastbomb01', '')
        Unknown2054(1)
        Unknown3032()
        Unknown1096(500)
        Unknown1007(-300000)
        Unknown23015(1)
    sprite('null', 4)
    sprite('null', 10)
    GFX_1('phef_lastbomb_end', -1)
    sprite('null', 9)
    Unknown3004(-26)

@State
def Eff_450_Burning():

    def upon_IMMEDIATE():
        Unknown4003('pheff450_winbg', '')
        GFX_2('pheff450_winbg')
        Unknown2054(1)
        Unknown3032()
        teleportRelativeX(600000)
        Unknown1096(800)
    label(0)
    sprite('null', 10)
    SFX_0('019_quake_0')
    sprite('null', 10)
    SFX_0('019_quake_1')
    loopRest()
    gotoLabel(0)

@State
def bphef_DDD_Particle():

    def upon_IMMEDIATE():
        Unknown4022(3)
        teleportRelativeY(64000)
    sprite('null', 30)
    GFX_1('bphef_DDD_Fire', -1)
    GFX_1('bphef_DDD_Hinoko', -1)
    sprite('null', 30)
    GFX_1('bphef_DDD_Fire', -1)
    GFX_1('bphef_DDD_Hinoko', -1)
    sprite('null', 30)
    GFX_1('bphef_DDD_Fire', -1)
    GFX_1('bphef_DDD_Hinoko', -1)
    sprite('null', 30)
    GFX_1('bphef_DDD_Hinoko', -1)
    sprite('null', 30)
    GFX_1('bphef_DDD_Hinoko', -1)
    sprite('null', 30)
    GFX_1('bphef_DDD_Hinoko', -1)
    sprite('null', 30)
    GFX_1('bphef_DDD_Hinoko', -1)

@State
def phef_600_bg():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4009(3)
        Unknown4061(3)
        Unknown3032()
        Unknown1056(20000)
        Unknown1064(20000)
        Unknown23015(15)
        Unknown2019(10000)

        def upon_3():
            Unknown23057(50)
            Unknown23058(50)
    sprite('vr_screen_black', 30)
    Unknown3001(0)
    Unknown3004(3)
    sprite('vr_screen_black', 60)
    Unknown3001(95)
    Unknown3004(0)
    sprite('vr_screen_black', 30)
    Unknown3004(-3)

@State
def phef_600_Fire():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        teleportRelativeX(100000)
    sprite('null', 1)
    GFX_1('phef_600bigen', 100)

@State
def phef_600_Fire2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4061(2)
        Unknown3033()
    sprite('phef600_10', 4)
    sprite('phef600_11', 4)
    sprite('phef600_12', 4)

@State
def phef_600_FireWall():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('pheff600_firewall', '')
        Unknown4015()
        GFX_2('phef_600ground')
        teleportRelativeX(100000)
        Unknown3033()
    sprite('null', 6)
    Unknown3001(0)
    Unknown3004(32)
    GFX_1('phef_600fireblow', -1)
    SFX_0('019_quake_0')
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    SFX_0('019_quake_1')
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    SFX_0('019_quake_0')
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    SFX_0('019_quake_1')
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    SFX_0('019_quake_0')
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    SFX_0('019_quake_1')
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    SFX_0('019_quake_0')
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 16)
    Unknown3004(-16)
    GFX_0('phef_600_Fire_End', -1)

@State
def phef_600_Fire_End():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
    sprite('null', 1)
    GFX_1('phef_600fire_end', -1)

@State
def phef_600_HatFire():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4061(2)
        Unknown3033()
        Unknown23015(6)
    sprite('phef600_01', 6)
    sprite('phef600_02', 6)
    sprite('phef600_03', 6)
    sprite('phef600_04', 6)
    sprite('phef600_05', 6)
    sprite('phef600_06', 6)

@State
def phef_600_Hat():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4061(0)
        Unknown3032()
    sprite('phef600_hat', 2)
    Unknown3001(127)
    sprite('phef600_hat', 2)
    Unknown3001(191)
    sprite('phef600_hat', 2)
    Unknown3001(255)

@State
def Entry_Hinokagutsuchi():

    def upon_IMMEDIATE():
        pass
    sprite('ph601cutin_ex01', 5)

@State
def Entry_HinoEff():

    def upon_IMMEDIATE():
        GFX_2('phef601_root')
        Unknown4010(2)
        sendToLabelUpon(32, 1)
        Unknown2037(0)

        def upon_33():
            clearUponHandler(33)
            SLOT_51 = 1
            Unknown2037(1)
    label(0)
    sprite('null', 16)
    GFX_0('Entry_Fire', -1)
    Unknown36(1)
    teleportRelativeX(-350000)
    Unknown35()
    GFX_0('Entry_Fire', -1)
    Unknown36(1)
    teleportRelativeX(300000)
    Unknown1007(100000)
    Unknown1097(500)
    Unknown23015(2)
    Unknown35()
    GFX_0('Entry_Fire', -1)
    Unknown36(1)
    teleportRelativeX(-300000)
    Unknown1007(100000)
    Unknown1097(800)
    Unknown23015(2)
    Unknown35()
    GFX_0('Entry_Fire', -1)
    Unknown36(1)
    teleportRelativeX(180000)
    Unknown1007(25000)
    Unknown1097(600)
    Unknown35()
    GFX_0('Entry_Fire', -1)
    Unknown36(1)
    teleportRelativeX(-200000)
    Unknown1097(600)
    Unknown35()
    GFX_0('Entry_Fire', -1)
    Unknown36(1)
    Unknown1057(300)
    Unknown35()
    if SLOT_2:
        SFX_0('019_quake_1')
    gotoLabel(0)
    label(1)
    sprite('null', 15)
    GFX_0('Entry_FireEnd', -1)
    Unknown3004(25)

@State
def Entry_Fire():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown1096(1000)
        Unknown1067(15)
        Unknown2054(1)
        Unknown21010(1)
        Unknown1010(-25000, 25000)
        Unknown1007(-50000)
    sprite('vr_phcmn_00', 3)
    sprite('vr_phcmn_01', 3)
    sprite('vr_phcmn_02', 3)
    sprite('vr_phcmn_03', 3)
    sprite('vr_phcmn_04', 3)
    sprite('vr_phcmn_05', 3)
    Unknown3004(-26)
    GFX_1('phef450_hinoko', 2)
    sprite('vr_phcmn_06', 3)
    sprite('vr_phcmn_07', 3)

@State
def Entry_FireEnd():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown3033()
        Unknown4003('pheff601_fire00', '')
        Unknown1096(800)
    sprite('null', 2)
    ScreenShake(5000, 5000)
    GFX_1('phef601_endray', -1)
    GFX_0('Entry_FireEndsub_b', -1)
    Unknown36(1)
    Unknown1007(100000)
    Unknown1097(1000)
    Unknown35()
    sprite('null', 2)
    GFX_0('Entry_FireEndsub_a', -1)
    Unknown36(1)
    Unknown1007(100000)
    Unknown1097(-2000)
    Unknown35()
    sprite('null', 2)
    GFX_0('Entry_FireEndsub_a', -1)
    Unknown36(1)
    Unknown1007(200000)
    Unknown35()
    sprite('null', 2)
    GFX_0('Entry_FireEndsub_a', -1)
    Unknown36(1)
    Unknown1007(300000)
    Unknown1097(-2000)
    Unknown35()
    sprite('null', 2)
    GFX_0('Entry_FireEndsub_a', -1)
    Unknown36(1)
    Unknown1007(400000)
    Unknown1097(-1500)
    Unknown35()
    sprite('null', 2)
    GFX_0('Entry_FireEndsub_a', -1)
    Unknown36(1)
    Unknown1007(550000)
    Unknown1097(-1200)
    Unknown35()
    sprite('null', 3)
    GFX_0('Entry_FireEndsub2', -1)

@State
def Entry_FireEndsub_a():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff432_yari01', '')
        Unknown2054(1)
        Unknown1096(3800)
        Unknown1007(10000)
    sprite('null', 5)
    sprite('null', 10)
    Unknown3004(-26)
    Unknown1099(240)
    GFX_0('Entry_FireEndsub_b2', -1)

@State
def Entry_FireEndsub_b():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff432_yari01', '')
        Unknown2054(1)
        Unknown1096(3800)
        Unknown1007(10000)
    sprite('null', 10)
    sprite('null', 10)
    Unknown3004(-26)
    Unknown1099(120)

@State
def Entry_FireEndsub_b2():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff_rrr00', '')
        Unknown1096(2500)
        Unknown3001(255)
        Unknown1072(20000)
    sprite('null', 5)
    sprite('null', 10)
    Unknown1099(120)
    Unknown3004(-26)

@State
def Entry_FireEndsub2():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4003('pheff432_yari03', '')
        Unknown2054(1)
        Unknown1056(1500)
        Unknown1064(1700)
    sprite('null', 10)
    sprite('null', 4)
    GFX_0('Entry_Fire', -1)
    Unknown36(1)
    Unknown1007(100000)
    Unknown1097(1200)
    Unknown23015(2)
    Unknown35()

@State
def phef_602_Fire():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        teleportRelativeX(-20000)
    sprite('null', 1)
    GFX_1('phef_600bigen', 100)

@State
def phef_602_Fire2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(2)
        Unknown3033()
        teleportRelativeX(-80000)
    sprite('phef600_10', 4)
    sprite('phef600_11', 4)
    sprite('phef600_12', 4)

@State
def phef_602_FireWall():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4003('pheff600_firewall', '')
        Unknown4015()
        teleportRelativeX(-20000)
        Unknown3033()
        GFX_2('phef_600ground')
        Unknown1056(1500)
    sprite('null', 6)
    SFX_0('019_quake_0')
    Unknown3001(0)
    Unknown3004(32)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    SFX_0('019_quake_1')
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    SFX_0('019_quake_0')
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    SFX_0('019_quake_1')
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    SFX_0('019_quake_0')
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    SFX_0('019_quake_1')
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    SFX_0('019_quake_0')
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 16)
    Unknown3004(-16)
    GFX_0('phef_602_Fire_End', -1)

@State
def phef_602_Fire_End():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        teleportRelativeX(-20000)
    sprite('null', 1)
    GFX_1('phef_600fire_end', -1)

@Subroutine
def ShotDelete_dmy():
    Unknown4011(2)
    Unknown4010(2)
    Unknown4007(2)
    Unknown4009(2)
    GuardPoint_(1)
    setInvincible(1)
    Unknown22019(0, 0, 0, 1, 0)
    Unknown22031(0, 0)
    Unknown22032(1)
    Unknown2037(1)

    def upon_3():
        if (not SLOT_30):

            def upon_42():
                if SLOT_2:
                    Unknown23029(3, 9002, 0)
                    Unknown2037(0)
                    Unknown13(25)

@State
def ph216_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ph216_03_col_damy', 3)
    sprite('ph216_04_col_damy', 3)

@State
def ph202_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ph202_03_col_damy', 3)

@State
def ph200_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ph200_03_col_damy', 3)

@State
def ph210_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ph210_05_col_damy', 4)

@State
def ph212_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ph212_05_col_damy', 4)

@State
def ph201_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ph201_04_col_damy', 3)
    sprite('ph201_05_col_damy', 3)

@State
def ph230_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ph230_03_col_damy', 3)

@State
def ph231_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ph231_03_col_damy', 3)
    sprite('ph231_04_col_damy', 3)

@State
def ph235_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ph235_03_col_damy', 5)

@State
def ph250_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ph250_03_col_damy', 5)

@State
def ph252_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ph252_03_col_damy', 3)

@State
def ph253_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ph253_03_col_damy', 3)

@State
def ph251_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ph251_03_col_damy', 3)
    sprite('ph251_04_col_damy', 3)

@State
def ph211_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ph211_05_col_damy', 4)
    sprite('ph211_06_col_damy', 4)