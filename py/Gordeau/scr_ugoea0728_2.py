@State
def EMB():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown2054(1)
        Unknown3038(1)
        Unknown23015(5)
        Unknown4003('ef_emb_hb.DIG', '')
        Unknown1007(265000)
        Unknown1096(1450)
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
def EMB_HB_OD():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('ef_emb_hb.DIG', '')
        Unknown23015(5)
        Unknown1007(265000)
        Unknown1096(1450)
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
def EMB_HB_AH():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown2054(1)
        Unknown4003('ef_emb_hb.DIG', '')
        Unknown23015(5)
        Unknown1007(265000)
        Unknown1096(1450)
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
def ModelMagicCircle1():

    def upon_IMMEDIATE():
        Unknown3038(1)
        Unknown4003('rgef_mc.DIG', 'rgef_mc_motion_000.mmot')
        Unknown4015()
        Unknown21004(224)
        Unknown2054(1)
    sprite('null', 74)

@State
def UGO_Nml5C_WeaponSummonIn():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown2054(1)
    sprite('Action_076_00', 5)
    sprite('Action_076_01', 5)
    sprite('Action_076_02', 5)
    sprite('Action_076_03', 5)
    sprite('Action_076_04', 5)

@State
def UGO_Nml5C_WeaponSummonOut():

    def upon_IMMEDIATE():
        Unknown2054(1)
    sprite('Action_102_00', 5)
    sprite('Action_102_01', 5)
    sprite('Action_102_02', 5)
    sprite('Action_102_03', 5)

@State
def UGO_Nml5C_Zanzo():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
    sprite('Action_101_00', 3)
    sprite('Action_101_01', 4)
    sprite('Action_101_02', 3)
    sprite('Action_101_03', 3)
    sprite('Action_101_04', 3)
    sprite('Action_101_05', 1)

@State
def UGO_Nml2C_Zanzo():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown2054(1)
    sprite('Action_081_00', 4)
    sprite('Action_081_01', 4)
    sprite('Action_081_02', 3)
    sprite('Action_081_03', 3)
    sprite('Action_081_04', 3)
    label(1)
    sprite('null', 1)

@State
def UGO_Nml2C_WeaponSummonOut():

    def upon_IMMEDIATE():
        Unknown2054(1)
    sprite('Action_082_00', 3)
    sprite('Action_082_01', 3)
    sprite('Action_082_02', 3)

@State
def UGO_NmlAIR5B_Zanzo1():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown2019(1)
    sprite('Action_084_00', 3)
    sprite('Action_084_01', 3)
    sprite('Action_084_02', 3)

@State
def UGO_NmlAIR5B_Zanzo2():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown2019(1)
    sprite('Action_083_00', 3)
    sprite('Action_083_01', 3)
    sprite('Action_083_02', 3)

@State
def UGO_NmlAIR5C_Zanzo():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown2019(1)
    sprite('Action_087_00', 5)
    sprite('Action_087_01', 5)
    sprite('Action_087_02', 3)
    sprite('Action_087_03', 3)
    sprite('Action_087_04', 3)

@State
def UGO_Invincible_Zanzo1():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
    sprite('Action_121_00', 4)
    sprite('Action_121_01', 4)
    sprite('Action_121_02', 4)
    sprite('Action_121_03', 4)
    sprite('Action_121_04', 4)
    sprite('Action_121_05', 1)

@State
def UGO_Invincible_Zanzo2():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
    sprite('Action_122_00', 4)
    sprite('Action_122_01', 4)
    sprite('Action_122_02', 4)
    sprite('Action_122_03', 4)
    sprite('Action_122_04', 3)
    sprite('Action_122_05', 3)

@State
def UGO_Invincible_SummonOut():

    def upon_IMMEDIATE():
        Unknown2054(1)
        teleportRelativeX(-40000)
        Unknown1007(-115000)
    sprite('Action_078_00', 8)
    sprite('Action_078_01', 8)
    sprite('Action_078_02', 1)

@State
def UGO_Assault_SummonIn():

    def upon_IMMEDIATE():
        Unknown2054(1)
    sprite('Action_076_00', 5)
    sprite('Action_076_01', 5)
    sprite('Action_076_02', 5)
    sprite('Action_076_03', 5)
    sprite('Action_076_04', 5)

@State
def UGO_Assault_Zanzou():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
    sprite('Action_091_00', 5)
    sprite('Action_091_01', 5)
    sprite('Action_091_02', 5)
    sprite('Action_091_03', 5)
    sprite('Action_091_04', 1)

@State
def UGO_Assault_SummonOut():

    def upon_IMMEDIATE():
        Unknown2054(1)
    sprite('Action_078_00', 8)
    sprite('Action_078_01', 8)
    sprite('Action_078_02', 1)

@State
def UGO_Assault2nd_Zanzou():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
    sprite('Action_092_00', 5)
    sprite('Action_092_01', 5)
    sprite('Action_092_02', 5)
    sprite('Action_092_03', 5)
    sprite('Action_092_04', 5)

