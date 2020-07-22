@State
def EMB():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1007(240000)
        Unknown2054(1)
        Unknown4003('ef_emb_HZ.DIG', 'ef_emb_HZ_motion_000.mmot')
        Unknown23015(5)
        Unknown3033()
        Unknown3038(1)
    sprite('null', 10)
    Unknown3026(-16777216)
    Unknown3025(-16776961, 10)
    Unknown1096(2950)
    Unknown1099(-100)
    Unknown1072(120000)
    Unknown1074(-6000)
    sprite('null', 10)
    Unknown3025(-8342273, 10)
    sprite('null', 10)
    Unknown3025(-1, 10)
    Unknown1099(0)
    Unknown1074(0)
    sprite('null', 10)
    Unknown3025(-8342273, 10)
    sprite('null', 20)

@State
def EMB_OD():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1007(240000)
        Unknown2054(1)
        Unknown4003('ef_emb_HZ.DIG', 'ef_emb_HZ_motion_000.mmot')
        Unknown23015(5)
        Unknown3033()
        Unknown3038(1)
    sprite('null', 10)
    Unknown3026(-16777216)
    Unknown3025(-1, 10)
    Unknown1096(2950)
    Unknown1099(-100)
    Unknown1072(120000)
    Unknown1074(-6000)
    sprite('null', 10)
    Unknown3025(-8342273, 10)
    sprite('null', 10)
    Unknown3025(-16744193, 10)
    Unknown1099(0)
    Unknown1074(0)
    sprite('null', 10)
    Unknown3025(-16744193, 10)
    sprite('null', 20)

@State
def EMB_AST():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1007(240000)
        Unknown2054(1)
        Unknown4003('ef_emb_HZ.DIG', 'ef_emb_HZ_motion_000.mmot')
        Unknown23015(5)
        Unknown3033()
        Unknown3038(1)
    sprite('null', 10)
    Unknown3026(-16777216)
    Unknown3025(-65536, 10)
    Unknown1096(2950)
    Unknown1099(-100)
    Unknown1072(120000)
    Unknown1074(-6000)
    sprite('null', 10)
    Unknown3025(-55256, 10)
    sprite('null', 10)
    Unknown3025(-4934476, 10)
    Unknown1099(0)
    Unknown1074(0)
    sprite('null', 10)
    Unknown3025(-65536, 10)
    sprite('null', 20)

@State
def HZEF_GuardLoop():

    def upon_IMMEDIATE():
        Unknown4007(3)
        teleportRelativeX(-16000)
        sendToLabelUpon(32, 99)
    sprite('null', 20)
    GFX_0('HZEF_GuardLoopParts', -1)
    Unknown36(1)
    teleportRelativeX(32000)
    Unknown1007(-97500)
    physicsYImpulse(20000)
    Unknown1082(4)
    Unknown35()
    GFX_0('HZEF_GuardLoopParts', -1)
    Unknown36(1)
    teleportRelativeX(16000)
    Unknown1007(110000)
    physicsYImpulse(-40000)
    Unknown1056(-1000)
    Unknown1082(4)
    Unknown35()
    GFX_0('HZEF_GuardLoopParts', -1)
    Unknown36(1)
    teleportRelativeX(-16000)
    Unknown1007(-100000)
    physicsYImpulse(40000)
    Unknown1056(-1000)
    Unknown1082(4)
    Unknown35()
    GFX_0('HZEF_GuardLoopParts', -1)
    Unknown36(1)
    teleportRelativeX(-40000)
    Unknown1007(95000)
    physicsYImpulse(-15000)
    Unknown1082(4)
    Unknown35()
    loopRest()
    ExitState()
    label(99)
    Unknown21012('HZEF_GuardLoopParts', 32)

@State
def HZEF_GuardLoopParts():

    def upon_IMMEDIATE():
        Unknown2019(-100)
        Unknown3032()
        sendToLabelUpon(32, 99)
    sprite('vrhzef_guard00', 4)
    Unknown3001(100)
    sprite('vrhzef_guard00', 2)
    Unknown4009(3)
    Unknown3001(200)
    sprite('vrhzef_guard00', 12)
    Unknown4009(0)
    Unknown3001(120)
    Unknown3004(-15)
    loopRest()
    ExitState()
    label(99)
    Unknown14()

@State
def HZEF_HeavyGuardLoop():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown21012('HZEF_GuardLoop', 32)
    sprite('null', 20)
    GFX_0('HZEF_HeavyGuardLoopObj', -1)
    Unknown36(1)
    teleportRelativeX(48000)
    Unknown1007(32000)
    physicsYImpulse(10000)
    Unknown35()
    GFX_0('HZEF_HeavyGuardLoopObj', -1)
    Unknown36(1)
    teleportRelativeX(16000)
    Unknown1007(-16000)
    physicsYImpulse(-15000)
    Unknown1056(-1000)
    Unknown35()
    GFX_0('HZEF_HeavyGuardLoopObj', -1)
    Unknown36(1)
    teleportRelativeX(-16000)
    Unknown1007(16000)
    physicsYImpulse(15000)
    Unknown1056(-1000)
    Unknown35()
    GFX_0('HZEF_HeavyGuardLoopObj', -1)
    Unknown36(1)
    teleportRelativeX(-48000)
    Unknown1007(-32000)
    physicsYImpulse(-10000)
    Unknown35()

@State
def HZEF_HeavyGuardLoopObj():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown2019(-100)
        Unknown3032()
        teleportRelativeX(-64000)
    sprite('vrhzef_guard00', 2)
    Unknown3001(250)
    sprite('vrhzef_guard00', 10)
    Unknown3001(150)
    Unknown3004(-15)

@State
def HZEF_BBStart():
    sprite('null', 120)
    teleportRelativeX(-80000)
    Unknown1007(220000)
    Unknown4049(1400)
    Unknown4046(-16777216, -16777216, 65280)
    Unknown4045('rgef_bloodkineR', -1)
    Unknown4049(900)
    Unknown4046(-16777216, -16777216, 65280)
    Unknown4045('rgef_bloodkineL', -1)
    Unknown4049(1400)
    Unknown4046(-16711886, -16711886, 65330)
    Unknown4045('rgef_bloodkineR2', -1)
    Unknown4049(900)
    Unknown4046(-16711886, -16711886, 65330)
    Unknown4045('rgef_bloodkineL2', -1)
    Unknown4045('rgef_bkburst', -1)
    Unknown4054(2)
    Unknown4046(-100598016, -1778319616, 65280)
    Unknown4045('rgef_bloodkineback', -1)

@State
def ModelMagicCircle1():

    def upon_IMMEDIATE():
        Unknown3038(1)
        Unknown4003('rgef_mc.DIG', 'rgef_mc_motion_000.mmot')
        Unknown4015()
        Unknown3026(-16711936)
        Unknown2054(1)
    sprite('null', 74)