@State
def UGO_Assault2nd_SummonOut():

    def upon_IMMEDIATE():
        Unknown2054(1)
    sprite('Action_077_00', 5)
    sprite('Action_077_01', 5)
    sprite('Action_077_02', 5)
    sprite('Action_077_03', 5)

@State
def UGO_DrainThrow_AuraA():

    def upon_IMMEDIATE():
        Unknown4010(3)
        teleportRelativeX(-15000)
    sprite('Action_089_00', 3)
    sprite('Action_089_01', 5)
    sprite('Action_089_02', 5)
    sprite('Action_089_03', 5)
    sprite('Action_089_04', 5)
    sprite('Action_089_05', 3)

@State
def UGO_DrainThrow_LandZanzou():

    def upon_IMMEDIATE():
        Unknown1007(28000)
    sprite('Action_097_00', 5)
    sprite('Action_097_01', 5)
    sprite('Action_097_02', 5)
    sprite('Action_097_03', 5)
    sprite('Action_097_04', 5)

@State
def UGO_DrainThrow_HitAura():
    sprite('Action_104_00', 4)
    sprite('Action_104_01', 4)
    sprite('Action_104_02', 4)
    sprite('Action_104_03', 4)
    sprite('Action_104_04', 4)
    sprite('Action_104_05', 4)

@State
def UGO_Drain_Yoin():

    def upon_IMMEDIATE():
        pass
    sprite('Action_098_00', 5)
    sprite('Action_098_01', 5)
    sprite('Action_098_02', 5)
    sprite('Action_098_03', 5)
    sprite('Action_098_04', 5)
    sprite('Action_098_05', 5)
    sprite('Action_098_06', 5)

@State
def UGO_Drain_Steal():

    def upon_IMMEDIATE():
        pass
    sprite('Action_103_00', 2)
    sprite('Action_103_01', 2)
    sprite('Action_103_02', 2)
    sprite('Action_103_03', 2)
    sprite('Action_103_04', 2)
    sprite('Action_103_05', 2)
    sprite('Action_103_06', 2)
    sprite('Action_103_07', 2)
    sprite('Action_103_08', 2)
    sprite('Action_103_09', 2)
    sprite('Action_103_10', 2)
    sprite('Action_103_11', 2)

@State
def UGO_DrainThrow_AntiAirZanzou():

    def upon_IMMEDIATE():
        pass
    sprite('Action_085_00', 5)
    sprite('Action_085_01', 5)
    sprite('Action_085_02', 5)
    sprite('Action_085_03', 5)
    sprite('Action_085_04', 5)

@State
def UGO_DrainThrow_AuraB():

    def upon_IMMEDIATE():
        Unknown4010(3)
        teleportRelativeX(-15000)
    sprite('Action_095_00', 3)
    sprite('Action_095_01', 3)
    sprite('Action_095_02', 3)
    sprite('Action_095_03', 3)
    sprite('Action_095_04', 3)
    sprite('Action_095_05', 3)

@State
def UGO_DrainThrow_AuraB_2():

    def upon_IMMEDIATE():
        Unknown4010(3)
    sprite('Action_089_00', 5)
    sprite('Action_089_01', 5)
    sprite('Action_089_02', 5)
    sprite('Action_089_03', 5)
    sprite('Action_089_04', 5)
    sprite('Action_089_05', 3)

@State
def UGO_Strike_SummonIn():

    def upon_IMMEDIATE():
        Unknown2054(1)
    sprite('Action_073_00', 5)
    sprite('Action_073_01', 5)
    sprite('Action_073_02', 5)
    sprite('Action_073_03', 5)
    sprite('Action_073_04', 5)

@State
def UGO_StrikeA_SummonOut():

    def upon_IMMEDIATE():
        Unknown2054(1)
    sprite('Action_088_00', 5)
    sprite('Action_088_01', 5)
    sprite('Action_088_02', 5)
    sprite('Action_088_03', 5)

@State
def UGO_StrikeA_Inpact():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_157_00', 5)
    sprite('Action_157_01', 5)
    sprite('Action_157_02', 5)
    sprite('Action_157_03', 5)
    sprite('Action_157_04', 5)

@State
def UGO_StrikeB_Zanzou():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
    sprite('Action_072_00', 4)
    sprite('Action_072_01', 4)
    sprite('Action_072_02', 4)
    sprite('Action_072_03', 4)
    sprite('Action_072_04', 4)

@State
def UGO_StrikeB_SummonOut():

    def upon_IMMEDIATE():
        Unknown2054(1)
        teleportRelativeX(-230000)
        Unknown1007(-10000)
    sprite('Action_102_00', 5)
    sprite('Action_102_01', 5)
    sprite('Action_102_02', 5)
    sprite('Action_102_03', 5)

@State
def UGO_StrikeB_AtkCol():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4009(3)
        Unknown4007(3)
        Unknown2003(1)
        Unknown4010(3)
        AttackLevel_(2)
        Damage(300)
        AttackP2(80)
        AttackP1(60)
        Unknown11092(1)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Hitstop(1)
        AirUntechableTime(25)
        Unknown9016(1)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(20000)
        AirPushbackY(9000)
        Unknown30055(100000, 70, 0)
        Unknown30056(-150000, 70, 0)
        AttackAttributes(1, 0, 0, 0, 0)
        HitAirUnblockable(3)
        Unknown1007(540000)

        def upon_78():
            Unknown23029(3, 201, 0)
    sprite('Action_163_00', 3)
    SFX_3('SE045')
    sprite('Action_163_00', 3)
    SFX_3('SE045')
    sprite('Action_163_00', 3)
    sprite('Action_163_01', 3)
    SFX_3('SE045')
    sprite('Action_163_02', 3)
    sprite('Action_163_03', 3)
    SFX_3('SE045')
    sprite('Action_163_01', 3)
    label(0)
    sprite('Action_163_02', 3)
    SFX_3('SE045')
    sprite('Action_163_03', 3)
    sprite('Action_163_01', 3)
    SFX_3('SE045')
    sprite('Action_163_02', 3)
    sprite('Action_163_03', 3)
    SFX_3('SE045')
    sprite('Action_163_01', 3)
    gotoLabel(0)

@State
def UGO_AirStrikeA_AtkCol():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4009(3)
        Unknown4007(3)
        Unknown4010(3)
        Unknown2003(1)
    sprite('Action_163_00', 3)
    sprite('Action_163_00', 3)
    sprite('Action_163_00', 3)
    sprite('Action_163_01', 3)
    sprite('Action_163_02', 3)
    sprite('Action_163_03', 3)
    sprite('Action_163_01', 3)
    sprite('Action_163_02', 3)
    sprite('Action_163_03', 3)
    sprite('Action_163_01', 3)
    sprite('Action_163_02', 3)
    sprite('Action_163_03', 3)
    sprite('Action_163_01', 3)

@State
def UGO_StrikeB_WeaponSummonOut():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown1072(36000)
        Unknown1007(290000)
        teleportRelativeX(-120000)
    sprite('Action_082_00', 3)
    sprite('Action_082_01', 3)
    sprite('Action_082_02', 3)

@State
def UGO_AirAssaultA_AtkCol():

    def upon_IMMEDIATE():
        Unknown2009()
        Unknown4007(3)
        Unknown4010(3)
        Unknown2003(1)
    sprite('Action_184_00', 4)
    sprite('Action_184_01', 4)
    sprite('Action_184_02', 4)
    sprite('Action_184_03', 4)
    sprite('Action_184_04', 1)

@State
def UGO_AirAssaultA_AtkCol_TAG():

    def upon_IMMEDIATE():
        Unknown2009()
        Unknown4007(3)
        Unknown4010(3)
        AttackAttributes(1, 0, 0, 0, 0)
        Unknown23078(1)
        Unknown2003(1)
    sprite('Action_184_00', 4)
    sprite('Action_184_01', 4)
    sprite('Action_184_02', 4)
    sprite('Action_184_03', 4)
    sprite('Action_184_04', 1)

@State
def UGO_Scratch_AtkCol():

    def upon_IMMEDIATE():
        Unknown2009()
        Unknown4009(3)
        AttackLevel_(4)
        Damage(900)
        Unknown11092(1)
        Hitstop(0)
        hitstun(30)
        AirUntechableTime(60)
        Unknown9016(1)
        AirHitstunAnimation(9)
        AirPushbackY(20000)
        AirPushbackX(6500)
        Unknown11106(0)
        Hitstop(2)
        teleportRelativeX(300000)
        teleportRelativeY(105000)
        Unknown1007(220000)
        Unknown11044(1)
        Unknown9266(12)
        Unknown1096(950)
        Unknown23089(3, 1, 1, 1, 1, 0, 3, 0)
        ProjectileDurabilityLvl(3)
        
        def upon_60():
            hitstun(45)
        
        def upon_44():
            sendToLabel(580)

        def upon_12():
            if (not SLOT_2):
                ConsumeSuperMeter(666)
                Unknown36(22)
                ConsumeSuperMeter(-666)
                Unknown35()
            else:
                Unknown2038(1)
            if SLOT_51:
                Unknown11050(5, '')
                SystemGFX('HitMzEff', 65535)
                Unknown36(1)
                Unknown1086(22)
                Unknown1012(-15000, 15000)
                Unknown1011(100000, 120000)
                Unknown35()
            else:
                SLOT_51 = 1
    sprite('Action_237_00', 1)
    SFX_3('SE049_SpecialSwing')
    sprite('Action_237_01', 1)
    RefreshMultihit()
    sprite('Action_237_01', 1)
    RefreshMultihit()
    sprite('Action_237_01', 2)
    RefreshMultihit()
    label(580)
    clearUponHandler(44)
    sprite('Action_237_02', 3)
    sprite('Action_237_03', 3)
    sprite('Action_237_04', 3)
    sprite('Action_237_05', 1)