@State
def UltimateKusari():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(2)
        Damage(500)
        AttackP2(100)
        AirHitstunAnimation(1)
        GroundedHitstunAnimation(1)
        AirPushbackY(39000)
        YImpluseBeforeWallbounce(1500)
        AirUntechableTime(120)
        Hitstop(20)
        Unknown11084(1)
        ProjectileDurabilityLvl(3)
        Unknown11034(3)
        Unknown9016(1)
        Unknown11066(1)
        Unknown11108(3)
        StarterRating(2)
        Unknown11064(1)
        Unknown4010(3)
        Unknown30048(1)

        def upon_48():
            Unknown23030('KusariIdling', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_31():
            Unknown23030('KusariDraw', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_3():
            if SLOT_2:
                Unknown23030('KusariAngleByChain', 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown4055(0)
        Unknown23030('KusariKansetsu', 0, 7, 0, 0, 0, 0, 0, 0)
        Unknown3029(0)
        AfterimageColor_1(200, 255, 255, 255)
        AfterimageColor_2(0, 255, 255, 255)
        Unknown3053(1)
        Unknown3054(56, 120)
        Unknown3054(57, 80)
        Unknown3054(58, 40)
        Unknown3032()
        sendToLabelUpon(78, 0)
        Unknown23030('UltimateKusariAtkVectorX', 0, 70, 0, 0, 0, 0, 0, 0)
        if Unknown23146('16000000556c74696d6174654d61676963436972636c6500000000000000000000000000'):
            Unknown11069('UltimateShot')
        if Unknown23146('16000000556c74696d6174654d61676963436972636c655f4f4400000000000000000000'):
            Unknown11069('UltimateShot_OD')
        if Unknown23146('16000000556c74696d6174654d61676963436972636c655f444444000000000000000000'):
            Damage(200)
            AttackP2(100)
            MinimumDamagePct(100)
            Unknown11069('UltimateShot_DDD')
        if Unknown23146('16000000556c74696d6174654d61676963436972636c655f4f4444444400000000000000'):
            Damage(200)
            AttackP2(100)
            MinimumDamagePct(100)
            Unknown11069('UltimateShot_ODDDD')
    sprite('vr_chain_tip03DD', 1)
    SFX_3('hzse_02')
    Unknown2019(-500)
    Unknown23143(70000, 0, 70)
    Unknown23030('KusariParam', 0, 0, 0, 7770, 0, 0, 0, 0)
    Unknown23030('KusariParam', 0, 1, 0, 16, 0, 0, 0, 10)
    Unknown23030('KusariParam', 0, 2, 0, 33, 0, 0, 0, 10)
    Unknown23030('KusariParam', 0, 3, 0, 50, 0, 0, 0, 10)
    Unknown23030('KusariParam', 0, 4, 0, 66, 0, 0, 0, 10)
    Unknown23030('KusariParam', 0, 5, 0, 83, 0, 0, 0, 10)
    Unknown23030('KusariParam', 0, 6, 0, 7771, 0, 0, 0, 0)
    Unknown23030('KusariFirstPosition', 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('vr_chain_tip03DD', 80)
    Unknown23030('KusariSpeed', 0, 3000, 0, 0, 0, 0, 0, 0)
    GFX_0('EffUltimateChainAura', -1)
    loopRest()
    ExitState()
    label(0)
    teleportRelativeX(120000)
    sprite('vr_chain_tip04', 3)
    Unknown21015('EffUltimateChainAura', 1010, 0)
    Unknown23029(3, 1010, 0)
    Unknown1084(1)
    Unknown23143(0, 0, 0)
    Unknown23144('03000000000000006f00000000000000000000000000000000000000000000004b0000000000000004000000')
    sprite('vr_chain_tip04', 27)
    Unknown2037(1)
    Unknown2019(500)
    sprite('vr_chain_tip04', 30)
    Unknown3004(-30)
    Unknown3032()

@State
def EffUltimateChainAura():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown2055(20)
        Unknown1007(-48000)

        def upon_43():
            if (SLOT_48 == 1010):
                Unknown14()
    label(0)
    sprite('null', 1)
    GFX_0('EffUltimateChainAuraObj', -1)
    loopRest()
    gotoLabel(0)

@State
def EffUltimateChainAuraObj():

    def upon_IMMEDIATE():
        GFX_2('hzef_antiairchain')
        Unknown1096(300)
        Unknown1102(0, 400)
        Unknown4054(2)
        Unknown4045('hzef_exheadmoveopt', -1)
    sprite('null', 30)

@State
def KusariAntiAir():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4009(3)

        def upon_31():
            Unknown23030('KusariDraw', 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown23030('KusariKansetsu', 0, 7, 0, 0, 0, 0, 0, 0)
        Unknown3029(1)
        AfterimageColor_1(200, 255, 255, 255)
        AfterimageColor_2(0, 255, 255, 255)
        Unknown3053(1)
        Unknown3054(56, 120)
        Unknown3054(57, 80)
        Unknown3054(58, 40)
        Unknown3032()

        def upon_48():
            Unknown23030('KusariIdling', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_3():
            if SLOT_51:
                Unknown1108(-180000)
            if SLOT_2:
                Unknown4055(0)
                Unknown4049(500)
                Unknown4045('hzef_antiairchain', -1)
                Unknown4054(5)
                Unknown4045('hzef_exheadmoveopt', -1)

        def upon_43():
            if (SLOT_48 == 503):
                sendToLabel(0)
    sprite('vr_chain_tip03aa', 1)
    Unknown23015(1)
    Unknown23143(60000, 60000, 70)
    Unknown3029(1)
    Unknown23030('KusariParam', 0, 0, 0, 7770, 0, 0, 0, 0)
    Unknown23030('KusariParam', 0, 1, 0, 16, 0, 0, 0, 10)
    Unknown23030('KusariParam', 0, 2, 0, 33, 0, 0, 0, 10)
    Unknown23030('KusariParam', 0, 3, 0, 50, 0, 0, 0, 10)
    Unknown23030('KusariParam', 0, 4, 0, 66, 0, 0, 0, 10)
    Unknown23030('KusariParam', 0, 5, 0, 83, 0, 0, 0, 10)
    Unknown23030('KusariParam', 0, 6, 0, 7771, 0, 0, 0, 0)
    Unknown23030('KusariFirstPosition', 0, 0, 0, 0, 0, 0, 0, 0)
    GFX_0('ExPortalSp', -1)
    Unknown36(1)
    Unknown1072(-40000)
    Unknown35()
    Unknown1072(-30000)
    sprite('vr_chain_tip03aa', 9)
    Unknown2037(1)
    Unknown23030('KusariSpeed', 0, 3000, 0, 0, 0, 0, 0, 0)
    sprite('vr_chain_tip04', 10)
    Unknown2037(0)
    SLOT_51 = 1
    Unknown3029(0)
    Unknown21015('ExPortalSp', 504, 0)
    Unknown23143(-60000, -45000, 20)
    Unknown1074(-1000)
    Unknown3032()
    Unknown3004(-5)
    sprite('vr_chain_tip04', 10)
    Unknown23015(5)
    sprite('vr_chain_tip04', 6)
    Unknown23143(100000, -50000, 25)
    sprite('vr_chain_tip04', 8)
    Unknown23015(0)
    Unknown23143(-100000, 60000, 25)
    Unknown2019(-500)
    Unknown1074(0)
    Unknown1072(30000)
    Unknown3004(-10)
    sprite('vr_chain_tip04', 1)
    Unknown14()
    loopRest()
    label(0)
    sprite('vr_chain_tip04ex01', 6)
    Unknown2037(0)
    Unknown21015('ExPortalSp', 504, 0)
    Unknown23143(-10000, -5000, 20)
    sprite('vr_chain_tip04ex01', 6)
    SLOT_51 = 1
    Unknown23143(-20000, 10000, 20)
    sprite('vr_chain_tip04ex01', 10)
    Unknown23143(-120000, -60000, 20)
    sprite('vr_chain_tip04ex01', 5)
    Unknown23143(0, 0, 20)
    sprite('vr_chain_tip04ex01', 30)
    Unknown23143(0, 0, 0)
    Unknown23144('03000000000000006d0000000000000000000000000000000000000000000000500000000000000003000000')

@State
def ExBodyAuraAntiAir():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown23015(5)
        Unknown3033()
        Unknown1096(0)
        Unknown3026(-939493356)
        teleportRelativeX(20000)
        Unknown1007(200000)
    sprite('vref_env', 10)
    Unknown1099(1200)
    sprite('vref_env', 30)
    Unknown1099(100)
    Unknown3004(-20)

@State
def AntiAirWindSmoke():

    def upon_IMMEDIATE():
        Unknown4003('hzef_windsmoke.DIG', 'hzef_windsmoke_motion_000.mmot')
        Unknown2054(1)
        Unknown3033()
        sendToLabelUpon(56, 99)

        def upon_43():
            if (SLOT_48 == 501):
                sendToLabel(0)
            if (SLOT_48 == 502):
                sendToLabel(99)
        Unknown1007(120000)
        Unknown3001(160)
    sprite('null', 32767)
    GFX_0('AntiAirWindSmokeOpt', -1)
    loopRest()
    label(0)
    sprite('null', 32767)
    Unknown1099(10)
    Unknown21015('AntiAirWindSmokeOpt', 501, 0)
    loopRest()
    loopRest()
    label(99)
    Unknown21015('AntiAirWindSmokeOpt', 502, 0)
    sprite('null', 10)
    Unknown1059(100)
    Unknown1067(-20)
    Unknown1091(100)
    Unknown3001(100)
    Unknown3004(-10)

@State
def AntiAirWindSmokeOpt():

    def upon_IMMEDIATE():
        Unknown4003('hzef_windsmoke.DIG', 'hzef_windsmoke_motion_000.mmot')
        Unknown2054(1)
        Unknown3033()
        sendToLabelUpon(56, 99)
        Unknown1072(-180000)
        Unknown1096(1250)
        Unknown1065(-500)
        Unknown3001(120)

        def upon_43():
            if (SLOT_48 == 501):
                sendToLabel(0)
            if (SLOT_48 == 502):
                sendToLabel(99)
    sprite('null', 32767)
    loopRest()
    label(0)
    sprite('null', 32767)
    Unknown1099(10)
    loopRest()
    label(99)
    sprite('null', 10)
    Unknown1059(100)
    Unknown1067(-20)
    Unknown1091(100)
    Unknown3001(100)
    Unknown3004(-10)

@State
def BasicDriveWindSmoke():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4006(2)
        Unknown4009(2)
    sprite('null', 1)
    Unknown4055(0)
    Unknown4054(5)
    Unknown4045('hzef_exheadmove', -1)

@State
def Kusari():

    def upon_IMMEDIATE():
        Unknown2053(1)
        Unknown23013(1)
        Unknown2015(10)
        Unknown2055(240)
        Unknown4009(3)

        def upon_31():
            Unknown23030('KusariDraw', 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown23030('KusariKansetsu', 0, 7, 0, 0, 0, 0, 0, 0)
        Unknown23015(8)
        Unknown23030('KusariRenderStage', 0, 7, 0, 6, 0, 0, 0, 0)

        def upon_48():
            Unknown23030('KusariIdling', 0, 0, 0, 0, 0, 0, 0, 0)
        SLOT_54 = 1

        def upon_3():
            if SLOT_51:
                Unknown23030('KusariAngleByChain', 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_IsInOverdrive2:
                Unknown1108(0)
            Unknown48(25, 2, 52, 3, 2, 54)
            if (not SLOT_52):
                if (not SLOT_53):
                    Unknown13(25)
            if SLOT_56:
                GFX_0('BasicDriveWindSmoke', -1)
                Unknown4054(2)
                Unknown4045('hzef_exheadmoveopt', -1)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown23029(3, 206, 0)

        def upon_55():
            if (SLOT_18 > 3):
                clearUponHandler(55)
                Unknown23029(3, 206, 0)

        def upon_43():
            if (SLOT_48 == 0):
                Unknown2037(0)
                Unknown23143(10000, 0, 70)
                Unknown1108(0)
                GFX_0('ExPortal', -1)
                Unknown48(1, 2, 1, 25, 2, 1)
                SLOT_57 = 109
            if (SLOT_48 == 1):
                Unknown2037(1)
                Unknown23143(9000, 5000, 70)
                Unknown1108(0)
                GFX_0('ExPortal', -1)
                Unknown48(1, 2, 1, 25, 2, 1)
                SLOT_57 = 109
            if (SLOT_48 == 2):
                Unknown2037(2)
                Unknown23143(5000, 9000, 70)
                Unknown1108(0)
                GFX_0('ExPortal', -1)
                Unknown48(1, 2, 1, 25, 2, 1)
                SLOT_57 = 109
            if (SLOT_48 == 3):
                Unknown2037(3)
                Unknown23143(0, 10000, 70)
                Unknown1108(0)
                GFX_0('ExPortal', -1)
                Unknown48(1, 2, 1, 25, 2, 1)
                SLOT_57 = 109
            if (SLOT_48 == 4):
                Unknown2037(4)
                Unknown23143(10000, 0, 70)
                Unknown1108(0)
                GFX_0('ExPortal', -1)
                Unknown48(1, 2, 1, 25, 2, 1)
                SLOT_57 = 0
                Unknown23030('KusariMochite', 0, 0, 0, 0, 0, 0, 0, 0)
            if (SLOT_48 == 5):
                Unknown2037(5)
                Unknown23143(9000, 5000, 70)
                Unknown1108(0)
                GFX_0('ExPortal', -1)
                Unknown48(1, 2, 1, 25, 2, 1)
                SLOT_57 = 1
                Unknown23030('KusariMochite', 0, 1, 0, 0, 0, 0, 0, 0)
            if (SLOT_48 == 6):
                Unknown2037(6)
                Unknown23143(9000, -5000, 70)
                Unknown1108(0)
                GFX_0('ExPortal', -1)
                Unknown48(1, 2, 1, 25, 2, 1)
                SLOT_57 = 2
                Unknown23030('KusariMochite', 0, 2, 0, 0, 0, 0, 0, 0)
            if (SLOT_48 == 7):
                Unknown2037(7)
                Unknown23143(5000, -9000, 70)
                Unknown1108(0)
                GFX_0('ExPortal', -1)
                Unknown48(1, 2, 1, 25, 2, 1)
                SLOT_57 = 3
                Unknown23030('KusariMochite', 0, 3, 0, 0, 0, 0, 0, 0)
            if (SLOT_48 == 8):
                Unknown2037(8)
                Unknown23143(0, -10000, 70)
                Unknown1108(0)
                GFX_0('ExPortal', -1)
                Unknown48(1, 2, 1, 25, 2, 1)
                SLOT_57 = 4
                Unknown23030('KusariMochite', 0, 4, 0, 0, 0, 0, 0, 0)
            if (SLOT_48 == 201):
                sendToLabel(0)
            if (SLOT_48 == 202):
                sendToLabel(1)
            if (SLOT_48 == 203):
                Unknown3029(0)
            if (SLOT_48 == 204):
                Unknown23015(11)
                Unknown23030('KusariRenderStage', 0, 12, 0, 13, 0, 0, 0, 0)
            if (SLOT_48 == 205):
                Unknown1084(1)
                Unknown23143(0, 0, 0)
                sendToLabel(1)
        Unknown3053(1)
        Unknown3054(56, 120)
        Unknown3054(57, 80)
        Unknown3054(58, 40)
        Unknown2019(500)
        Unknown3032()
    sprite('vr_chain_tip04', 1)
    SFX_3('hzse_04')
    Unknown23030('KusariParam', 0, 0, 0, 7770, 0, 0, 0, 0)
    Unknown23030('KusariParam', 0, 1, 0, 16, 0, 0, 0, 10)
    Unknown23030('KusariParam', 0, 2, 0, 33, 0, 0, 0, 10)
    Unknown23030('KusariParam', 0, 3, 0, 50, 0, 0, 0, 10)
    Unknown23030('KusariParam', 0, 4, 0, 66, 0, 0, 0, 10)
    Unknown23030('KusariParam', 0, 5, 0, 83, 0, 0, 0, 10)
    Unknown23030('KusariParam', 0, 6, 0, 7771, 0, 0, 0, 0)
    Unknown23030('KusariSpeed', 0, 3000, 0, 0, 0, 0, 0, 0)
    Unknown23030('KusariFirstPosition', 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('vr_chain_tip04', 3)
    SFX_3('hzse_02')
    Unknown23030('KusariFirstPosition', 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('vr_chain_tip03', 32767)
    Unknown3029(1)
    AfterimageColor_1(200, 255, 255, 255)
    AfterimageColor_2(0, 255, 255, 255)
    if (SLOT_2 == 0):
        Unknown23143(60000, 0, 70)
    if (SLOT_2 == 1):
        Unknown23143(54000, 30000, 70)
    if (SLOT_2 == 2):
        Unknown23143(30000, 54000, 70)
    if (SLOT_2 == 3):
        Unknown23143(0, 60000, 70)
    if (SLOT_2 == 4):
        Unknown23143(60000, 0, 70)
    if (SLOT_2 == 5):
        Unknown23143(54000, 30000, 70)
    if (SLOT_2 == 6):
        Unknown23143(54000, -30000, 70)
    if (SLOT_2 == 7):
        Unknown23143(30000, -54000, 70)
    if (SLOT_2 == 8):
        Unknown23143(0, -60000, 70)
    SLOT_56 = 1
    loopRest()
    label(0)
    sprite('vr_chain_tip04', 8)
    SLOT_56 = 0
    SLOT_51 = 1
    SLOT_54 = 0
    Unknown3004(-5)
    Unknown23143(0, 0, 0)
    Unknown23144('0300000002000000390000000000000000000000000000000000000000000000500000000000000003000000')
    Unknown3029(0)
    Unknown21015('ExPortal', 207, 0)
    GFX_0('ExHeadStop', -1)
    sprite('vr_chain_tip04', 14)
    Unknown3004(-25)
    loopRest()
    ExitState()
    label(1)
    sprite('vr_chain_tip04', 32767)
    SFX_3('hzse_13')
    SLOT_56 = 0
    Unknown23143(0, 0, 0)
    Unknown1084(1)
    Unknown3029(0)
    GFX_0('ExHeadLock', -1)
    GFX_0('yugami_ring', -1)
    SLOT_51 = 0
    SLOT_54 = 0
    loopRest()
    ExitState()
    label(10)
    sprite('null', 1)
    clearUponHandler(31)
    SLOT_56 = 0
    SLOT_51 = 1
    SLOT_54 = 0
    Unknown21015('ExPortal', 207, 0)

@State
def ExPortal():

    def upon_IMMEDIATE():
        Unknown4054(0)
        Unknown23067('hzef_exportal')
        Unknown4010(2)
        Unknown4009(3)
        Unknown4007(3)
        Unknown4011(3)

        def upon_43():
            if (SLOT_48 == 207):
                sendToLabel(99)
        Unknown2055(180)
    sprite('vrexdmy', 1)
    sprite('vrexdmy', 32767)
    GFX_0('ExPortalParts', -1)
    GFX_0('ExPortalPartsOpt', 0)
    GFX_0('ExPortalPartsOpt', 1)
    GFX_0('ExPortalPartsOpt', 2)
    label(99)
    sprite('null', 20)
    clearUponHandler(43)
    Unknown21015('ExPortalParts', 207, 0)
    Unknown21015('ExPortalPartsOpt', 207, 0)
    Unknown3032()
    Unknown3001(200)
    Unknown1099(-50)

@State
def ExPortalParts():

    def upon_IMMEDIATE():
        Unknown4054(1)
        Unknown23067('hzef_exportalparts')
        Unknown4007(2)
        Unknown4006(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4011(3)
        teleportRelativeX(8000)
        Unknown3033()
        Unknown3001(255)

        def upon_43():
            if (SLOT_48 == 207):
                sendToLabel(99)
        Unknown2055(180)
    sprite('null', 10)
    Unknown3004(-10)
    Unknown1096(0)
    Unknown1099(80)
    sprite('null', 32767)
    Unknown3004(0)
    Unknown1099(5)
    label(99)
    sprite('null', 10)
    Unknown4007(0)
    Unknown3001(50)
    Unknown3004(-5)
    Unknown1099(100)

@State
def ExPortalPartsOpt():

    def upon_IMMEDIATE():
        Unknown4046(-256, -256, -256)
        Unknown4054(1)
        Unknown23067('hzef_exportalopt')
        Unknown4007(2)
        Unknown4006(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4011(3)
        teleportRelativeX(8000)
        Unknown3033()
        Unknown3001(255)

        def upon_43():
            if (SLOT_48 == 207):
                sendToLabel(99)
        Unknown2055(180)
    sprite('null', 10)
    Unknown1096(0)
    Unknown1099(60)
    sprite('null', 32767)
    Unknown1099(-3)
    label(99)
    sprite('null', 15)
    Unknown4007(0)
    Unknown3001(150)
    Unknown3004(-10)
    Unknown1099(100)

@State
def ExPortalSp():

    def upon_IMMEDIATE():
        Unknown4054(0)
        Unknown23067('hzef_exportal')
        Unknown4010(2)
        Unknown4009(3)
        Unknown4007(3)
        Unknown4011(3)
        Unknown1096(2000)

        def upon_43():
            if (SLOT_48 == 504):
                sendToLabel(99)
    sprite('vrexdmy', 1)
    sprite('vrexdmy', 32767)
    GFX_0('ExPortalPartsSp', -1)
    GFX_0('ExPortalPartsOptSp', 0)
    GFX_0('ExPortalPartsOptSp', 1)
    GFX_0('ExPortalPartsOptSp', 2)
    Unknown3032()
    Unknown3001(200)
    Unknown3004(-10)
    label(99)
    sprite('null', 20)
    clearUponHandler(43)
    Unknown21015('ExPortalPartsSp', 504, 0)
    Unknown21015('ExPortalPartsOptSp', 504, 0)
    Unknown1099(-200)

@State
def ExPortalPartsSp():

    def upon_IMMEDIATE():
        Unknown4054(1)
        Unknown4046(-256, -256, -256)
        Unknown23067('hzef_exportalparts')
        Unknown4007(2)
        Unknown4006(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4011(3)
        teleportRelativeX(8000)
        Unknown3033()
        Unknown3001(255)

        def upon_43():
            if (SLOT_48 == 504):
                sendToLabel(99)
    sprite('null', 10)
    Unknown3004(-10)
    Unknown1096(0)
    Unknown1099(160)
    sprite('null', 32767)
    Unknown3004(0)
    Unknown1099(5)
    label(99)
    sprite('null', 10)
    Unknown4007(0)
    Unknown3001(50)
    Unknown3004(-5)
    Unknown1099(100)

@State
def ExPortalPartsOptSp():

    def upon_IMMEDIATE():
        Unknown4046(-256, -256, -256)
        Unknown4054(1)
        Unknown23067('hzef_exportalopt')
        Unknown4007(2)
        Unknown4006(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4011(3)
        teleportRelativeX(8000)
        Unknown3033()
        Unknown3001(255)

        def upon_43():
            if (SLOT_48 == 504):
                sendToLabel(99)
    sprite('null', 10)
    Unknown1096(0)
    Unknown1099(60)
    sprite('null', 32767)
    Unknown1099(-3)
    label(99)
    sprite('null', 15)
    Unknown4007(0)
    Unknown3001(150)
    Unknown3004(-10)
    Unknown1099(100)

@State
def ExHeadMove():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4006(2)
        Unknown4009(2)
        sendToLabelUpon(32, 99)
    label(0)
    sprite('null', 1)
    Unknown4055(0)
    Unknown4045('hzef_exheadmove', -1)
    Unknown4054(2)
    Unknown4045('hzef_exheadmoveopt', -1)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('null', 1)
    clearUponHandler(32)

@State
def ExHeadStop():

    def upon_IMMEDIATE():
        GFX_2('hzef_exheadstop')
        Unknown1096(500)
    sprite('null', 5)
    Unknown1099(100)
    sprite('null', 10)
    Unknown3033()
    Unknown3001(100)
    Unknown3004(-10)
    Unknown1099(0)

@State
def ExHeadLock():

    def upon_IMMEDIATE():
        GFX_2('hzef_exheadlock')
        Unknown1096(500)
    sprite('null', 5)
    Unknown1099(100)
    sprite('null', 10)
    Unknown3033()
    Unknown3001(100)
    Unknown3004(-10)
    Unknown1099(0)

@State
def yugami_ring():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown21010(1)
        Unknown1096(2000)
    sprite('vr_yugami', 5)
    Unknown1099(50)
    Unknown3057(1)
    Unknown3058(32000)
    sprite('vr_yugami', 10)
    Unknown1099(100)
    Unknown3059(-3200)

@State
def MoveTest():
    sprite('vr_chain_tip03', 60)
    Unknown1072(20000)
    Unknown4055(0)
    Unknown4045('hzef_exheadmove', -1)
    sprite('vr_chain_tip03', 60)
    Unknown1072(30000)
    Unknown4055(0)
    Unknown4045('hzef_exheadmove', -1)
    sprite('vr_chain_tip03', 60)
    Unknown1072(60000)
    Unknown4055(0)
    Unknown4045('hzef_exheadmove', -1)
    sprite('vr_chain_tip03', 10)
    Unknown23143(40000, 40000, 70)
    Unknown1007(400000)
    Unknown3029(1)
    Unknown1072(180000)
    Unknown4055(0)
    Unknown4045('hzef_exheadmove', -1)
    sprite('vr_chain_tip03', 14)
    Unknown23143(-60000, -45000, 20)
    Unknown1072(270000)
    Unknown4055(0)
    Unknown4045('hzef_exheadmove', -1)
    sprite('vr_chain_tip03', 9)
    Unknown23143(90000, -45000, 15)
    Unknown1072(90000)
    Unknown4055(0)
    Unknown4045('hzef_exheadmove', -1)
    sprite('vr_chain_tip03', 9)
    Unknown23143(-60000, 80000, 15)
    sprite('vr_chain_tip03', 14)
    Unknown23143(60000, -100000, 6)

@State
def KusariTest():

    def upon_IMMEDIATE():
        Unknown4008(3)

        def upon_31():
            Unknown23030('KusariDraw', 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown23030('KusariKansetsu', 0, 7, 0, 0, 0, 0, 0, 0)

        def upon_3():
            Unknown23030('KusariIdling', 0, 0, 0, 0, 0, 0, 0, 0)
            if CheckInput(0x93):
                Unknown1021(800)
            if CheckInput(0x45):
                Unknown1021(-800)
            if CheckInput(0x5f):
                Unknown1015(-800)
            if CheckInput(0x79):
                Unknown1015(800)
            if CheckInput(0xa):
                physicsXImpulse(0)
                physicsYImpulse(0)
            Unknown1019(99)
            YAccel(99)
            Unknown23030('KusariAngleByChain', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_5():
            YAccel(-100)
        teleportRelativeX(600000)
        Unknown1007(300000)
    sprite('vr_chain_tip03', 60)
    Unknown23030('KusariParam', 0, 0, 0, 7770, 0, 10, 0, 0)
    Unknown23030('KusariParam', 0, 1, 0, 16, 0, -20, 0, 0)
    Unknown23030('KusariParam', 0, 2, 0, 33, 0, 20, 0, 0)
    Unknown23030('KusariParam', 0, 3, 0, 50, 0, -20, 0, 0)
    Unknown23030('KusariParam', 0, 4, 0, 66, 0, 20, 0, 0)
    Unknown23030('KusariParam', 0, 5, 0, 83, 0, -20, 0, 0)
    Unknown23030('KusariParam', 0, 6, 0, 7771, 0, 10, 0, 10)
    Unknown23030('KusariSpeed', 0, 60, 0, 0, 0, 0, 0, 0)
    Unknown23030('KusariFirstPosition', 0, 60, 0, 0, 0, 0, 0, 0)
    loopRest()
    label(0)
    sprite('vr_chain_tip03', 60)
    Unknown23030('KusariParam', 0, 0, 0, 7770, 0, 10, 0, 0)
    Unknown23030('KusariParam', 0, 1, 0, 16, 0, 20, 0, 0)
    Unknown23030('KusariParam', 0, 2, 0, 33, 0, -20, 0, 0)
    Unknown23030('KusariParam', 0, 3, 0, 50, 0, 20, 0, 0)
    Unknown23030('KusariParam', 0, 4, 0, 66, 0, -20, 0, 0)
    Unknown23030('KusariParam', 0, 5, 0, 83, 0, 20, 0, 0)
    Unknown23030('KusariParam', 0, 6, 0, 7771, 0, 10, 0, 10)
    Unknown23030('KusariSpeed', 0, 60, 0, 0, 0, 0, 0, 0)
    sprite('vr_chain_tip03', 60)
    Unknown23030('KusariParam', 0, 0, 0, 7770, 0, 10, 0, 0)
    Unknown23030('KusariParam', 0, 1, 0, 16, 0, -20, 0, 0)
    Unknown23030('KusariParam', 0, 2, 0, 33, 0, 20, 0, 0)
    Unknown23030('KusariParam', 0, 3, 0, 50, 0, -20, 0, 0)
    Unknown23030('KusariParam', 0, 4, 0, 66, 0, 20, 0, 0)
    Unknown23030('KusariParam', 0, 5, 0, 83, 0, -20, 0, 0)
    Unknown23030('KusariParam', 0, 6, 0, 7771, 0, 10, 0, 10)
    Unknown23030('KusariSpeed', 0, 60, 0, 0, 0, 0, 0, 0)
    sprite('vr_chain_tip03', 60)
    Unknown23030('KusariParam', 0, 0, 0, 7770, 0, 10, 0, 0)
    Unknown23030('KusariParam', 0, 1, 0, 16, 0, 20, 0, 0)
    Unknown23030('KusariParam', 0, 2, 0, 33, 0, -20, 0, 0)
    Unknown23030('KusariParam', 0, 3, 0, 50, 0, 20, 0, 0)
    Unknown23030('KusariParam', 0, 4, 0, 66, 0, -20, 0, 0)
    Unknown23030('KusariParam', 0, 5, 0, 83, 0, 20, 0, 0)
    Unknown23030('KusariParam', 0, 6, 0, 7771, 0, 10, 0, 10)
    Unknown23030('KusariSpeed', 0, 60, 0, 0, 0, 0, 0, 0)
    sprite('vr_chain_tip03', 60)
    Unknown4055(0)
    Unknown4045('hzef_exheadmove', -1)
    Unknown23030('KusariParam', 0, 0, 0, 7770, 0, 10, 0, 0)
    Unknown23030('KusariParam', 0, 1, 0, -10, 0, 10, 0, 0)
    Unknown23030('KusariParam', 0, 2, 0, -20, 0, 50, 0, 0)
    Unknown23030('KusariParam', 0, 3, 0, -10, 0, 55, 0, 0)
    Unknown23030('KusariParam', 0, 4, 0, 0, 0, 50, 0, 0)
    Unknown23030('KusariParam', 0, 5, 0, 10, 0, 45, 0, 0)
    Unknown23030('KusariParam', 0, 6, 0, 7771, 0, 10, 0, 10)
    Unknown23030('KusariSpeed', 0, 60, 0, 0, 0, 0, 0, 0)
    sprite('vr_chain_tip03', 60)
    Unknown23030('KusariParam', 0, 0, 0, 7770, 0, 10, 0, 0)
    Unknown23030('KusariParam', 0, 1, 0, 90, 0, -45, 0, 0)
    Unknown23030('KusariParam', 0, 2, 0, 100, 0, -50, 0, 0)
    Unknown23030('KusariParam', 0, 3, 0, 110, 0, -55, 0, 0)
    Unknown23030('KusariParam', 0, 4, 0, 120, 0, -50, 0, 0)
    Unknown23030('KusariParam', 0, 5, 0, 110, 0, -10, 0, 0)
    Unknown23030('KusariParam', 0, 6, 0, 7771, 0, 10, 0, 10)
    Unknown23030('KusariSpeed', 0, 60, 0, 0, 0, 0, 0, 0)
    sprite('vr_chain_tip03', 60)
    Unknown23030('KusariParam', 0, 0, 0, 7770, 0, 10, 0, 0)
    Unknown23030('KusariParam', 0, 1, 0, -10, 0, 10, 0, 0)
    Unknown23030('KusariParam', 0, 2, 0, -20, 0, 50, 0, 0)
    Unknown23030('KusariParam', 0, 3, 0, -10, 0, 55, 0, 0)
    Unknown23030('KusariParam', 0, 4, 0, 0, 0, 50, 0, 0)
    Unknown23030('KusariParam', 0, 5, 0, 10, 0, 45, 0, 0)
    Unknown23030('KusariParam', 0, 6, 0, 7771, 0, 10, 0, 10)
    Unknown23030('KusariSpeed', 0, 60, 0, 0, 0, 0, 0, 0)
    sprite('vr_chain_tip03', 60)
    Unknown23030('KusariParam', 0, 0, 0, 7770, 0, 10, 0, 0)
    Unknown23030('KusariParam', 0, 1, 0, 90, 0, -45, 0, 0)
    Unknown23030('KusariParam', 0, 2, 0, 100, 0, -50, 0, 0)
    Unknown23030('KusariParam', 0, 3, 0, 110, 0, -55, 0, 0)
    Unknown23030('KusariParam', 0, 4, 0, 120, 0, -50, 0, 0)
    Unknown23030('KusariParam', 0, 5, 0, 110, 0, -10, 0, 0)
    Unknown23030('KusariParam', 0, 6, 0, 7771, 0, 10, 0, 10)
    Unknown23030('KusariSpeed', 0, 60, 0, 0, 0, 0, 0, 0)
    loopRest()
    gotoLabel(0)

@State
def ExBodyAura():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown23015(5)
        Unknown3033()
        Unknown1096(0)
        Unknown3026(-939493356)
        teleportRelativeX(20000)
        Unknown1007(200000)
        sendToLabelUpon(44, 99)

        def upon_43():
            if (SLOT_48 == 301):
                sendToLabel(99)
        Unknown2055(160)
    sprite('vref_env', 10)
    Unknown1099(600)
    sprite('vref_env', 40)
    Unknown1099(0)
    label(99)
    sprite('vref_env', 14)
    clearUponHandler(43)
    clearUponHandler(44)
    Unknown4010(0)
    Unknown4007(0)
    Unknown1099(-100)
    Unknown3004(-20)

@State
def EffKnifeSignal():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown2054(1)
    sprite('null', 10)
    Unknown3038(1)
    GFX_2('hzef_knifesignal')
    GFX_1('hzef_knifesignalopt', -1)
    Unknown1096(900)
    Unknown1077(-90000, 90000)

@State
def Eff5CZanzo():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3033()
        Unknown4061(2)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3041(255)
        Unknown3042(1)
        Unknown3043(254)
        Unknown3044(1)
        teleportRelativeX(48000)
        Unknown1007(260000)
        Unknown3026(-1)
        Unknown3025(16711935, 14)
    sprite('vrhzef202_00', 1)
    sprite('vrhzef202_00', 1)
    GFX_0('Eff5CZanzo2nd', -1)
    sprite('vrhzef202_01', 12)
    Unknown3002(-100)

@State
def Eff5CZanzo2nd():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3033()
        Unknown4061(2)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3041(255)
        Unknown3042(1)
        Unknown3043(254)
        Unknown3044(1)
        Unknown1007(-20000)
        Unknown3026(-1)
        Unknown3025(16711935, 14)
    sprite('vrhzef202_02', 2)
    sprite('vrhzef202_03', 12)
    Unknown3002(-100)

@State
def ShotKnife():
    sprite('null', 2)
    teleportRelativeX(-30000)
    sprite('null', 2)
    GFX_0('ShotKnifeObj', -1)
    Unknown1010(-16000, -32000)
    sprite('null', 1)
    GFX_0('ShotKnifeObj', -1)
    Unknown1010(-16000, -32000)

@State
def ShotKnifeObj():

    def upon_IMMEDIATE():
        Unknown4009(3)
        Unknown3032()
        Unknown3029(1)
        physicsXImpulse(40000)
        physicsYImpulse(-40000)
        Unknown1019(150)
        YAccel(150)
        sendToLabelUpon(2, 1)
    sprite('vr_6cknife00', 4)
    sprite('vr_6cknife00', 32767)
    label(1)
    sprite('vr_6cknife01', 15)
    Unknown1084(1)
    teleportRelativeY(0)
    sprite('vr_6cknife01', 15)
    Unknown3004(-15)

@State
def Eff2CZanzo():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3033()
        Unknown4061(2)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3041(255)
        Unknown3042(1)
        Unknown3043(254)
        Unknown3044(1)
        teleportRelativeX(128000)
        Unknown1007(280000)
        Unknown3026(-1)
        Unknown3025(16711935, 18)
    sprite('vrhzef232_00', 2)
    sprite('vrhzef232_01', 16)
    Unknown3002(-100)

@State
def Eff3CZanzo():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3033()
        Unknown4061(2)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3041(255)
        Unknown3042(1)
        Unknown3043(254)
        Unknown3044(1)
        teleportRelativeX(200000)
        Unknown1007(100000)
        Unknown3026(-1)
        Unknown3025(16711935, 10)
    sprite('vrhzef240_00', 2)
    sprite('vrhzef240_01', 8)
    Unknown3002(-100)

@State
def Eff8CZanzo():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown2054(1)
        Unknown3033()
        Unknown4061(2)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3041(255)
        Unknown3042(1)
        Unknown3043(254)
        Unknown3044(1)
        teleportRelativeX(20000)
        Unknown3026(-1)
        Unknown3025(16711935, 8)
    sprite('vrhzef252_00', 2)
    sprite('vrhzef252_01', 6)
    Unknown3002(-100)
    Unknown4007(0)

@State
def Eff8CZanzo_2():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown2054(1)
        Unknown3033()
        Unknown4061(2)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3041(255)
        Unknown3042(1)
        Unknown3043(254)
        Unknown3044(1)
        teleportRelativeX(20000)
        Unknown3026(-1)
        Unknown3025(16711935, 8)
    sprite('vrhzef252_02', 2)
    sprite('vrhzef252_03', 6)
    Unknown3002(-100)
    Unknown4007(0)

@State
def Eff8CZanzo_3():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown2054(1)
        Unknown3033()
        Unknown4061(2)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3041(255)
        Unknown3042(1)
        Unknown3043(254)
        Unknown3044(1)
        teleportRelativeX(20000)
        Unknown3026(-1)
        Unknown3025(16711935, 8)
    sprite('vrhzef252_04', 2)
    sprite('vrhzef252_05', 6)
    Unknown3002(-100)
    Unknown4007(0)

@State
def Eff8CZanzo_4():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown2054(1)
        Unknown3033()
        Unknown4061(2)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3041(255)
        Unknown3042(1)
        Unknown3043(254)
        Unknown3044(1)
        teleportRelativeX(20000)
        Unknown3026(-1)
        Unknown3025(16711935, 8)
    sprite('vrhzef252_06', 2)
    sprite('vrhzef252_07', 6)
    Unknown3002(-100)
    Unknown4007(0)

@State
def Eff8CZanzo_5():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown2054(1)
        Unknown3033()
        Unknown4061(2)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3041(255)
        Unknown3042(1)
        Unknown3043(254)
        Unknown3044(1)
        teleportRelativeX(20000)
        Unknown3026(-1)
        Unknown3025(16711935, 8)
    sprite('vrhzef252_08', 2)
    sprite('vrhzef252_09', 6)
    Unknown3002(-100)
    Unknown4007(0)

@State
def EffAir2CZanzo():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown3033()
        Unknown4061(2)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3041(255)
        Unknown3042(1)
        Unknown3043(254)
        Unknown3044(1)
        teleportRelativeX(28000)
        Unknown1007(-80000)
        Unknown3026(-1)
        Unknown3025(16711935, 17)
    sprite('vrhzef253_00', 4)
    sprite('vrhzef253_01', 15)
    Unknown3002(-100)
    Unknown4007(0)

@State
def HZEF_Aura():

    def upon_IMMEDIATE():
        Unknown4009(3)
        GFX_2('hzef_envaura')
        Unknown3033()
        Unknown1096(800)
        Unknown2055(17)
    sprite('null', 17)
    Unknown3004(-15)

@State
def HZEF_AuraDelete():

    def upon_IMMEDIATE():
        Unknown4009(3)
        Unknown4054(2)
        Unknown4049(600)
        Unknown4045('hzef_deleteaura', -1)
        Unknown1096(600)
        Unknown2055(1)
    sprite('null', 1)

@State
def EffUltimateAssaultBunshinA():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown3029(1)
        Unknown3069(2)
        setInvincible(1)
    sprite('hz430_00', 20)
    physicsXImpulse(32000)
    Unknown3004(-10)

@State
def EffUltimateAssaultBunshinB():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown3029(1)
        Unknown3069(2)
        setInvincible(1)
    sprite('hz430_00', 20)
    physicsXImpulse(-32000)
    Unknown3004(-10)

@State
def EffKamae():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        GFX_2('hzef_kamaeaura')
        sendToLabelUpon(56, 99)

        def upon_43():
            if (SLOT_48 == 102):
                sendToLabel(99)
    sprite('null', 32767)
    loopRest()
    label(99)
    sprite('null', 10)
    Unknown3032()
    Unknown3001(100)
    Unknown3004(-10)
    Unknown1099(100)

@State
def EffKamaeLand():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4054(5)
        Unknown23067('hzef_landaura')
        sendToLabelUpon(56, 99)

        def upon_43():
            if (SLOT_48 == 101):
                sendToLabel(99)
    sprite('null', 10)
    Unknown1099(50)
    sprite('null', 32767)
    Unknown1099(0)
    loopRest()
    label(99)
    sprite('null', 10)
    Unknown3032()
    Unknown3001(100)
    Unknown3004(-10)
    Unknown1099(100)

@State
def EffLandAura():

    def upon_IMMEDIATE():
        Unknown4054(5)
        Unknown23067('hzef_landaura')
    sprite('null', 10)
    Unknown3032()
    Unknown3001(100)
    Unknown3004(-10)
    Unknown1096(1500)
    Unknown1099(200)

@State
def EffAirAura():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    sprite('null', 10)
    Unknown4054(5)
    Unknown23067('hzef_airaura')
    Unknown3032()
    Unknown3001(100)
    Unknown3004(-10)
    Unknown1096(1500)
    Unknown1099(200)

@State
def EffCommandThrowAura():

    def upon_IMMEDIATE():
        GFX_2('hzef_spaura')
    sprite('null', 60)

@State
def EffCommandThrowWind():

    def upon_IMMEDIATE():
        Unknown4054(5)
        Unknown23067('hzef_comthrowwind')
        Unknown1096(1200)
        Unknown1102(-200, 250)
        Unknown3001(150)
    sprite('null', 30)

@State
def EffSamaso():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4009(3)
        Unknown4007(3)
        Unknown4061(1)
        Unknown3032()
    sprite('vrhzef401_00', 2)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    sprite('vrhzef401_01', 2)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    Unknown4007(0)
    sprite('vrhzef401_02', 4)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    sprite('vrhzef401_03', 4)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_Aura', 5)
    GFX_0('HZEF_Aura', 6)
    GFX_0('HZEF_Aura', 7)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    GFX_0('HZEF_AuraDelete', 6)
    GFX_0('HZEF_AuraDelete', 7)
    sprite('vrhzef401_04', 4)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_Aura', 5)
    GFX_0('HZEF_Aura', 6)
    GFX_0('HZEF_Aura', 7)
    GFX_0('HZEF_Aura', 8)
    GFX_0('HZEF_Aura', 9)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    GFX_0('HZEF_AuraDelete', 6)
    GFX_0('HZEF_AuraDelete', 7)
    GFX_0('HZEF_AuraDelete', 8)
    GFX_0('HZEF_AuraDelete', 9)
    sprite('vrhzef401_05', 4)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    sprite('vrhzef401_06', 4)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)

@State
def EffChudan():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4061(1)
        Unknown3032()
        teleportRelativeX(40000)
        Unknown1007(280000)
    sprite('vrhzef402_00', 2)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    Unknown3001(55)
    Unknown3004(25)
    sprite('vrhzef402_01', 2)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    sprite('vrhzef402_02', 4)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    sprite('vrhzef402_03', 4)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_Aura', 5)
    GFX_0('HZEF_Aura', 6)
    GFX_0('HZEF_Aura', 7)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    GFX_0('HZEF_AuraDelete', 6)
    GFX_0('HZEF_AuraDelete', 7)
    sprite('vrhzef402_04', 6)
    Unknown4007(0)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_Aura', 5)
    GFX_0('HZEF_Aura', 6)
    GFX_0('HZEF_Aura', 7)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    GFX_0('HZEF_AuraDelete', 6)
    GFX_0('HZEF_AuraDelete', 7)
    sprite('vrhzef402_05', 4)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    GFX_0('HZEF_AuraDelete', 6)
    GFX_0('HZEF_AuraDelete', 7)
    sprite('vrhzef402_06', 4)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    GFX_0('HZEF_AuraDelete', 6)
    GFX_0('HZEF_AuraDelete', 7)

@State
def EffGedan():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4061(1)
        Unknown3032()
        teleportRelativeX(100000)
        Unknown1007(-16000)
    sprite('vrhzef403_00', 2)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    Unknown3001(55)
    Unknown3004(25)
    sprite('vrhzef403_01', 3)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    sprite('vrhzef403_02', 2)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_Aura', 5)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    sprite('vrhzef403_03', 6)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_Aura', 5)
    GFX_0('HZEF_Aura', 6)
    GFX_0('HZEF_Aura', 7)
    GFX_0('HZEF_Aura', 8)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    GFX_0('HZEF_AuraDelete', 6)
    GFX_0('HZEF_AuraDelete', 7)
    GFX_0('HZEF_AuraDelete', 8)
    sprite('vrhzef403_04', 4)
    Unknown4007(0)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    sprite('vrhzef403_05', 4)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    sprite('vrhzef403_06', 4)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)

@State
def EffUchiOtoshi():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4061(1)
        Unknown3032()
        teleportRelativeX(64000)
        Unknown1007(280000)
    sprite('vrhzef404_00', 4)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    Unknown3001(55)
    Unknown3004(25)
    sprite('vrhzef404_01', 3)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    sprite('vrhzef404_02', 1)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    sprite('vrhzef404_03', 1)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_Aura', 5)
    GFX_0('HZEF_Aura', 6)
    GFX_0('HZEF_Aura', 7)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    GFX_0('HZEF_AuraDelete', 6)
    GFX_0('HZEF_AuraDelete', 7)
    sprite('vrhzef404_04', 4)
    Unknown4007(0)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_Aura', 5)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    sprite('vrhzef404_05', 4)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    sprite('vrhzef404_06', 4)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)

@State
def EffSpKensei():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4061(1)
        Unknown3032()
        teleportRelativeX(220000)
        Unknown1007(210000)
    sprite('vrhzef407_00', 4)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_Aura', 5)
    GFX_0('HZEF_Aura', 6)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    GFX_0('HZEF_AuraDelete', 6)
    Unknown3001(55)
    Unknown3004(25)
    sprite('vrhzef407_01', 3)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_Aura', 5)
    GFX_0('HZEF_Aura', 6)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    GFX_0('HZEF_AuraDelete', 6)
    sprite('vrhzef407_02', 4)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_Aura', 5)
    GFX_0('HZEF_Aura', 6)
    GFX_0('HZEF_Aura', 7)
    GFX_0('HZEF_Aura', 8)
    GFX_0('HZEF_Aura', 9)
    GFX_0('HZEF_Aura', 10)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    GFX_0('HZEF_AuraDelete', 6)
    GFX_0('HZEF_AuraDelete', 7)
    GFX_0('HZEF_AuraDelete', 8)
    GFX_0('HZEF_AuraDelete', 9)
    GFX_0('HZEF_AuraDelete', 10)
    sprite('vrhzef407_03', 4)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_Aura', 5)
    GFX_0('HZEF_Aura', 6)
    GFX_0('HZEF_Aura', 7)
    GFX_0('HZEF_Aura', 8)
    GFX_0('HZEF_Aura', 9)
    GFX_0('HZEF_Aura', 10)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    GFX_0('HZEF_AuraDelete', 6)
    GFX_0('HZEF_AuraDelete', 7)
    GFX_0('HZEF_AuraDelete', 8)
    GFX_0('HZEF_AuraDelete', 9)
    GFX_0('HZEF_AuraDelete', 10)
    sprite('vrhzef407_04', 4)
    Unknown4007(0)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_Aura', 5)
    GFX_0('HZEF_Aura', 6)
    GFX_0('HZEF_Aura', 7)
    GFX_0('HZEF_Aura', 8)
    GFX_0('HZEF_Aura', 9)
    GFX_0('HZEF_Aura', 10)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    GFX_0('HZEF_AuraDelete', 6)
    GFX_0('HZEF_AuraDelete', 7)
    GFX_0('HZEF_AuraDelete', 8)
    GFX_0('HZEF_AuraDelete', 9)
    GFX_0('HZEF_AuraDelete', 10)
    sprite('vrhzef407_05', 4)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    sprite('vrhzef407_06', 4)

@State
def EffSpKensei_PS():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4061(1)
        Unknown3032()
        teleportRelativeX(220000)
        Unknown1007(210000)
        Unknown1096(1300)
    sprite('vrhzef407_00', 4)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_Aura', 5)
    GFX_0('HZEF_Aura', 6)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    GFX_0('HZEF_AuraDelete', 6)
    Unknown3001(55)
    Unknown3004(25)
    sprite('vrhzef407_01', 3)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_Aura', 5)
    GFX_0('HZEF_Aura', 6)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    GFX_0('HZEF_AuraDelete', 6)
    sprite('vrhzef407_02', 4)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_Aura', 5)
    GFX_0('HZEF_Aura', 6)
    GFX_0('HZEF_Aura', 7)
    GFX_0('HZEF_Aura', 8)
    GFX_0('HZEF_Aura', 9)
    GFX_0('HZEF_Aura', 10)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    GFX_0('HZEF_AuraDelete', 6)
    GFX_0('HZEF_AuraDelete', 7)
    GFX_0('HZEF_AuraDelete', 8)
    GFX_0('HZEF_AuraDelete', 9)
    GFX_0('HZEF_AuraDelete', 10)
    sprite('vrhzef407_03', 4)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_Aura', 5)
    GFX_0('HZEF_Aura', 6)
    GFX_0('HZEF_Aura', 7)
    GFX_0('HZEF_Aura', 8)
    GFX_0('HZEF_Aura', 9)
    GFX_0('HZEF_Aura', 10)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    GFX_0('HZEF_AuraDelete', 6)
    GFX_0('HZEF_AuraDelete', 7)
    GFX_0('HZEF_AuraDelete', 8)
    GFX_0('HZEF_AuraDelete', 9)
    GFX_0('HZEF_AuraDelete', 10)
    sprite('vrhzef407_04', 4)
    Unknown4007(0)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_Aura', 5)
    GFX_0('HZEF_Aura', 6)
    GFX_0('HZEF_Aura', 7)
    GFX_0('HZEF_Aura', 8)
    GFX_0('HZEF_Aura', 9)
    GFX_0('HZEF_Aura', 10)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    GFX_0('HZEF_AuraDelete', 6)
    GFX_0('HZEF_AuraDelete', 7)
    GFX_0('HZEF_AuraDelete', 8)
    GFX_0('HZEF_AuraDelete', 9)
    GFX_0('HZEF_AuraDelete', 10)
    sprite('vrhzef407_05', 4)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    sprite('vrhzef407_06', 4)

@State
def Eff410():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown3032()
        Unknown4061(1)
    sprite('vrhzef410_00', 2)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    Unknown3001(55)
    Unknown3004(25)
    sprite('vrhzef410_01', 2)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    sprite('vrhzef410_02', 4)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_Aura', 5)
    GFX_0('HZEF_Aura', 6)
    GFX_0('HZEF_Aura', 7)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    GFX_0('HZEF_AuraDelete', 6)
    GFX_0('HZEF_AuraDelete', 7)
    sprite('vrhzef410_03', 2)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_Aura', 5)
    GFX_0('HZEF_Aura', 6)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    GFX_0('HZEF_AuraDelete', 6)
    sprite('vrhzef410_04', 6)
    Unknown4007(0)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    sprite('vrhzef410_05', 4)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    sprite('vrhzef410_06', 4)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)

@State
def hzef432_bind():

    def upon_IMMEDIATE():
        Unknown4003('hz_432bind.DIG', 'hzef_drainfield_motion_000.mmot')
        Unknown4015()
        Unknown23023()
        Unknown4010(3)
        Unknown23151(22, 103)
        Unknown23144('1600000000000000670000000000000000000000000000000000000000000000320000000000000014000000')

        def upon_43():
            if (SLOT_48 == 1003):
                clearUponHandler(43)
                sendToLabel(1)
    sprite('null', 10)
    Unknown1096(0)
    Unknown3001(0)
    Unknown3004(30)
    Unknown1099(120)
    GFX_0('hzef432_bindaura', 103)
    sprite('null', 10)
    Unknown1099(-20)
    sprite('null', 1)
    Unknown3004(0)
    Unknown1096(875)
    Unknown1099(0)
    label(0)
    sprite('null', 10)
    gotoLabel(0)
    label(1)
    Unknown26('hzef432_bindaura')
    GFX_1('hzef_432bindaura_end', -1)
    sprite('null', 5)
    sprite('null', 10)
    Unknown1099(80)
    Unknown3004(-26)

@State
def hzef432_bindaura():

    def upon_IMMEDIATE():
        Unknown4007(22)
        GFX_2('hzef_432bindaura')
        Unknown2054(1)
        sendToLabelUpon(56, 99)
    sprite('null', 32767)
    loopRest()
    label(99)
    sprite('null', 10)
    Unknown3032()
    Unknown3001(100)
    Unknown3004(-10)
    Unknown1099(100)

@State
def UltimateThrowCamera():

    def upon_IMMEDIATE():
        Unknown20000(1)
        Unknown20003(1)
        Unknown4007(3)
        Unknown4010(3)
        Unknown4011(3)
    sprite('null', 32767)
    teleportRelativeX(100000)

@State
def EffUltimateLockSignal():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown23067('hzef_ultimatelocksignal')
        Unknown4009(3)
        Unknown2055(200)
        if (SLOT_19 > 450000):
            Unknown48(25, 2, 83, 22, 2, 83)
        else:
            teleportRelativeX(450000)
    sprite('null', 16)
    Unknown3033()
    Unknown3001(0)
    Unknown3004(20)
    Unknown1096(80)
    Unknown1099(100)
    sprite('null', 36)
    Unknown1099(5)
    sprite('null', 10)
    Unknown1099(100)
    Unknown3001(100)
    Unknown3004(-10)

@State
def EffUltimateMagicOpt():

    def upon_IMMEDIATE():
        Unknown23067('hzef_eyeloop')
        Unknown2055(60)
        Unknown2054(1)
        Unknown3033()
    sprite('null', 15)
    Unknown3001(255)
    Unknown1096(500)
    Unknown1099(100)
    sprite('null', 30)
    Unknown1099(0)
    sprite('null', 15)
    Unknown3001(100)
    Unknown3004(-10)
    Unknown1099(100)

@State
def UltimateLockMagic():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4003('hzef_lockcircleC.DIG', 'hzef_lockcircleC_motion_000.mmo')
        Unknown4015()
        Unknown2054(1)
        Unknown3033()
        Unknown3001(0)
        Unknown2055(60)
        teleportRelativeY(300000)
        sendToLabelUpon(56, 99)

        def upon_43():
            if (SLOT_48 == 1001):
                sendToLabel(0)
            if (SLOT_48 == 1002):
                sendToLabel(99)
    sprite('null', 12)
    Unknown1096(200)
    Unknown1099(40)
    Unknown3004(20)
    GFX_0('EffUltimateMagicOpt', -1)
    GFX_0('UltimateLockMagicA', -1)
    GFX_0('UltimateLockMagicB', -1)
    GFX_0('UltimateLockMagicC', -1)
    sprite('null', 4)
    Unknown1099(10)
    sprite('null', 32767)
    Unknown3004(0)
    Unknown1099(0)
    loopRest()
    label(0)
    sprite('null', 32767)
    Unknown1099(5)
    Unknown21015('UltimateLockMagicA', 1003, 0)
    Unknown21015('UltimateLockMagicB', 1003, 0)
    Unknown21015('UltimateLockMagicC', 1003, 0)
    loopRest()
    label(99)
    sprite('null', 10)
    GFX_1('hzef_eyespark', -1)
    Unknown1096(1000)
    Unknown1099(500)
    Unknown3001(255)
    Unknown3004(-25)

@State
def UltimateLockMagicA():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4003('hzef_lockcircleC.DIG', 'hzef_lockcircleC_motion_000.mmo')
        Unknown4015()
        Unknown2054(1)
        Unknown3033()
        Unknown3001(0)
        Unknown1096(0)
        Unknown1007(80000)
        sendToLabelUpon(56, 0)

        def upon_43():
            if (SLOT_48 == 1003):
                sendToLabel(0)
    sprite('null', 12)
    Unknown1096(300)
    Unknown1099(50)
    Unknown3001(200)
    sprite('null', 32767)
    Unknown1099(0)
    loopRest()
    label(0)
    sprite('null', 5)
    physicsYImpulse(-16000)
    Unknown3001(50)
    Unknown3004(-10)
    Unknown1099(-5)
    sprite('null', 5)
    Unknown1084(1)

@State
def UltimateLockMagicB():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4003('hzef_lockcircleC.DIG', 'hzef_lockcircleC_motion_000.mmo')
        Unknown4015()
        Unknown2054(1)
        Unknown3033()
        Unknown3001(0)
        Unknown1096(0)
        teleportRelativeX(80000)
        Unknown1007(-60000)
        sendToLabelUpon(56, 0)

        def upon_43():
            if (SLOT_48 == 1003):
                sendToLabel(0)
    sprite('null', 12)
    Unknown1096(300)
    Unknown1099(50)
    Unknown3001(200)
    sprite('null', 32767)
    Unknown1099(0)
    loopRest()
    label(0)
    sprite('null', 5)
    physicsXImpulse(-16000)
    physicsYImpulse(12000)
    Unknown3001(50)
    Unknown3004(-10)
    Unknown1099(-5)
    sprite('null', 20)
    Unknown1084(1)

@State
def UltimateLockMagicC():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4003('hzef_lockcircleC.DIG', 'hzef_lockcircleC_motion_000.mmo')
        Unknown4015()
        Unknown2054(1)
        Unknown3033()
        Unknown3001(0)
        Unknown1096(0)
        teleportRelativeX(-80000)
        Unknown1007(-60000)
        sendToLabelUpon(56, 0)

        def upon_43():
            if (SLOT_48 == 1003):
                sendToLabel(0)
    sprite('null', 12)
    Unknown1096(300)
    Unknown1099(50)
    Unknown3001(200)
    sprite('null', 32767)
    Unknown1099(0)
    loopRest()
    label(0)
    sprite('null', 5)
    physicsXImpulse(16000)
    physicsYImpulse(12000)
    Unknown3001(50)
    Unknown3004(-10)
    Unknown1099(-5)
    sprite('null', 20)
    Unknown1084(1)

@State
def EffUltimateLockPtc():

    def upon_IMMEDIATE():
        Unknown23067('hzef_ultimatelock')
        Unknown4009(3)
        Unknown2055(60)
    sprite('null', 60)
    Unknown1096(1500)

@State
def UltimateLockObj():

    def upon_IMMEDIATE():
        if (SLOT_19 > 450000):
            Unknown48(25, 2, 83, 22, 2, 83)
        else:
            teleportRelativeX(450000)
    sprite('null', 30)
    GFX_0('UltimateLockObjTop', -1)
    GFX_0('UltimateLockObjCenter', -1)
    GFX_0('UltimateLockObjBottom', -1)
    GFX_0('UltimateMagicCircle', -1)
    SFX_3('hzse_07')

@State
def UltimateLockObj_OD():

    def upon_IMMEDIATE():
        if (SLOT_19 > 450000):
            Unknown48(25, 2, 83, 22, 2, 83)
        else:
            teleportRelativeX(450000)
    sprite('null', 30)
    GFX_0('UltimateLockObjTop', -1)
    GFX_0('UltimateLockObjCenter', -1)
    GFX_0('UltimateLockObjBottom', -1)
    GFX_0('UltimateMagicCircle_OD', -1)
    SFX_3('hzse_07')

@State
def UltimateLockObj_DDD():

    def upon_IMMEDIATE():
        if (SLOT_19 > 450000):
            Unknown48(25, 2, 83, 22, 2, 83)
        else:
            teleportRelativeX(450000)
    sprite('null', 30)
    GFX_0('UltimateLockObjTop', -1)
    GFX_0('UltimateLockObjCenter', -1)
    GFX_0('UltimateLockObjBottom', -1)
    GFX_0('UltimateMagicCircle_DDD', -1)
    SFX_3('hzse_07')

@State
def UltimateLockObj_ODDDDD():

    def upon_IMMEDIATE():
        if (SLOT_19 > 450000):
            Unknown48(25, 2, 83, 22, 2, 83)
        else:
            teleportRelativeX(450000)
    sprite('null', 30)
    GFX_0('UltimateLockObjTop', -1)
    GFX_0('UltimateLockObjCenter', -1)
    GFX_0('UltimateLockObjBottom', -1)
    GFX_0('UltimateMagicCircle_ODDDD', -1)
    SFX_3('hzse_07')

@State
def UltimateLockObjCenter():

    def upon_IMMEDIATE():
        Unknown4003('hzef_lockcircleA.DIG', 'hzef_lockcircleA_motion_000.mmo')
        Unknown2054(1)
        Unknown3033()
        Unknown2055(120)
        sendToLabelUpon(17, 99)

        def upon_43():
            if (SLOT_48 == 1003):
                sendToLabel(99)
    sprite('null', 10)
    loopRelated(17, 90)
    Unknown1096(900)
    Unknown1067(10)
    physicsYImpulse(20000)
    setGravity(800)
    sprite('null', 32767)
    physicsYImpulse(0)
    setGravity(0)
    label(99)
    sprite('null', 20)
    Unknown1099(100)
    Unknown3001(200)
    Unknown3004(-10)
    physicsYImpulse(20000)

@State
def UltimateLockObjTop():

    def upon_IMMEDIATE():
        Unknown4003('hzef_lockcircleB.DIG', 'hzef_lockcircleB_motion_000.mmo')
        Unknown2054(1)
        Unknown3033()
        Unknown2055(120)
        sendToLabelUpon(17, 99)

        def upon_43():
            if (SLOT_48 == 1003):
                sendToLabel(99)
    sprite('null', 10)
    loopRelated(17, 90)
    Unknown1096(600)
    physicsYImpulse(32000)
    setGravity(800)
    Unknown1067(10)
    sprite('null', 32767)
    physicsYImpulse(0)
    setGravity(0)
    label(99)
    sprite('null', 20)
    Unknown1099(100)
    Unknown3001(200)
    Unknown3004(-10)
    physicsYImpulse(32000)

@State
def UltimateLockObjBottom():

    def upon_IMMEDIATE():
        Unknown4003('hzef_lockcircleB.DIG', 'hzef_lockcircleB_motion_000.mmo')
        Unknown2054(1)
        Unknown3033()
        Unknown2055(120)
        sendToLabelUpon(17, 99)

        def upon_43():
            if (SLOT_48 == 1003):
                sendToLabel(99)
    sprite('null', 10)
    loopRelated(17, 90)
    Unknown1096(600)
    physicsYImpulse(10000)
    setGravity(800)
    Unknown1067(10)
    sprite('null', 32767)
    physicsYImpulse(0)
    setGravity(0)
    label(99)
    sprite('null', 20)
    Unknown1099(100)
    Unknown3001(200)
    Unknown3004(-10)
    physicsYImpulse(5000)

@State
def UltimateMagicCircle():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown4009(3)
        Unknown4010(3)
        Hitstop(0)
        Damage(500)
        AttackP2(100)
        PushbackX(0)
        Unknown11001(0, 60, 60)
        Unknown11072(1, 0, 0)
        AirHitstunAnimation(4)
        GroundedHitstunAnimation(4)
        Unknown11064(1)
        Unknown2053(1)

        def upon_78():
            Unknown23029(3, 1008, 0)

        def upon_3():
            if Unknown2065(25):
                clearUponHandler(3)
                Unknown23029(3, 1009, 0)
        Unknown3038(1)
        Unknown11069('UltimateKusari')
    sprite('vr_magiccircle00', 2)
    GFX_1('hzef_ultimatelock', -1)

@State
def UltimateMagicCircle_OD():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown4009(3)
        Unknown4010(3)
        Hitstop(0)
        Damage(500)
        AttackP2(100)
        PushbackX(0)
        Unknown11001(0, 60, 60)
        Unknown11072(1, 0, 0)
        AirHitstunAnimation(4)
        GroundedHitstunAnimation(4)
        Unknown11064(1)
        Unknown2053(1)

        def upon_78():
            Unknown23029(3, 1008, 0)

        def upon_3():
            if Unknown2065(25):
                clearUponHandler(3)
                Unknown23029(3, 1009, 0)
        Unknown3038(1)
        Unknown11069('UltimateKusari')
    sprite('vr_magiccircle00', 2)
    GFX_1('hzef_ultimatelock', -1)

@State
def UltimateMagicCircle_DDD():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown4009(3)
        Unknown4010(3)
        Hitstop(0)
        Damage(200)
        AttackP1(100)
        AttackP2(100)
        MinimumDamagePct(100)
        PushbackX(0)
        Unknown11001(0, 60, 60)
        Unknown11072(1, 0, 0)
        AirHitstunAnimation(4)
        GroundedHitstunAnimation(4)
        Unknown11064(1)
        Unknown2053(1)

        def upon_78():
            Unknown23029(3, 1008, 0)

        def upon_3():
            if Unknown2065(25):
                clearUponHandler(3)
                Unknown23029(3, 1009, 0)
        Unknown3038(1)
        Unknown11069('UltimateKusari')
    sprite('vr_magiccircle00', 2)
    GFX_1('hzef_ultimatelock', -1)

@State
def UltimateMagicCircle_ODDDD():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown4009(3)
        Unknown4010(3)
        Hitstop(0)
        Damage(200)
        AttackP1(100)
        AttackP2(100)
        MinimumDamagePct(100)
        PushbackX(0)
        Unknown11001(0, 60, 60)
        Unknown11072(1, 0, 0)
        AirHitstunAnimation(4)
        GroundedHitstunAnimation(4)
        Unknown11064(1)
        Unknown2053(1)

        def upon_78():
            Unknown23029(3, 1008, 0)

        def upon_3():
            if Unknown2065(25):
                clearUponHandler(3)
                Unknown23029(3, 1009, 0)
        Unknown3038(1)
        Unknown11069('UltimateKusari')
    sprite('vr_magiccircle00', 2)
    GFX_1('hzef_ultimatelock', -1)

@State
def EffDDZanzoA():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3033()
        Unknown4061(2)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3041(255)
        Unknown3042(1)
        Unknown3043(254)
        Unknown3044(0)
        teleportRelativeX(220000)
        Unknown1010(120000, -240000)
        Unknown1007(220000)
        Unknown1011(60000, -30000)
        Unknown23015(1)
    sprite('vrhzef431_00', 2)
    sprite('vrhzef431_00', 10)
    Unknown3001(100)
    Unknown3004(-10)

@State
def EffDDZanzoB():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3033()
        Unknown4061(2)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3041(255)
        Unknown3042(1)
        Unknown3043(254)
        Unknown3044(0)
        teleportRelativeX(240000)
        Unknown1010(160000, -160000)
        Unknown1007(240000)
        Unknown1011(60000, -30000)
        Unknown23015(1)
    sprite('vrhzef431_01', 2)
    sprite('vrhzef431_01', 10)
    Unknown3001(100)
    Unknown3004(-10)

@State
def EffDDZanzoC():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3033()
        Unknown4061(2)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3041(255)
        Unknown3042(1)
        Unknown3043(254)
        Unknown3044(0)
        teleportRelativeX(220000)
        Unknown1010(120000, -200000)
        Unknown1007(260000)
        Unknown1011(60000, -30000)
        Unknown23015(1)
    sprite('vrhzef431_02', 2)
    sprite('vrhzef431_02', 10)
    Unknown3001(100)
    Unknown3004(-10)

@State
def EffDDZanzoD():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3033()
        Unknown4061(2)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3041(255)
        Unknown3042(1)
        Unknown3043(254)
        Unknown3044(0)
        teleportRelativeX(200000)
        Unknown1010(200000, -120000)
        Unknown1007(260000)
        Unknown1011(60000, -30000)
        Unknown23015(1)
    sprite('vrhzef431_03', 2)
    sprite('vrhzef431_03', 10)
    Unknown3001(100)
    Unknown3004(-10)

@State
def DDLockAura():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown23015(2)
        Unknown3033()
        Unknown1096(0)
        Unknown3026(-268384156)
        teleportRelativeY(300000)
        sendToLabelUpon(56, 99)

        def upon_43():
            if (SLOT_48 == 1003):
                sendToLabel(99)
    sprite('vref_env', 10)
    Unknown1099(600)
    sprite('vref_env', 32767)
    Unknown1099(0)
    loopRest()
    label(0)
    sprite('vref_env', 32767)
    teleportRelativeX(20000)
    Unknown1007(-100000)
    Unknown1099(200)
    Unknown3025(-923127246, 10)
    loopRest()
    label(99)
    sprite('vref_env', 20)
    clearUponHandler(43)
    clearUponHandler(44)
    Unknown4010(0)
    Unknown4007(0)
    Unknown23131()
    Unknown1099(100)
    Unknown3004(-10)

@State
def DDBodyAura():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown23015(2)
        Unknown3033()
        Unknown1096(0)
        Unknown3026(-16751466)
        teleportRelativeX(20000)
        teleportRelativeY(100000)
        sendToLabelUpon(56, 99)

        def upon_43():
            if (SLOT_48 == 1006):
                sendToLabel(0)
            if (SLOT_48 == 1007):
                sendToLabel(99)
    sprite('vref_env', 10)
    Unknown1099(1000)
    sprite('vref_env', 32767)
    Unknown1099(0)
    loopRest()
    label(0)
    sprite('vref_env', 30)
    Unknown3025(-65536, 30)
    sprite('vref_env', 32767)
    Unknown23131()
    Unknown1099(500)
    loopRest()
    label(99)
    sprite('vref_env', 60)
    clearUponHandler(43)
    clearUponHandler(44)
    Unknown4010(0)
    Unknown4007(0)
    Unknown3025(25800, 60)
    Unknown1099(100)
    Unknown3004(-5)

@State
def HZEF_DDBackAura():

    def upon_IMMEDIATE():
        Unknown4054(5)
        Unknown4010(3)
        Unknown23067('hzef_ultimateaura')
        Unknown3033()
        Unknown1096(1500)
        sendToLabelUpon(56, 99)

        def upon_43():
            if (SLOT_48 == 1003):
                sendToLabel(99)
    sprite('null', 32767)
    GFX_0('HZEF_DDBackAuraFront', -1)
    label(99)
    sprite('null', 20)
    Unknown3001(200)
    Unknown3004(-10)

@State
def HZEF_DDBackAuraFront():

    def upon_IMMEDIATE():
        Unknown4054(1)
        Unknown4010(3)
        Unknown23067('hzef_ultimateaurafront')
        Unknown3033()
        Unknown1096(3000)
        Unknown1007(12000)
        sendToLabelUpon(56, 99)

        def upon_43():
            if (SLOT_48 == 1003):
                sendToLabel(99)
    sprite('null', 32767)
    label(99)
    sprite('null', 20)
    Unknown3001(200)
    Unknown3004(-10)

@State
def EffUltimateSnakeEye():

    def upon_IMMEDIATE():
        Unknown23067('hzef_eyeloop')
        Unknown2055(60)
        Unknown2054(1)
        Unknown3033()
    sprite('null', 3)

@State
def EffDDSnakeFang():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4061(1)
        Unknown3032()

        def upon_56():
            Unknown14()
        teleportRelativeX(120000)
        Unknown1007(260000)
    sprite('vrhzef431atk_00', 20)
    Unknown3001(0)
    Unknown3004(10)
    Unknown4054(1)
    Unknown4045('hzef_snakeeye', 0)
    Unknown4054(1)
    Unknown4045('hzef_snakeeye', 1)
    Unknown4054(1)
    Unknown4045('hzef_snakeeye', 2)
    Unknown4054(1)
    Unknown4045('hzef_snakeeye', 3)
    Unknown4054(1)
    Unknown4045('hzef_snakeeye', 4)
    Unknown4054(1)
    GFX_1('hzef_snakeeye', 5)
    sprite('vrhzef431atk_00', 10)
    sprite('vrhzef431atk_01', 3)
    Unknown21015('HZEF_DDBackAuraFront', 1003, 0)
    Unknown23117(-16764396, 3)
    GFX_0('EffUltimateSnakeEye', 0)
    GFX_0('EffUltimateSnakeEye', 1)
    GFX_0('EffUltimateSnakeEye', 2)
    GFX_0('EffUltimateSnakeEye', 3)
    GFX_0('EffUltimateSnakeEye', 4)
    GFX_0('EffUltimateSnakeEye', 5)
    sprite('vrhzef431atk_02', 3)
    Unknown23117(-16777216, 11)
    sprite('vrhzef431atk_03', 4)
    sprite('vrhzef431atk_04', 4)
    sprite('vrhzef431atk_05', 8)
    Unknown23120()
    Unknown3004(-20)
    physicsXImpulse(5000)
    physicsYImpulse(-2000)

@State
def EffDDSnakeFangOD():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4061(1)
        Unknown3032()

        def upon_56():
            Unknown14()
        teleportRelativeX(120000)
        Unknown1007(260000)
    sprite('vrhzef431atk_00', 5)
    Unknown3001(0)
    Unknown3004(10)
    sprite('vrhzef431atk_00', 15)
    Unknown4054(1)
    Unknown4045('hzef_snakeeye', 0)
    Unknown4054(1)
    Unknown4045('hzef_snakeeye', 1)
    Unknown4054(1)
    Unknown4045('hzef_snakeeye', 2)
    Unknown4054(1)
    Unknown4045('hzef_snakeeye', 3)
    Unknown4054(1)
    Unknown4045('hzef_snakeeye', 4)
    Unknown4054(1)
    GFX_1('hzef_snakeeye', 5)
    sprite('vrhzef431atk_00', 10)
    sprite('vrhzef431atk_01', 3)
    Unknown21015('HZEF_DDBackAuraFront', 1003, 0)
    Unknown23117(-16764396, 3)
    GFX_0('EffUltimateSnakeEye', 0)
    GFX_0('EffUltimateSnakeEye', 1)
    GFX_0('EffUltimateSnakeEye', 2)
    GFX_0('EffUltimateSnakeEye', 3)
    GFX_0('EffUltimateSnakeEye', 4)
    GFX_0('EffUltimateSnakeEye', 5)
    sprite('vrhzef431atk_02', 3)
    Unknown23117(-16777216, 11)
    sprite('vrhzef431atk_03', 4)
    sprite('vrhzef431atk_04', 4)
    sprite('vrhzef431atk_05', 8)
    Unknown23120()
    Unknown3004(-20)
    physicsXImpulse(5000)
    physicsYImpulse(-2000)

@State
def UltimateWindSmoke():

    def upon_IMMEDIATE():
        Unknown4003('hzef_windsmoke.DIG', 'hzef_windsmoke_motion_000.mmot')
        Unknown2054(1)
        Unknown3033()
        sendToLabelUpon(56, 99)

        def upon_43():
            if (SLOT_48 == 1004):
                sendToLabel(0)
            if (SLOT_48 == 1005):
                sendToLabel(99)
        Unknown1007(120000)
        Unknown3001(160)
    sprite('null', 32767)
    GFX_0('UltimateWindSmokeOpt', -1)
    loopRest()
    label(0)
    sprite('null', 32767)
    Unknown1099(10)
    Unknown21015('UltimateWindSmokeOpt', 1004, 0)
    loopRest()
    loopRest()
    label(99)
    Unknown21015('UltimateWindSmokeOpt', 1005, 0)
    sprite('null', 10)
    Unknown1059(100)
    Unknown1067(-20)
    Unknown1091(100)
    Unknown3001(100)
    Unknown3004(-10)

@State
def UltimateWindSmokeOpt():

    def upon_IMMEDIATE():
        Unknown4003('hzef_windsmoke.DIG', 'hzef_windsmoke_motion_000.mmot')
        Unknown2054(1)
        Unknown3033()
        sendToLabelUpon(56, 99)

        def upon_43():
            if (SLOT_48 == 1004):
                sendToLabel(0)
            if (SLOT_48 == 1005):
                sendToLabel(99)
        Unknown1072(-180000)
        Unknown1096(1250)
        Unknown1065(-500)
        Unknown3001(120)
    sprite('null', 32767)
    loopRest()
    label(0)
    sprite('null', 32767)
    Unknown1099(10)
    loopRest()
    label(99)
    sprite('null', 10)
    Unknown1059(100)
    Unknown1067(-20)
    Unknown1091(100)
    Unknown3001(100)
    Unknown3004(-10)

@State
def HZEF_UltimateAssault():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4054(2)
        Unknown23067('hzef_ultimateassault')
        Unknown4009(3)
        Unknown1096(900)
        teleportRelativeX(128000)
        Unknown1007(-160000)

        def upon_56():
            Unknown2055(10)
            Unknown3032()
            Unknown3004(-30)
    sprite('null', 110)

@State
def HZEF_UltimateAssaultOD():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('hzef_odjayoku00', '')
        teleportRelativeX(150000)
        Unknown2054(2)
        Unknown1056(2300)
        Unknown1064(1250)
        Unknown1072(6000)
    sprite('null', 20)
    GFX_2('hzef_odjayoku')
    sprite('null', 10)
    Unknown3004(-26)

@State
def HZEF_DrainField():

    def upon_IMMEDIATE():
        Unknown1007(300000)
        Unknown4003('hzef_drainfield.DIG', 'hzef_drainfield_motion_000.mmot')
        Unknown2054(1)
        Unknown3033()
        Unknown23023()

        def upon_3():
            Unknown23030('BossHazamaDrainField', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_44():
            clearUponHandler(44)
            clearUponHandler(43)
            sendToLabel(2)

        def upon_43():
            if (101 == 0):
                clearUponHandler(44)
                clearUponHandler(43)
                sendToLabel(2)
        Unknown23151(3, 103)
        Unknown23144('0300000000000000670000000000000000000000000000000000000000000000320000000000000014000000')
    sprite('null', 10)
    Unknown1096(0)
    Unknown3001(0)
    Unknown3004(30)
    Unknown1099(120)
    sprite('null', 10)
    Unknown1099(-20)
    sprite('null', 1)
    Unknown3004(0)
    Unknown1096(1000)
    Unknown1099(0)
    label(0)
    sprite('null', 10)
    physicsYImpulse(-300)
    sprite('null', 30)
    physicsYImpulse(-200)
    sprite('null', 30)
    physicsYImpulse(-100)
    sprite('null', 10)
    YAccel(0)
    sprite('null', 10)
    physicsYImpulse(300)
    sprite('null', 30)
    physicsYImpulse(200)
    sprite('null', 30)
    physicsYImpulse(100)
    sprite('null', 10)
    YAccel(0)
    loopRest()
    gotoLabel(0)
    label(2)
    sprite('null', 10)
    Unknown1099(80)
    Unknown3004(-26)

@State
def HZEF_DrainLoop():

    def upon_IMMEDIATE():
        Unknown23151(3, 103)
        GFX_2('hzef_drainloop')
        Unknown3033()
        Unknown23144('0300000000000000670000000000000000000000000000000000000000000000320000000000000014000000')
        Unknown2054(1)
    sprite('null', 120)

@State
def HZEF_DrainEnemy():

    def upon_IMMEDIATE():
        Unknown23151(22, 103)
        GFX_2('hzef_drainenemy')
        Unknown3033()
        Unknown23144('1600000000000000670000000000000000000000000000000000000000000000320000000000000014000000')
        Unknown2054(1)
    sprite('null', 120)

@State
def hzef432():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4009(3)
        Unknown4061(1)
        Unknown3032()
    sprite('vrhzef432_00', 6)
    GFX_1('hzef_432backaura_01', 0)
    sprite('vrhzef432_01', 6)
    GFX_1('hzef_432backaura_01', 0)
    GFX_1('hzef_432backaura_01', 1)
    GFX_1('hzef_432backaura_01', 2)
    sprite('vrhzef432_02', 6)
    GFX_1('hzef_432backaura_01', 0)
    GFX_1('hzef_432backaura_01', 1)
    GFX_1('hzef_432backaura_01', 2)
    GFX_1('hzef_432backaura_01', 3)
    sprite('vrhzef432_03', 6)
    GFX_1('hzef_432backaura_01', 0)
    GFX_1('hzef_432backaura_01', 1)
    GFX_1('hzef_432backaura_01', 2)
    GFX_1('hzef_432backaura_01', 3)
    sprite('vrhzef432_04', 6)
    Unknown23015(11)
    GFX_1('hzef_432backaura_01', 0)
    GFX_1('hzef_432backaura_01', 1)
    GFX_1('hzef_432backaura_01', 2)
    sprite('vrhzef432_05', 6)
    sprite('vrhzef432_06', 3)
    Unknown1096(1100)
    Unknown3001(226)
    sprite('vrhzef432_06', 3)

@State
def HZEF_ASTBACK():

    def upon_IMMEDIATE():
        Unknown4022(2)
        Unknown4054(5)
        Unknown23067('hzef_astback')
        Unknown4009(3)
        Unknown2054(1)
        Unknown3032()
        sendToLabelUpon(32, 0)
        sendToLabelUpon(44, 99)
    sprite('null', 90)
    label(0)
    sprite('null', 30)
    Unknown3004(-9)
    loopRest()
    ExitState()
    label(99)
    sprite('null', 10)
    Unknown3001(100)
    Unknown3004(-10)

@State
def HZEF_ASTMagicCircle():

    def upon_IMMEDIATE():
        Unknown4022(2)
        Unknown4054(2)
        Unknown23067('hzef_aststartcircle')
        Unknown2054(1)
        Unknown3033()
        sendToLabelUpon(44, 99)
    sprite('null', 120)
    Unknown1099(10)
    Unknown3004(-2)
    SFX_0('022_magiccircle_c')
    loopRest()
    ExitState()
    label(99)
    sprite('null', 10)
    Unknown3001(100)
    Unknown3004(-10)

@State
def HZEF_ASTSIGNAL():

    def upon_IMMEDIATE():
        Unknown4054(1)
        Unknown23067('hzef_astsignal')
        Unknown2054(1)
        Unknown3032()
        Unknown1007(280000)
    sprite('null', 70)
    SFX_0('022_magiccircle_c')

@State
def KusariAstral():

    def upon_IMMEDIATE():
        Unknown2012()
        AttackLevel_(5)
        Damage(0)
        AirPushbackX(0)
        YImpluseBeforeWallbounce(-50)
        AirUntechableTime(1200)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        Unknown11072(3, 0, 64000)
        Unknown11069('AstralHeat')
        Unknown4010(3)
        Unknown4009(3)

        def upon_31():
            Unknown23030('KusariDraw', 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown23030('KusariKansetsu', 0, 7, 0, 0, 0, 0, 0, 0)
        Unknown1084(1)
        Unknown3029(1)
        AfterimageColor_1(200, 255, 255, 255)
        AfterimageColor_2(0, 255, 255, 255)
        Unknown3053(1)
        Unknown3054(56, 120)
        Unknown3054(57, 80)
        Unknown3054(58, 40)
        Unknown3032()

        def upon_48():
            Unknown23030('KusariIdling', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_3():
            pass

        def upon_43():
            if (SLOT_48 == 1501):
                Unknown2037(0)
                Unknown2019(-500)
                Unknown23030('KusariMochite', 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown23143(-8000, 60000, 70)
                Unknown1108(0)
                Unknown23015(8)
                Unknown23030('KusariRenderStage', 0, 7, 0, 6, 0, 0, 0, 0)
            if (SLOT_48 == 1502):
                Unknown2037(0)
                Unknown2019(-500)
                Unknown23030('KusariMochite', 0, 1, 0, 0, 0, 0, 0, 0)
                Unknown23143(-9000, 60000, 70)
                Unknown1108(0)
                Unknown23015(8)
                Unknown23030('KusariRenderStage', 0, 7, 0, 6, 0, 0, 0, 0)
            if (SLOT_48 == 1503):
                Unknown2037(0)
                Unknown2019(-500)
                Unknown23030('KusariMochite', 0, 2, 0, 0, 0, 0, 0, 0)
                Unknown23143(-10000, 60000, 70)
                Unknown1108(0)
                Unknown23015(8)
                Unknown23030('KusariRenderStage', 0, 7, 0, 6, 0, 0, 0, 0)
            if (SLOT_48 == 1504):
                Unknown2037(0)
                Unknown2019(-500)
                Unknown23030('KusariMochite', 0, 3, 0, 0, 0, 0, 0, 0)
                Unknown23143(0, 60000, 70)
                Unknown1108(0)
                Unknown23015(8)
                Unknown23030('KusariRenderStage', 0, 7, 0, 6, 0, 0, 0, 0)
            if (SLOT_48 == 1505):
                Unknown2037(0)
                Unknown2019(-500)
                Unknown23030('KusariMochite', 0, 4, 0, 0, 0, 0, 0, 0)
                Unknown23143(3500, 60000, 70)
                Unknown1108(0)
                Unknown23015(8)
                Unknown23030('KusariRenderStage', 0, 7, 0, 6, 0, 0, 0, 0)
            if (SLOT_48 == 1506):
                Unknown2037(1)
                Unknown2019(500)
                Unknown23030('KusariMochite', 0, 5, 0, 0, 0, 0, 0, 0)
                Unknown23143(6500, 60000, 70)
                Unknown1108(0)
                Unknown23015(11)
                Unknown23030('KusariRenderStage', 0, 12, 0, 13, 0, 0, 0, 0)
            if (SLOT_48 == 1507):
                Unknown2037(1)
                Unknown2019(500)
                Unknown23030('KusariMochite', 0, 6, 0, 0, 0, 0, 0, 0)
                Unknown23143(6500, 60000, 70)
                Unknown1108(0)
                Unknown23015(11)
                Unknown23030('KusariRenderStage', 0, 12, 0, 13, 0, 0, 0, 0)
            if (SLOT_48 == 1508):
                Unknown2037(1)
                Unknown2019(500)
                Unknown23030('KusariMochite', 0, 7, 0, 0, 0, 0, 0, 0)
                Unknown23143(1000, 60000, 70)
                Unknown1108(0)
                Unknown23015(11)
                Unknown23030('KusariRenderStage', 0, 12, 0, 13, 0, 0, 0, 0)
            if (SLOT_48 == 1511):
                sendToLabel(0)
            if (SLOT_48 == 1510):
                Unknown2001()

        def upon_12():
            Unknown23029(3, 1512, 0)
            Unknown23084(1)
            GFX_0('AST_Lock', 101)
    sprite('vr_chain_tip03', 1)
    Unknown3029(1)
    if SLOT_2:
        Unknown23030('KusariParam', 0, 0, 0, 7770, 0, 0, 0, 0)
        Unknown23030('KusariParam', 0, 1, 0, 16, 0, 0, 0, -10)
        Unknown23030('KusariParam', 0, 2, 0, 33, 0, 0, 0, -10)
        Unknown23030('KusariParam', 0, 3, 0, 50, 0, 0, 0, -10)
        Unknown23030('KusariParam', 0, 4, 0, 66, 0, 0, 0, -10)
        Unknown23030('KusariParam', 0, 5, 0, 83, 0, 0, 0, -10)
        Unknown23030('KusariParam', 0, 6, 0, 7771, 0, 0, 0, 0)
    else:
        Unknown23030('KusariParam', 0, 0, 0, 7770, 0, 0, 0, 0)
        Unknown23030('KusariParam', 0, 1, 0, 16, 0, 0, 0, 10)
        Unknown23030('KusariParam', 0, 2, 0, 33, 0, 0, 0, 10)
        Unknown23030('KusariParam', 0, 3, 0, 50, 0, 0, 0, 10)
        Unknown23030('KusariParam', 0, 4, 0, 66, 0, 0, 0, 10)
        Unknown23030('KusariParam', 0, 5, 0, 83, 0, 0, 0, 10)
        Unknown23030('KusariParam', 0, 6, 0, 7771, 0, 0, 0, 0)
    Unknown23030('KusariFirstPosition', 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('vr_chain_tip03', 9)
    Unknown23030('KusariSpeed', 0, 3000, 0, 0, 0, 0, 0, 0)
    sprite('vr_chain_tip04', 20)
    sprite('vr_chain_tip04', 6)
    sprite('vr_chain_tip04', 3)
    sprite('vr_chain_tip04', 3)
    sprite('vr_chain_tip04', 4)
    sprite('vr_chain_tip04', 14)
    sprite('vr_chain_tip04', 32767)
    loopRest()
    label(0)
    sprite('vr_chain_tip04ex01', 30)
    Unknown3004(-20)

@State
def AST_Lock():

    def upon_IMMEDIATE():
        Unknown4007(22)
        Unknown4010(2)
        Unknown2054(1)
        Unknown4003('hz_lock_C.DIG', 'hz_lock_C_mot_000.mmot')
        Unknown3033()
        Unknown3038(1)
        Unknown1007(128000)
        Unknown1096(1500)
        Unknown3001(0)
        Unknown3004(40)
    sprite('null', 5)
    Unknown1099(-120)
    sprite('null', 25)
    Unknown3004(-10)
    Unknown1099(-10)

@State
def AST_Enshutsu():

    def upon_IMMEDIATE():
        Unknown2055(600)
    sprite('null', 120)
    GFX_0('AST_Circle', -1)
    GFX_0('AST_Snake', -1)
    Unknown36(1)
    Unknown1010(256000, 420000)
    Unknown1025(100, 500)
    Unknown1011(0, 32000)
    Unknown35()
    GFX_0('AST_Snake', -1)
    Unknown36(1)
    Unknown1010(-256000, -420000)
    Unknown1025(-100, -500)
    Unknown1011(0, 32000)
    Unknown35()
    sprite('null', 150)
    GFX_0('AST_Unite', -1)
    sprite('null', 170)
    GFX_0('AST_Body', -1)
    GFX_0('AST_Head', -1)
    sprite('null', 30)
    GFX_0('AST_Breath', -1)
    sprite('null', 60)
    GFX_0('HZAST_RedOut', -1)

@State
def AST_Circle():

    def upon_IMMEDIATE():
        Unknown2008()
        Unknown2054(1)
        Unknown4003('hz_ah_A_circle.DIG', 'hz_ah_A_circle_mot_000.mmot')
        Unknown3033()
        Unknown3038(1)
    sprite('null', 150)
    Unknown1099(4)

@State
def AST_Snake():

    def upon_IMMEDIATE():
        Unknown2008()
        Unknown2054(1)
        Unknown4003('hz_ah_A_snake.DIG', 'hz_ah_A_snake_mot_000.mmot')
        Unknown3038(1)
    sprite('null', 150)

@State
def AST_Unite():

    def upon_IMMEDIATE():
        Unknown2008()
        Unknown2054(1)
        Unknown4003('hz_ah_A_unite.DIG', 'hz_ah_A_unite_mot_000.mmot')
        Unknown23015(4)
        Unknown3038(1)
        Unknown3032()
        Unknown1096(1500)
        Unknown1007(-160000)
        Unknown3001(0)
    sprite('null', 30)
    Unknown1074(-500)
    Unknown3004(10)
    sprite('null', 130)
    sprite('null', 50)
    Unknown3004(-5)

@State
def AST_Body():

    def upon_IMMEDIATE():
        Unknown2008()
        Unknown4010(2)
        Unknown2054(1)
        Unknown4003('hz_ah_B_body.DIG', 'hz_ah_B_body_mot_000.mmot')
        Unknown4015()
        Unknown3032()
        Unknown3038(1)
    sprite('null', 220)

@State
def AST_Breath():

    def upon_IMMEDIATE():
        Unknown2008()
        Unknown2054(1)
        GFX_2('efbg_hz_breath')
        teleportRelativeY(256000)
        Unknown23015(1)
        Unknown3033()
        Unknown3038(1)
        Unknown1096(500)
    sprite('null', 200)

@State
def AST_Head():

    def upon_IMMEDIATE():
        Unknown2008()
        Unknown4010(2)
        Unknown2054(1)
        Unknown4003('hz_ah_B_head.DIG', 'hz_ah_B_head_mot_000.mmot')
        Unknown4015()
        Unknown3032()
        Unknown3038(1)
    sprite('null', 220)

@State
def HZAST_RedOut():

    def upon_IMMEDIATE():
        Unknown23015(3)
        Unknown2054(1)
        Unknown1000(0)
        teleportRelativeY(0)
        Unknown3032()
        Unknown3026(-65536)
        Unknown1096(20000)
        Unknown3001(0)
    sprite('vr_white', 40)
    Unknown3004(40)
    sprite('vr_white', 20)
    Unknown3004(-15)

@State
def HZAST_BlackOut():

    def upon_IMMEDIATE():
        Unknown23015(4)
        Unknown2054(1)
        Unknown1000(0)
        teleportRelativeY(0)
        Unknown3032()
        Unknown3026(-16777216)
        Unknown1096(20000)
        Unknown3001(0)
    sprite('vr_white', 20)
    Unknown3004(12)
    sprite('vr_white', 40)
    sprite('vr_white', 20)
    Unknown3004(-15)

@State
def bhz_AH_ray():

    def upon_IMMEDIATE():
        Unknown23057(50)
        teleportRelativeY(308000)
        Unknown4054(4)
        Unknown23067('ef_speedline_wt')
    sprite('null', 120)

@State
def bhz_AH_ray2():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23057(50)
        teleportRelativeY(308000)
        Unknown4054(4)
        Unknown23067('ef_speedline_bk')
    sprite('null', 120)

@State
def NoelEntry():

    def upon_IMMEDIATE():
        sendToLabelUpon(56, 1)
        Unknown4061(7)
        Unknown1000(-50000)
    sprite('no602_00', 32767)
    label(1)
    sprite('no602_00', 200)
    loopRest()

@State
def NoelWarp():

    def upon_IMMEDIATE():
        Unknown2019(-500)
        Unknown4061(7)
        Unknown1000(-50000)
        Unknown2034(0)
        Unknown3032()
    sprite('no602_00', 90)
    sprite('no602_00', 15)
    GFX_1('haef_event_lose', 0)
    SFX_0('014_electric_m')
    SFX_0('001_airbackdash_0')
    sprite('no602_00', 15)
    sprite('no602_00', 15)
    GFX_1('haef_event_lose', 0)
    SFX_0('014_electric_s')
    SFX_0('001_airbackdash_0')
    sprite('no602_00', 15)
    sprite('no602_00', 15)
    GFX_1('haef_event_lose', 0)
    SFX_0('014_electric_m')
    SFX_0('001_airbackdash_0')
    sprite('no602_00', 15)
    sprite('no602_00', 15)
    GFX_1('haef_event_lose', 0)
    SFX_0('014_electric_s')
    SFX_0('001_airbackdash_0')
    sprite('no602_00', 15)
    sprite('no602_00', 4)
    GFX_1('haef_event_lose', 0)
    SFX_0('014_electric_s')
    SFX_0('000_airdash_2')
    Unknown3004(-10)
    sprite('no602_00', 6)
    sprite('no602_00', 6)
    sprite('no602_00', 6)
    GFX_1('haef_event_lose_end', 0)
    sprite('no602_00', 6)
    Unknown1000(-500000)

@State
def NoelTimeUpLose():

    def upon_IMMEDIATE():
        sendToLabelUpon(56, 1)
        Unknown4061(7)
        Unknown1000(0)
    sprite('no620_08', 32767)
    loopRest()
    label(1)
    clearUponHandler(56)
    sendToLabelUpon(56, 2)
    sprite('no620_08', 32767)
    loopRest()
    label(2)
    clearUponHandler(56)
    sendToLabelUpon(56, 3)
    sprite('no620_08', 32767)
    loopRest()
    label(3)
    sprite('no620_08', 20)
    loopRest()

@State
def NoelDownUpperSet():

    def upon_IMMEDIATE():
        sendToLabelUpon(56, 1)
        Unknown4061(7)
        Unknown1000(-130000)
        teleportRelativeY(100000)
        setGravity(0)
    sprite('no062_00', 32767)
    loopRest()
    label(1)
    sprite('no062_00', 1)
    loopRest()

@State
def NoelDownUpperGo():

    def upon_IMMEDIATE():
        Unknown4061(7)
        Unknown1000(-130000)
        teleportRelativeY(100000)
        setGravity(0)
        Unknown2019(100)
        Unknown2055(150)
    sprite('no062_00', 3)
    Unknown1000(-130000)
    sprite('no062_00', 4)
    Unknown1000(-130000)
    sprite('no062_00', 4)
    Unknown1000(-210000)
    sprite('no062_00', 4)
    Unknown1000(-290000)
    sprite('no062_00', 4)
    Unknown1000(-370000)
    sprite('no062_00', 4)
    sprite('no062_00', 4)
    sprite('no062_00', 4)
    setGravity(1000)
    sprite('no062_00', 6)
    sprite('no062_00', 3)
    sprite('no062_00', 1)
    Unknown4045('ef_hitmd', 108)
    physicsYImpulse(0)
    setGravity(0)
    sprite('no062_00', 1)
    teleportRelativeX(-3000)
    sprite('no062_00', 1)
    teleportRelativeX(3000)
    sprite('no062_00', 1)
    teleportRelativeX(-3000)
    sprite('no062_00', 1)
    teleportRelativeX(3000)
    sprite('no062_00', 1)
    teleportRelativeX(-3000)
    sprite('no062_00', 1)
    teleportRelativeX(3000)
    sprite('no072_01', 100)
    physicsXImpulse(-22000)
    physicsYImpulse(14000)
    Unknown1043()

@State
def RLAstLockmc():

    def upon_IMMEDIATE():
        Unknown3038(1)
        Unknown4054(5)
        Unknown23067('rlef_ashlock_mc')
        Unknown4010(3)
    sprite('null', 120)
    Unknown3001(0)
    Unknown3004(2)
    sprite('null', 32767)
    Unknown3004(0)

@State
def RLAstLockAura():

    def upon_IMMEDIATE():
        Unknown3038(1)
        Unknown23067('rlef_ashlock_aura')
        Unknown4010(3)
    sprite('null', 120)
    Unknown3001(0)
    Unknown3004(2)
    sprite('null', 32767)
    Unknown3004(0)

@State
def KusariBurstDD():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4009(3)

        def upon_31():
            Unknown23030('KusariDraw', 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown23030('KusariKansetsu', 0, 7, 0, 0, 0, 0, 0, 0)
        Unknown3029(1)
        AfterimageColor_1(200, 255, 255, 255)
        AfterimageColor_2(0, 255, 255, 255)
        Unknown3053(1)
        Unknown3054(56, 120)
        Unknown3054(57, 80)
        Unknown3054(58, 40)
        Unknown3032()

        def upon_48():
            Unknown23030('KusariIdling', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_3():
            if SLOT_51:
                Unknown1108(-180000)
            if SLOT_2:
                Unknown4055(0)
                Unknown4049(500)
                Unknown4045('hzef_antiairchain', -1)
                Unknown4054(5)
                Unknown4045('hzef_exheadmoveopt', -1)
        sendToLabelUpon(32, 0)
    sprite('vr_chain_tip03aa', 1)
    Unknown23015(1)
    Unknown23143(40000, 80000, 70)
    Unknown3029(1)
    Unknown23030('KusariParam', 0, 0, 0, 7770, 0, 0, 0, 0)
    Unknown23030('KusariParam', 0, 1, 0, 16, 0, 0, 0, 10)
    Unknown23030('KusariParam', 0, 2, 0, 33, 0, 0, 0, 10)
    Unknown23030('KusariParam', 0, 3, 0, 50, 0, 0, 0, 10)
    Unknown23030('KusariParam', 0, 4, 0, 66, 0, 0, 0, 10)
    Unknown23030('KusariParam', 0, 5, 0, 83, 0, 0, 0, 10)
    Unknown23030('KusariParam', 0, 6, 0, 7771, 0, 0, 0, 0)
    Unknown23030('KusariFirstPosition', 0, 0, 0, 0, 0, 0, 0, 0)
    GFX_0('ExPortalSp', -1)
    Unknown36(1)
    Unknown1072(-40000)
    Unknown35()
    Unknown1072(-30000)
    sprite('vr_chain_tip03aa', 9)
    Unknown2037(1)
    Unknown23030('KusariSpeed', 0, 3000, 0, 0, 0, 0, 0, 0)
    label(0)
    sprite('vr_chain_tip04ex01', 6)
    Unknown2037(0)
    Unknown21012('ExPortalSp', 32)
    Unknown23143(-10000, -50000, 50)
    sprite('vr_chain_tip04ex01', 4)
    SLOT_51 = 1
    Unknown23143(-80000, -20000, 10)
    sprite('vr_chain_tip04ex01', 8)
    Unknown23143(-100000, -60000, 10)
    sprite('vr_chain_tip04ex01', 4)
    Unknown23143(10000, 10000, 20)
    sprite('vr_chain_tip04ex01', 10)
    Unknown23143(0, 0, 0)
    Unknown23144('03000000000000006d0000000000000000000000000000000000000000000000500000000000000003000000')

@State
def Eff440Zanzo():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown3033()
        Unknown4061(2)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3041(255)
        Unknown3042(1)
        Unknown3043(254)
        Unknown3044(1)
        Unknown3026(-1)
        Unknown3025(16711935, 18)
    sprite('vrhzef440_00', 2)
    teleportRelativeX(-100000)
    sprite('vrhzef440_01', 16)
    Unknown4007(0)
    Unknown3002(-100)

@State
def Eff440Zanzo_b():

    def upon_IMMEDIATE():
        Unknown4022(3)
        Unknown3033()
        Unknown4061(2)
        teleportRelativeX(100000)
    sprite('null', 1)
    sprite('vrhzef440_10', 5)

@State
def Eff440Zanzo_b2():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(2)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3041(255)
        Unknown3042(1)
        Unknown3043(254)
        Unknown3044(1)
        Unknown3026(-1)
        Unknown3025(16711935, 18)
        teleportRelativeY(0)
        teleportRelativeX(100000)
    sprite('vrhzef440_11', 2)
    sprite('vrhzef440_12', 16)
    Unknown3002(-100)

@State
def Eff440snake():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4061(1)
        Unknown3032()
        teleportRelativeX(-128000)
        teleportRelativeY(-32000)
    sprite('vrhzef440_30', 3)
    GFX_1('hzef_432backaura_01', 0)
    sprite('vrhzef440_31', 3)
    GFX_1('hzef_432backaura_01', 0)
    sprite('vrhzef440_32', 4)
    GFX_1('hzef_432backaura_01', 0)
    GFX_1('hzef_432backaura_01', 1)
    sprite('vrhzef440_33', 4)
    GFX_1('hzef_432backaura_01', 0)
    GFX_1('hzef_432backaura_01', 1)
    GFX_1('hzef_432backaura_01', 2)
    sprite('vrhzef440_34', 4)
    GFX_1('hzef_432backaura_01', 0)
    sprite('vrhzef440_35', 4)
    sprite('vrhzef440_36', 4)

@State
def Eff411():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4061(1)
        Unknown3032()
        Unknown1096(1125)
        teleportRelativeX(-35000)
        teleportRelativeY(-32000)
    sprite('vrhzef411_00', 3)
    Unknown3001(55)
    Unknown3004(25)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    sprite('vrhzef411_01', 2)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    sprite('vrhzef411_02', 3)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_Aura', 5)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    sprite('vrhzef411_03', 3)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    sprite('vrhzef411_04', 3)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    sprite('vrhzef411_05', 3)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)

@State
def Eff412Zanzo():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2054(1)
        Unknown3033()
        Unknown4061(2)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3041(255)
        Unknown3042(1)
        Unknown3043(254)
        Unknown3044(1)
        teleportRelativeX(7000)
        Unknown1007(-7000)
        Unknown3026(-1)
        Unknown3025(16711935, 8)
    sprite('vrhzef412_00', 2)
    sprite('vrhzef412_01', 8)
    Unknown3002(-127)

@State
def Act2Event_Yure():
    label(0)
    sprite('null', 10)
    ScreenShake(3000, 3000)
    SFX_0('019_quake_0')
    loopRest()
    gotoLabel(0)

@State
def Act3Event_Ragna():

    def upon_IMMEDIATE():
        Unknown30012(0)
        Unknown1000(120000)
        Unknown2019(750)
        EnableCollision(0)
        Unknown2034(0)
        Unknown2005()
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        sendToLabelUpon(2, 2)
    sprite('rg620_05', 32767)
    label(0)
    sprite('rg620_05', 5)
    sprite('rg620_04', 5)
    sprite('rg620_03', 5)
    sprite('rg620_02', 5)
    sprite('rg620_01', 5)
    sprite('rg620_00', 5)
    label(9)
    sprite('rg000_00', 7)
    sprite('rg000_01', 7)
    sprite('rg000_02', 7)
    sprite('rg000_03', 7)
    sprite('rg000_04', 7)
    sprite('rg000_05', 7)
    sprite('rg000_06', 7)
    sprite('rg000_05', 7)
    sprite('rg000_04', 7)
    sprite('rg000_03', 7)
    sprite('rg000_02', 7)
    sprite('rg000_01', 7)
    loopRest()
    gotoLabel(9)
    label(1)
    sprite('rg033_00', 4)
    sprite('rg033_01', 4)
    SFX_3('rgse_00')
    physicsXImpulse(-28000)
    physicsYImpulse(20000)
    setGravity(1400)
    Unknown8002()
    Unknown8001(3, 100)
    label(99)
    sprite('rg033_02', 3)
    sprite('rg033_03', 3)
    loopRest()
    gotoLabel(99)
    label(2)
    sprite('null', 10)
    Unknown1084(1)
    Unknown3038(1)

@State
def Act3Event_EffGedan():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4061(1)
        Unknown3032()
        teleportRelativeX(240000)
        Unknown1007(-16000)
    sprite('vrhzef403_00', 2)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    Unknown3001(55)
    Unknown3004(25)
    sprite('vrhzef403_01', 3)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    sprite('vrhzef403_02', 2)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_Aura', 5)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    sprite('vrhzef403_03', 18)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_Aura', 5)
    GFX_0('HZEF_Aura', 6)
    GFX_0('HZEF_Aura', 7)
    GFX_0('HZEF_Aura', 8)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    GFX_0('HZEF_AuraDelete', 6)
    GFX_0('HZEF_AuraDelete', 7)
    GFX_0('HZEF_AuraDelete', 8)
    sprite('vrhzef403_04', 4)
    Unknown4007(0)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    sprite('vrhzef403_05', 4)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    sprite('vrhzef403_06', 4)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)

@State
def Eventoffset_Sosai_ntvshz():

    def upon_IMMEDIATE():
        Unknown1001(0)
        teleportRelativeY(200000)
        Unknown1010(-20000, 20000)
    sprite('null', 4)
    GFX_1('ef_offset', 0)
    SFX_0('108_attack_offset')
    ScreenShake(30000, 30000)