@State
def UGO_Scratch_AtkCol_Assist():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4009(3)
        AttackLevel_(4)
        Damage(900)
        AttackP1(70)
        Unknown11092(1)
        Hitstop(0)
        hitstun(30)
        AirUntechableTime(30)
        Unknown9016(1)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackY(25000)
        AirPushbackX(6500)
        Unknown11106(0)
        Hitstop(2)
        teleportRelativeX(300000)
        Unknown1007(220000)
        Unknown23078(1)
        Unknown11042(1)
        Unknown9266(12)

        def upon_44():
            sendToLabel(580)

        def upon_12():
            if (not SLOT_2):
                ConsumeSuperMeter(666)
                Unknown36(22)
                ConsumeSuperMeter(-666)
                Unknown35()
            else:
                Unknown2038(1)
            if SLOT_51:
                Unknown11050(5, '')
                SystemGFX('HitMzEff', 65535)
                Unknown36(1)
                Unknown1086(22)
                Unknown1012(-15000, 15000)
                Unknown1011(100000, 120000)
                Unknown35()
            else:
                SLOT_51 = 1
    sprite('Action_237_00', 1)
    SFX_3('SE049_SpecialSwing')
    sprite('Action_237_01', 1)
    RefreshMultihit()
    sprite('Action_237_01', 1)
    RefreshMultihit()
    sprite('Action_237_01', 2)
    RefreshMultihit()
    label(580)
    clearUponHandler(44)
    sprite('Action_237_02', 3)
    sprite('Action_237_03', 3)
    sprite('Action_237_04', 3)
    sprite('Action_237_05', 1)

@State
def UGO_AssaultEx_Zanzou1():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
    sprite('Action_129_00', 4)
    sprite('Action_129_01', 4)
    sprite('Action_129_02', 4)
    sprite('Action_129_03', 4)
    sprite('Action_129_04', 4)

@State
def UGO_AssaultEx_Zanzou2():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
    sprite('Action_134_00', 6)
    sprite('Action_134_01', 4)
    sprite('Action_134_02', 4)
    sprite('Action_134_03', 4)
    sprite('Action_134_04', 4)

@State
def UGO_DrainThrow_Aura_Catch():

    def upon_IMMEDIATE():
        Unknown4007(3)
    sprite('Action_203_00', 4)
    sprite('Action_203_01', 4)
    sprite('Action_203_02', 4)
    sprite('Action_203_03', 4)

@State
def UGO_DrainThrow_AuraEx():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown3004(-10)
    sprite('Action_090_00', 5)
    sprite('Action_090_01', 5)
    sprite('Action_090_02', 5)
    sprite('Action_090_03', 5)
    sprite('Action_090_04', 5)
    sprite('Action_090_05', 3)

@State
def UGO_AssaultEx_DrainYoin():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        teleportRelativeX(15000)
        Unknown1007(-85000)
        Unknown3004(-10)
    sprite('Action_086_00', 5)
    sprite('Action_086_01', 5)
    sprite('Action_086_02', 5)
    sprite('Action_086_03', 5)
    sprite('Action_086_04', 5)
    sprite('Action_086_05', 3)
    sprite('Action_086_06', 5)

@State
def UGO_AirAssaultEx_AtkCol1():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4007(3)
        AttackLevel_(4)
        Damage(800)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        AttackP1(70)
        AttackP2(80)
        Unknown11092(1)
        AirUntechableTime(40)
        Hitstop(0)
        Unknown9016(1)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(18000)
        AirPushbackY(30000)
        YImpluseBeforeWallbounce(1800)
        PushbackX(21000)
        AttackAttributes(1, 0, 0, 0, 0)
        Unknown23078(1)
    sprite('Action_186_00', 4)
    sprite('Action_186_01', 4)
    RefreshMultihit()
    sprite('Action_186_02', 4)
    sprite('Action_186_03', 4)
    sprite('Action_186_04', 1)

@State
def UGO_AirAssaultEx_AtkCol2():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4007(3)
        AttackLevel_(4)
        Damage(800)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        AirUntechableTime(40)
        Hitstop(0)
        AttackP1(70)
        AttackP2(80)
        Unknown11092(1)
        Unknown9016(1)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(18000)
        AirPushbackY(30000)
        YImpluseBeforeWallbounce(1800)
        PushbackX(21000)
        AttackAttributes(1, 0, 0, 0, 0)
        Unknown23078(1)
    sprite('Action_187_00', 4)
    sprite('Action_187_01', 4)
    RefreshMultihit()
    sprite('Action_187_02', 4)
    sprite('Action_187_03', 4)
    sprite('Action_187_04', 1)

@State
def UGO_StrikeEx_AtkCol():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4007(3)
        Unknown4010(3)
        AttackLevel_(2)
        Damage(120)
        AttackP2(100)
        Unknown11092(1)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Hitstop(0)
        AirUntechableTime(21)
        Unknown9016(1)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(12000)
        AirPushbackY(12000)
        Unknown30055(1000, 70, 0)
        Unknown30056(-150000, 70, 0)
        Unknown23078(1)
        Unknown1096(750)
    sprite('Action_172_00', 5)
    RefreshMultihit()
    sprite('Action_172_01', 4)
    RefreshMultihit()
    sprite('Action_172_02', 4)
    RefreshMultihit()
    sprite('Action_172_03', 3)
    RefreshMultihit()
    sprite('Action_172_04', 3)
    RefreshMultihit()
    sprite('Action_172_05', 3)
    RefreshMultihit()
    sprite('Action_172_06', 2)
    RefreshMultihit()
    sprite('Action_172_07', 2)
    RefreshMultihit()
    sprite('Action_172_08', 2)
    RefreshMultihit()
    sprite('Action_172_09', 2)
    RefreshMultihit()
    sprite('Action_172_07', 1)
    RefreshMultihit()
    sprite('Action_172_08', 1)
    RefreshMultihit()
    sprite('Action_172_09', 1)
    RefreshMultihit()
    sprite('Action_172_07', 1)
    RefreshMultihit()
    sprite('Action_172_08', 1)
    RefreshMultihit()
    sprite('Action_172_09', 1)
    RefreshMultihit()

@State
def UGO_AirStrikeEx_AtkCol():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4007(3)
        Unknown4010(3)
        AttackLevel_(2)
        Damage(200)
        AttackP1(80)
        AttackP2(89)
        Unknown11092(1)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Hitstop(0)
        AirUntechableTime(36)
        Unknown9016(1)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(12000)
        AirPushbackY(27000)
        YImpluseBeforeWallbounce(1800)

        def upon_12():
            AirPushbackY(13000)
            Unknown30056(-30000, 70, 0)
        Unknown23078(1)
    sprite('Action_172_00', 5)
    RefreshMultihit()
    sprite('Action_172_01', 4)
    RefreshMultihit()
    sprite('Action_172_02', 4)
    RefreshMultihit()
    sprite('Action_172_03', 3)
    RefreshMultihit()
    sprite('Action_172_04', 3)
    RefreshMultihit()
    sprite('Action_172_05', 3)
    RefreshMultihit()
    sprite('Action_172_06', 2)
    RefreshMultihit()
    sprite('Action_172_07', 2)
    RefreshMultihit()
    sprite('Action_172_08', 2)
    RefreshMultihit()
    sprite('Action_172_09', 2)
    RefreshMultihit()
    sprite('Action_172_07', 1)
    RefreshMultihit()
    sprite('Action_172_08', 1)
    RefreshMultihit()
    sprite('Action_172_09', 1)
    RefreshMultihit()
    sprite('Action_172_07', 1)
    RefreshMultihit()
    sprite('Action_172_08', 1)
    RefreshMultihit()
    sprite('Action_172_09', 1)
    RefreshMultihit()

@State
def UGO_UltimateAssault_Start():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown2054(1)
        Unknown2019(1)
        Unknown4010(3)

        def upon_43():
            if (SLOT_48 == 501):
                sendToLabel(1)
    sprite('Action_247_00', 5)
    sprite('Action_247_01', 5)
    sprite('Action_247_02', 5)
    sprite('Action_247_03', 5)
    SFX_3('SE045')
    label(0)
    sprite('Action_247_04', 3)
    sprite('Action_247_05', 3)
    SFX_3('SE045')
    sprite('Action_247_06', 3)
    sprite('Action_247_07', 3)
    gotoLabel(0)
    label(1)
    sprite('Action_247_08', 3)
    sprite('Action_247_09', 3)
    sprite('Action_247_10', 1)

@State
def UGO_UltimateAssault_AtkEff1():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
    sprite('Action_241_00', 3)
    sprite('Action_241_01', 3)
    sprite('Action_241_02', 3)
    sprite('Action_241_03', 3)
    sprite('Action_241_04', 3)

@State
def UGO_UltimateAssault_AtkEff2():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
    sprite('Action_242_00', 3)
    sprite('Action_242_01', 3)
    sprite('Action_242_02', 3)
    sprite('Action_242_03', 3)
    sprite('Action_242_04', 3)
    sprite('Action_242_05', 3)

@State
def UGO_UltimateAssault_AtkEff3():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
    sprite('Action_243_00', 3)
    sprite('Action_243_01', 3)
    sprite('Action_243_02', 3)
    sprite('Action_243_03', 3)
    sprite('Action_243_04', 3)
    sprite('Action_243_05', 3)

@State
def UGO_UltimateAssault_AtkEff4():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
    sprite('Action_244_00', 3)
    sprite('Action_244_01', 3)
    sprite('Action_244_02', 3)
    sprite('Action_244_03', 3)
    sprite('Action_244_04', 3)
    sprite('Action_244_05', 3)

@State
def UGO_UltimateAssault_AtkEff5():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
    sprite('Action_245_00', 3)
    sprite('Action_245_01', 3)
    sprite('Action_245_02', 3)
    sprite('Action_245_03', 3)
    sprite('Action_245_04', 3)

@State
def UGO_Ultimate_AtkCol_0():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown2019(1)
        Unknown2003(1)
    sprite('Action_249_01', 10)
    SFX_3('SE045')

@State
def UGO_Ultimate_AtkCol_1():

    def upon_IMMEDIATE():
        Unknown26('UGO_Ultimate_AtkCol_0')
        Unknown2011()
        Unknown4010(3)
        Unknown4009(3)
        Unknown4007(3)
        Unknown2019(1)
        Unknown2003(1)
    sprite('Action_249_02', 3)
    RefreshMultihit()
    SFX_3('SE045')
    sprite('Action_249_03', 3)
    SFX_3('SE045')
    sprite('Action_249_04', 3)
    RefreshMultihit()
    SFX_3('SE045')
    sprite('Action_249_01', 3)
    SFX_3('SE045')
    sprite('Action_249_02', 3)
    RefreshMultihit()
    SFX_3('SE045')
    loopRest()
    sprite('Action_249_04', 3)
    SFX_3('SE045')
    sprite('Action_249_01', 3)
    SFX_3('SE045')
    sprite('Action_249_02', 3)
    SFX_3('SE045')
    sprite('Action_249_03', 3)
    SFX_3('SE045')
    sprite('Action_249_04', 3)
    SFX_3('SE045')
    sprite('Action_249_01', 3)
    SFX_3('SE045')
    sprite('Action_249_02', 3)
    SFX_3('SE045')
    sprite('Action_249_03', 3)
    SFX_3('SE045')
    sprite('Action_249_04', 3)
    SFX_3('SE045')
    sprite('Action_249_01', 3)
    SFX_3('SE045')

@State
def UGO_Ultimate_AtkCol_1_OD():

    def upon_IMMEDIATE():
        Unknown26('UGO_Ultimate_AtkCol_0')
        Unknown2011()
        Unknown4010(3)
        Unknown4009(3)
        Unknown4007(3)
        Unknown2019(1)
        Unknown2003(1)
    sprite('Action_249_02', 3)
    SFX_3('SE045')
    sprite('Action_249_03', 3)
    SFX_3('SE045')
    sprite('Action_249_04', 3)
    SFX_3('SE045')
    sprite('Action_249_01', 3)
    SFX_3('SE045')
    sprite('Action_249_02', 3)
    SFX_3('SE045')
    sprite('Action_249_03', 3)
    SFX_3('SE045')
    sprite('Action_249_04', 3)
    SFX_3('SE045')
    sprite('Action_249_01', 2)
    SFX_3('SE045')
    sprite('Action_249_02', 2)
    SFX_3('SE045')
    sprite('Action_249_03', 2)
    SFX_3('SE045')
    sprite('Action_249_04', 2)
    SFX_3('SE045')
    sprite('Action_249_03', 2)
    SFX_3('SE045')
    sprite('Action_249_04', 2)
    SFX_3('SE045')
    sprite('Action_249_01', 2)
    SFX_3('SE045')
    sprite('Action_249_02', 2)
    SFX_3('SE045')
    sprite('Action_249_03', 2)
    SFX_3('SE045')
    sprite('Action_249_04', 2)
    SFX_3('SE045')
    sprite('Action_249_01', 2)
    SFX_3('SE045')
    sprite('Action_249_02', 2)
    SFX_3('SE045')
    sprite('Action_249_03', 2)
    SFX_3('SE045')
    sprite('Action_249_04', 2)
    SFX_3('SE045')
    sprite('Action_249_01', 2)
    SFX_3('SE045')
    sprite('Action_249_02', 2)
    SFX_3('SE045')
    sprite('Action_249_03', 2)
    SFX_3('SE045')
    sprite('Action_249_04', 2)
    SFX_3('SE045')
    sprite('Action_249_01', 2)
    SFX_3('SE045')
    sprite('Action_249_02', 2)
    SFX_3('SE045')
    sprite('Action_249_03', 2)
    SFX_3('SE045')
    sprite('Action_249_04', 2)
    SFX_3('SE045')
    sprite('Action_249_01', 2)
    SFX_3('SE045')
    sprite('Action_249_02', 2)
    SFX_3('SE045')
    sprite('Action_249_03', 2)

@State
def UGO_UltimateAssault_AtkEff_Fini():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown2019(1)
    sprite('Action_246_00', 5)
    sprite('Action_246_01', 5)
    sprite('Action_246_02', 4)
    sprite('Action_246_03', 3)
    sprite('Action_246_04', 3)
    sprite('Action_246_05', 3)
    sprite('Action_246_06', 3)

@State
def UGO_UltimateAssault_AtkEff_Fini():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown2019(1)
    sprite('Action_246_00', 5)
    sprite('Action_246_01', 5)
    sprite('Action_246_02', 4)
    sprite('Action_246_03', 3)
    sprite('Action_246_04', 3)
    sprite('Action_246_05', 3)
    sprite('Action_246_06', 3)

@State
def UGO_UltimateAssault_Start_TAG1():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown2019(1)
    sprite('Action_249_01', 10)
    SFX_3('SE045')

@State
def UGO_UltimateAssault_Start_TAG2():

    def upon_IMMEDIATE():
        Unknown26('UGO_UltimateAssault_Start_TAG1')
        Unknown4007(3)
        Unknown4010(3)
        Unknown2019(1)
    sprite('Action_249_02', 3)
    SFX_3('SE045')
    sprite('Action_249_03', 3)
    SFX_3('SE045')
    sprite('Action_249_04', 3)
    SFX_3('SE045')
    sprite('Action_249_01', 3)
    SFX_3('SE045')
    sprite('Action_249_02', 3)
    SFX_3('SE045')
    loopRest()

@State
def UGO_AstralBlade1():

    def upon_IMMEDIATE():
        EnableCollision(0)
        Unknown2053(0)
        Unknown2034(0)
        Unknown2054(1)
    sprite('Action_211_00', 4)
    sprite('Action_211_01', 4)
    sprite('Action_211_02', 4)
    sprite('Action_211_03', 4)
    sprite('Action_211_04', 4)

@State
def UGO_AstralBlade2():

    def upon_IMMEDIATE():
        EnableCollision(0)
        Unknown2053(0)
        Unknown2034(0)
        Unknown2054(1)
    sprite('Action_209_00', 3)
    sprite('Action_209_01', 3)
    sprite('Action_209_02', 3)
    sprite('Action_209_03', 3)
    sprite('Action_209_04', 3)
    sprite('Action_209_05', 3)

@State
def UGO_AstralEff1():

    def upon_IMMEDIATE():
        EnableCollision(0)
        Unknown2053(0)
        Unknown2034(0)
        Unknown2054(1)
        Unknown1086(22)
        teleportRelativeX(50000)
        Unknown1007(100000)
    sprite('Action_212_00', 4)
    sprite('Action_212_01', 4)
    sprite('Action_212_02', 4)
    sprite('Action_212_03', 4)

@State
def UGO_AstralEff2():

    def upon_IMMEDIATE():
        EnableCollision(0)
        Unknown2053(0)
        Unknown2034(0)
        Unknown2054(1)
        teleportRelativeX(-75000)
    sprite('Action_213_00', 4)
    label(0)
    sprite('Action_213_01', 7)
    sprite('Action_213_02', 7)
    sprite('Action_213_03', 7)
    gotoLabel(0)

@State
def UGO_AstralEff3():

    def upon_IMMEDIATE():
        EnableCollision(0)
        Unknown2053(0)
        Unknown2034(0)
        Unknown2054(1)
        Unknown1086(22)
        Unknown1007(85000)
    sprite('Action_214_00', 4)
    sprite('Action_214_01', 4)
    sprite('Action_214_02', 4)
    sprite('Action_214_03', 4)
    sprite('Action_214_04', 4)

@State
def UGO_AstralFinishBlade1():

    def upon_IMMEDIATE():
        Unknown2054(1)
        EnableCollision(0)
        Unknown2053(0)
        Unknown2034(0)
    sprite('Action_217_00', 4)
    sprite('Action_217_01', 4)
    sprite('Action_217_02', 4)
    sprite('Action_217_03', 4)
    sprite('Action_217_04', 4)
    sprite('Action_217_05', 4)
    sprite('Action_217_06', 4)
    sprite('Action_217_07', 4)
    sprite('Action_217_08', 4)
    sprite('Action_217_09', 4)

@State
def UGO_AstralFinishImpact():

    def upon_IMMEDIATE():
        Unknown2054(1)
        EnableCollision(0)
        Unknown2053(0)
        Unknown2034(0)
        Unknown26('AstralDrainYarare2')
    sprite('Action_218_00', 4)
    sprite('Action_218_01', 4)
    sprite('Action_218_02', 4)
    sprite('Action_218_03', 4)
    sprite('Action_218_04', 4)
    sprite('Action_218_05', 32767)
    Unknown36(22)
    Unknown3038(1)
    setGravity(0)
    Unknown35()

    def upon_3():
        Unknown1086(3)

@State
def UGO_WhiteIn():

    def upon_IMMEDIATE():
        Unknown1000(0)
        Unknown26('UGO_AstralFinishImpact')
        Unknown2054(1)
        EnableCollision(0)
        Unknown2053(0)
        Unknown2034(0)
    sprite('Action_219_00', 4)
    Unknown23033(60)
    sprite('Action_219_01', 4)
    sprite('Action_219_02', 4)
    sprite('Action_219_03', 4)
    sprite('Action_219_04', 4)
    sprite('Action_219_05', 4)
    sprite('Action_219_06', 4)

@State
def UGO_WhiteDummy():
    sprite('Action_218_05', 30)

@State
def UGO_AstralCutIn():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown2054(1)
        Unknown23015(5)
        Unknown6001(1)
        Unknown1000(640000)
        teleportRelativeY(-640000)
        if SLOT_38:
            Unknown1000(-640000)
        EnableCollision(0)
        Unknown2053(0)
        Unknown2034(0)
    sprite('null', 2)
    sprite('Action_999_01', 3)
    sprite('Action_999_02', 3)
    sprite('Action_999_03', 3)
    sprite('Action_999_04', 3)
    sprite('Action_999_05', 6)
    sprite('Action_999_06', 4)
    sprite('Action_999_07', 5)
    sprite('Action_999_08', 4)
    sprite('Action_999_09', 4)
    sprite('Action_999_10', 4)
    sprite('Action_999_11', 6)
    sprite('Action_999_12', 3)
    sprite('Action_999_13', 3)
    sprite('Action_999_14', 3)
    sprite('Action_999_15', 2)
    sprite('Action_999_16', 3)
    sprite('Action_999_17', 3)
    Unknown3001(200)
    Unknown3004(-20)
    Unknown1099(100)
    sprite('Action_999_18', 3)
    sprite('Action_999_19', 3)
    sprite('Action_999_20', 1)

@State
def UGO_AstralBG():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23015(2)
        EnableCollision(0)
        Unknown2053(0)
        Unknown2034(0)

        def upon_3():
            Unknown23057(50)
            Unknown23058(50)

        def upon_32():
            clearUponHandler(3)
            Unknown1007(200000)
    sprite('Action_210_00', 30)
    label(0)
    sprite('Action_210_01', 4)
    sprite('Action_210_02', 4)
    loopRest()
    gotoLabel(0)

@State
def AstralBoundDummy():

    def upon_IMMEDIATE():
        Unknown2012()
        Unknown4010(3)
        Unknown11067(1)
        Damage(0)
        MinimumDamagePct(100)
        AirPushbackX(-800)
        AirPushbackY(4000)
        AirUntechableTime(600)
        YImpluseBeforeWallbounce(33)
        Hitstop(0)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown11062(1)
        Unknown1086(22)
        Unknown11050(5, '')
    sprite('astral_dammy_atk', 3)
    RefreshMultihit()

@State
def AstralDrainYarare():

    def upon_IMMEDIATE():
        Unknown1096(750)
        Unknown2054(1)
        Unknown11062(1)
        Unknown11067(1)

        def upon_45():
            Unknown1086(22)
            teleportRelativeX(100000)
            Unknown1007(100000)
    sprite('Action_216_00', 4)
    sprite('Action_216_01', 4)
    sprite('Action_216_02', 4)
    sprite('Action_216_03', 4)
    sprite('Action_216_04', 4)
    sprite('Action_216_01', 4)
    sprite('Action_216_02', 4)
    sprite('Action_216_03', 4)
    sprite('Action_216_04', 4)
    sprite('Action_216_01', 4)
    sprite('Action_216_02', 4)
    sprite('Action_216_03', 4)
    sprite('Action_216_04', 4)
    sprite('Action_216_01', 4)
    sprite('Action_216_02', 4)
    sprite('Action_216_03', 4)
    sprite('Action_216_04', 4)
    sprite('Action_216_05', 4)

@State
def AstralDrainYarare2():

    def upon_IMMEDIATE():
        Unknown1096(500)
        Unknown2054(1)
        Unknown11062(1)
        Unknown11067(1)

        def upon_45():
            Unknown1086(22)
            teleportRelativeX(100000)
            Unknown1007(100000)
    sprite('Action_216_00', 4)
    label(0)
    sprite('Action_216_01', 4)
    sprite('Action_216_02', 4)
    sprite('Action_216_03', 4)
    sprite('Action_216_04', 4)
    gotoLabel(0)

@State
def AstralShaker():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown1086(3)
        Unknown2054(1)
        Unknown23015(2)
        EnableCollision(0)
        Unknown2053(0)
        Unknown2034(0)
    label(0)
    sprite('null', 4)
    ScreenShake(3000, 3000)
    SFX_0('019_quake_0')
    sprite('null', 4)
    ScreenShake(3000, 3000)
    SFX_0('019_quake_0')
    loopRest()
    gotoLabel(0)

@State
def AstralCamera():

    def upon_IMMEDIATE():
        Unknown2054(1)
        EnableCollision(0)
        Unknown2053(0)
        Unknown2034(0)
        Unknown20003(1)
        Unknown20004(1)
        Unknown20000(1)
        sendToLabelUpon(33, 1)
        sendToLabelUpon(34, 2)
        sendToLabelUpon(35, 3)
        GFX_0('UGO_AstralBG', 100)
    label(0)
    sprite('null', 32767)
    Unknown1086(3)
    label(1)
    sprite('null', 7)
    clearUponHandler(45)
    Unknown1086(3)
    physicsXImpulse(40000)
    sprite('null', 32767)
    Unknown1084(1)
    label(2)
    sprite('null', 5)
    Unknown1007(150000)
    physicsYImpulse(62000)
    sprite('null', 32767)
    Unknown1084(1)
    label(3)
    sprite('null', 2)
    physicsYImpulse(-150000)
    sprite('null', 32767)
    teleportRelativeY(0)
    Unknown26('AstralShaker')
    ScreenShake(25000, 25000)

@State
def UGO_Entry_SummonOut():

    def upon_IMMEDIATE():
        Unknown2054(1)
        teleportRelativeX(48000)
        Unknown2019(1000)
    sprite('Action_079_00', 4)
    sprite('Action_079_01', 4)
    sprite('Action_079_02', 4)

@State
def UGO_MatchWin_SummonIn():

    def upon_IMMEDIATE():
        Unknown2054(1)
    sprite('Action_080_00', 3)
    sprite('Action_080_01', 3)
    sprite('Action_080_02', 3)
    sprite('Action_080_03', 3)