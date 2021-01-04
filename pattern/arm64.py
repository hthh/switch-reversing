def is_dataproc_immediate(d): return (d & 0x1c000000) == 0x10000000
def is_branch_and_sys(d): return (d & 0x1c000000) == 0x14000000
def is_load_and_store(d): return (d & 0x0a000000) == 0x08000000
def is_dataproc_register(d): return (d & 0x0e000000) == 0x0a000000
def is_dataproc_simd(d): return (d & 0x0e000000) == 0x0e000000
def is_pcreladdr(d): return (d & 0x1f000000) == 0x10000000
def is_addsub_imm(d): return (d & 0x1f000000) == 0x11000000
def is_log_imm(d): return (d & 0x1f800000) == 0x12000000
def is_movewide(d): return (d & 0x1f800000) == 0x12800000
def is_bitfield(d): return (d & 0x1f800000) == 0x13000000
def is_extract(d): return (d & 0x1f800000) == 0x13800000
def is_condbranch(d): return (d & 0xfe000000) == 0x54000000
def is_exception(d): return (d & 0xff000000) == 0xd4000000
def is_system(d): return (d & 0xffc00000) == 0xd5000000
def is_branch_reg(d): return (d & 0xfe000000) == 0xd6000000
def is_branch_imm(d): return (d & 0x7c000000) == 0x14000000
def is_compbranch(d): return (d & 0x7e000000) == 0x34000000
def is_testbranch(d): return (d & 0x7e000000) == 0x36000000
def is_asisdlse(d): return (d & 0xbfbf0000) == 0x0c000000
def is_asisdlsep(d): return (d & 0xbfa00000) == 0x0c800000
def is_asisdlso(d): return (d & 0xbf9f0000) == 0x0d000000
def is_asisdlsop(d): return (d & 0xbf800000) == 0x0d800000
def is_ldstexcl(d): return (d & 0x3f000000) == 0x08000000
def is_loadlit(d): return (d & 0x3b000000) == 0x18000000
def is_ldstnapair_offs(d): return (d & 0x3b800000) == 0x28000000
def is_ldstpair_post(d): return (d & 0x3b800000) == 0x28800000
def is_ldstpair_off(d): return (d & 0x3b800000) == 0x29000000
def is_ldstpair_pre(d): return (d & 0x3b800000) == 0x29800000
def is_ldst_unscaled(d): return (d & 0x3b200c00) == 0x38000000
def is_ldst_immpost(d): return (d & 0x3b200c00) == 0x38000400
def is_ldst_unpriv(d): return (d & 0x3b200c00) == 0x38000800
def is_ldst_immpre(d): return (d & 0x3b200c00) == 0x38000c00
def is_memop(d): return (d & 0x3b200c00) == 0x38200000
def is_ldst_regoff(d): return (d & 0x3b200c00) == 0x38200800
def is_ldst_pac(d): return (d & 0x3b200400) == 0x38200400
def is_ldst_pos(d): return (d & 0x3b000000) == 0x39000000
def is_dp_2src(d): return (d & 0x5fe00000) == 0x1ac00000
def is_dp_1src(d): return (d & 0x5fe00000) == 0x5ac00000
def is_log_shift(d): return (d & 0x1f000000) == 0x0a000000
def is_addsub_shift(d): return (d & 0x1f200000) == 0x0b000000
def is_addsub_ext(d): return (d & 0x1f200000) == 0x0b200000
def is_addsub_carry(d): return (d & 0x1fe00000) == 0x1a000000
def is_condcmp_reg(d): return (d & 0x1fe00800) == 0x1a400000
def is_condcmp_imm(d): return (d & 0x1fe00800) == 0x1a400800
def is_condsel(d): return (d & 0x1fe00000) == 0x1a800000
def is_dp_3src(d): return (d & 0x1f000000) == 0x1b000000
def is_cryptoaes(d): return (d & 0xff3e0c00) == 0x4e280800
def is_cryptosha3(d): return (d & 0xff208c00) == 0x5e000000
def is_cryptosha2(d): return (d & 0xff3e0c00) == 0x5e280800
def is_asisdone(d): return (d & 0xdfe08400) == 0x5e000400
def is_asisdsamefp16(d): return (d & 0xdf60c400) == 0x5e400400
def is_asisdmiscfp16(d): return (d & 0xdf7e0c00) == 0x5e780800
def is_asisdsame2(d): return (d & 0xdf208400) == 0x5e008400
def is_asisdmisc(d): return (d & 0xdf3e0c00) == 0x5e200800
def is_asisdpair(d): return (d & 0xdf3e0c00) == 0x5e300800
def is_asisddiff(d): return (d & 0xdf200c00) == 0x5e200000
def is_asisdsame(d): return (d & 0xdf200400) == 0x5e200400
def is_asisdshf(d): return (d & 0xdf800400) == 0x5f000400
def is_asisdelem(d): return (d & 0xdf000400) == 0x5f000000
def is_asimdtbl(d): return (d & 0xbf208c00) == 0x0e000000
def is_asimdperm(d): return (d & 0xbf208c00) == 0x0e000800
def is_asimdext(d): return (d & 0xbf208400) == 0x2e000000
def is_asimdins(d): return (d & 0x9fe08400) == 0x0e000400
def is_asimdsamefp16(d): return (d & 0x9f60c400) == 0x0e400400
def is_asimdmiscfp16(d): return (d & 0x9f7e0c00) == 0x0e780800
def is_asimdsame2(d): return (d & 0x9f208400) == 0x0e008400
def is_asimdmisc(d): return (d & 0x9f3e0c00) == 0x0e200800
def is_asimdall(d): return (d & 0x9f3e0c00) == 0x0e300800
def is_asimddiff(d): return (d & 0x9f200c00) == 0x0e200000
def is_asimdsame(d): return (d & 0x9f200400) == 0x0e200400
def is_asimdimm(d): return (d & 0x9ff80400) == 0x0f000400
def is_asimdshf(d): return (d & 0x9f800400) == 0x0f000400 and (d & 0x780000) != 0x000000
def is_asimdelem(d): return (d & 0x9f000400) == 0x0f000000
def is_crypto3_imm2(d): return (d & 0xffe0c000) == 0xce408000
def is_cryptosha512_3(d): return (d & 0xffe0b000) == 0xce608000
def is_crypto4(d): return (d & 0xff808000) == 0xce000000
def is_crypto3_imm6(d): return (d & 0xffe00000) == 0xce800000
def is_cryptosha512_2(d): return (d & 0xfffff000) == 0xcec08000
def is_float2fix(d): return (d & 0x5f200000) == 0x1e000000
def is_float2int(d): return (d & 0x5f20fc00) == 0x1e200000
def is_floatdp1(d): return (d & 0x5f207c00) == 0x1e204000
def is_floatcmp(d): return (d & 0x5f203c00) == 0x1e202000
def is_floatimm(d): return (d & 0x5f201c00) == 0x1e201000
def is_floatccmp(d): return (d & 0x5f200c00) == 0x1e200400
def is_floatdp2(d): return (d & 0x5f200c00) == 0x1e200800
def is_floatsel(d): return (d & 0x5f200c00) == 0x1e200c00
def is_floatdp3(d): return (d & 0x5f000000) == 0x1f000000
def is_CBZ_32_compbranch(d): return (d & 0xff000000) == 0x34000000
def is_CBNZ_32_compbranch(d): return (d & 0xff000000) == 0x35000000
def is_CBZ_64_compbranch(d): return (d & 0xff000000) == 0xb4000000
def is_CBNZ_64_compbranch(d): return (d & 0xff000000) == 0xb5000000
def is_B_only_condbranch(d): return (d & 0xff000010) == 0x54000000
def is_SVC_EX_exception(d): return (d & 0xffe0001f) == 0xd4000001
def is_HVC_EX_exception(d): return (d & 0xffe0001f) == 0xd4000002
def is_SMC_EX_exception(d): return (d & 0xffe0001f) == 0xd4000003
def is_BRK_EX_exception(d): return (d & 0xffe0001f) == 0xd4200000
def is_HLT_EX_exception(d): return (d & 0xffe0001f) == 0xd4400000
def is_DCPS1_DC_exception(d): return (d & 0xffe0001f) == 0xd4a00001
def is_DCPS2_DC_exception(d): return (d & 0xffe0001f) == 0xd4a00002
def is_DCPS3_DC_exception(d): return (d & 0xffe0001f) == 0xd4a00003
def is_MSR_SI_system(d): return (d & 0xfff8f01f) == 0xd500401f
def is_HINT_2(d): return (d & 0xfffff01f) == 0xd503201f and (d & 0x000d00) != 0x000000
def is_NOP_HI_system(d): return (d & 0xffffffff) == 0xd503201f
def is_YIELD_HI_system(d): return (d & 0xffffffff) == 0xd503203f
def is_WFE_HI_system(d): return (d & 0xffffffff) == 0xd503205f
def is_WFI_HI_system(d): return (d & 0xffffffff) == 0xd503207f
def is_SEV_HI_system(d): return (d & 0xffffffff) == 0xd503209f
def is_SEVL_HI_system(d): return (d & 0xffffffff) == 0xd50320bf
def is_HINT_1(d): return (d & 0xffffffdf) == 0xd50320df
def is_XPACLRI_HI_system(d): return (d & 0xffffffff) == 0xd50320ff
def is_PACIA1716_HI_system(d): return (d & 0xffffffff) == 0xd503211f
def is_PACIB1716_HI_system(d): return (d & 0xffffffff) == 0xd503215f
def is_AUTIA1716_HI_system(d): return (d & 0xffffffff) == 0xd503219f
def is_AUTIB1716_HI_system(d): return (d & 0xffffffff) == 0xd50321df
def is_HINT_3(d): return (d & 0xffffff1f) == 0xd503221f and (d & 0x0000c0) != 0x000000
def is_ESB_HI_system(d): return (d & 0xffffffff) == 0xd503221f
def is_PSB_HC_system(d): return (d & 0xffffffff) == 0xd503223f
def is_PACIAZ_HI_system(d): return (d & 0xffffffff) == 0xd503231f
def is_PACIASP_HI_system(d): return (d & 0xffffffff) == 0xd503233f
def is_PACIBZ_HI_system(d): return (d & 0xffffffff) == 0xd503235f
def is_PACIBSP_HI_system(d): return (d & 0xffffffff) == 0xd503237f
def is_AUTIAZ_HI_system(d): return (d & 0xffffffff) == 0xd503239f
def is_AUTIASP_HI_system(d): return (d & 0xffffffff) == 0xd50323bf
def is_AUTIBZ_HI_system(d): return (d & 0xffffffff) == 0xd50323df
def is_AUTIBSP_HI_system(d): return (d & 0xffffffff) == 0xd50323ff
def is_CLREX_BN_system(d): return (d & 0xfffff0ff) == 0xd503305f
def is_DSB_BO_system(d): return (d & 0xfffff0ff) == 0xd503309f
def is_DMB_BO_system(d): return (d & 0xfffff0ff) == 0xd50330bf
def is_ISB_BI_system(d): return (d & 0xfffff0ff) == 0xd50330df
def is_SYS_CR_system(d): return (d & 0xfff80000) == 0xd5080000
def is_MSR_SR_system(d): return (d & 0xfff00000) == 0xd5100000
def is_SYSL_RC_system(d): return (d & 0xfff80000) == 0xd5280000
def is_MRS_RS_system(d): return (d & 0xfff00000) == 0xd5300000
def is_TBZ_only_testbranch(d): return (d & 0x7f000000) == 0x36000000
def is_TBNZ_only_testbranch(d): return (d & 0x7f000000) == 0x37000000
def is_B_only_branch_imm(d): return (d & 0xfc000000) == 0x14000000
def is_BL_only_branch_imm(d): return (d & 0xfc000000) == 0x94000000
def is_BR_64_branch_reg(d): return (d & 0xfffffc1f) == 0xd61f0000
def is_BRAAZ_64_branch_reg(d): return (d & 0xfffffc1f) == 0xd61f081f
def is_BRABZ_64_branch_reg(d): return (d & 0xfffffc1f) == 0xd61f0c1f
def is_BLR_64_branch_reg(d): return (d & 0xfffffc1f) == 0xd63f0000
def is_BLRAAZ_64_branch_reg(d): return (d & 0xfffffc1f) == 0xd63f081f
def is_BLRABZ_64_branch_reg(d): return (d & 0xfffffc1f) == 0xd63f0c1f
def is_RET_64R_branch_reg(d): return (d & 0xfffffc1f) == 0xd65f0000
def is_RETAA_64E_branch_reg(d): return (d & 0xffffffff) == 0xd65f0bff
def is_RETAB_64E_branch_reg(d): return (d & 0xffffffff) == 0xd65f0fff
def is_ERET_64E_branch_reg(d): return (d & 0xffffffff) == 0xd69f03e0
def is_ERETAA_64E_branch_reg(d): return (d & 0xffffffff) == 0xd69f0bff
def is_ERETAB_64E_branch_reg(d): return (d & 0xffffffff) == 0xd69f0fff
def is_DRPS_64E_branch_reg(d): return (d & 0xffffffff) == 0xd6bf03e0
def is_BRAA_64P_branch_reg(d): return (d & 0xfffffc00) == 0xd71f0800
def is_BRAB_64P_branch_reg(d): return (d & 0xfffffc00) == 0xd71f0c00
def is_BLRAA_64P_branch_reg(d): return (d & 0xfffffc00) == 0xd73f0800
def is_BLRAB_64P_branch_reg(d): return (d & 0xfffffc00) == 0xd73f0c00
def is_ST4_asisdlse_R4(d): return (d & 0xbffff000) == 0x0c000000
def is_ST1_asisdlse_R4_4v(d): return (d & 0xbffff000) == 0x0c002000
def is_ST3_asisdlse_R3(d): return (d & 0xbffff000) == 0x0c004000
def is_ST1_asisdlse_R3_3v(d): return (d & 0xbffff000) == 0x0c006000
def is_ST1_asisdlse_R1_1v(d): return (d & 0xbffff000) == 0x0c007000
def is_ST2_asisdlse_R2(d): return (d & 0xbffff000) == 0x0c008000
def is_ST1_asisdlse_R2_2v(d): return (d & 0xbffff000) == 0x0c00a000
def is_LD4_asisdlse_R4(d): return (d & 0xbffff000) == 0x0c400000
def is_LD1_asisdlse_R4_4v(d): return (d & 0xbffff000) == 0x0c402000
def is_LD3_asisdlse_R3(d): return (d & 0xbffff000) == 0x0c404000
def is_LD1_asisdlse_R3_3v(d): return (d & 0xbffff000) == 0x0c406000
def is_LD1_asisdlse_R1_1v(d): return (d & 0xbffff000) == 0x0c407000
def is_LD2_asisdlse_R2(d): return (d & 0xbffff000) == 0x0c408000
def is_LD1_asisdlse_R2_2v(d): return (d & 0xbffff000) == 0x0c40a000
def is_ST4_asisdlsep_R4_r(d): return (d & 0xbfe0f000) == 0x0c800000 and (d & 0x1f0000) != 0x1f0000
def is_ST1_asisdlsep_R4_r4(d): return (d & 0xbfe0f000) == 0x0c802000 and (d & 0x1f0000) != 0x1f0000
def is_ST3_asisdlsep_R3_r(d): return (d & 0xbfe0f000) == 0x0c804000 and (d & 0x1f0000) != 0x1f0000
def is_ST1_asisdlsep_R3_r3(d): return (d & 0xbfe0f000) == 0x0c806000 and (d & 0x1f0000) != 0x1f0000
def is_ST1_asisdlsep_R1_r1(d): return (d & 0xbfe0f000) == 0x0c807000 and (d & 0x1f0000) != 0x1f0000
def is_ST2_asisdlsep_R2_r(d): return (d & 0xbfe0f000) == 0x0c808000 and (d & 0x1f0000) != 0x1f0000
def is_ST1_asisdlsep_R2_r2(d): return (d & 0xbfe0f000) == 0x0c80a000 and (d & 0x1f0000) != 0x1f0000
def is_ST4_asisdlsep_I4_i(d): return (d & 0xbffff000) == 0x0c9f0000
def is_ST1_asisdlsep_I4_i4(d): return (d & 0xbffff000) == 0x0c9f2000
def is_ST3_asisdlsep_I3_i(d): return (d & 0xbffff000) == 0x0c9f4000
def is_ST1_asisdlsep_I3_i3(d): return (d & 0xbffff000) == 0x0c9f6000
def is_ST1_asisdlsep_I1_i1(d): return (d & 0xbffff000) == 0x0c9f7000
def is_ST2_asisdlsep_I2_i(d): return (d & 0xbffff000) == 0x0c9f8000
def is_ST1_asisdlsep_I2_i2(d): return (d & 0xbffff000) == 0x0c9fa000
def is_LD4_asisdlsep_R4_r(d): return (d & 0xbfe0f000) == 0x0cc00000 and (d & 0x1f0000) != 0x1f0000
def is_LD1_asisdlsep_R4_r4(d): return (d & 0xbfe0f000) == 0x0cc02000 and (d & 0x1f0000) != 0x1f0000
def is_LD3_asisdlsep_R3_r(d): return (d & 0xbfe0f000) == 0x0cc04000 and (d & 0x1f0000) != 0x1f0000
def is_LD1_asisdlsep_R3_r3(d): return (d & 0xbfe0f000) == 0x0cc06000 and (d & 0x1f0000) != 0x1f0000
def is_LD1_asisdlsep_R1_r1(d): return (d & 0xbfe0f000) == 0x0cc07000 and (d & 0x1f0000) != 0x1f0000
def is_LD2_asisdlsep_R2_r(d): return (d & 0xbfe0f000) == 0x0cc08000 and (d & 0x1f0000) != 0x1f0000
def is_LD1_asisdlsep_R2_r2(d): return (d & 0xbfe0f000) == 0x0cc0a000 and (d & 0x1f0000) != 0x1f0000
def is_LD4_asisdlsep_I4_i(d): return (d & 0xbffff000) == 0x0cdf0000
def is_LD1_asisdlsep_I4_i4(d): return (d & 0xbffff000) == 0x0cdf2000
def is_LD3_asisdlsep_I3_i(d): return (d & 0xbffff000) == 0x0cdf4000
def is_LD1_asisdlsep_I3_i3(d): return (d & 0xbffff000) == 0x0cdf6000
def is_LD1_asisdlsep_I1_i1(d): return (d & 0xbffff000) == 0x0cdf7000
def is_LD2_asisdlsep_I2_i(d): return (d & 0xbffff000) == 0x0cdf8000
def is_LD1_asisdlsep_I2_i2(d): return (d & 0xbffff000) == 0x0cdfa000
def is_ST1_asisdlso_B1_1b(d): return (d & 0xbfffe000) == 0x0d000000
def is_ST3_asisdlso_B3_3b(d): return (d & 0xbfffe000) == 0x0d002000
def is_ST1_asisdlso_H1_1h(d): return (d & 0xbfffe400) == 0x0d004000
def is_ST3_asisdlso_H3_3h(d): return (d & 0xbfffe400) == 0x0d006000
def is_ST1_asisdlso_S1_1s(d): return (d & 0xbfffec00) == 0x0d008000
def is_ST1_asisdlso_D1_1d(d): return (d & 0xbffffc00) == 0x0d008400
def is_ST3_asisdlso_S3_3s(d): return (d & 0xbfffec00) == 0x0d00a000
def is_ST3_asisdlso_D3_3d(d): return (d & 0xbffffc00) == 0x0d00a400
def is_ST2_asisdlso_B2_2b(d): return (d & 0xbfffe000) == 0x0d200000
def is_ST4_asisdlso_B4_4b(d): return (d & 0xbfffe000) == 0x0d202000
def is_ST2_asisdlso_H2_2h(d): return (d & 0xbfffe400) == 0x0d204000
def is_ST4_asisdlso_H4_4h(d): return (d & 0xbfffe400) == 0x0d206000
def is_ST2_asisdlso_S2_2s(d): return (d & 0xbfffec00) == 0x0d208000
def is_ST2_asisdlso_D2_2d(d): return (d & 0xbffffc00) == 0x0d208400
def is_ST4_asisdlso_S4_4s(d): return (d & 0xbfffec00) == 0x0d20a000
def is_ST4_asisdlso_D4_4d(d): return (d & 0xbffffc00) == 0x0d20a400
def is_LD1_asisdlso_B1_1b(d): return (d & 0xbfffe000) == 0x0d400000
def is_LD3_asisdlso_B3_3b(d): return (d & 0xbfffe000) == 0x0d402000
def is_LD1_asisdlso_H1_1h(d): return (d & 0xbfffe400) == 0x0d404000
def is_LD3_asisdlso_H3_3h(d): return (d & 0xbfffe400) == 0x0d406000
def is_LD1_asisdlso_S1_1s(d): return (d & 0xbfffec00) == 0x0d408000
def is_LD1_asisdlso_D1_1d(d): return (d & 0xbffffc00) == 0x0d408400
def is_LD3_asisdlso_S3_3s(d): return (d & 0xbfffec00) == 0x0d40a000
def is_LD3_asisdlso_D3_3d(d): return (d & 0xbffffc00) == 0x0d40a400
def is_LD1R_asisdlso_R1(d): return (d & 0xbffff000) == 0x0d40c000
def is_LD3R_asisdlso_R3(d): return (d & 0xbffff000) == 0x0d40e000
def is_LD2_asisdlso_B2_2b(d): return (d & 0xbfffe000) == 0x0d600000
def is_LD4_asisdlso_B4_4b(d): return (d & 0xbfffe000) == 0x0d602000
def is_LD2_asisdlso_H2_2h(d): return (d & 0xbfffe400) == 0x0d604000
def is_LD4_asisdlso_H4_4h(d): return (d & 0xbfffe400) == 0x0d606000
def is_LD2_asisdlso_S2_2s(d): return (d & 0xbfffec00) == 0x0d608000
def is_LD2_asisdlso_D2_2d(d): return (d & 0xbffffc00) == 0x0d608400
def is_LD4_asisdlso_S4_4s(d): return (d & 0xbfffec00) == 0x0d60a000
def is_LD4_asisdlso_D4_4d(d): return (d & 0xbffffc00) == 0x0d60a400
def is_LD2R_asisdlso_R2(d): return (d & 0xbffff000) == 0x0d60c000
def is_LD4R_asisdlso_R4(d): return (d & 0xbffff000) == 0x0d60e000
def is_ST1_asisdlsop_BX1_r1b(d): return (d & 0xbfe0e000) == 0x0d800000 and (d & 0x1f0000) != 0x1f0000
def is_ST3_asisdlsop_BX3_r3b(d): return (d & 0xbfe0e000) == 0x0d802000 and (d & 0x1f0000) != 0x1f0000
def is_ST1_asisdlsop_HX1_r1h(d): return (d & 0xbfe0e400) == 0x0d804000 and (d & 0x1f0000) != 0x1f0000
def is_ST3_asisdlsop_HX3_r3h(d): return (d & 0xbfe0e400) == 0x0d806000 and (d & 0x1f0000) != 0x1f0000
def is_ST1_asisdlsop_SX1_r1s(d): return (d & 0xbfe0ec00) == 0x0d808000 and (d & 0x1f0000) != 0x1f0000
def is_ST1_asisdlsop_DX1_r1d(d): return (d & 0xbfe0fc00) == 0x0d808400 and (d & 0x1f0000) != 0x1f0000
def is_ST3_asisdlsop_SX3_r3s(d): return (d & 0xbfe0ec00) == 0x0d80a000 and (d & 0x1f0000) != 0x1f0000
def is_ST3_asisdlsop_DX3_r3d(d): return (d & 0xbfe0fc00) == 0x0d80a400 and (d & 0x1f0000) != 0x1f0000
def is_ST1_asisdlsop_B1_i1b(d): return (d & 0xbfffe000) == 0x0d9f0000
def is_ST3_asisdlsop_B3_i3b(d): return (d & 0xbfffe000) == 0x0d9f2000
def is_ST1_asisdlsop_H1_i1h(d): return (d & 0xbfffe400) == 0x0d9f4000
def is_ST3_asisdlsop_H3_i3h(d): return (d & 0xbfffe400) == 0x0d9f6000
def is_ST1_asisdlsop_S1_i1s(d): return (d & 0xbfffec00) == 0x0d9f8000
def is_ST1_asisdlsop_D1_i1d(d): return (d & 0xbffffc00) == 0x0d9f8400
def is_ST3_asisdlsop_S3_i3s(d): return (d & 0xbfffec00) == 0x0d9fa000
def is_ST3_asisdlsop_D3_i3d(d): return (d & 0xbffffc00) == 0x0d9fa400
def is_ST2_asisdlsop_BX2_r2b(d): return (d & 0xbfe0e000) == 0x0da00000 and (d & 0x1f0000) != 0x1f0000
def is_ST4_asisdlsop_BX4_r4b(d): return (d & 0xbfe0e000) == 0x0da02000 and (d & 0x1f0000) != 0x1f0000
def is_ST2_asisdlsop_HX2_r2h(d): return (d & 0xbfe0e400) == 0x0da04000 and (d & 0x1f0000) != 0x1f0000
def is_ST4_asisdlsop_HX4_r4h(d): return (d & 0xbfe0e400) == 0x0da06000 and (d & 0x1f0000) != 0x1f0000
def is_ST2_asisdlsop_SX2_r2s(d): return (d & 0xbfe0ec00) == 0x0da08000 and (d & 0x1f0000) != 0x1f0000
def is_ST2_asisdlsop_DX2_r2d(d): return (d & 0xbfe0fc00) == 0x0da08400 and (d & 0x1f0000) != 0x1f0000
def is_ST4_asisdlsop_SX4_r4s(d): return (d & 0xbfe0ec00) == 0x0da0a000 and (d & 0x1f0000) != 0x1f0000
def is_ST4_asisdlsop_DX4_r4d(d): return (d & 0xbfe0fc00) == 0x0da0a400 and (d & 0x1f0000) != 0x1f0000
def is_ST2_asisdlsop_B2_i2b(d): return (d & 0xbfffe000) == 0x0dbf0000
def is_ST4_asisdlsop_B4_i4b(d): return (d & 0xbfffe000) == 0x0dbf2000
def is_ST2_asisdlsop_H2_i2h(d): return (d & 0xbfffe400) == 0x0dbf4000
def is_ST4_asisdlsop_H4_i4h(d): return (d & 0xbfffe400) == 0x0dbf6000
def is_ST2_asisdlsop_S2_i2s(d): return (d & 0xbfffec00) == 0x0dbf8000
def is_ST2_asisdlsop_D2_i2d(d): return (d & 0xbffffc00) == 0x0dbf8400
def is_ST4_asisdlsop_S4_i4s(d): return (d & 0xbfffec00) == 0x0dbfa000
def is_ST4_asisdlsop_D4_i4d(d): return (d & 0xbffffc00) == 0x0dbfa400
def is_LD1_asisdlsop_BX1_r1b(d): return (d & 0xbfe0e000) == 0x0dc00000 and (d & 0x1f0000) != 0x1f0000
def is_LD3_asisdlsop_BX3_r3b(d): return (d & 0xbfe0e000) == 0x0dc02000 and (d & 0x1f0000) != 0x1f0000
def is_LD1_asisdlsop_HX1_r1h(d): return (d & 0xbfe0e400) == 0x0dc04000 and (d & 0x1f0000) != 0x1f0000
def is_LD3_asisdlsop_HX3_r3h(d): return (d & 0xbfe0e400) == 0x0dc06000 and (d & 0x1f0000) != 0x1f0000
def is_LD1_asisdlsop_SX1_r1s(d): return (d & 0xbfe0ec00) == 0x0dc08000 and (d & 0x1f0000) != 0x1f0000
def is_LD1_asisdlsop_DX1_r1d(d): return (d & 0xbfe0fc00) == 0x0dc08400 and (d & 0x1f0000) != 0x1f0000
def is_LD3_asisdlsop_SX3_r3s(d): return (d & 0xbfe0ec00) == 0x0dc0a000 and (d & 0x1f0000) != 0x1f0000
def is_LD3_asisdlsop_DX3_r3d(d): return (d & 0xbfe0fc00) == 0x0dc0a400 and (d & 0x1f0000) != 0x1f0000
def is_LD1R_asisdlsop_RX1_r(d): return (d & 0xbfe0f000) == 0x0dc0c000 and (d & 0x1f0000) != 0x1f0000
def is_LD3R_asisdlsop_RX3_r(d): return (d & 0xbfe0f000) == 0x0dc0e000 and (d & 0x1f0000) != 0x1f0000
def is_LD1_asisdlsop_B1_i1b(d): return (d & 0xbfffe000) == 0x0ddf0000
def is_LD3_asisdlsop_B3_i3b(d): return (d & 0xbfffe000) == 0x0ddf2000
def is_LD1_asisdlsop_H1_i1h(d): return (d & 0xbfffe400) == 0x0ddf4000
def is_LD3_asisdlsop_H3_i3h(d): return (d & 0xbfffe400) == 0x0ddf6000
def is_LD1_asisdlsop_S1_i1s(d): return (d & 0xbfffec00) == 0x0ddf8000
def is_LD1_asisdlsop_D1_i1d(d): return (d & 0xbffffc00) == 0x0ddf8400
def is_LD3_asisdlsop_S3_i3s(d): return (d & 0xbfffec00) == 0x0ddfa000
def is_LD3_asisdlsop_D3_i3d(d): return (d & 0xbffffc00) == 0x0ddfa400
def is_LD1R_asisdlsop_R1_i(d): return (d & 0xbffff000) == 0x0ddfc000
def is_LD3R_asisdlsop_R3_i(d): return (d & 0xbffff000) == 0x0ddfe000
def is_LD2_asisdlsop_BX2_r2b(d): return (d & 0xbfe0e000) == 0x0de00000 and (d & 0x1f0000) != 0x1f0000
def is_LD4_asisdlsop_BX4_r4b(d): return (d & 0xbfe0e000) == 0x0de02000 and (d & 0x1f0000) != 0x1f0000
def is_LD2_asisdlsop_HX2_r2h(d): return (d & 0xbfe0e400) == 0x0de04000 and (d & 0x1f0000) != 0x1f0000
def is_LD4_asisdlsop_HX4_r4h(d): return (d & 0xbfe0e400) == 0x0de06000 and (d & 0x1f0000) != 0x1f0000
def is_LD2_asisdlsop_SX2_r2s(d): return (d & 0xbfe0ec00) == 0x0de08000 and (d & 0x1f0000) != 0x1f0000
def is_LD2_asisdlsop_DX2_r2d(d): return (d & 0xbfe0fc00) == 0x0de08400 and (d & 0x1f0000) != 0x1f0000
def is_LD4_asisdlsop_SX4_r4s(d): return (d & 0xbfe0ec00) == 0x0de0a000 and (d & 0x1f0000) != 0x1f0000
def is_LD4_asisdlsop_DX4_r4d(d): return (d & 0xbfe0fc00) == 0x0de0a400 and (d & 0x1f0000) != 0x1f0000
def is_LD2R_asisdlsop_RX2_r(d): return (d & 0xbfe0f000) == 0x0de0c000 and (d & 0x1f0000) != 0x1f0000
def is_LD4R_asisdlsop_RX4_r(d): return (d & 0xbfe0f000) == 0x0de0e000 and (d & 0x1f0000) != 0x1f0000
def is_LD2_asisdlsop_B2_i2b(d): return (d & 0xbfffe000) == 0x0dff0000
def is_LD4_asisdlsop_B4_i4b(d): return (d & 0xbfffe000) == 0x0dff2000
def is_LD2_asisdlsop_H2_i2h(d): return (d & 0xbfffe400) == 0x0dff4000
def is_LD4_asisdlsop_H4_i4h(d): return (d & 0xbfffe400) == 0x0dff6000
def is_LD2_asisdlsop_S2_i2s(d): return (d & 0xbfffec00) == 0x0dff8000
def is_LD2_asisdlsop_D2_i2d(d): return (d & 0xbffffc00) == 0x0dff8400
def is_LD4_asisdlsop_S4_i4s(d): return (d & 0xbfffec00) == 0x0dffa000
def is_LD4_asisdlsop_D4_i4d(d): return (d & 0xbffffc00) == 0x0dffa400
def is_LD2R_asisdlsop_R2_i(d): return (d & 0xbffff000) == 0x0dffc000
def is_LD4R_asisdlsop_R4_i(d): return (d & 0xbffff000) == 0x0dffe000
def is_LDADDB_32_memop(d): return (d & 0xffe0fc00) == 0x38200000 and (d & 0x00001f) != 0x00001f
def is_STADDB_32S_memop(d): return (d & 0xffe0fc1f) == 0x3820001f
def is_LDCLRB_32_memop(d): return (d & 0xffe0fc00) == 0x38201000 and (d & 0x00001f) != 0x00001f
def is_STCLRB_32S_memop(d): return (d & 0xffe0fc1f) == 0x3820101f
def is_LDEORB_32_memop(d): return (d & 0xffe0fc00) == 0x38202000 and (d & 0x00001f) != 0x00001f
def is_STEORB_32S_memop(d): return (d & 0xffe0fc1f) == 0x3820201f
def is_LDSETB_32_memop(d): return (d & 0xffe0fc00) == 0x38203000 and (d & 0x00001f) != 0x00001f
def is_STSETB_32S_memop(d): return (d & 0xffe0fc1f) == 0x3820301f
def is_LDSMAXB_32_memop(d): return (d & 0xffe0fc00) == 0x38204000 and (d & 0x00001f) != 0x00001f
def is_STSMAXB_32S_memop(d): return (d & 0xffe0fc1f) == 0x3820401f
def is_LDSMINB_32_memop(d): return (d & 0xffe0fc00) == 0x38205000 and (d & 0x00001f) != 0x00001f
def is_STSMINB_32S_memop(d): return (d & 0xffe0fc1f) == 0x3820501f
def is_LDUMAXB_32_memop(d): return (d & 0xffe0fc00) == 0x38206000 and (d & 0x00001f) != 0x00001f
def is_STUMAXB_32S_memop(d): return (d & 0xffe0fc1f) == 0x3820601f
def is_LDUMINB_32_memop(d): return (d & 0xffe0fc00) == 0x38207000 and (d & 0x00001f) != 0x00001f
def is_STUMINB_32S_memop(d): return (d & 0xffe0fc1f) == 0x3820701f
def is_SWPB_32_memop(d): return (d & 0xffe0fc00) == 0x38208000
def is_LDADDLB_32_memop(d): return (d & 0xffe0fc00) == 0x38600000 and (d & 0x00001f) != 0x00001f
def is_STADDLB_32S_memop(d): return (d & 0xffe0fc1f) == 0x3860001f
def is_LDCLRLB_32_memop(d): return (d & 0xffe0fc00) == 0x38601000 and (d & 0x00001f) != 0x00001f
def is_STCLRLB_32S_memop(d): return (d & 0xffe0fc1f) == 0x3860101f
def is_LDEORLB_32_memop(d): return (d & 0xffe0fc00) == 0x38602000 and (d & 0x00001f) != 0x00001f
def is_STEORLB_32S_memop(d): return (d & 0xffe0fc1f) == 0x3860201f
def is_LDSETLB_32_memop(d): return (d & 0xffe0fc00) == 0x38603000 and (d & 0x00001f) != 0x00001f
def is_STSETLB_32S_memop(d): return (d & 0xffe0fc1f) == 0x3860301f
def is_LDSMAXLB_32_memop(d): return (d & 0xffe0fc00) == 0x38604000 and (d & 0x00001f) != 0x00001f
def is_STSMAXLB_32S_memop(d): return (d & 0xffe0fc1f) == 0x3860401f
def is_LDSMINLB_32_memop(d): return (d & 0xffe0fc00) == 0x38605000 and (d & 0x00001f) != 0x00001f
def is_STSMINLB_32S_memop(d): return (d & 0xffe0fc1f) == 0x3860501f
def is_LDUMAXLB_32_memop(d): return (d & 0xffe0fc00) == 0x38606000 and (d & 0x00001f) != 0x00001f
def is_STUMAXLB_32S_memop(d): return (d & 0xffe0fc1f) == 0x3860601f
def is_LDUMINLB_32_memop(d): return (d & 0xffe0fc00) == 0x38607000 and (d & 0x00001f) != 0x00001f
def is_STUMINLB_32S_memop(d): return (d & 0xffe0fc1f) == 0x3860701f
def is_SWPLB_32_memop(d): return (d & 0xffe0fc00) == 0x38608000
def is_LDADDAB_32_memop(d): return (d & 0xffe0fc00) == 0x38a00000
def is_LDCLRAB_32_memop(d): return (d & 0xffe0fc00) == 0x38a01000
def is_LDEORAB_32_memop(d): return (d & 0xffe0fc00) == 0x38a02000
def is_LDSETAB_32_memop(d): return (d & 0xffe0fc00) == 0x38a03000
def is_LDSMAXAB_32_memop(d): return (d & 0xffe0fc00) == 0x38a04000
def is_LDSMINAB_32_memop(d): return (d & 0xffe0fc00) == 0x38a05000
def is_LDUMAXAB_32_memop(d): return (d & 0xffe0fc00) == 0x38a06000
def is_LDUMINAB_32_memop(d): return (d & 0xffe0fc00) == 0x38a07000
def is_SWPAB_32_memop(d): return (d & 0xffe0fc00) == 0x38a08000
def is_LDAPRB_32L_memop(d): return (d & 0xffe0fc00) == 0x38a0c000
def is_LDADDALB_32_memop(d): return (d & 0xffe0fc00) == 0x38e00000
def is_LDCLRALB_32_memop(d): return (d & 0xffe0fc00) == 0x38e01000
def is_LDEORALB_32_memop(d): return (d & 0xffe0fc00) == 0x38e02000
def is_LDSETALB_32_memop(d): return (d & 0xffe0fc00) == 0x38e03000
def is_LDSMAXALB_32_memop(d): return (d & 0xffe0fc00) == 0x38e04000
def is_LDSMINALB_32_memop(d): return (d & 0xffe0fc00) == 0x38e05000
def is_LDUMAXALB_32_memop(d): return (d & 0xffe0fc00) == 0x38e06000
def is_LDUMINALB_32_memop(d): return (d & 0xffe0fc00) == 0x38e07000
def is_SWPALB_32_memop(d): return (d & 0xffe0fc00) == 0x38e08000
def is_LDADDH_32_memop(d): return (d & 0xffe0fc00) == 0x78200000 and (d & 0x00001f) != 0x00001f
def is_STADDH_32S_memop(d): return (d & 0xffe0fc1f) == 0x7820001f
def is_LDCLRH_32_memop(d): return (d & 0xffe0fc00) == 0x78201000 and (d & 0x00001f) != 0x00001f
def is_STCLRH_32S_memop(d): return (d & 0xffe0fc1f) == 0x7820101f
def is_LDEORH_32_memop(d): return (d & 0xffe0fc00) == 0x78202000 and (d & 0x00001f) != 0x00001f
def is_STEORH_32S_memop(d): return (d & 0xffe0fc1f) == 0x7820201f
def is_LDSETH_32_memop(d): return (d & 0xffe0fc00) == 0x78203000 and (d & 0x00001f) != 0x00001f
def is_STSETH_32S_memop(d): return (d & 0xffe0fc1f) == 0x7820301f
def is_LDSMAXH_32_memop(d): return (d & 0xffe0fc00) == 0x78204000 and (d & 0x00001f) != 0x00001f
def is_STSMAXH_32S_memop(d): return (d & 0xffe0fc1f) == 0x7820401f
def is_LDSMINH_32_memop(d): return (d & 0xffe0fc00) == 0x78205000 and (d & 0x00001f) != 0x00001f
def is_STSMINH_32S_memop(d): return (d & 0xffe0fc1f) == 0x7820501f
def is_LDUMAXH_32_memop(d): return (d & 0xffe0fc00) == 0x78206000 and (d & 0x00001f) != 0x00001f
def is_STUMAXH_32S_memop(d): return (d & 0xffe0fc1f) == 0x7820601f
def is_LDUMINH_32_memop(d): return (d & 0xffe0fc00) == 0x78207000 and (d & 0x00001f) != 0x00001f
def is_STUMINH_32S_memop(d): return (d & 0xffe0fc1f) == 0x7820701f
def is_SWPH_32_memop(d): return (d & 0xffe0fc00) == 0x78208000
def is_LDADDLH_32_memop(d): return (d & 0xffe0fc00) == 0x78600000 and (d & 0x00001f) != 0x00001f
def is_STADDLH_32S_memop(d): return (d & 0xffe0fc1f) == 0x7860001f
def is_LDCLRLH_32_memop(d): return (d & 0xffe0fc00) == 0x78601000 and (d & 0x00001f) != 0x00001f
def is_STCLRLH_32S_memop(d): return (d & 0xffe0fc1f) == 0x7860101f
def is_LDEORLH_32_memop(d): return (d & 0xffe0fc00) == 0x78602000 and (d & 0x00001f) != 0x00001f
def is_STEORLH_32S_memop(d): return (d & 0xffe0fc1f) == 0x7860201f
def is_LDSETLH_32_memop(d): return (d & 0xffe0fc00) == 0x78603000 and (d & 0x00001f) != 0x00001f
def is_STSETLH_32S_memop(d): return (d & 0xffe0fc1f) == 0x7860301f
def is_LDSMAXLH_32_memop(d): return (d & 0xffe0fc00) == 0x78604000 and (d & 0x00001f) != 0x00001f
def is_STSMAXLH_32S_memop(d): return (d & 0xffe0fc1f) == 0x7860401f
def is_LDSMINLH_32_memop(d): return (d & 0xffe0fc00) == 0x78605000 and (d & 0x00001f) != 0x00001f
def is_STSMINLH_32S_memop(d): return (d & 0xffe0fc1f) == 0x7860501f
def is_LDUMAXLH_32_memop(d): return (d & 0xffe0fc00) == 0x78606000 and (d & 0x00001f) != 0x00001f
def is_STUMAXLH_32S_memop(d): return (d & 0xffe0fc1f) == 0x7860601f
def is_LDUMINLH_32_memop(d): return (d & 0xffe0fc00) == 0x78607000 and (d & 0x00001f) != 0x00001f
def is_STUMINLH_32S_memop(d): return (d & 0xffe0fc1f) == 0x7860701f
def is_SWPLH_32_memop(d): return (d & 0xffe0fc00) == 0x78608000
def is_LDADDAH_32_memop(d): return (d & 0xffe0fc00) == 0x78a00000
def is_LDCLRAH_32_memop(d): return (d & 0xffe0fc00) == 0x78a01000
def is_LDEORAH_32_memop(d): return (d & 0xffe0fc00) == 0x78a02000
def is_LDSETAH_32_memop(d): return (d & 0xffe0fc00) == 0x78a03000
def is_LDSMAXAH_32_memop(d): return (d & 0xffe0fc00) == 0x78a04000
def is_LDSMINAH_32_memop(d): return (d & 0xffe0fc00) == 0x78a05000
def is_LDUMAXAH_32_memop(d): return (d & 0xffe0fc00) == 0x78a06000
def is_LDUMINAH_32_memop(d): return (d & 0xffe0fc00) == 0x78a07000
def is_SWPAH_32_memop(d): return (d & 0xffe0fc00) == 0x78a08000
def is_LDAPRH_32L_memop(d): return (d & 0xffe0fc00) == 0x78a0c000
def is_LDADDALH_32_memop(d): return (d & 0xffe0fc00) == 0x78e00000
def is_LDCLRALH_32_memop(d): return (d & 0xffe0fc00) == 0x78e01000
def is_LDEORALH_32_memop(d): return (d & 0xffe0fc00) == 0x78e02000
def is_LDSETALH_32_memop(d): return (d & 0xffe0fc00) == 0x78e03000
def is_LDSMAXALH_32_memop(d): return (d & 0xffe0fc00) == 0x78e04000
def is_LDSMINALH_32_memop(d): return (d & 0xffe0fc00) == 0x78e05000
def is_LDUMAXALH_32_memop(d): return (d & 0xffe0fc00) == 0x78e06000
def is_LDUMINALH_32_memop(d): return (d & 0xffe0fc00) == 0x78e07000
def is_SWPALH_32_memop(d): return (d & 0xffe0fc00) == 0x78e08000
def is_LDADD_32_memop(d): return (d & 0xffe0fc00) == 0xb8200000 and (d & 0x00001f) != 0x00001f
def is_STADD_32S_memop(d): return (d & 0xffe0fc1f) == 0xb820001f
def is_LDCLR_32_memop(d): return (d & 0xffe0fc00) == 0xb8201000 and (d & 0x00001f) != 0x00001f
def is_STCLR_32S_memop(d): return (d & 0xffe0fc1f) == 0xb820101f
def is_LDEOR_32_memop(d): return (d & 0xffe0fc00) == 0xb8202000 and (d & 0x00001f) != 0x00001f
def is_STEOR_32S_memop(d): return (d & 0xffe0fc1f) == 0xb820201f
def is_LDSET_32_memop(d): return (d & 0xffe0fc00) == 0xb8203000 and (d & 0x00001f) != 0x00001f
def is_STSET_32S_memop(d): return (d & 0xffe0fc1f) == 0xb820301f
def is_LDSMAX_32_memop(d): return (d & 0xffe0fc00) == 0xb8204000 and (d & 0x00001f) != 0x00001f
def is_STSMAX_32S_memop(d): return (d & 0xffe0fc1f) == 0xb820401f
def is_LDSMIN_32_memop(d): return (d & 0xffe0fc00) == 0xb8205000 and (d & 0x00001f) != 0x00001f
def is_STSMIN_32S_memop(d): return (d & 0xffe0fc1f) == 0xb820501f
def is_LDUMAX_32_memop(d): return (d & 0xffe0fc00) == 0xb8206000 and (d & 0x00001f) != 0x00001f
def is_STUMAX_32S_memop(d): return (d & 0xffe0fc1f) == 0xb820601f
def is_LDUMIN_32_memop(d): return (d & 0xffe0fc00) == 0xb8207000 and (d & 0x00001f) != 0x00001f
def is_STUMIN_32S_memop(d): return (d & 0xffe0fc1f) == 0xb820701f
def is_SWP_32_memop(d): return (d & 0xffe0fc00) == 0xb8208000
def is_LDADDL_32_memop(d): return (d & 0xffe0fc00) == 0xb8600000 and (d & 0x00001f) != 0x00001f
def is_STADDL_32S_memop(d): return (d & 0xffe0fc1f) == 0xb860001f
def is_LDCLRL_32_memop(d): return (d & 0xffe0fc00) == 0xb8601000 and (d & 0x00001f) != 0x00001f
def is_STCLRL_32S_memop(d): return (d & 0xffe0fc1f) == 0xb860101f
def is_LDEORL_32_memop(d): return (d & 0xffe0fc00) == 0xb8602000 and (d & 0x00001f) != 0x00001f
def is_STEORL_32S_memop(d): return (d & 0xffe0fc1f) == 0xb860201f
def is_LDSETL_32_memop(d): return (d & 0xffe0fc00) == 0xb8603000 and (d & 0x00001f) != 0x00001f
def is_STSETL_32S_memop(d): return (d & 0xffe0fc1f) == 0xb860301f
def is_LDSMAXL_32_memop(d): return (d & 0xffe0fc00) == 0xb8604000 and (d & 0x00001f) != 0x00001f
def is_STSMAXL_32S_memop(d): return (d & 0xffe0fc1f) == 0xb860401f
def is_LDSMINL_32_memop(d): return (d & 0xffe0fc00) == 0xb8605000 and (d & 0x00001f) != 0x00001f
def is_STSMINL_32S_memop(d): return (d & 0xffe0fc1f) == 0xb860501f
def is_LDUMAXL_32_memop(d): return (d & 0xffe0fc00) == 0xb8606000 and (d & 0x00001f) != 0x00001f
def is_STUMAXL_32S_memop(d): return (d & 0xffe0fc1f) == 0xb860601f
def is_LDUMINL_32_memop(d): return (d & 0xffe0fc00) == 0xb8607000 and (d & 0x00001f) != 0x00001f
def is_STUMINL_32S_memop(d): return (d & 0xffe0fc1f) == 0xb860701f
def is_SWPL_32_memop(d): return (d & 0xffe0fc00) == 0xb8608000
def is_LDADDA_32_memop(d): return (d & 0xffe0fc00) == 0xb8a00000
def is_LDCLRA_32_memop(d): return (d & 0xffe0fc00) == 0xb8a01000
def is_LDEORA_32_memop(d): return (d & 0xffe0fc00) == 0xb8a02000
def is_LDSETA_32_memop(d): return (d & 0xffe0fc00) == 0xb8a03000
def is_LDSMAXA_32_memop(d): return (d & 0xffe0fc00) == 0xb8a04000
def is_LDSMINA_32_memop(d): return (d & 0xffe0fc00) == 0xb8a05000
def is_LDUMAXA_32_memop(d): return (d & 0xffe0fc00) == 0xb8a06000
def is_LDUMINA_32_memop(d): return (d & 0xffe0fc00) == 0xb8a07000
def is_SWPA_32_memop(d): return (d & 0xffe0fc00) == 0xb8a08000
def is_LDAPR_32L_memop(d): return (d & 0xffe0fc00) == 0xb8a0c000
def is_LDADDAL_32_memop(d): return (d & 0xffe0fc00) == 0xb8e00000
def is_LDCLRAL_32_memop(d): return (d & 0xffe0fc00) == 0xb8e01000
def is_LDEORAL_32_memop(d): return (d & 0xffe0fc00) == 0xb8e02000
def is_LDSETAL_32_memop(d): return (d & 0xffe0fc00) == 0xb8e03000
def is_LDSMAXAL_32_memop(d): return (d & 0xffe0fc00) == 0xb8e04000
def is_LDSMINAL_32_memop(d): return (d & 0xffe0fc00) == 0xb8e05000
def is_LDUMAXAL_32_memop(d): return (d & 0xffe0fc00) == 0xb8e06000
def is_LDUMINAL_32_memop(d): return (d & 0xffe0fc00) == 0xb8e07000
def is_SWPAL_32_memop(d): return (d & 0xffe0fc00) == 0xb8e08000
def is_LDADD_64_memop(d): return (d & 0xffe0fc00) == 0xf8200000 and (d & 0x00001f) != 0x00001f
def is_STADD_64S_memop(d): return (d & 0xffe0fc1f) == 0xf820001f
def is_LDCLR_64_memop(d): return (d & 0xffe0fc00) == 0xf8201000 and (d & 0x00001f) != 0x00001f
def is_STCLR_64S_memop(d): return (d & 0xffe0fc1f) == 0xf820101f
def is_LDEOR_64_memop(d): return (d & 0xffe0fc00) == 0xf8202000 and (d & 0x00001f) != 0x00001f
def is_STEOR_64S_memop(d): return (d & 0xffe0fc1f) == 0xf820201f
def is_LDSET_64_memop(d): return (d & 0xffe0fc00) == 0xf8203000 and (d & 0x00001f) != 0x00001f
def is_STSET_64S_memop(d): return (d & 0xffe0fc1f) == 0xf820301f
def is_LDSMAX_64_memop(d): return (d & 0xffe0fc00) == 0xf8204000 and (d & 0x00001f) != 0x00001f
def is_STSMAX_64S_memop(d): return (d & 0xffe0fc1f) == 0xf820401f
def is_LDSMIN_64_memop(d): return (d & 0xffe0fc00) == 0xf8205000 and (d & 0x00001f) != 0x00001f
def is_STSMIN_64S_memop(d): return (d & 0xffe0fc1f) == 0xf820501f
def is_LDUMAX_64_memop(d): return (d & 0xffe0fc00) == 0xf8206000 and (d & 0x00001f) != 0x00001f
def is_STUMAX_64S_memop(d): return (d & 0xffe0fc1f) == 0xf820601f
def is_LDUMIN_64_memop(d): return (d & 0xffe0fc00) == 0xf8207000 and (d & 0x00001f) != 0x00001f
def is_STUMIN_64S_memop(d): return (d & 0xffe0fc1f) == 0xf820701f
def is_SWP_64_memop(d): return (d & 0xffe0fc00) == 0xf8208000
def is_LDADDL_64_memop(d): return (d & 0xffe0fc00) == 0xf8600000 and (d & 0x00001f) != 0x00001f
def is_STADDL_64S_memop(d): return (d & 0xffe0fc1f) == 0xf860001f
def is_LDCLRL_64_memop(d): return (d & 0xffe0fc00) == 0xf8601000 and (d & 0x00001f) != 0x00001f
def is_STCLRL_64S_memop(d): return (d & 0xffe0fc1f) == 0xf860101f
def is_LDEORL_64_memop(d): return (d & 0xffe0fc00) == 0xf8602000 and (d & 0x00001f) != 0x00001f
def is_STEORL_64S_memop(d): return (d & 0xffe0fc1f) == 0xf860201f
def is_LDSETL_64_memop(d): return (d & 0xffe0fc00) == 0xf8603000 and (d & 0x00001f) != 0x00001f
def is_STSETL_64S_memop(d): return (d & 0xffe0fc1f) == 0xf860301f
def is_LDSMAXL_64_memop(d): return (d & 0xffe0fc00) == 0xf8604000 and (d & 0x00001f) != 0x00001f
def is_STSMAXL_64S_memop(d): return (d & 0xffe0fc1f) == 0xf860401f
def is_LDSMINL_64_memop(d): return (d & 0xffe0fc00) == 0xf8605000 and (d & 0x00001f) != 0x00001f
def is_STSMINL_64S_memop(d): return (d & 0xffe0fc1f) == 0xf860501f
def is_LDUMAXL_64_memop(d): return (d & 0xffe0fc00) == 0xf8606000 and (d & 0x00001f) != 0x00001f
def is_STUMAXL_64S_memop(d): return (d & 0xffe0fc1f) == 0xf860601f
def is_LDUMINL_64_memop(d): return (d & 0xffe0fc00) == 0xf8607000 and (d & 0x00001f) != 0x00001f
def is_STUMINL_64S_memop(d): return (d & 0xffe0fc1f) == 0xf860701f
def is_SWPL_64_memop(d): return (d & 0xffe0fc00) == 0xf8608000
def is_LDADDA_64_memop(d): return (d & 0xffe0fc00) == 0xf8a00000
def is_LDCLRA_64_memop(d): return (d & 0xffe0fc00) == 0xf8a01000
def is_LDEORA_64_memop(d): return (d & 0xffe0fc00) == 0xf8a02000
def is_LDSETA_64_memop(d): return (d & 0xffe0fc00) == 0xf8a03000
def is_LDSMAXA_64_memop(d): return (d & 0xffe0fc00) == 0xf8a04000
def is_LDSMINA_64_memop(d): return (d & 0xffe0fc00) == 0xf8a05000
def is_LDUMAXA_64_memop(d): return (d & 0xffe0fc00) == 0xf8a06000
def is_LDUMINA_64_memop(d): return (d & 0xffe0fc00) == 0xf8a07000
def is_SWPA_64_memop(d): return (d & 0xffe0fc00) == 0xf8a08000
def is_LDAPR_64L_memop(d): return (d & 0xffe0fc00) == 0xf8a0c000
def is_LDADDAL_64_memop(d): return (d & 0xffe0fc00) == 0xf8e00000
def is_LDCLRAL_64_memop(d): return (d & 0xffe0fc00) == 0xf8e01000
def is_LDEORAL_64_memop(d): return (d & 0xffe0fc00) == 0xf8e02000
def is_LDSETAL_64_memop(d): return (d & 0xffe0fc00) == 0xf8e03000
def is_LDSMAXAL_64_memop(d): return (d & 0xffe0fc00) == 0xf8e04000
def is_LDSMINAL_64_memop(d): return (d & 0xffe0fc00) == 0xf8e05000
def is_LDUMAXAL_64_memop(d): return (d & 0xffe0fc00) == 0xf8e06000
def is_LDUMINAL_64_memop(d): return (d & 0xffe0fc00) == 0xf8e07000
def is_SWPAL_64_memop(d): return (d & 0xffe0fc00) == 0xf8e08000
def is_LDR_32_loadlit(d): return (d & 0xff000000) == 0x18000000
def is_LDR_S_loadlit(d): return (d & 0xff000000) == 0x1c000000
def is_LDR_64_loadlit(d): return (d & 0xff000000) == 0x58000000
def is_LDR_D_loadlit(d): return (d & 0xff000000) == 0x5c000000
def is_LDRSW_64_loadlit(d): return (d & 0xff000000) == 0x98000000
def is_LDR_Q_loadlit(d): return (d & 0xff000000) == 0x9c000000
def is_PRFM_P_loadlit(d): return (d & 0xff000000) == 0xd8000000
def is_STXRB_SR32_ldstexcl(d): return (d & 0xffe08000) == 0x08000000
def is_STLXRB_SR32_ldstexcl(d): return (d & 0xffe08000) == 0x08008000
def is_CASP_CP32_ldstexcl(d): return (d & 0xffe0fc00) == 0x08207c00
def is_CASPL_CP32_ldstexcl(d): return (d & 0xffe0fc00) == 0x0820fc00
def is_LDXRB_LR32_ldstexcl(d): return (d & 0xffe08000) == 0x08400000
def is_LDAXRB_LR32_ldstexcl(d): return (d & 0xffe08000) == 0x08408000
def is_CASPA_CP32_ldstexcl(d): return (d & 0xffe0fc00) == 0x08607c00
def is_CASPAL_CP32_ldstexcl(d): return (d & 0xffe0fc00) == 0x0860fc00
def is_STLLRB_SL32_ldstexcl(d): return (d & 0xffe08000) == 0x08800000
def is_STLRB_SL32_ldstexcl(d): return (d & 0xffe08000) == 0x08808000
def is_CASB_C32_ldstexcl(d): return (d & 0xffe0fc00) == 0x08a07c00
def is_CASLB_C32_ldstexcl(d): return (d & 0xffe0fc00) == 0x08a0fc00
def is_LDLARB_LR32_ldstexcl(d): return (d & 0xffe08000) == 0x08c00000
def is_LDARB_LR32_ldstexcl(d): return (d & 0xffe08000) == 0x08c08000
def is_CASAB_C32_ldstexcl(d): return (d & 0xffe0fc00) == 0x08e07c00
def is_CASALB_C32_ldstexcl(d): return (d & 0xffe0fc00) == 0x08e0fc00
def is_STXRH_SR32_ldstexcl(d): return (d & 0xffe08000) == 0x48000000
def is_STLXRH_SR32_ldstexcl(d): return (d & 0xffe08000) == 0x48008000
def is_CASP_CP64_ldstexcl(d): return (d & 0xffe0fc00) == 0x48207c00
def is_CASPL_CP64_ldstexcl(d): return (d & 0xffe0fc00) == 0x4820fc00
def is_LDXRH_LR32_ldstexcl(d): return (d & 0xffe08000) == 0x48400000
def is_LDAXRH_LR32_ldstexcl(d): return (d & 0xffe08000) == 0x48408000
def is_CASPA_CP64_ldstexcl(d): return (d & 0xffe0fc00) == 0x48607c00
def is_CASPAL_CP64_ldstexcl(d): return (d & 0xffe0fc00) == 0x4860fc00
def is_STLLRH_SL32_ldstexcl(d): return (d & 0xffe08000) == 0x48800000
def is_STLRH_SL32_ldstexcl(d): return (d & 0xffe08000) == 0x48808000
def is_CASH_C32_ldstexcl(d): return (d & 0xffe0fc00) == 0x48a07c00
def is_CASLH_C32_ldstexcl(d): return (d & 0xffe0fc00) == 0x48a0fc00
def is_LDLARH_LR32_ldstexcl(d): return (d & 0xffe08000) == 0x48c00000
def is_LDARH_LR32_ldstexcl(d): return (d & 0xffe08000) == 0x48c08000
def is_CASAH_C32_ldstexcl(d): return (d & 0xffe0fc00) == 0x48e07c00
def is_CASALH_C32_ldstexcl(d): return (d & 0xffe0fc00) == 0x48e0fc00
def is_STXR_SR32_ldstexcl(d): return (d & 0xffe08000) == 0x88000000
def is_STLXR_SR32_ldstexcl(d): return (d & 0xffe08000) == 0x88008000
def is_STXP_SP32_ldstexcl(d): return (d & 0xffe08000) == 0x88200000
def is_STLXP_SP32_ldstexcl(d): return (d & 0xffe08000) == 0x88208000
def is_LDXR_LR32_ldstexcl(d): return (d & 0xffe08000) == 0x88400000
def is_LDAXR_LR32_ldstexcl(d): return (d & 0xffe08000) == 0x88408000
def is_LDXP_LP32_ldstexcl(d): return (d & 0xffe08000) == 0x88600000
def is_LDAXP_LP32_ldstexcl(d): return (d & 0xffe08000) == 0x88608000
def is_STLLR_SL32_ldstexcl(d): return (d & 0xffe08000) == 0x88800000
def is_STLR_SL32_ldstexcl(d): return (d & 0xffe08000) == 0x88808000
def is_CAS_C32_ldstexcl(d): return (d & 0xffe0fc00) == 0x88a07c00
def is_CASL_C32_ldstexcl(d): return (d & 0xffe0fc00) == 0x88a0fc00
def is_LDLAR_LR32_ldstexcl(d): return (d & 0xffe08000) == 0x88c00000
def is_LDAR_LR32_ldstexcl(d): return (d & 0xffe08000) == 0x88c08000
def is_CASA_C32_ldstexcl(d): return (d & 0xffe0fc00) == 0x88e07c00
def is_CASAL_C32_ldstexcl(d): return (d & 0xffe0fc00) == 0x88e0fc00
def is_STXR_SR64_ldstexcl(d): return (d & 0xffe08000) == 0xc8000000
def is_STLXR_SR64_ldstexcl(d): return (d & 0xffe08000) == 0xc8008000
def is_STXP_SP64_ldstexcl(d): return (d & 0xffe08000) == 0xc8200000
def is_STLXP_SP64_ldstexcl(d): return (d & 0xffe08000) == 0xc8208000
def is_LDXR_LR64_ldstexcl(d): return (d & 0xffe08000) == 0xc8400000
def is_LDAXR_LR64_ldstexcl(d): return (d & 0xffe08000) == 0xc8408000
def is_LDXP_LP64_ldstexcl(d): return (d & 0xffe08000) == 0xc8600000
def is_LDAXP_LP64_ldstexcl(d): return (d & 0xffe08000) == 0xc8608000
def is_STLLR_SL64_ldstexcl(d): return (d & 0xffe08000) == 0xc8800000
def is_STLR_SL64_ldstexcl(d): return (d & 0xffe08000) == 0xc8808000
def is_CAS_C64_ldstexcl(d): return (d & 0xffe0fc00) == 0xc8a07c00
def is_CASL_C64_ldstexcl(d): return (d & 0xffe0fc00) == 0xc8a0fc00
def is_LDLAR_LR64_ldstexcl(d): return (d & 0xffe08000) == 0xc8c00000
def is_LDAR_LR64_ldstexcl(d): return (d & 0xffe08000) == 0xc8c08000
def is_CASA_C64_ldstexcl(d): return (d & 0xffe0fc00) == 0xc8e07c00
def is_CASAL_C64_ldstexcl(d): return (d & 0xffe0fc00) == 0xc8e0fc00
def is_STNP_32_ldstnapair_offs(d): return (d & 0xffc00000) == 0x28000000
def is_LDNP_32_ldstnapair_offs(d): return (d & 0xffc00000) == 0x28400000
def is_STNP_S_ldstnapair_offs(d): return (d & 0xffc00000) == 0x2c000000
def is_LDNP_S_ldstnapair_offs(d): return (d & 0xffc00000) == 0x2c400000
def is_STNP_D_ldstnapair_offs(d): return (d & 0xffc00000) == 0x6c000000
def is_LDNP_D_ldstnapair_offs(d): return (d & 0xffc00000) == 0x6c400000
def is_STNP_64_ldstnapair_offs(d): return (d & 0xffc00000) == 0xa8000000
def is_LDNP_64_ldstnapair_offs(d): return (d & 0xffc00000) == 0xa8400000
def is_STNP_Q_ldstnapair_offs(d): return (d & 0xffc00000) == 0xac000000
def is_LDNP_Q_ldstnapair_offs(d): return (d & 0xffc00000) == 0xac400000
def is_STRB_32_ldst_immpost(d): return (d & 0xffe00c00) == 0x38000400
def is_LDRB_32_ldst_immpost(d): return (d & 0xffe00c00) == 0x38400400
def is_LDRSB_64_ldst_immpost(d): return (d & 0xffe00c00) == 0x38800400
def is_LDRSB_32_ldst_immpost(d): return (d & 0xffe00c00) == 0x38c00400
def is_STR_B_ldst_immpost(d): return (d & 0xffe00c00) == 0x3c000400
def is_LDR_B_ldst_immpost(d): return (d & 0xffe00c00) == 0x3c400400
def is_STR_Q_ldst_immpost(d): return (d & 0xffe00c00) == 0x3c800400
def is_LDR_Q_ldst_immpost(d): return (d & 0xffe00c00) == 0x3cc00400
def is_STRH_32_ldst_immpost(d): return (d & 0xffe00c00) == 0x78000400
def is_LDRH_32_ldst_immpost(d): return (d & 0xffe00c00) == 0x78400400
def is_LDRSH_64_ldst_immpost(d): return (d & 0xffe00c00) == 0x78800400
def is_LDRSH_32_ldst_immpost(d): return (d & 0xffe00c00) == 0x78c00400
def is_STR_H_ldst_immpost(d): return (d & 0xffe00c00) == 0x7c000400
def is_LDR_H_ldst_immpost(d): return (d & 0xffe00c00) == 0x7c400400
def is_STR_32_ldst_immpost(d): return (d & 0xffe00c00) == 0xb8000400
def is_LDR_32_ldst_immpost(d): return (d & 0xffe00c00) == 0xb8400400
def is_LDRSW_64_ldst_immpost(d): return (d & 0xffe00c00) == 0xb8800400
def is_STR_S_ldst_immpost(d): return (d & 0xffe00c00) == 0xbc000400
def is_LDR_S_ldst_immpost(d): return (d & 0xffe00c00) == 0xbc400400
def is_STR_64_ldst_immpost(d): return (d & 0xffe00c00) == 0xf8000400
def is_LDR_64_ldst_immpost(d): return (d & 0xffe00c00) == 0xf8400400
def is_STR_D_ldst_immpost(d): return (d & 0xffe00c00) == 0xfc000400
def is_LDR_D_ldst_immpost(d): return (d & 0xffe00c00) == 0xfc400400
def is_STRB_32_ldst_immpre(d): return (d & 0xffe00c00) == 0x38000c00
def is_LDRB_32_ldst_immpre(d): return (d & 0xffe00c00) == 0x38400c00
def is_LDRSB_64_ldst_immpre(d): return (d & 0xffe00c00) == 0x38800c00
def is_LDRSB_32_ldst_immpre(d): return (d & 0xffe00c00) == 0x38c00c00
def is_STR_B_ldst_immpre(d): return (d & 0xffe00c00) == 0x3c000c00
def is_LDR_B_ldst_immpre(d): return (d & 0xffe00c00) == 0x3c400c00
def is_STR_Q_ldst_immpre(d): return (d & 0xffe00c00) == 0x3c800c00
def is_LDR_Q_ldst_immpre(d): return (d & 0xffe00c00) == 0x3cc00c00
def is_STRH_32_ldst_immpre(d): return (d & 0xffe00c00) == 0x78000c00
def is_LDRH_32_ldst_immpre(d): return (d & 0xffe00c00) == 0x78400c00
def is_LDRSH_64_ldst_immpre(d): return (d & 0xffe00c00) == 0x78800c00
def is_LDRSH_32_ldst_immpre(d): return (d & 0xffe00c00) == 0x78c00c00
def is_STR_H_ldst_immpre(d): return (d & 0xffe00c00) == 0x7c000c00
def is_LDR_H_ldst_immpre(d): return (d & 0xffe00c00) == 0x7c400c00
def is_STR_32_ldst_immpre(d): return (d & 0xffe00c00) == 0xb8000c00
def is_LDR_32_ldst_immpre(d): return (d & 0xffe00c00) == 0xb8400c00
def is_LDRSW_64_ldst_immpre(d): return (d & 0xffe00c00) == 0xb8800c00
def is_STR_S_ldst_immpre(d): return (d & 0xffe00c00) == 0xbc000c00
def is_LDR_S_ldst_immpre(d): return (d & 0xffe00c00) == 0xbc400c00
def is_STR_64_ldst_immpre(d): return (d & 0xffe00c00) == 0xf8000c00
def is_LDR_64_ldst_immpre(d): return (d & 0xffe00c00) == 0xf8400c00
def is_STR_D_ldst_immpre(d): return (d & 0xffe00c00) == 0xfc000c00
def is_LDR_D_ldst_immpre(d): return (d & 0xffe00c00) == 0xfc400c00
def is_LDRAA_64_ldst_pac(d): return (d & 0xfba00c00) == 0xf8200400
def is_LDRAA_64W_ldst_pac(d): return (d & 0xfba00c00) == 0xf8200c00
def is_LDRAB_64_ldst_pac(d): return (d & 0xfba00c00) == 0xf8a00400
def is_LDRAB_64W_ldst_pac(d): return (d & 0xfba00c00) == 0xf8a00c00
def is_STRB_32B_ldst_regoff(d): return (d & 0xffe00c00) == 0x38200800 and (d & 0x00e000) != 0x006000
def is_STRB_32BL_ldst_regoff(d): return (d & 0xffe0ec00) == 0x38206800
def is_LDRB_32B_ldst_regoff(d): return (d & 0xffe00c00) == 0x38600800 and (d & 0x00e000) != 0x006000
def is_LDRB_32BL_ldst_regoff(d): return (d & 0xffe0ec00) == 0x38606800
def is_LDRSB_64B_ldst_regoff(d): return (d & 0xffe00c00) == 0x38a00800 and (d & 0x00e000) != 0x006000
def is_LDRSB_64BL_ldst_regoff(d): return (d & 0xffe0ec00) == 0x38a06800
def is_LDRSB_32B_ldst_regoff(d): return (d & 0xffe00c00) == 0x38e00800 and (d & 0x00e000) != 0x006000
def is_LDRSB_32BL_ldst_regoff(d): return (d & 0xffe0ec00) == 0x38e06800
def is_STR_B_ldst_regoff(d): return (d & 0xffe00c00) == 0x3c200800 and (d & 0x00e000) != 0x006000
def is_STR_BL_ldst_regoff(d): return (d & 0xffe0ec00) == 0x3c206800
def is_LDR_B_ldst_regoff(d): return (d & 0xffe00c00) == 0x3c600800 and (d & 0x00e000) != 0x006000
def is_LDR_BL_ldst_regoff(d): return (d & 0xffe0ec00) == 0x3c606800
def is_STR_Q_ldst_regoff(d): return (d & 0xffe00c00) == 0x3ca00800
def is_LDR_Q_ldst_regoff(d): return (d & 0xffe00c00) == 0x3ce00800
def is_STRH_32_ldst_regoff(d): return (d & 0xffe00c00) == 0x78200800
def is_LDRH_32_ldst_regoff(d): return (d & 0xffe00c00) == 0x78600800
def is_LDRSH_64_ldst_regoff(d): return (d & 0xffe00c00) == 0x78a00800
def is_LDRSH_32_ldst_regoff(d): return (d & 0xffe00c00) == 0x78e00800
def is_STR_H_ldst_regoff(d): return (d & 0xffe00c00) == 0x7c200800
def is_LDR_H_ldst_regoff(d): return (d & 0xffe00c00) == 0x7c600800
def is_STR_32_ldst_regoff(d): return (d & 0xffe00c00) == 0xb8200800
def is_LDR_32_ldst_regoff(d): return (d & 0xffe00c00) == 0xb8600800
def is_LDRSW_64_ldst_regoff(d): return (d & 0xffe00c00) == 0xb8a00800
def is_STR_S_ldst_regoff(d): return (d & 0xffe00c00) == 0xbc200800
def is_LDR_S_ldst_regoff(d): return (d & 0xffe00c00) == 0xbc600800
def is_STR_64_ldst_regoff(d): return (d & 0xffe00c00) == 0xf8200800
def is_LDR_64_ldst_regoff(d): return (d & 0xffe00c00) == 0xf8600800
def is_PRFM_P_ldst_regoff(d): return (d & 0xffe00c00) == 0xf8a00800
def is_STR_D_ldst_regoff(d): return (d & 0xffe00c00) == 0xfc200800
def is_LDR_D_ldst_regoff(d): return (d & 0xffe00c00) == 0xfc600800
def is_STTRB_32_ldst_unpriv(d): return (d & 0xffe00c00) == 0x38000800
def is_LDTRB_32_ldst_unpriv(d): return (d & 0xffe00c00) == 0x38400800
def is_LDTRSB_64_ldst_unpriv(d): return (d & 0xffe00c00) == 0x38800800
def is_LDTRSB_32_ldst_unpriv(d): return (d & 0xffe00c00) == 0x38c00800
def is_STTRH_32_ldst_unpriv(d): return (d & 0xffe00c00) == 0x78000800
def is_LDTRH_32_ldst_unpriv(d): return (d & 0xffe00c00) == 0x78400800
def is_LDTRSH_64_ldst_unpriv(d): return (d & 0xffe00c00) == 0x78800800
def is_LDTRSH_32_ldst_unpriv(d): return (d & 0xffe00c00) == 0x78c00800
def is_STTR_32_ldst_unpriv(d): return (d & 0xffe00c00) == 0xb8000800
def is_LDTR_32_ldst_unpriv(d): return (d & 0xffe00c00) == 0xb8400800
def is_LDTRSW_64_ldst_unpriv(d): return (d & 0xffe00c00) == 0xb8800800
def is_STTR_64_ldst_unpriv(d): return (d & 0xffe00c00) == 0xf8000800
def is_LDTR_64_ldst_unpriv(d): return (d & 0xffe00c00) == 0xf8400800
def is_STURB_32_ldst_unscaled(d): return (d & 0xffe00c00) == 0x38000000
def is_LDURB_32_ldst_unscaled(d): return (d & 0xffe00c00) == 0x38400000
def is_LDURSB_64_ldst_unscaled(d): return (d & 0xffe00c00) == 0x38800000
def is_LDURSB_32_ldst_unscaled(d): return (d & 0xffe00c00) == 0x38c00000
def is_STUR_B_ldst_unscaled(d): return (d & 0xffe00c00) == 0x3c000000
def is_LDUR_B_ldst_unscaled(d): return (d & 0xffe00c00) == 0x3c400000
def is_STUR_Q_ldst_unscaled(d): return (d & 0xffe00c00) == 0x3c800000
def is_LDUR_Q_ldst_unscaled(d): return (d & 0xffe00c00) == 0x3cc00000
def is_STURH_32_ldst_unscaled(d): return (d & 0xffe00c00) == 0x78000000
def is_LDURH_32_ldst_unscaled(d): return (d & 0xffe00c00) == 0x78400000
def is_LDURSH_64_ldst_unscaled(d): return (d & 0xffe00c00) == 0x78800000
def is_LDURSH_32_ldst_unscaled(d): return (d & 0xffe00c00) == 0x78c00000
def is_STUR_H_ldst_unscaled(d): return (d & 0xffe00c00) == 0x7c000000
def is_LDUR_H_ldst_unscaled(d): return (d & 0xffe00c00) == 0x7c400000
def is_STUR_32_ldst_unscaled(d): return (d & 0xffe00c00) == 0xb8000000
def is_LDUR_32_ldst_unscaled(d): return (d & 0xffe00c00) == 0xb8400000
def is_LDURSW_64_ldst_unscaled(d): return (d & 0xffe00c00) == 0xb8800000
def is_STUR_S_ldst_unscaled(d): return (d & 0xffe00c00) == 0xbc000000
def is_LDUR_S_ldst_unscaled(d): return (d & 0xffe00c00) == 0xbc400000
def is_STUR_64_ldst_unscaled(d): return (d & 0xffe00c00) == 0xf8000000
def is_LDUR_64_ldst_unscaled(d): return (d & 0xffe00c00) == 0xf8400000
def is_PRFUM_P_ldst_unscaled(d): return (d & 0xffe00c00) == 0xf8800000
def is_STUR_D_ldst_unscaled(d): return (d & 0xffe00c00) == 0xfc000000
def is_LDUR_D_ldst_unscaled(d): return (d & 0xffe00c00) == 0xfc400000
def is_STRB_32_ldst_pos(d): return (d & 0xffc00000) == 0x39000000
def is_LDRB_32_ldst_pos(d): return (d & 0xffc00000) == 0x39400000
def is_LDRSB_64_ldst_pos(d): return (d & 0xffc00000) == 0x39800000
def is_LDRSB_32_ldst_pos(d): return (d & 0xffc00000) == 0x39c00000
def is_STR_B_ldst_pos(d): return (d & 0xffc00000) == 0x3d000000
def is_LDR_B_ldst_pos(d): return (d & 0xffc00000) == 0x3d400000
def is_STR_Q_ldst_pos(d): return (d & 0xffc00000) == 0x3d800000
def is_LDR_Q_ldst_pos(d): return (d & 0xffc00000) == 0x3dc00000
def is_STRH_32_ldst_pos(d): return (d & 0xffc00000) == 0x79000000
def is_LDRH_32_ldst_pos(d): return (d & 0xffc00000) == 0x79400000
def is_LDRSH_64_ldst_pos(d): return (d & 0xffc00000) == 0x79800000
def is_LDRSH_32_ldst_pos(d): return (d & 0xffc00000) == 0x79c00000
def is_STR_H_ldst_pos(d): return (d & 0xffc00000) == 0x7d000000
def is_LDR_H_ldst_pos(d): return (d & 0xffc00000) == 0x7d400000
def is_STR_32_ldst_pos(d): return (d & 0xffc00000) == 0xb9000000
def is_LDR_32_ldst_pos(d): return (d & 0xffc00000) == 0xb9400000
def is_LDRSW_64_ldst_pos(d): return (d & 0xffc00000) == 0xb9800000
def is_STR_S_ldst_pos(d): return (d & 0xffc00000) == 0xbd000000
def is_LDR_S_ldst_pos(d): return (d & 0xffc00000) == 0xbd400000
def is_STR_64_ldst_pos(d): return (d & 0xffc00000) == 0xf9000000
def is_LDR_64_ldst_pos(d): return (d & 0xffc00000) == 0xf9400000
def is_PRFM_P_ldst_pos(d): return (d & 0xffc00000) == 0xf9800000
def is_STR_D_ldst_pos(d): return (d & 0xffc00000) == 0xfd000000
def is_LDR_D_ldst_pos(d): return (d & 0xffc00000) == 0xfd400000
def is_STP_32_ldstpair_off(d): return (d & 0xffc00000) == 0x29000000
def is_LDP_32_ldstpair_off(d): return (d & 0xffc00000) == 0x29400000
def is_STP_S_ldstpair_off(d): return (d & 0xffc00000) == 0x2d000000
def is_LDP_S_ldstpair_off(d): return (d & 0xffc00000) == 0x2d400000
def is_LDPSW_64_ldstpair_off(d): return (d & 0xffc00000) == 0x69400000
def is_STP_D_ldstpair_off(d): return (d & 0xffc00000) == 0x6d000000
def is_LDP_D_ldstpair_off(d): return (d & 0xffc00000) == 0x6d400000
def is_STP_64_ldstpair_off(d): return (d & 0xffc00000) == 0xa9000000
def is_LDP_64_ldstpair_off(d): return (d & 0xffc00000) == 0xa9400000
def is_STP_Q_ldstpair_off(d): return (d & 0xffc00000) == 0xad000000
def is_LDP_Q_ldstpair_off(d): return (d & 0xffc00000) == 0xad400000
def is_STP_32_ldstpair_post(d): return (d & 0xffc00000) == 0x28800000
def is_LDP_32_ldstpair_post(d): return (d & 0xffc00000) == 0x28c00000
def is_STP_S_ldstpair_post(d): return (d & 0xffc00000) == 0x2c800000
def is_LDP_S_ldstpair_post(d): return (d & 0xffc00000) == 0x2cc00000
def is_LDPSW_64_ldstpair_post(d): return (d & 0xffc00000) == 0x68c00000
def is_STP_D_ldstpair_post(d): return (d & 0xffc00000) == 0x6c800000
def is_LDP_D_ldstpair_post(d): return (d & 0xffc00000) == 0x6cc00000
def is_STP_64_ldstpair_post(d): return (d & 0xffc00000) == 0xa8800000
def is_LDP_64_ldstpair_post(d): return (d & 0xffc00000) == 0xa8c00000
def is_STP_Q_ldstpair_post(d): return (d & 0xffc00000) == 0xac800000
def is_LDP_Q_ldstpair_post(d): return (d & 0xffc00000) == 0xacc00000
def is_STP_32_ldstpair_pre(d): return (d & 0xffc00000) == 0x29800000
def is_LDP_32_ldstpair_pre(d): return (d & 0xffc00000) == 0x29c00000
def is_STP_S_ldstpair_pre(d): return (d & 0xffc00000) == 0x2d800000
def is_LDP_S_ldstpair_pre(d): return (d & 0xffc00000) == 0x2dc00000
def is_LDPSW_64_ldstpair_pre(d): return (d & 0xffc00000) == 0x69c00000
def is_STP_D_ldstpair_pre(d): return (d & 0xffc00000) == 0x6d800000
def is_LDP_D_ldstpair_pre(d): return (d & 0xffc00000) == 0x6dc00000
def is_STP_64_ldstpair_pre(d): return (d & 0xffc00000) == 0xa9800000
def is_LDP_64_ldstpair_pre(d): return (d & 0xffc00000) == 0xa9c00000
def is_STP_Q_ldstpair_pre(d): return (d & 0xffc00000) == 0xad800000
def is_LDP_Q_ldstpair_pre(d): return (d & 0xffc00000) == 0xadc00000
def is_ADD_32_addsub_imm(d): return (d & 0xff000000) == 0x11000000
def is_ADDS_32S_addsub_imm(d): return (d & 0xff000000) == 0x31000000
def is_SUB_32_addsub_imm(d): return (d & 0xff000000) == 0x51000000
def is_SUBS_32S_addsub_imm(d): return (d & 0xff000000) == 0x71000000
def is_ADD_64_addsub_imm(d): return (d & 0xff000000) == 0x91000000
def is_ADDS_64S_addsub_imm(d): return (d & 0xff000000) == 0xb1000000
def is_SUB_64_addsub_imm(d): return (d & 0xff000000) == 0xd1000000
def is_SUBS_64S_addsub_imm(d): return (d & 0xff000000) == 0xf1000000
def is_SBFM_32M_bitfield(d): return (d & 0xffc00000) == 0x13000000
def is_BFM_32M_bitfield(d): return (d & 0xffc00000) == 0x33000000
def is_UBFM_32M_bitfield(d): return (d & 0xffc00000) == 0x53000000
def is_SBFM_64M_bitfield(d): return (d & 0xffc00000) == 0x93400000
def is_BFM_64M_bitfield(d): return (d & 0xffc00000) == 0xb3400000
def is_UBFM_64M_bitfield(d): return (d & 0xffc00000) == 0xd3400000
def is_EXTR_32_extract(d): return (d & 0xffe08000) == 0x13800000
def is_EXTR_64_extract(d): return (d & 0xffe00000) == 0x93c00000
def is_AND_32_log_imm(d): return (d & 0xffc00000) == 0x12000000
def is_ORR_32_log_imm(d): return (d & 0xffc00000) == 0x32000000
def is_EOR_32_log_imm(d): return (d & 0xffc00000) == 0x52000000
def is_ANDS_32S_log_imm(d): return (d & 0xffc00000) == 0x72000000
def is_AND_64_log_imm(d): return (d & 0xff800000) == 0x92000000
def is_ORR_64_log_imm(d): return (d & 0xff800000) == 0xb2000000
def is_EOR_64_log_imm(d): return (d & 0xff800000) == 0xd2000000
def is_ANDS_64S_log_imm(d): return (d & 0xff800000) == 0xf2000000
def is_MOVN_32_movewide(d): return (d & 0xff800000) == 0x12800000
def is_MOVZ_32_movewide(d): return (d & 0xff800000) == 0x52800000
def is_MOVK_32_movewide(d): return (d & 0xff800000) == 0x72800000
def is_MOVN_64_movewide(d): return (d & 0xff800000) == 0x92800000
def is_MOVZ_64_movewide(d): return (d & 0xff800000) == 0xd2800000
def is_MOVK_64_movewide(d): return (d & 0xff800000) == 0xf2800000
def is_ADR_only_pcreladdr(d): return (d & 0x9f000000) == 0x10000000
def is_ADRP_only_pcreladdr(d): return (d & 0x9f000000) == 0x90000000
def is_ADD_32_addsub_ext(d): return (d & 0xffe00000) == 0x0b200000
def is_ADDS_32S_addsub_ext(d): return (d & 0xffe00000) == 0x2b200000
def is_SUB_32_addsub_ext(d): return (d & 0xffe00000) == 0x4b200000
def is_SUBS_32S_addsub_ext(d): return (d & 0xffe00000) == 0x6b200000
def is_ADD_64_addsub_ext(d): return (d & 0xffe00000) == 0x8b200000
def is_ADDS_64S_addsub_ext(d): return (d & 0xffe00000) == 0xab200000
def is_SUB_64_addsub_ext(d): return (d & 0xffe00000) == 0xcb200000
def is_SUBS_64S_addsub_ext(d): return (d & 0xffe00000) == 0xeb200000
def is_ADD_32_addsub_shift(d): return (d & 0xff200000) == 0x0b000000
def is_ADDS_32_addsub_shift(d): return (d & 0xff200000) == 0x2b000000
def is_SUB_32_addsub_shift(d): return (d & 0xff200000) == 0x4b000000
def is_SUBS_32_addsub_shift(d): return (d & 0xff200000) == 0x6b000000
def is_ADD_64_addsub_shift(d): return (d & 0xff200000) == 0x8b000000
def is_ADDS_64_addsub_shift(d): return (d & 0xff200000) == 0xab000000
def is_SUB_64_addsub_shift(d): return (d & 0xff200000) == 0xcb000000
def is_SUBS_64_addsub_shift(d): return (d & 0xff200000) == 0xeb000000
def is_ADC_32_addsub_carry(d): return (d & 0xffe0fc00) == 0x1a000000
def is_ADCS_32_addsub_carry(d): return (d & 0xffe0fc00) == 0x3a000000
def is_SBC_32_addsub_carry(d): return (d & 0xffe0fc00) == 0x5a000000
def is_SBCS_32_addsub_carry(d): return (d & 0xffe0fc00) == 0x7a000000
def is_ADC_64_addsub_carry(d): return (d & 0xffe0fc00) == 0x9a000000
def is_ADCS_64_addsub_carry(d): return (d & 0xffe0fc00) == 0xba000000
def is_SBC_64_addsub_carry(d): return (d & 0xffe0fc00) == 0xda000000
def is_SBCS_64_addsub_carry(d): return (d & 0xffe0fc00) == 0xfa000000
def is_CCMN_32_condcmp_imm(d): return (d & 0xffe00c10) == 0x3a400800
def is_CCMP_32_condcmp_imm(d): return (d & 0xffe00c10) == 0x7a400800
def is_CCMN_64_condcmp_imm(d): return (d & 0xffe00c10) == 0xba400800
def is_CCMP_64_condcmp_imm(d): return (d & 0xffe00c10) == 0xfa400800
def is_CCMN_32_condcmp_reg(d): return (d & 0xffe00c10) == 0x3a400000
def is_CCMP_32_condcmp_reg(d): return (d & 0xffe00c10) == 0x7a400000
def is_CCMN_64_condcmp_reg(d): return (d & 0xffe00c10) == 0xba400000
def is_CCMP_64_condcmp_reg(d): return (d & 0xffe00c10) == 0xfa400000
def is_CSEL_32_condsel(d): return (d & 0xffe00c00) == 0x1a800000
def is_CSINC_32_condsel(d): return (d & 0xffe00c00) == 0x1a800400
def is_CSINV_32_condsel(d): return (d & 0xffe00c00) == 0x5a800000
def is_CSNEG_32_condsel(d): return (d & 0xffe00c00) == 0x5a800400
def is_CSEL_64_condsel(d): return (d & 0xffe00c00) == 0x9a800000
def is_CSINC_64_condsel(d): return (d & 0xffe00c00) == 0x9a800400
def is_CSINV_64_condsel(d): return (d & 0xffe00c00) == 0xda800000
def is_CSNEG_64_condsel(d): return (d & 0xffe00c00) == 0xda800400
def is_RBIT_32_dp_1src(d): return (d & 0xfffffc00) == 0x5ac00000
def is_REV16_32_dp_1src(d): return (d & 0xfffffc00) == 0x5ac00400
def is_REV_32_dp_1src(d): return (d & 0xfffffc00) == 0x5ac00800
def is_CLZ_32_dp_1src(d): return (d & 0xfffffc00) == 0x5ac01000
def is_CLS_32_dp_1src(d): return (d & 0xfffffc00) == 0x5ac01400
def is_RBIT_64_dp_1src(d): return (d & 0xfffffc00) == 0xdac00000
def is_REV16_64_dp_1src(d): return (d & 0xfffffc00) == 0xdac00400
def is_REV32_64_dp_1src(d): return (d & 0xfffffc00) == 0xdac00800
def is_REV_64_dp_1src(d): return (d & 0xfffffc00) == 0xdac00c00
def is_CLZ_64_dp_1src(d): return (d & 0xfffffc00) == 0xdac01000
def is_CLS_64_dp_1src(d): return (d & 0xfffffc00) == 0xdac01400
def is_PACIA_64P_dp_1src(d): return (d & 0xfffffc00) == 0xdac10000
def is_PACIB_64P_dp_1src(d): return (d & 0xfffffc00) == 0xdac10400
def is_PACDA_64P_dp_1src(d): return (d & 0xfffffc00) == 0xdac10800
def is_PACDB_64P_dp_1src(d): return (d & 0xfffffc00) == 0xdac10c00
def is_AUTIA_64P_dp_1src(d): return (d & 0xfffffc00) == 0xdac11000
def is_AUTIB_64P_dp_1src(d): return (d & 0xfffffc00) == 0xdac11400
def is_AUTDA_64P_dp_1src(d): return (d & 0xfffffc00) == 0xdac11800
def is_AUTDB_64P_dp_1src(d): return (d & 0xfffffc00) == 0xdac11c00
def is_PACIZA_64Z_dp_1src(d): return (d & 0xffffffe0) == 0xdac123e0
def is_PACIZB_64Z_dp_1src(d): return (d & 0xffffffe0) == 0xdac127e0
def is_PACDZA_64Z_dp_1src(d): return (d & 0xffffffe0) == 0xdac12be0
def is_PACDZB_64Z_dp_1src(d): return (d & 0xffffffe0) == 0xdac12fe0
def is_AUTIZA_64Z_dp_1src(d): return (d & 0xffffffe0) == 0xdac133e0
def is_AUTIZB_64Z_dp_1src(d): return (d & 0xffffffe0) == 0xdac137e0
def is_AUTDZA_64Z_dp_1src(d): return (d & 0xffffffe0) == 0xdac13be0
def is_AUTDZB_64Z_dp_1src(d): return (d & 0xffffffe0) == 0xdac13fe0
def is_XPACI_64Z_dp_1src(d): return (d & 0xffffffe0) == 0xdac143e0
def is_XPACD_64Z_dp_1src(d): return (d & 0xffffffe0) == 0xdac147e0
def is_UDIV_32_dp_2src(d): return (d & 0xffe0fc00) == 0x1ac00800
def is_SDIV_32_dp_2src(d): return (d & 0xffe0fc00) == 0x1ac00c00
def is_LSLV_32_dp_2src(d): return (d & 0xffe0fc00) == 0x1ac02000
def is_LSRV_32_dp_2src(d): return (d & 0xffe0fc00) == 0x1ac02400
def is_ASRV_32_dp_2src(d): return (d & 0xffe0fc00) == 0x1ac02800
def is_RORV_32_dp_2src(d): return (d & 0xffe0fc00) == 0x1ac02c00
def is_CRC32B_32C_dp_2src(d): return (d & 0xffe0fc00) == 0x1ac04000
def is_CRC32H_32C_dp_2src(d): return (d & 0xffe0fc00) == 0x1ac04400
def is_CRC32W_32C_dp_2src(d): return (d & 0xffe0fc00) == 0x1ac04800
def is_CRC32CB_32C_dp_2src(d): return (d & 0xffe0fc00) == 0x1ac05000
def is_CRC32CH_32C_dp_2src(d): return (d & 0xffe0fc00) == 0x1ac05400
def is_CRC32CW_32C_dp_2src(d): return (d & 0xffe0fc00) == 0x1ac05800
def is_UDIV_64_dp_2src(d): return (d & 0xffe0fc00) == 0x9ac00800
def is_SDIV_64_dp_2src(d): return (d & 0xffe0fc00) == 0x9ac00c00
def is_LSLV_64_dp_2src(d): return (d & 0xffe0fc00) == 0x9ac02000
def is_LSRV_64_dp_2src(d): return (d & 0xffe0fc00) == 0x9ac02400
def is_ASRV_64_dp_2src(d): return (d & 0xffe0fc00) == 0x9ac02800
def is_RORV_64_dp_2src(d): return (d & 0xffe0fc00) == 0x9ac02c00
def is_PACGA_64P_dp_2src(d): return (d & 0xffe0fc00) == 0x9ac03000
def is_CRC32X_64C_dp_2src(d): return (d & 0xffe0fc00) == 0x9ac04c00
def is_CRC32CX_64C_dp_2src(d): return (d & 0xffe0fc00) == 0x9ac05c00
def is_MADD_32A_dp_3src(d): return (d & 0xffe08000) == 0x1b000000
def is_MSUB_32A_dp_3src(d): return (d & 0xffe08000) == 0x1b008000
def is_MADD_64A_dp_3src(d): return (d & 0xffe08000) == 0x9b000000
def is_MSUB_64A_dp_3src(d): return (d & 0xffe08000) == 0x9b008000
def is_SMADDL_64WA_dp_3src(d): return (d & 0xffe08000) == 0x9b200000
def is_SMSUBL_64WA_dp_3src(d): return (d & 0xffe08000) == 0x9b208000
def is_SMULH_64_dp_3src(d): return (d & 0xffe08000) == 0x9b400000
def is_UMADDL_64WA_dp_3src(d): return (d & 0xffe08000) == 0x9ba00000
def is_UMSUBL_64WA_dp_3src(d): return (d & 0xffe08000) == 0x9ba08000
def is_UMULH_64_dp_3src(d): return (d & 0xffe08000) == 0x9bc00000
def is_AND_32_log_shift(d): return (d & 0xff200000) == 0x0a000000
def is_BIC_32_log_shift(d): return (d & 0xff200000) == 0x0a200000
def is_ORR_32_log_shift(d): return (d & 0xff200000) == 0x2a000000
def is_ORN_32_log_shift(d): return (d & 0xff200000) == 0x2a200000
def is_EOR_32_log_shift(d): return (d & 0xff200000) == 0x4a000000
def is_EON_32_log_shift(d): return (d & 0xff200000) == 0x4a200000
def is_ANDS_32_log_shift(d): return (d & 0xff200000) == 0x6a000000
def is_BICS_32_log_shift(d): return (d & 0xff200000) == 0x6a200000
def is_AND_64_log_shift(d): return (d & 0xff200000) == 0x8a000000
def is_BIC_64_log_shift(d): return (d & 0xff200000) == 0x8a200000
def is_ORR_64_log_shift(d): return (d & 0xff200000) == 0xaa000000
def is_ORN_64_log_shift(d): return (d & 0xff200000) == 0xaa200000
def is_EOR_64_log_shift(d): return (d & 0xff200000) == 0xca000000
def is_EON_64_log_shift(d): return (d & 0xff200000) == 0xca200000
def is_ANDS_64_log_shift(d): return (d & 0xff200000) == 0xea000000
def is_BICS_64_log_shift(d): return (d & 0xff200000) == 0xea200000
def is_SADDLV_asimdall_only(d): return (d & 0xbf3ffc00) == 0x0e303800
def is_SMAXV_asimdall_only(d): return (d & 0xbf3ffc00) == 0x0e30a800
def is_SMINV_asimdall_only(d): return (d & 0xbf3ffc00) == 0x0e31a800
def is_ADDV_asimdall_only(d): return (d & 0xbf3ffc00) == 0x0e31b800
def is_FMAXNMV_asimdall_only_H(d): return (d & 0xbffffc00) == 0x0e30c800
def is_FMAXV_asimdall_only_H(d): return (d & 0xbffffc00) == 0x0e30f800
def is_FMINNMV_asimdall_only_H(d): return (d & 0xbffffc00) == 0x0eb0c800
def is_FMINV_asimdall_only_H(d): return (d & 0xbffffc00) == 0x0eb0f800
def is_UADDLV_asimdall_only(d): return (d & 0xbf3ffc00) == 0x2e303800
def is_UMAXV_asimdall_only(d): return (d & 0xbf3ffc00) == 0x2e30a800
def is_UMINV_asimdall_only(d): return (d & 0xbf3ffc00) == 0x2e31a800
def is_FMAXNMV_asimdall_only_SD(d): return (d & 0xbfbffc00) == 0x2e30c800
def is_FMAXV_asimdall_only_SD(d): return (d & 0xbfbffc00) == 0x2e30f800
def is_FMINNMV_asimdall_only_SD(d): return (d & 0xbfbffc00) == 0x2eb0c800
def is_FMINV_asimdall_only_SD(d): return (d & 0xbfbffc00) == 0x2eb0f800
def is_DUP_asimdins_DV_v(d): return (d & 0xbfe0fc00) == 0x0e000400
def is_DUP_asimdins_DR_r(d): return (d & 0xbfe0fc00) == 0x0e000c00
def is_SMOV_asimdins_W_w(d): return (d & 0xffe0fc00) == 0x0e002c00
def is_UMOV_asimdins_W_w(d): return (d & 0xffe0fc00) == 0x0e003c00
def is_INS_asimdins_IR_r(d): return (d & 0xffe0fc00) == 0x4e001c00
def is_SMOV_asimdins_X_x(d): return (d & 0xffe0fc00) == 0x4e002c00
def is_UMOV_asimdins_X_x(d): return (d & 0xffeffc00) == 0x4e083c00
def is_INS_asimdins_IV_v(d): return (d & 0xffe08400) == 0x6e000400
def is_EXT_asimdext_only(d): return (d & 0xbfe08400) == 0x2e000000
def is_MOVI_asimdimm_L_sl(d): return (d & 0xbff89c00) == 0x0f000400
def is_ORR_asimdimm_L_sl(d): return (d & 0xbff89c00) == 0x0f001400
def is_MOVI_asimdimm_L_hl(d): return (d & 0xbff8dc00) == 0x0f008400
def is_ORR_asimdimm_L_hl(d): return (d & 0xbff8dc00) == 0x0f009400
def is_MOVI_asimdimm_M_sm(d): return (d & 0xbff8ec00) == 0x0f00c400
def is_MOVI_asimdimm_N_b(d): return (d & 0xbff8fc00) == 0x0f00e400
def is_FMOV_asimdimm_S_s(d): return (d & 0xbff8fc00) == 0x0f00f400
def is_FMOV_asimdimm_H_h(d): return (d & 0xbff8fc00) == 0x0f00fc00
def is_MVNI_asimdimm_L_sl(d): return (d & 0xbff89c00) == 0x2f000400
def is_BIC_asimdimm_L_sl(d): return (d & 0xbff89c00) == 0x2f001400
def is_MVNI_asimdimm_L_hl(d): return (d & 0xbff8dc00) == 0x2f008400
def is_BIC_asimdimm_L_hl(d): return (d & 0xbff8dc00) == 0x2f009400
def is_MVNI_asimdimm_M_sm(d): return (d & 0xbff8ec00) == 0x2f00c400
def is_MOVI_asimdimm_D_ds(d): return (d & 0xfff8fc00) == 0x2f00e400
def is_MOVI_asimdimm_D2_d(d): return (d & 0xfff8fc00) == 0x6f00e400
def is_FMOV_asimdimm_D2_d(d): return (d & 0xfff8fc00) == 0x6f00f400
def is_UZP1_asimdperm_only(d): return (d & 0xbf20fc00) == 0x0e001800
def is_TRN1_asimdperm_only(d): return (d & 0xbf20fc00) == 0x0e002800
def is_ZIP1_asimdperm_only(d): return (d & 0xbf20fc00) == 0x0e003800
def is_UZP2_asimdperm_only(d): return (d & 0xbf20fc00) == 0x0e005800
def is_TRN2_asimdperm_only(d): return (d & 0xbf20fc00) == 0x0e006800
def is_ZIP2_asimdperm_only(d): return (d & 0xbf20fc00) == 0x0e007800
def is_DUP_asisdone_only(d): return (d & 0xffe0fc00) == 0x5e000400
def is_ADDP_asisdpair_only(d): return (d & 0xff3ffc00) == 0x5e31b800
def is_FMAXNMP_asisdpair_only_H(d): return (d & 0xfffffc00) == 0x5e30c800
def is_FADDP_asisdpair_only_H(d): return (d & 0xfffffc00) == 0x5e30d800
def is_FMAXP_asisdpair_only_H(d): return (d & 0xfffffc00) == 0x5e30f800
def is_FMINNMP_asisdpair_only_H(d): return (d & 0xfffffc00) == 0x5eb0c800
def is_FMINP_asisdpair_only_H(d): return (d & 0xfffffc00) == 0x5eb0f800
def is_FMAXNMP_asisdpair_only_SD(d): return (d & 0xffbffc00) == 0x7e30c800
def is_FADDP_asisdpair_only_SD(d): return (d & 0xffbffc00) == 0x7e30d800
def is_FMAXP_asisdpair_only_SD(d): return (d & 0xffbffc00) == 0x7e30f800
def is_FMINNMP_asisdpair_only_SD(d): return (d & 0xffbffc00) == 0x7eb0c800
def is_FMINP_asisdpair_only_SD(d): return (d & 0xffbffc00) == 0x7eb0f800
def is_SSHR_asisdshf_R(d): return (d & 0xff80fc00) == 0x5f000400 and (d & 0x780000) != 0x000000
def is_SSRA_asisdshf_R(d): return (d & 0xff80fc00) == 0x5f001400 and (d & 0x780000) != 0x000000
def is_SRSHR_asisdshf_R(d): return (d & 0xff80fc00) == 0x5f002400 and (d & 0x780000) != 0x000000
def is_SRSRA_asisdshf_R(d): return (d & 0xff80fc00) == 0x5f003400 and (d & 0x780000) != 0x000000
def is_SHL_asisdshf_R(d): return (d & 0xff80fc00) == 0x5f005400 and (d & 0x780000) != 0x000000
def is_SQSHL_asisdshf_R(d): return (d & 0xff80fc00) == 0x5f007400 and (d & 0x780000) != 0x000000
def is_SQSHRN_asisdshf_N(d): return (d & 0xff80fc00) == 0x5f009400 and (d & 0x780000) != 0x000000
def is_SQRSHRN_asisdshf_N(d): return (d & 0xff80fc00) == 0x5f009c00 and (d & 0x780000) != 0x000000
def is_SCVTF_asisdshf_C(d): return (d & 0xff80fc00) == 0x5f00e400 and (d & 0x780000) != 0x000000
def is_FCVTZS_asisdshf_C(d): return (d & 0xff80fc00) == 0x5f00fc00 and (d & 0x780000) != 0x000000
def is_USHR_asisdshf_R(d): return (d & 0xff80fc00) == 0x7f000400 and (d & 0x780000) != 0x000000
def is_USRA_asisdshf_R(d): return (d & 0xff80fc00) == 0x7f001400 and (d & 0x780000) != 0x000000
def is_URSHR_asisdshf_R(d): return (d & 0xff80fc00) == 0x7f002400 and (d & 0x780000) != 0x000000
def is_URSRA_asisdshf_R(d): return (d & 0xff80fc00) == 0x7f003400 and (d & 0x780000) != 0x000000
def is_SRI_asisdshf_R(d): return (d & 0xff80fc00) == 0x7f004400 and (d & 0x780000) != 0x000000
def is_SLI_asisdshf_R(d): return (d & 0xff80fc00) == 0x7f005400 and (d & 0x780000) != 0x000000
def is_SQSHLU_asisdshf_R(d): return (d & 0xff80fc00) == 0x7f006400 and (d & 0x780000) != 0x000000
def is_UQSHL_asisdshf_R(d): return (d & 0xff80fc00) == 0x7f007400 and (d & 0x780000) != 0x000000
def is_SQSHRUN_asisdshf_N(d): return (d & 0xff80fc00) == 0x7f008400 and (d & 0x780000) != 0x000000
def is_SQRSHRUN_asisdshf_N(d): return (d & 0xff80fc00) == 0x7f008c00 and (d & 0x780000) != 0x000000
def is_UQSHRN_asisdshf_N(d): return (d & 0xff80fc00) == 0x7f009400 and (d & 0x780000) != 0x000000
def is_UQRSHRN_asisdshf_N(d): return (d & 0xff80fc00) == 0x7f009c00 and (d & 0x780000) != 0x000000
def is_UCVTF_asisdshf_C(d): return (d & 0xff80fc00) == 0x7f00e400 and (d & 0x780000) != 0x000000
def is_FCVTZU_asisdshf_C(d): return (d & 0xff80fc00) == 0x7f00fc00 and (d & 0x780000) != 0x000000
def is_SQDMLAL_asisddiff_only(d): return (d & 0xff20fc00) == 0x5e209000
def is_SQDMLSL_asisddiff_only(d): return (d & 0xff20fc00) == 0x5e20b000
def is_SQDMULL_asisddiff_only(d): return (d & 0xff20fc00) == 0x5e20d000
def is_SQADD_asisdsame_only(d): return (d & 0xff20fc00) == 0x5e200c00
def is_SQSUB_asisdsame_only(d): return (d & 0xff20fc00) == 0x5e202c00
def is_CMGT_asisdsame_only(d): return (d & 0xff20fc00) == 0x5e203400
def is_CMGE_asisdsame_only(d): return (d & 0xff20fc00) == 0x5e203c00
def is_SSHL_asisdsame_only(d): return (d & 0xff20fc00) == 0x5e204400
def is_SQSHL_asisdsame_only(d): return (d & 0xff20fc00) == 0x5e204c00
def is_SRSHL_asisdsame_only(d): return (d & 0xff20fc00) == 0x5e205400
def is_SQRSHL_asisdsame_only(d): return (d & 0xff20fc00) == 0x5e205c00
def is_ADD_asisdsame_only(d): return (d & 0xff20fc00) == 0x5e208400
def is_CMTST_asisdsame_only(d): return (d & 0xff20fc00) == 0x5e208c00
def is_SQDMULH_asisdsame_only(d): return (d & 0xff20fc00) == 0x5e20b400
def is_FMULX_asisdsame_only(d): return (d & 0xffa0fc00) == 0x5e20dc00
def is_FCMEQ_asisdsame_only(d): return (d & 0xffa0fc00) == 0x5e20e400
def is_FRECPS_asisdsame_only(d): return (d & 0xffa0fc00) == 0x5e20fc00
def is_FRSQRTS_asisdsame_only(d): return (d & 0xffa0fc00) == 0x5ea0fc00
def is_UQADD_asisdsame_only(d): return (d & 0xff20fc00) == 0x7e200c00
def is_UQSUB_asisdsame_only(d): return (d & 0xff20fc00) == 0x7e202c00
def is_CMHI_asisdsame_only(d): return (d & 0xff20fc00) == 0x7e203400
def is_CMHS_asisdsame_only(d): return (d & 0xff20fc00) == 0x7e203c00
def is_USHL_asisdsame_only(d): return (d & 0xff20fc00) == 0x7e204400
def is_UQSHL_asisdsame_only(d): return (d & 0xff20fc00) == 0x7e204c00
def is_URSHL_asisdsame_only(d): return (d & 0xff20fc00) == 0x7e205400
def is_UQRSHL_asisdsame_only(d): return (d & 0xff20fc00) == 0x7e205c00
def is_SUB_asisdsame_only(d): return (d & 0xff20fc00) == 0x7e208400
def is_CMEQ_asisdsame_only(d): return (d & 0xff20fc00) == 0x7e208c00
def is_SQRDMULH_asisdsame_only(d): return (d & 0xff20fc00) == 0x7e20b400
def is_FCMGE_asisdsame_only(d): return (d & 0xffa0fc00) == 0x7e20e400
def is_FACGE_asisdsame_only(d): return (d & 0xffa0fc00) == 0x7e20ec00
def is_FABD_asisdsame_only(d): return (d & 0xffa0fc00) == 0x7ea0d400
def is_FCMGT_asisdsame_only(d): return (d & 0xffa0fc00) == 0x7ea0e400
def is_FACGT_asisdsame_only(d): return (d & 0xffa0fc00) == 0x7ea0ec00
def is_FMULX_asisdsamefp16_only(d): return (d & 0xffe0fc00) == 0x5e401c00
def is_FCMEQ_asisdsamefp16_only(d): return (d & 0xffe0fc00) == 0x5e402400
def is_FRECPS_asisdsamefp16_only(d): return (d & 0xffe0fc00) == 0x5e403c00
def is_FRSQRTS_asisdsamefp16_only(d): return (d & 0xffe0fc00) == 0x5ec03c00
def is_FCMGE_asisdsamefp16_only(d): return (d & 0xffe0fc00) == 0x7e402400
def is_FACGE_asisdsamefp16_only(d): return (d & 0xffe0fc00) == 0x7e402c00
def is_FABD_asisdsamefp16_only(d): return (d & 0xffe0fc00) == 0x7ec01400
def is_FCMGT_asisdsamefp16_only(d): return (d & 0xffe0fc00) == 0x7ec02400
def is_FACGT_asisdsamefp16_only(d): return (d & 0xffe0fc00) == 0x7ec02c00
def is_SQRDMLAH_asisdsame2_only(d): return (d & 0xff20fc00) == 0x7e008400
def is_SQRDMLSH_asisdsame2_only(d): return (d & 0xff20fc00) == 0x7e008c00
def is_SUQADD_asisdmisc_R(d): return (d & 0xff3ffc00) == 0x5e203800
def is_SQABS_asisdmisc_R(d): return (d & 0xff3ffc00) == 0x5e207800
def is_CMGT_asisdmisc_Z(d): return (d & 0xff3ffc00) == 0x5e208800
def is_CMEQ_asisdmisc_Z(d): return (d & 0xff3ffc00) == 0x5e209800
def is_CMLT_asisdmisc_Z(d): return (d & 0xff3ffc00) == 0x5e20a800
def is_ABS_asisdmisc_R(d): return (d & 0xff3ffc00) == 0x5e20b800
def is_SQXTN_asisdmisc_N(d): return (d & 0xff3ffc00) == 0x5e214800
def is_FCVTNS_asisdmisc_R(d): return (d & 0xffbffc00) == 0x5e21a800
def is_FCVTMS_asisdmisc_R(d): return (d & 0xffbffc00) == 0x5e21b800
def is_FCVTAS_asisdmisc_R(d): return (d & 0xffbffc00) == 0x5e21c800
def is_SCVTF_asisdmisc_R(d): return (d & 0xffbffc00) == 0x5e21d800
def is_FCMGT_asisdmisc_FZ(d): return (d & 0xffbffc00) == 0x5ea0c800
def is_FCMEQ_asisdmisc_FZ(d): return (d & 0xffbffc00) == 0x5ea0d800
def is_FCMLT_asisdmisc_FZ(d): return (d & 0xffbffc00) == 0x5ea0e800
def is_FCVTPS_asisdmisc_R(d): return (d & 0xffbffc00) == 0x5ea1a800
def is_FCVTZS_asisdmisc_R(d): return (d & 0xffbffc00) == 0x5ea1b800
def is_FRECPE_asisdmisc_R(d): return (d & 0xffbffc00) == 0x5ea1d800
def is_FRECPX_asisdmisc_R(d): return (d & 0xffbffc00) == 0x5ea1f800
def is_USQADD_asisdmisc_R(d): return (d & 0xff3ffc00) == 0x7e203800
def is_SQNEG_asisdmisc_R(d): return (d & 0xff3ffc00) == 0x7e207800
def is_CMGE_asisdmisc_Z(d): return (d & 0xff3ffc00) == 0x7e208800
def is_CMLE_asisdmisc_Z(d): return (d & 0xff3ffc00) == 0x7e209800
def is_NEG_asisdmisc_R(d): return (d & 0xff3ffc00) == 0x7e20b800
def is_SQXTUN_asisdmisc_N(d): return (d & 0xff3ffc00) == 0x7e212800
def is_UQXTN_asisdmisc_N(d): return (d & 0xff3ffc00) == 0x7e214800
def is_FCVTXN_asisdmisc_N(d): return (d & 0xffbffc00) == 0x7e216800
def is_FCVTNU_asisdmisc_R(d): return (d & 0xffbffc00) == 0x7e21a800
def is_FCVTMU_asisdmisc_R(d): return (d & 0xffbffc00) == 0x7e21b800
def is_FCVTAU_asisdmisc_R(d): return (d & 0xffbffc00) == 0x7e21c800
def is_UCVTF_asisdmisc_R(d): return (d & 0xffbffc00) == 0x7e21d800
def is_FCMGE_asisdmisc_FZ(d): return (d & 0xffbffc00) == 0x7ea0c800
def is_FCMLE_asisdmisc_FZ(d): return (d & 0xffbffc00) == 0x7ea0d800
def is_FCVTPU_asisdmisc_R(d): return (d & 0xffbffc00) == 0x7ea1a800
def is_FCVTZU_asisdmisc_R(d): return (d & 0xffbffc00) == 0x7ea1b800
def is_FRSQRTE_asisdmisc_R(d): return (d & 0xffbffc00) == 0x7ea1d800
def is_FCVTNS_asisdmiscfp16_R(d): return (d & 0xfffffc00) == 0x5e79a800
def is_FCVTMS_asisdmiscfp16_R(d): return (d & 0xfffffc00) == 0x5e79b800
def is_FCVTAS_asisdmiscfp16_R(d): return (d & 0xfffffc00) == 0x5e79c800
def is_SCVTF_asisdmiscfp16_R(d): return (d & 0xfffffc00) == 0x5e79d800
def is_FCMGT_asisdmiscfp16_FZ(d): return (d & 0xfffffc00) == 0x5ef8c800
def is_FCMEQ_asisdmiscfp16_FZ(d): return (d & 0xfffffc00) == 0x5ef8d800
def is_FCMLT_asisdmiscfp16_FZ(d): return (d & 0xfffffc00) == 0x5ef8e800
def is_FCVTPS_asisdmiscfp16_R(d): return (d & 0xfffffc00) == 0x5ef9a800
def is_FCVTZS_asisdmiscfp16_R(d): return (d & 0xfffffc00) == 0x5ef9b800
def is_FRECPE_asisdmiscfp16_R(d): return (d & 0xfffffc00) == 0x5ef9d800
def is_FRECPX_asisdmiscfp16_R(d): return (d & 0xfffffc00) == 0x5ef9f800
def is_FCVTNU_asisdmiscfp16_R(d): return (d & 0xfffffc00) == 0x7e79a800
def is_FCVTMU_asisdmiscfp16_R(d): return (d & 0xfffffc00) == 0x7e79b800
def is_FCVTAU_asisdmiscfp16_R(d): return (d & 0xfffffc00) == 0x7e79c800
def is_UCVTF_asisdmiscfp16_R(d): return (d & 0xfffffc00) == 0x7e79d800
def is_FCMGE_asisdmiscfp16_FZ(d): return (d & 0xfffffc00) == 0x7ef8c800
def is_FCMLE_asisdmiscfp16_FZ(d): return (d & 0xfffffc00) == 0x7ef8d800
def is_FCVTPU_asisdmiscfp16_R(d): return (d & 0xfffffc00) == 0x7ef9a800
def is_FCVTZU_asisdmiscfp16_R(d): return (d & 0xfffffc00) == 0x7ef9b800
def is_FRSQRTE_asisdmiscfp16_R(d): return (d & 0xfffffc00) == 0x7ef9d800
def is_SQDMLAL_asisdelem_L(d): return (d & 0xff00f400) == 0x5f003000
def is_SQDMLSL_asisdelem_L(d): return (d & 0xff00f400) == 0x5f007000
def is_SQDMULL_asisdelem_L(d): return (d & 0xff00f400) == 0x5f00b000
def is_SQDMULH_asisdelem_R(d): return (d & 0xff00f400) == 0x5f00c000
def is_SQRDMULH_asisdelem_R(d): return (d & 0xff00f400) == 0x5f00d000
def is_FMLA_asisdelem_RH_H(d): return (d & 0xffc0f400) == 0x5f001000
def is_FMLS_asisdelem_RH_H(d): return (d & 0xffc0f400) == 0x5f005000
def is_FMUL_asisdelem_RH_H(d): return (d & 0xffc0f400) == 0x5f009000
def is_FMLA_asisdelem_R_SD(d): return (d & 0xff80f400) == 0x5f801000
def is_FMLS_asisdelem_R_SD(d): return (d & 0xff80f400) == 0x5f805000
def is_FMUL_asisdelem_R_SD(d): return (d & 0xff80f400) == 0x5f809000
def is_SQRDMLAH_asisdelem_R(d): return (d & 0xff00f400) == 0x7f00d000
def is_SQRDMLSH_asisdelem_R(d): return (d & 0xff00f400) == 0x7f00f000
def is_FMULX_asisdelem_RH_H(d): return (d & 0xffc0f400) == 0x7f009000
def is_FMULX_asisdelem_R_SD(d): return (d & 0xff80f400) == 0x7f809000
def is_SSHR_asimdshf_R(d): return (d & 0xbf80fc00) == 0x0f000400 and (d & 0x780000) != 0x000000
def is_SSRA_asimdshf_R(d): return (d & 0xbf80fc00) == 0x0f001400 and (d & 0x780000) != 0x000000
def is_SRSHR_asimdshf_R(d): return (d & 0xbf80fc00) == 0x0f002400 and (d & 0x780000) != 0x000000
def is_SRSRA_asimdshf_R(d): return (d & 0xbf80fc00) == 0x0f003400 and (d & 0x780000) != 0x000000
def is_SHL_asimdshf_R(d): return (d & 0xbf80fc00) == 0x0f005400 and (d & 0x780000) != 0x000000
def is_SQSHL_asimdshf_R(d): return (d & 0xbf80fc00) == 0x0f007400 and (d & 0x780000) != 0x000000
def is_SHRN_asimdshf_N(d): return (d & 0xbf80fc00) == 0x0f008400 and (d & 0x780000) != 0x000000
def is_RSHRN_asimdshf_N(d): return (d & 0xbf80fc00) == 0x0f008c00 and (d & 0x780000) != 0x000000
def is_SQSHRN_asimdshf_N(d): return (d & 0xbf80fc00) == 0x0f009400 and (d & 0x780000) != 0x000000
def is_SQRSHRN_asimdshf_N(d): return (d & 0xbf80fc00) == 0x0f009c00 and (d & 0x780000) != 0x000000
def is_SSHLL_asimdshf_L(d): return (d & 0xbf80fc00) == 0x0f00a400 and (d & 0x780000) != 0x000000
def is_SCVTF_asimdshf_C(d): return (d & 0xbf80fc00) == 0x0f00e400 and (d & 0x780000) != 0x000000
def is_FCVTZS_asimdshf_C(d): return (d & 0xbf80fc00) == 0x0f00fc00 and (d & 0x780000) != 0x000000
def is_USHR_asimdshf_R(d): return (d & 0xbf80fc00) == 0x2f000400 and (d & 0x780000) != 0x000000
def is_USRA_asimdshf_R(d): return (d & 0xbf80fc00) == 0x2f001400 and (d & 0x780000) != 0x000000
def is_URSHR_asimdshf_R(d): return (d & 0xbf80fc00) == 0x2f002400 and (d & 0x780000) != 0x000000
def is_URSRA_asimdshf_R(d): return (d & 0xbf80fc00) == 0x2f003400 and (d & 0x780000) != 0x000000
def is_SRI_asimdshf_R(d): return (d & 0xbf80fc00) == 0x2f004400 and (d & 0x780000) != 0x000000
def is_SLI_asimdshf_R(d): return (d & 0xbf80fc00) == 0x2f005400 and (d & 0x780000) != 0x000000
def is_SQSHLU_asimdshf_R(d): return (d & 0xbf80fc00) == 0x2f006400 and (d & 0x780000) != 0x000000
def is_UQSHL_asimdshf_R(d): return (d & 0xbf80fc00) == 0x2f007400 and (d & 0x780000) != 0x000000
def is_SQSHRUN_asimdshf_N(d): return (d & 0xbf80fc00) == 0x2f008400 and (d & 0x780000) != 0x000000
def is_SQRSHRUN_asimdshf_N(d): return (d & 0xbf80fc00) == 0x2f008c00 and (d & 0x780000) != 0x000000
def is_UQSHRN_asimdshf_N(d): return (d & 0xbf80fc00) == 0x2f009400 and (d & 0x780000) != 0x000000
def is_UQRSHRN_asimdshf_N(d): return (d & 0xbf80fc00) == 0x2f009c00 and (d & 0x780000) != 0x000000
def is_USHLL_asimdshf_L(d): return (d & 0xbf80fc00) == 0x2f00a400 and (d & 0x780000) != 0x000000
def is_UCVTF_asimdshf_C(d): return (d & 0xbf80fc00) == 0x2f00e400 and (d & 0x780000) != 0x000000
def is_FCVTZU_asimdshf_C(d): return (d & 0xbf80fc00) == 0x2f00fc00 and (d & 0x780000) != 0x000000
def is_TBL_asimdtbl_L1_1(d): return (d & 0xbfe0fc00) == 0x0e000000
def is_TBX_asimdtbl_L1_1(d): return (d & 0xbfe0fc00) == 0x0e001000
def is_TBL_asimdtbl_L2_2(d): return (d & 0xbfe0fc00) == 0x0e002000
def is_TBX_asimdtbl_L2_2(d): return (d & 0xbfe0fc00) == 0x0e003000
def is_TBL_asimdtbl_L3_3(d): return (d & 0xbfe0fc00) == 0x0e004000
def is_TBX_asimdtbl_L3_3(d): return (d & 0xbfe0fc00) == 0x0e005000
def is_TBL_asimdtbl_L4_4(d): return (d & 0xbfe0fc00) == 0x0e006000
def is_TBX_asimdtbl_L4_4(d): return (d & 0xbfe0fc00) == 0x0e007000
def is_SADDL_asimddiff_L(d): return (d & 0xbf20fc00) == 0x0e200000
def is_SADDW_asimddiff_W(d): return (d & 0xbf20fc00) == 0x0e201000
def is_SSUBL_asimddiff_L(d): return (d & 0xbf20fc00) == 0x0e202000
def is_SSUBW_asimddiff_W(d): return (d & 0xbf20fc00) == 0x0e203000
def is_ADDHN_asimddiff_N(d): return (d & 0xbf20fc00) == 0x0e204000
def is_SABAL_asimddiff_L(d): return (d & 0xbf20fc00) == 0x0e205000
def is_SUBHN_asimddiff_N(d): return (d & 0xbf20fc00) == 0x0e206000
def is_SABDL_asimddiff_L(d): return (d & 0xbf20fc00) == 0x0e207000
def is_SMLAL_asimddiff_L(d): return (d & 0xbf20fc00) == 0x0e208000
def is_SQDMLAL_asimddiff_L(d): return (d & 0xbf20fc00) == 0x0e209000
def is_SMLSL_asimddiff_L(d): return (d & 0xbf20fc00) == 0x0e20a000
def is_SQDMLSL_asimddiff_L(d): return (d & 0xbf20fc00) == 0x0e20b000
def is_SMULL_asimddiff_L(d): return (d & 0xbf20fc00) == 0x0e20c000
def is_SQDMULL_asimddiff_L(d): return (d & 0xbf20fc00) == 0x0e20d000
def is_PMULL_asimddiff_L(d): return (d & 0xbf20fc00) == 0x0e20e000
def is_UADDL_asimddiff_L(d): return (d & 0xbf20fc00) == 0x2e200000
def is_UADDW_asimddiff_W(d): return (d & 0xbf20fc00) == 0x2e201000
def is_USUBL_asimddiff_L(d): return (d & 0xbf20fc00) == 0x2e202000
def is_USUBW_asimddiff_W(d): return (d & 0xbf20fc00) == 0x2e203000
def is_RADDHN_asimddiff_N(d): return (d & 0xbf20fc00) == 0x2e204000
def is_UABAL_asimddiff_L(d): return (d & 0xbf20fc00) == 0x2e205000
def is_RSUBHN_asimddiff_N(d): return (d & 0xbf20fc00) == 0x2e206000
def is_UABDL_asimddiff_L(d): return (d & 0xbf20fc00) == 0x2e207000
def is_UMLAL_asimddiff_L(d): return (d & 0xbf20fc00) == 0x2e208000
def is_UMLSL_asimddiff_L(d): return (d & 0xbf20fc00) == 0x2e20a000
def is_UMULL_asimddiff_L(d): return (d & 0xbf20fc00) == 0x2e20c000
def is_SHADD_asimdsame_only(d): return (d & 0xbf20fc00) == 0x0e200400
def is_SQADD_asimdsame_only(d): return (d & 0xbf20fc00) == 0x0e200c00
def is_SRHADD_asimdsame_only(d): return (d & 0xbf20fc00) == 0x0e201400
def is_SHSUB_asimdsame_only(d): return (d & 0xbf20fc00) == 0x0e202400
def is_SQSUB_asimdsame_only(d): return (d & 0xbf20fc00) == 0x0e202c00
def is_CMGT_asimdsame_only(d): return (d & 0xbf20fc00) == 0x0e203400
def is_CMGE_asimdsame_only(d): return (d & 0xbf20fc00) == 0x0e203c00
def is_SSHL_asimdsame_only(d): return (d & 0xbf20fc00) == 0x0e204400
def is_SQSHL_asimdsame_only(d): return (d & 0xbf20fc00) == 0x0e204c00
def is_SRSHL_asimdsame_only(d): return (d & 0xbf20fc00) == 0x0e205400
def is_SQRSHL_asimdsame_only(d): return (d & 0xbf20fc00) == 0x0e205c00
def is_SMAX_asimdsame_only(d): return (d & 0xbf20fc00) == 0x0e206400
def is_SMIN_asimdsame_only(d): return (d & 0xbf20fc00) == 0x0e206c00
def is_SABD_asimdsame_only(d): return (d & 0xbf20fc00) == 0x0e207400
def is_SABA_asimdsame_only(d): return (d & 0xbf20fc00) == 0x0e207c00
def is_ADD_asimdsame_only(d): return (d & 0xbf20fc00) == 0x0e208400
def is_CMTST_asimdsame_only(d): return (d & 0xbf20fc00) == 0x0e208c00
def is_MLA_asimdsame_only(d): return (d & 0xbf20fc00) == 0x0e209400
def is_MUL_asimdsame_only(d): return (d & 0xbf20fc00) == 0x0e209c00
def is_SMAXP_asimdsame_only(d): return (d & 0xbf20fc00) == 0x0e20a400
def is_SMINP_asimdsame_only(d): return (d & 0xbf20fc00) == 0x0e20ac00
def is_SQDMULH_asimdsame_only(d): return (d & 0xbf20fc00) == 0x0e20b400
def is_ADDP_asimdsame_only(d): return (d & 0xbf20fc00) == 0x0e20bc00
def is_FMAXNM_asimdsame_only(d): return (d & 0xbfa0fc00) == 0x0e20c400
def is_FMLA_asimdsame_only(d): return (d & 0xbfa0fc00) == 0x0e20cc00
def is_FADD_asimdsame_only(d): return (d & 0xbfa0fc00) == 0x0e20d400
def is_FMULX_asimdsame_only(d): return (d & 0xbfa0fc00) == 0x0e20dc00
def is_FCMEQ_asimdsame_only(d): return (d & 0xbfa0fc00) == 0x0e20e400
def is_FMAX_asimdsame_only(d): return (d & 0xbfa0fc00) == 0x0e20f400
def is_FRECPS_asimdsame_only(d): return (d & 0xbfa0fc00) == 0x0e20fc00
def is_AND_asimdsame_only(d): return (d & 0xbfe0fc00) == 0x0e201c00
def is_BIC_asimdsame_only(d): return (d & 0xbfe0fc00) == 0x0e601c00
def is_FMINNM_asimdsame_only(d): return (d & 0xbfa0fc00) == 0x0ea0c400
def is_FMLS_asimdsame_only(d): return (d & 0xbfa0fc00) == 0x0ea0cc00
def is_FSUB_asimdsame_only(d): return (d & 0xbfa0fc00) == 0x0ea0d400
def is_FMIN_asimdsame_only(d): return (d & 0xbfa0fc00) == 0x0ea0f400
def is_FRSQRTS_asimdsame_only(d): return (d & 0xbfa0fc00) == 0x0ea0fc00
def is_ORR_asimdsame_only(d): return (d & 0xbfe0fc00) == 0x0ea01c00
def is_ORN_asimdsame_only(d): return (d & 0xbfe0fc00) == 0x0ee01c00
def is_UHADD_asimdsame_only(d): return (d & 0xbf20fc00) == 0x2e200400
def is_UQADD_asimdsame_only(d): return (d & 0xbf20fc00) == 0x2e200c00
def is_URHADD_asimdsame_only(d): return (d & 0xbf20fc00) == 0x2e201400
def is_UHSUB_asimdsame_only(d): return (d & 0xbf20fc00) == 0x2e202400
def is_UQSUB_asimdsame_only(d): return (d & 0xbf20fc00) == 0x2e202c00
def is_CMHI_asimdsame_only(d): return (d & 0xbf20fc00) == 0x2e203400
def is_CMHS_asimdsame_only(d): return (d & 0xbf20fc00) == 0x2e203c00
def is_USHL_asimdsame_only(d): return (d & 0xbf20fc00) == 0x2e204400
def is_UQSHL_asimdsame_only(d): return (d & 0xbf20fc00) == 0x2e204c00
def is_URSHL_asimdsame_only(d): return (d & 0xbf20fc00) == 0x2e205400
def is_UQRSHL_asimdsame_only(d): return (d & 0xbf20fc00) == 0x2e205c00
def is_UMAX_asimdsame_only(d): return (d & 0xbf20fc00) == 0x2e206400
def is_UMIN_asimdsame_only(d): return (d & 0xbf20fc00) == 0x2e206c00
def is_UABD_asimdsame_only(d): return (d & 0xbf20fc00) == 0x2e207400
def is_UABA_asimdsame_only(d): return (d & 0xbf20fc00) == 0x2e207c00
def is_SUB_asimdsame_only(d): return (d & 0xbf20fc00) == 0x2e208400
def is_CMEQ_asimdsame_only(d): return (d & 0xbf20fc00) == 0x2e208c00
def is_MLS_asimdsame_only(d): return (d & 0xbf20fc00) == 0x2e209400
def is_PMUL_asimdsame_only(d): return (d & 0xbf20fc00) == 0x2e209c00
def is_UMAXP_asimdsame_only(d): return (d & 0xbf20fc00) == 0x2e20a400
def is_UMINP_asimdsame_only(d): return (d & 0xbf20fc00) == 0x2e20ac00
def is_SQRDMULH_asimdsame_only(d): return (d & 0xbf20fc00) == 0x2e20b400
def is_FMAXNMP_asimdsame_only(d): return (d & 0xbfa0fc00) == 0x2e20c400
def is_FADDP_asimdsame_only(d): return (d & 0xbfa0fc00) == 0x2e20d400
def is_FMUL_asimdsame_only(d): return (d & 0xbfa0fc00) == 0x2e20dc00
def is_FCMGE_asimdsame_only(d): return (d & 0xbfa0fc00) == 0x2e20e400
def is_FACGE_asimdsame_only(d): return (d & 0xbfa0fc00) == 0x2e20ec00
def is_FMAXP_asimdsame_only(d): return (d & 0xbfa0fc00) == 0x2e20f400
def is_FDIV_asimdsame_only(d): return (d & 0xbfa0fc00) == 0x2e20fc00
def is_EOR_asimdsame_only(d): return (d & 0xbfe0fc00) == 0x2e201c00
def is_BSL_asimdsame_only(d): return (d & 0xbfe0fc00) == 0x2e601c00
def is_FMINNMP_asimdsame_only(d): return (d & 0xbfa0fc00) == 0x2ea0c400
def is_FABD_asimdsame_only(d): return (d & 0xbfa0fc00) == 0x2ea0d400
def is_FCMGT_asimdsame_only(d): return (d & 0xbfa0fc00) == 0x2ea0e400
def is_FACGT_asimdsame_only(d): return (d & 0xbfa0fc00) == 0x2ea0ec00
def is_FMINP_asimdsame_only(d): return (d & 0xbfa0fc00) == 0x2ea0f400
def is_BIT_asimdsame_only(d): return (d & 0xbfe0fc00) == 0x2ea01c00
def is_BIF_asimdsame_only(d): return (d & 0xbfe0fc00) == 0x2ee01c00
def is_FMAXNM_asimdsamefp16_only(d): return (d & 0xbfe0fc00) == 0x0e400400
def is_FMLA_asimdsamefp16_only(d): return (d & 0xbfe0fc00) == 0x0e400c00
def is_FADD_asimdsamefp16_only(d): return (d & 0xbfe0fc00) == 0x0e401400
def is_FMULX_asimdsamefp16_only(d): return (d & 0xbfe0fc00) == 0x0e401c00
def is_FCMEQ_asimdsamefp16_only(d): return (d & 0xbfe0fc00) == 0x0e402400
def is_FMAX_asimdsamefp16_only(d): return (d & 0xbfe0fc00) == 0x0e403400
def is_FRECPS_asimdsamefp16_only(d): return (d & 0xbfe0fc00) == 0x0e403c00
def is_FMINNM_asimdsamefp16_only(d): return (d & 0xbfe0fc00) == 0x0ec00400
def is_FMLS_asimdsamefp16_only(d): return (d & 0xbfe0fc00) == 0x0ec00c00
def is_FSUB_asimdsamefp16_only(d): return (d & 0xbfe0fc00) == 0x0ec01400
def is_FMIN_asimdsamefp16_only(d): return (d & 0xbfe0fc00) == 0x0ec03400
def is_FRSQRTS_asimdsamefp16_only(d): return (d & 0xbfe0fc00) == 0x0ec03c00
def is_FMAXNMP_asimdsamefp16_only(d): return (d & 0xbfe0fc00) == 0x2e400400
def is_FADDP_asimdsamefp16_only(d): return (d & 0xbfe0fc00) == 0x2e401400
def is_FMUL_asimdsamefp16_only(d): return (d & 0xbfe0fc00) == 0x2e401c00
def is_FCMGE_asimdsamefp16_only(d): return (d & 0xbfe0fc00) == 0x2e402400
def is_FACGE_asimdsamefp16_only(d): return (d & 0xbfe0fc00) == 0x2e402c00
def is_FMAXP_asimdsamefp16_only(d): return (d & 0xbfe0fc00) == 0x2e403400
def is_FDIV_asimdsamefp16_only(d): return (d & 0xbfe0fc00) == 0x2e403c00
def is_FMINNMP_asimdsamefp16_only(d): return (d & 0xbfe0fc00) == 0x2ec00400
def is_FABD_asimdsamefp16_only(d): return (d & 0xbfe0fc00) == 0x2ec01400
def is_FCMGT_asimdsamefp16_only(d): return (d & 0xbfe0fc00) == 0x2ec02400
def is_FACGT_asimdsamefp16_only(d): return (d & 0xbfe0fc00) == 0x2ec02c00
def is_FMINP_asimdsamefp16_only(d): return (d & 0xbfe0fc00) == 0x2ec03400
def is_SDOT_asimdsame2_D(d): return (d & 0xbf20fc00) == 0x0e009400
def is_SQRDMLAH_asimdsame2_only(d): return (d & 0xbf20fc00) == 0x2e008400
def is_SQRDMLSH_asimdsame2_only(d): return (d & 0xbf20fc00) == 0x2e008c00
def is_UDOT_asimdsame2_D(d): return (d & 0xbf20fc00) == 0x2e009400
def is_FCMLA_asimdsame2_C(d): return (d & 0xbf20e400) == 0x2e00c400
def is_FCADD_asimdsame2_C(d): return (d & 0xbf20ec00) == 0x2e00e400
def is_REV64_asimdmisc_R(d): return (d & 0xbf3ffc00) == 0x0e200800
def is_REV16_asimdmisc_R(d): return (d & 0xbf3ffc00) == 0x0e201800
def is_SADDLP_asimdmisc_P(d): return (d & 0xbf3ffc00) == 0x0e202800
def is_SUQADD_asimdmisc_R(d): return (d & 0xbf3ffc00) == 0x0e203800
def is_CLS_asimdmisc_R(d): return (d & 0xbf3ffc00) == 0x0e204800
def is_CNT_asimdmisc_R(d): return (d & 0xbf3ffc00) == 0x0e205800
def is_SADALP_asimdmisc_P(d): return (d & 0xbf3ffc00) == 0x0e206800
def is_SQABS_asimdmisc_R(d): return (d & 0xbf3ffc00) == 0x0e207800
def is_CMGT_asimdmisc_Z(d): return (d & 0xbf3ffc00) == 0x0e208800
def is_CMEQ_asimdmisc_Z(d): return (d & 0xbf3ffc00) == 0x0e209800
def is_CMLT_asimdmisc_Z(d): return (d & 0xbf3ffc00) == 0x0e20a800
def is_ABS_asimdmisc_R(d): return (d & 0xbf3ffc00) == 0x0e20b800
def is_XTN_asimdmisc_N(d): return (d & 0xbf3ffc00) == 0x0e212800
def is_SQXTN_asimdmisc_N(d): return (d & 0xbf3ffc00) == 0x0e214800
def is_FCVTN_asimdmisc_N(d): return (d & 0xbfbffc00) == 0x0e216800
def is_FCVTL_asimdmisc_L(d): return (d & 0xbfbffc00) == 0x0e217800
def is_FRINTN_asimdmisc_R(d): return (d & 0xbfbffc00) == 0x0e218800
def is_FRINTM_asimdmisc_R(d): return (d & 0xbfbffc00) == 0x0e219800
def is_FCVTNS_asimdmisc_R(d): return (d & 0xbfbffc00) == 0x0e21a800
def is_FCVTMS_asimdmisc_R(d): return (d & 0xbfbffc00) == 0x0e21b800
def is_FCVTAS_asimdmisc_R(d): return (d & 0xbfbffc00) == 0x0e21c800
def is_SCVTF_asimdmisc_R(d): return (d & 0xbfbffc00) == 0x0e21d800
def is_FCMGT_asimdmisc_FZ(d): return (d & 0xbfbffc00) == 0x0ea0c800
def is_FCMEQ_asimdmisc_FZ(d): return (d & 0xbfbffc00) == 0x0ea0d800
def is_FCMLT_asimdmisc_FZ(d): return (d & 0xbfbffc00) == 0x0ea0e800
def is_FABS_asimdmisc_R(d): return (d & 0xbfbffc00) == 0x0ea0f800
def is_FRINTP_asimdmisc_R(d): return (d & 0xbfbffc00) == 0x0ea18800
def is_FRINTZ_asimdmisc_R(d): return (d & 0xbfbffc00) == 0x0ea19800
def is_FCVTPS_asimdmisc_R(d): return (d & 0xbfbffc00) == 0x0ea1a800
def is_FCVTZS_asimdmisc_R(d): return (d & 0xbfbffc00) == 0x0ea1b800
def is_URECPE_asimdmisc_R(d): return (d & 0xbfbffc00) == 0x0ea1c800
def is_FRECPE_asimdmisc_R(d): return (d & 0xbfbffc00) == 0x0ea1d800
def is_REV32_asimdmisc_R(d): return (d & 0xbf3ffc00) == 0x2e200800
def is_UADDLP_asimdmisc_P(d): return (d & 0xbf3ffc00) == 0x2e202800
def is_USQADD_asimdmisc_R(d): return (d & 0xbf3ffc00) == 0x2e203800
def is_CLZ_asimdmisc_R(d): return (d & 0xbf3ffc00) == 0x2e204800
def is_UADALP_asimdmisc_P(d): return (d & 0xbf3ffc00) == 0x2e206800
def is_SQNEG_asimdmisc_R(d): return (d & 0xbf3ffc00) == 0x2e207800
def is_CMGE_asimdmisc_Z(d): return (d & 0xbf3ffc00) == 0x2e208800
def is_CMLE_asimdmisc_Z(d): return (d & 0xbf3ffc00) == 0x2e209800
def is_NEG_asimdmisc_R(d): return (d & 0xbf3ffc00) == 0x2e20b800
def is_SQXTUN_asimdmisc_N(d): return (d & 0xbf3ffc00) == 0x2e212800
def is_SHLL_asimdmisc_S(d): return (d & 0xbf3ffc00) == 0x2e213800
def is_UQXTN_asimdmisc_N(d): return (d & 0xbf3ffc00) == 0x2e214800
def is_FCVTXN_asimdmisc_N(d): return (d & 0xbfbffc00) == 0x2e216800
def is_FRINTA_asimdmisc_R(d): return (d & 0xbfbffc00) == 0x2e218800
def is_FRINTX_asimdmisc_R(d): return (d & 0xbfbffc00) == 0x2e219800
def is_FCVTNU_asimdmisc_R(d): return (d & 0xbfbffc00) == 0x2e21a800
def is_FCVTMU_asimdmisc_R(d): return (d & 0xbfbffc00) == 0x2e21b800
def is_FCVTAU_asimdmisc_R(d): return (d & 0xbfbffc00) == 0x2e21c800
def is_UCVTF_asimdmisc_R(d): return (d & 0xbfbffc00) == 0x2e21d800
def is_NOT_asimdmisc_R(d): return (d & 0xbffffc00) == 0x2e205800
def is_RBIT_asimdmisc_R(d): return (d & 0xbffffc00) == 0x2e605800
def is_FCMGE_asimdmisc_FZ(d): return (d & 0xbfbffc00) == 0x2ea0c800
def is_FCMLE_asimdmisc_FZ(d): return (d & 0xbfbffc00) == 0x2ea0d800
def is_FNEG_asimdmisc_R(d): return (d & 0xbfbffc00) == 0x2ea0f800
def is_FRINTI_asimdmisc_R(d): return (d & 0xbfbffc00) == 0x2ea19800
def is_FCVTPU_asimdmisc_R(d): return (d & 0xbfbffc00) == 0x2ea1a800
def is_FCVTZU_asimdmisc_R(d): return (d & 0xbfbffc00) == 0x2ea1b800
def is_URSQRTE_asimdmisc_R(d): return (d & 0xbfbffc00) == 0x2ea1c800
def is_FRSQRTE_asimdmisc_R(d): return (d & 0xbfbffc00) == 0x2ea1d800
def is_FSQRT_asimdmisc_R(d): return (d & 0xbfbffc00) == 0x2ea1f800
def is_FRINTN_asimdmiscfp16_R(d): return (d & 0xbffffc00) == 0x0e798800
def is_FRINTM_asimdmiscfp16_R(d): return (d & 0xbffffc00) == 0x0e799800
def is_FCVTNS_asimdmiscfp16_R(d): return (d & 0xbffffc00) == 0x0e79a800
def is_FCVTMS_asimdmiscfp16_R(d): return (d & 0xbffffc00) == 0x0e79b800
def is_FCVTAS_asimdmiscfp16_R(d): return (d & 0xbffffc00) == 0x0e79c800
def is_SCVTF_asimdmiscfp16_R(d): return (d & 0xbffffc00) == 0x0e79d800
def is_FCMGT_asimdmiscfp16_FZ(d): return (d & 0xbffffc00) == 0x0ef8c800
def is_FCMEQ_asimdmiscfp16_FZ(d): return (d & 0xbffffc00) == 0x0ef8d800
def is_FCMLT_asimdmiscfp16_FZ(d): return (d & 0xbffffc00) == 0x0ef8e800
def is_FABS_asimdmiscfp16_R(d): return (d & 0xbffffc00) == 0x0ef8f800
def is_FRINTP_asimdmiscfp16_R(d): return (d & 0xbffffc00) == 0x0ef98800
def is_FRINTZ_asimdmiscfp16_R(d): return (d & 0xbffffc00) == 0x0ef99800
def is_FCVTPS_asimdmiscfp16_R(d): return (d & 0xbffffc00) == 0x0ef9a800
def is_FCVTZS_asimdmiscfp16_R(d): return (d & 0xbffffc00) == 0x0ef9b800
def is_FRECPE_asimdmiscfp16_R(d): return (d & 0xbffffc00) == 0x0ef9d800
def is_FRINTA_asimdmiscfp16_R(d): return (d & 0xbffffc00) == 0x2e798800
def is_FRINTX_asimdmiscfp16_R(d): return (d & 0xbffffc00) == 0x2e799800
def is_FCVTNU_asimdmiscfp16_R(d): return (d & 0xbffffc00) == 0x2e79a800
def is_FCVTMU_asimdmiscfp16_R(d): return (d & 0xbffffc00) == 0x2e79b800
def is_FCVTAU_asimdmiscfp16_R(d): return (d & 0xbffffc00) == 0x2e79c800
def is_UCVTF_asimdmiscfp16_R(d): return (d & 0xbffffc00) == 0x2e79d800
def is_FCMGE_asimdmiscfp16_FZ(d): return (d & 0xbffffc00) == 0x2ef8c800
def is_FCMLE_asimdmiscfp16_FZ(d): return (d & 0xbffffc00) == 0x2ef8d800
def is_FNEG_asimdmiscfp16_R(d): return (d & 0xbffffc00) == 0x2ef8f800
def is_FRINTI_asimdmiscfp16_R(d): return (d & 0xbffffc00) == 0x2ef99800
def is_FCVTPU_asimdmiscfp16_R(d): return (d & 0xbffffc00) == 0x2ef9a800
def is_FCVTZU_asimdmiscfp16_R(d): return (d & 0xbffffc00) == 0x2ef9b800
def is_FRSQRTE_asimdmiscfp16_R(d): return (d & 0xbffffc00) == 0x2ef9d800
def is_FSQRT_asimdmiscfp16_R(d): return (d & 0xbffffc00) == 0x2ef9f800
def is_SMLAL_asimdelem_L(d): return (d & 0xbf00f400) == 0x0f002000
def is_SQDMLAL_asimdelem_L(d): return (d & 0xbf00f400) == 0x0f003000
def is_SMLSL_asimdelem_L(d): return (d & 0xbf00f400) == 0x0f006000
def is_SQDMLSL_asimdelem_L(d): return (d & 0xbf00f400) == 0x0f007000
def is_MUL_asimdelem_R(d): return (d & 0xbf00f400) == 0x0f008000
def is_SMULL_asimdelem_L(d): return (d & 0xbf00f400) == 0x0f00a000
def is_SQDMULL_asimdelem_L(d): return (d & 0xbf00f400) == 0x0f00b000
def is_SQDMULH_asimdelem_R(d): return (d & 0xbf00f400) == 0x0f00c000
def is_SQRDMULH_asimdelem_R(d): return (d & 0xbf00f400) == 0x0f00d000
def is_SDOT_asimdelem_D(d): return (d & 0xbf00f400) == 0x0f00e000
def is_FMLA_asimdelem_RH_H(d): return (d & 0xbfc0f400) == 0x0f001000
def is_FMLS_asimdelem_RH_H(d): return (d & 0xbfc0f400) == 0x0f005000
def is_FMUL_asimdelem_RH_H(d): return (d & 0xbfc0f400) == 0x0f009000
def is_FMLA_asimdelem_R_SD(d): return (d & 0xbf80f400) == 0x0f801000
def is_FMLS_asimdelem_R_SD(d): return (d & 0xbf80f400) == 0x0f805000
def is_FMUL_asimdelem_R_SD(d): return (d & 0xbf80f400) == 0x0f809000
def is_MLA_asimdelem_R(d): return (d & 0xbf00f400) == 0x2f000000
def is_UMLAL_asimdelem_L(d): return (d & 0xbf00f400) == 0x2f002000
def is_MLS_asimdelem_R(d): return (d & 0xbf00f400) == 0x2f004000
def is_UMLSL_asimdelem_L(d): return (d & 0xbf00f400) == 0x2f006000
def is_UMULL_asimdelem_L(d): return (d & 0xbf00f400) == 0x2f00a000
def is_SQRDMLAH_asimdelem_R(d): return (d & 0xbf00f400) == 0x2f00d000
def is_UDOT_asimdelem_D(d): return (d & 0xbf00f400) == 0x2f00e000
def is_SQRDMLSH_asimdelem_R(d): return (d & 0xbf00f400) == 0x2f00f000
def is_FMULX_asimdelem_RH_H(d): return (d & 0xbfc0f400) == 0x2f009000
def is_FCMLA_asimdelem_C_H(d): return (d & 0xbfc09400) == 0x2f401000
def is_FMULX_asimdelem_R_SD(d): return (d & 0xbf80f400) == 0x2f809000
def is_FCMLA_asimdelem_C_S(d): return (d & 0xbfc09400) == 0x2f801000
def is_SCVTF_S32_float2fix(d): return (d & 0xffff0000) == 0x1e020000
def is_UCVTF_S32_float2fix(d): return (d & 0xffff0000) == 0x1e030000
def is_FCVTZS_32S_float2fix(d): return (d & 0xffff0000) == 0x1e180000
def is_FCVTZU_32S_float2fix(d): return (d & 0xffff0000) == 0x1e190000
def is_SCVTF_D32_float2fix(d): return (d & 0xffff0000) == 0x1e420000
def is_UCVTF_D32_float2fix(d): return (d & 0xffff0000) == 0x1e430000
def is_FCVTZS_32D_float2fix(d): return (d & 0xffff0000) == 0x1e580000
def is_FCVTZU_32D_float2fix(d): return (d & 0xffff0000) == 0x1e590000
def is_SCVTF_H32_float2fix(d): return (d & 0xffff0000) == 0x1ec20000
def is_UCVTF_H32_float2fix(d): return (d & 0xffff0000) == 0x1ec30000
def is_FCVTZS_32H_float2fix(d): return (d & 0xffff0000) == 0x1ed80000
def is_FCVTZU_32H_float2fix(d): return (d & 0xffff0000) == 0x1ed90000
def is_SCVTF_S64_float2fix(d): return (d & 0xffff0000) == 0x9e020000
def is_UCVTF_S64_float2fix(d): return (d & 0xffff0000) == 0x9e030000
def is_FCVTZS_64S_float2fix(d): return (d & 0xffff0000) == 0x9e180000
def is_FCVTZU_64S_float2fix(d): return (d & 0xffff0000) == 0x9e190000
def is_SCVTF_D64_float2fix(d): return (d & 0xffff0000) == 0x9e420000
def is_UCVTF_D64_float2fix(d): return (d & 0xffff0000) == 0x9e430000
def is_FCVTZS_64D_float2fix(d): return (d & 0xffff0000) == 0x9e580000
def is_FCVTZU_64D_float2fix(d): return (d & 0xffff0000) == 0x9e590000
def is_SCVTF_H64_float2fix(d): return (d & 0xffff0000) == 0x9ec20000
def is_UCVTF_H64_float2fix(d): return (d & 0xffff0000) == 0x9ec30000
def is_FCVTZS_64H_float2fix(d): return (d & 0xffff0000) == 0x9ed80000
def is_FCVTZU_64H_float2fix(d): return (d & 0xffff0000) == 0x9ed90000
def is_FCVTNS_32S_float2int(d): return (d & 0xfffffc00) == 0x1e200000
def is_FCVTNU_32S_float2int(d): return (d & 0xfffffc00) == 0x1e210000
def is_SCVTF_S32_float2int(d): return (d & 0xfffffc00) == 0x1e220000
def is_UCVTF_S32_float2int(d): return (d & 0xfffffc00) == 0x1e230000
def is_FCVTAS_32S_float2int(d): return (d & 0xfffffc00) == 0x1e240000
def is_FCVTAU_32S_float2int(d): return (d & 0xfffffc00) == 0x1e250000
def is_FMOV_32S_float2int(d): return (d & 0xfffffc00) == 0x1e260000
def is_FMOV_S32_float2int(d): return (d & 0xfffffc00) == 0x1e270000
def is_FCVTPS_32S_float2int(d): return (d & 0xfffffc00) == 0x1e280000
def is_FCVTPU_32S_float2int(d): return (d & 0xfffffc00) == 0x1e290000
def is_FCVTMS_32S_float2int(d): return (d & 0xfffffc00) == 0x1e300000
def is_FCVTMU_32S_float2int(d): return (d & 0xfffffc00) == 0x1e310000
def is_FCVTZS_32S_float2int(d): return (d & 0xfffffc00) == 0x1e380000
def is_FCVTZU_32S_float2int(d): return (d & 0xfffffc00) == 0x1e390000
def is_FCVTNS_32D_float2int(d): return (d & 0xfffffc00) == 0x1e600000
def is_FCVTNU_32D_float2int(d): return (d & 0xfffffc00) == 0x1e610000
def is_SCVTF_D32_float2int(d): return (d & 0xfffffc00) == 0x1e620000
def is_UCVTF_D32_float2int(d): return (d & 0xfffffc00) == 0x1e630000
def is_FCVTAS_32D_float2int(d): return (d & 0xfffffc00) == 0x1e640000
def is_FCVTAU_32D_float2int(d): return (d & 0xfffffc00) == 0x1e650000
def is_FCVTPS_32D_float2int(d): return (d & 0xfffffc00) == 0x1e680000
def is_FCVTPU_32D_float2int(d): return (d & 0xfffffc00) == 0x1e690000
def is_FCVTMS_32D_float2int(d): return (d & 0xfffffc00) == 0x1e700000
def is_FCVTMU_32D_float2int(d): return (d & 0xfffffc00) == 0x1e710000
def is_FCVTZS_32D_float2int(d): return (d & 0xfffffc00) == 0x1e780000
def is_FCVTZU_32D_float2int(d): return (d & 0xfffffc00) == 0x1e790000
def is_FJCVTZS_32D_float2int(d): return (d & 0xfffffc00) == 0x1e7e0000
def is_FCVTNS_32H_float2int(d): return (d & 0xfffffc00) == 0x1ee00000
def is_FCVTNU_32H_float2int(d): return (d & 0xfffffc00) == 0x1ee10000
def is_SCVTF_H32_float2int(d): return (d & 0xfffffc00) == 0x1ee20000
def is_UCVTF_H32_float2int(d): return (d & 0xfffffc00) == 0x1ee30000
def is_FCVTAS_32H_float2int(d): return (d & 0xfffffc00) == 0x1ee40000
def is_FCVTAU_32H_float2int(d): return (d & 0xfffffc00) == 0x1ee50000
def is_FMOV_32H_float2int(d): return (d & 0xfffffc00) == 0x1ee60000
def is_FMOV_H32_float2int(d): return (d & 0xfffffc00) == 0x1ee70000
def is_FCVTPS_32H_float2int(d): return (d & 0xfffffc00) == 0x1ee80000
def is_FCVTPU_32H_float2int(d): return (d & 0xfffffc00) == 0x1ee90000
def is_FCVTMS_32H_float2int(d): return (d & 0xfffffc00) == 0x1ef00000
def is_FCVTMU_32H_float2int(d): return (d & 0xfffffc00) == 0x1ef10000
def is_FCVTZS_32H_float2int(d): return (d & 0xfffffc00) == 0x1ef80000
def is_FCVTZU_32H_float2int(d): return (d & 0xfffffc00) == 0x1ef90000
def is_FCVTNS_64S_float2int(d): return (d & 0xfffffc00) == 0x9e200000
def is_FCVTNU_64S_float2int(d): return (d & 0xfffffc00) == 0x9e210000
def is_SCVTF_S64_float2int(d): return (d & 0xfffffc00) == 0x9e220000
def is_UCVTF_S64_float2int(d): return (d & 0xfffffc00) == 0x9e230000
def is_FCVTAS_64S_float2int(d): return (d & 0xfffffc00) == 0x9e240000
def is_FCVTAU_64S_float2int(d): return (d & 0xfffffc00) == 0x9e250000
def is_FCVTPS_64S_float2int(d): return (d & 0xfffffc00) == 0x9e280000
def is_FCVTPU_64S_float2int(d): return (d & 0xfffffc00) == 0x9e290000
def is_FCVTMS_64S_float2int(d): return (d & 0xfffffc00) == 0x9e300000
def is_FCVTMU_64S_float2int(d): return (d & 0xfffffc00) == 0x9e310000
def is_FCVTZS_64S_float2int(d): return (d & 0xfffffc00) == 0x9e380000
def is_FCVTZU_64S_float2int(d): return (d & 0xfffffc00) == 0x9e390000
def is_FCVTNS_64D_float2int(d): return (d & 0xfffffc00) == 0x9e600000
def is_FCVTNU_64D_float2int(d): return (d & 0xfffffc00) == 0x9e610000
def is_SCVTF_D64_float2int(d): return (d & 0xfffffc00) == 0x9e620000
def is_UCVTF_D64_float2int(d): return (d & 0xfffffc00) == 0x9e630000
def is_FCVTAS_64D_float2int(d): return (d & 0xfffffc00) == 0x9e640000
def is_FCVTAU_64D_float2int(d): return (d & 0xfffffc00) == 0x9e650000
def is_FMOV_64D_float2int(d): return (d & 0xfffffc00) == 0x9e660000
def is_FMOV_D64_float2int(d): return (d & 0xfffffc00) == 0x9e670000
def is_FCVTPS_64D_float2int(d): return (d & 0xfffffc00) == 0x9e680000
def is_FCVTPU_64D_float2int(d): return (d & 0xfffffc00) == 0x9e690000
def is_FCVTMS_64D_float2int(d): return (d & 0xfffffc00) == 0x9e700000
def is_FCVTMU_64D_float2int(d): return (d & 0xfffffc00) == 0x9e710000
def is_FCVTZS_64D_float2int(d): return (d & 0xfffffc00) == 0x9e780000
def is_FCVTZU_64D_float2int(d): return (d & 0xfffffc00) == 0x9e790000
def is_FMOV_64VX_float2int(d): return (d & 0xfffffc00) == 0x9eae0000
def is_FMOV_V64I_float2int(d): return (d & 0xfffffc00) == 0x9eaf0000
def is_FCVTNS_64H_float2int(d): return (d & 0xfffffc00) == 0x9ee00000
def is_FCVTNU_64H_float2int(d): return (d & 0xfffffc00) == 0x9ee10000
def is_SCVTF_H64_float2int(d): return (d & 0xfffffc00) == 0x9ee20000
def is_UCVTF_H64_float2int(d): return (d & 0xfffffc00) == 0x9ee30000
def is_FCVTAS_64H_float2int(d): return (d & 0xfffffc00) == 0x9ee40000
def is_FCVTAU_64H_float2int(d): return (d & 0xfffffc00) == 0x9ee50000
def is_FMOV_64H_float2int(d): return (d & 0xfffffc00) == 0x9ee60000
def is_FMOV_H64_float2int(d): return (d & 0xfffffc00) == 0x9ee70000
def is_FCVTPS_64H_float2int(d): return (d & 0xfffffc00) == 0x9ee80000
def is_FCVTPU_64H_float2int(d): return (d & 0xfffffc00) == 0x9ee90000
def is_FCVTMS_64H_float2int(d): return (d & 0xfffffc00) == 0x9ef00000
def is_FCVTMU_64H_float2int(d): return (d & 0xfffffc00) == 0x9ef10000
def is_FCVTZS_64H_float2int(d): return (d & 0xfffffc00) == 0x9ef80000
def is_FCVTZU_64H_float2int(d): return (d & 0xfffffc00) == 0x9ef90000
def is_AESE_B_cryptoaes(d): return (d & 0xfffffc00) == 0x4e284800
def is_AESD_B_cryptoaes(d): return (d & 0xfffffc00) == 0x4e285800
def is_AESMC_B_cryptoaes(d): return (d & 0xfffffc00) == 0x4e286800
def is_AESIMC_B_cryptoaes(d): return (d & 0xfffffc00) == 0x4e287800
def is_EOR3_VVV16_crypto4(d): return (d & 0xffe08000) == 0xce000000
def is_BCAX_VVV16_crypto4(d): return (d & 0xffe08000) == 0xce200000
def is_SM3SS1_VVV4_crypto4(d): return (d & 0xffe08000) == 0xce400000
def is_SHA1C_QSV_cryptosha3(d): return (d & 0xffe0fc00) == 0x5e000000
def is_SHA1P_QSV_cryptosha3(d): return (d & 0xffe0fc00) == 0x5e001000
def is_SHA1M_QSV_cryptosha3(d): return (d & 0xffe0fc00) == 0x5e002000
def is_SHA1SU0_VVV_cryptosha3(d): return (d & 0xffe0fc00) == 0x5e003000
def is_SHA256H_QQV_cryptosha3(d): return (d & 0xffe0fc00) == 0x5e004000
def is_SHA256H2_QQV_cryptosha3(d): return (d & 0xffe0fc00) == 0x5e005000
def is_SHA256SU1_VVV_cryptosha3(d): return (d & 0xffe0fc00) == 0x5e006000
def is_SHA512H_QQV_cryptosha512_3(d): return (d & 0xffe0fc00) == 0xce608000
def is_SHA512H2_QQV_cryptosha512_3(d): return (d & 0xffe0fc00) == 0xce608400
def is_SHA512SU1_VVV2_cryptosha512_3(d): return (d & 0xffe0fc00) == 0xce608800
def is_RAX1_VVV2_cryptosha512_3(d): return (d & 0xffe0fc00) == 0xce608c00
def is_SM3PARTW1_VVV4_cryptosha512_3(d): return (d & 0xffe0fc00) == 0xce60c000
def is_SM3PARTW2_VVV4_cryptosha512_3(d): return (d & 0xffe0fc00) == 0xce60c400
def is_SM4EKEY_VVV4_cryptosha512_3(d): return (d & 0xffe0fc00) == 0xce60c800
def is_SM3TT1A_VVV4_crypto3_imm2(d): return (d & 0xffe0cc00) == 0xce408000
def is_SM3TT1B_VVV4_crypto3_imm2(d): return (d & 0xffe0cc00) == 0xce408400
def is_SM3TT2A_VVV4_crypto3_imm2(d): return (d & 0xffe0cc00) == 0xce408800
def is_SM3TT2B_VVV_crypto3_imm2(d): return (d & 0xffe0cc00) == 0xce408c00
def is_XAR_VVV2_crypto3_imm6(d): return (d & 0xffe00000) == 0xce800000
def is_SHA1H_SS_cryptosha2(d): return (d & 0xfffffc00) == 0x5e280800
def is_SHA1SU1_VV_cryptosha2(d): return (d & 0xfffffc00) == 0x5e281800
def is_SHA256SU0_VV_cryptosha2(d): return (d & 0xfffffc00) == 0x5e282800
def is_SHA512SU0_VV2_cryptosha512_2(d): return (d & 0xfffffc00) == 0xcec08000
def is_SM4E_VV4_cryptosha512_2(d): return (d & 0xfffffc00) == 0xcec08400
def is_FCMP_S_floatcmp(d): return (d & 0xffe0fc1f) == 0x1e202000
def is_FCMP_SZ_floatcmp(d): return (d & 0xffe0fc1f) == 0x1e202008
def is_FCMPE_S_floatcmp(d): return (d & 0xffe0fc1f) == 0x1e202010
def is_FCMPE_SZ_floatcmp(d): return (d & 0xffe0fc1f) == 0x1e202018
def is_FCMP_D_floatcmp(d): return (d & 0xffe0fc1f) == 0x1e602000
def is_FCMP_DZ_floatcmp(d): return (d & 0xffe0fc1f) == 0x1e602008
def is_FCMPE_D_floatcmp(d): return (d & 0xffe0fc1f) == 0x1e602010
def is_FCMPE_DZ_floatcmp(d): return (d & 0xffe0fc1f) == 0x1e602018
def is_FCMP_H_floatcmp(d): return (d & 0xffe0fc1f) == 0x1ee02000
def is_FCMP_HZ_floatcmp(d): return (d & 0xffe0fc1f) == 0x1ee02008
def is_FCMPE_H_floatcmp(d): return (d & 0xffe0fc1f) == 0x1ee02010
def is_FCMPE_HZ_floatcmp(d): return (d & 0xffe0fc1f) == 0x1ee02018
def is_FCCMP_S_floatccmp(d): return (d & 0xffe00c10) == 0x1e200400
def is_FCCMPE_S_floatccmp(d): return (d & 0xffe00c10) == 0x1e200410
def is_FCCMP_D_floatccmp(d): return (d & 0xffe00c10) == 0x1e600400
def is_FCCMPE_D_floatccmp(d): return (d & 0xffe00c10) == 0x1e600410
def is_FCCMP_H_floatccmp(d): return (d & 0xffe00c10) == 0x1ee00400
def is_FCCMPE_H_floatccmp(d): return (d & 0xffe00c10) == 0x1ee00410
def is_FCSEL_S_floatsel(d): return (d & 0xffe00c00) == 0x1e200c00
def is_FCSEL_D_floatsel(d): return (d & 0xffe00c00) == 0x1e600c00
def is_FCSEL_H_floatsel(d): return (d & 0xffe00c00) == 0x1ee00c00
def is_FMOV_S_floatdp1(d): return (d & 0xfffffc00) == 0x1e204000
def is_FABS_S_floatdp1(d): return (d & 0xfffffc00) == 0x1e20c000
def is_FNEG_S_floatdp1(d): return (d & 0xfffffc00) == 0x1e214000
def is_FSQRT_S_floatdp1(d): return (d & 0xfffffc00) == 0x1e21c000
def is_FCVT_DS_floatdp1(d): return (d & 0xfffffc00) == 0x1e22c000
def is_FCVT_HS_floatdp1(d): return (d & 0xfffffc00) == 0x1e23c000
def is_FRINTN_S_floatdp1(d): return (d & 0xfffffc00) == 0x1e244000
def is_FRINTP_S_floatdp1(d): return (d & 0xfffffc00) == 0x1e24c000
def is_FRINTM_S_floatdp1(d): return (d & 0xfffffc00) == 0x1e254000
def is_FRINTZ_S_floatdp1(d): return (d & 0xfffffc00) == 0x1e25c000
def is_FRINTA_S_floatdp1(d): return (d & 0xfffffc00) == 0x1e264000
def is_FRINTX_S_floatdp1(d): return (d & 0xfffffc00) == 0x1e274000
def is_FRINTI_S_floatdp1(d): return (d & 0xfffffc00) == 0x1e27c000
def is_FMOV_D_floatdp1(d): return (d & 0xfffffc00) == 0x1e604000
def is_FABS_D_floatdp1(d): return (d & 0xfffffc00) == 0x1e60c000
def is_FNEG_D_floatdp1(d): return (d & 0xfffffc00) == 0x1e614000
def is_FSQRT_D_floatdp1(d): return (d & 0xfffffc00) == 0x1e61c000
def is_FCVT_SD_floatdp1(d): return (d & 0xfffffc00) == 0x1e624000
def is_FCVT_HD_floatdp1(d): return (d & 0xfffffc00) == 0x1e63c000
def is_FRINTN_D_floatdp1(d): return (d & 0xfffffc00) == 0x1e644000
def is_FRINTP_D_floatdp1(d): return (d & 0xfffffc00) == 0x1e64c000
def is_FRINTM_D_floatdp1(d): return (d & 0xfffffc00) == 0x1e654000
def is_FRINTZ_D_floatdp1(d): return (d & 0xfffffc00) == 0x1e65c000
def is_FRINTA_D_floatdp1(d): return (d & 0xfffffc00) == 0x1e664000
def is_FRINTX_D_floatdp1(d): return (d & 0xfffffc00) == 0x1e674000
def is_FRINTI_D_floatdp1(d): return (d & 0xfffffc00) == 0x1e67c000
def is_FMOV_H_floatdp1(d): return (d & 0xfffffc00) == 0x1ee04000
def is_FABS_H_floatdp1(d): return (d & 0xfffffc00) == 0x1ee0c000
def is_FNEG_H_floatdp1(d): return (d & 0xfffffc00) == 0x1ee14000
def is_FSQRT_H_floatdp1(d): return (d & 0xfffffc00) == 0x1ee1c000
def is_FCVT_SH_floatdp1(d): return (d & 0xfffffc00) == 0x1ee24000
def is_FCVT_DH_floatdp1(d): return (d & 0xfffffc00) == 0x1ee2c000
def is_FRINTN_H_floatdp1(d): return (d & 0xfffffc00) == 0x1ee44000
def is_FRINTP_H_floatdp1(d): return (d & 0xfffffc00) == 0x1ee4c000
def is_FRINTM_H_floatdp1(d): return (d & 0xfffffc00) == 0x1ee54000
def is_FRINTZ_H_floatdp1(d): return (d & 0xfffffc00) == 0x1ee5c000
def is_FRINTA_H_floatdp1(d): return (d & 0xfffffc00) == 0x1ee64000
def is_FRINTX_H_floatdp1(d): return (d & 0xfffffc00) == 0x1ee74000
def is_FRINTI_H_floatdp1(d): return (d & 0xfffffc00) == 0x1ee7c000
def is_FMUL_S_floatdp2(d): return (d & 0xffe0fc00) == 0x1e200800
def is_FDIV_S_floatdp2(d): return (d & 0xffe0fc00) == 0x1e201800
def is_FADD_S_floatdp2(d): return (d & 0xffe0fc00) == 0x1e202800
def is_FSUB_S_floatdp2(d): return (d & 0xffe0fc00) == 0x1e203800
def is_FMAX_S_floatdp2(d): return (d & 0xffe0fc00) == 0x1e204800
def is_FMIN_S_floatdp2(d): return (d & 0xffe0fc00) == 0x1e205800
def is_FMAXNM_S_floatdp2(d): return (d & 0xffe0fc00) == 0x1e206800
def is_FMINNM_S_floatdp2(d): return (d & 0xffe0fc00) == 0x1e207800
def is_FNMUL_S_floatdp2(d): return (d & 0xffe0fc00) == 0x1e208800
def is_FMUL_D_floatdp2(d): return (d & 0xffe0fc00) == 0x1e600800
def is_FDIV_D_floatdp2(d): return (d & 0xffe0fc00) == 0x1e601800
def is_FADD_D_floatdp2(d): return (d & 0xffe0fc00) == 0x1e602800
def is_FSUB_D_floatdp2(d): return (d & 0xffe0fc00) == 0x1e603800
def is_FMAX_D_floatdp2(d): return (d & 0xffe0fc00) == 0x1e604800
def is_FMIN_D_floatdp2(d): return (d & 0xffe0fc00) == 0x1e605800
def is_FMAXNM_D_floatdp2(d): return (d & 0xffe0fc00) == 0x1e606800
def is_FMINNM_D_floatdp2(d): return (d & 0xffe0fc00) == 0x1e607800
def is_FNMUL_D_floatdp2(d): return (d & 0xffe0fc00) == 0x1e608800
def is_FMUL_H_floatdp2(d): return (d & 0xffe0fc00) == 0x1ee00800
def is_FDIV_H_floatdp2(d): return (d & 0xffe0fc00) == 0x1ee01800
def is_FADD_H_floatdp2(d): return (d & 0xffe0fc00) == 0x1ee02800
def is_FSUB_H_floatdp2(d): return (d & 0xffe0fc00) == 0x1ee03800
def is_FMAX_H_floatdp2(d): return (d & 0xffe0fc00) == 0x1ee04800
def is_FMIN_H_floatdp2(d): return (d & 0xffe0fc00) == 0x1ee05800
def is_FMAXNM_H_floatdp2(d): return (d & 0xffe0fc00) == 0x1ee06800
def is_FMINNM_H_floatdp2(d): return (d & 0xffe0fc00) == 0x1ee07800
def is_FNMUL_H_floatdp2(d): return (d & 0xffe0fc00) == 0x1ee08800
def is_FMADD_S_floatdp3(d): return (d & 0xffe08000) == 0x1f000000
def is_FMSUB_S_floatdp3(d): return (d & 0xffe08000) == 0x1f008000
def is_FNMADD_S_floatdp3(d): return (d & 0xffe08000) == 0x1f200000
def is_FNMSUB_S_floatdp3(d): return (d & 0xffe08000) == 0x1f208000
def is_FMADD_D_floatdp3(d): return (d & 0xffe08000) == 0x1f400000
def is_FMSUB_D_floatdp3(d): return (d & 0xffe08000) == 0x1f408000
def is_FNMADD_D_floatdp3(d): return (d & 0xffe08000) == 0x1f600000
def is_FNMSUB_D_floatdp3(d): return (d & 0xffe08000) == 0x1f608000
def is_FMADD_H_floatdp3(d): return (d & 0xffe08000) == 0x1fc00000
def is_FMSUB_H_floatdp3(d): return (d & 0xffe08000) == 0x1fc08000
def is_FNMADD_H_floatdp3(d): return (d & 0xffe08000) == 0x1fe00000
def is_FNMSUB_H_floatdp3(d): return (d & 0xffe08000) == 0x1fe08000
def is_FMOV_S_floatimm(d): return (d & 0xffe01fe0) == 0x1e201000
def is_FMOV_D_floatimm(d): return (d & 0xffe01fe0) == 0x1e601000
def is_FMOV_H_floatimm(d): return (d & 0xffe01fe0) == 0x1ee01000

def get_A(d): return (d >> 23) & 1
def get_CRm(d): return (d >> 8) & 0xF
def get_CRn(d): return (d >> 12) & 0xF
def get_H(d): return (d >> 11) & 1
# def get_L(d): return (d >> 21) & 1	# system, asisdelem, asimdelem
# def get_L(d): return (d >> 22) & 1	# asisdlse, asisdlsep, asisdlso, asisdlsop, ldstexcl, ldstnapair_offs, ldstpair_off, ldstpair_post, ldstpair_pre
def get_LL(d): return (d >> 0) & 3
# def get_M(d): return (d >> 20) & 1	# asisdelem, asimdelem
# def get_M(d): return (d >> 23) & 1	# ldst_pac
# def get_M(d): return (d >> 31) & 1	# floatcmp, floatccmp, floatsel, floatdp1, floatdp2, floatdp3, floatimm
# def get_N(d): return (d >> 21) & 1	# log_shift
# def get_N(d): return (d >> 22) & 1	# bitfield, extract, log_imm
def get_O(d): return (d >> 14) & 1
def get_Op0(d): return (d >> 21) & 3
def get_Q(d): return (d >> 30) & 1
# def get_R(d): return (d >> 21) & 1	# asisdlso, asisdlsop
# def get_R(d): return (d >> 22) & 1	# memop
def get_Ra(d): return (d >> 10) & 0x1F
def get_Rd(d): return (d >> 0) & 0x1F
# def get_Rm(d): return (d >> 16) & 0x1F	# asisdlsep, asisdlsop, ldst_regoff, extract, addsub_ext, addsub_shift, addsub_carry, condcmp_reg, condsel, dp_2src, dp_3src, log_shift, asimdext, asimdperm, asisddiff, asisdsame, asisdsamefp16, asisdsame2, asimdtbl, asimddiff, asimdsame, asimdsamefp16, asimdsame2, crypto4, cryptosha3, cryptosha512_3, crypto3_imm2, crypto3_imm6, floatcmp, floatccmp, floatsel, floatdp2, floatdp3
# def get_Rm(d): return (d >> 16) & 0xF	# asisdelem, asimdelem
def get_Rn(d): return (d >> 5) & 0x1F
def get_Rs(d): return (d >> 16) & 0x1F
def get_Rt(d): return (d >> 0) & 0x1F
def get_Rt2(d): return (d >> 10) & 0x1F
# def get_S(d): return (d >> 12) & 1	# asisdlso, asisdlsop, ldst_regoff
# def get_S(d): return (d >> 22) & 1	# ldst_pac
# def get_S(d): return (d >> 29) & 1	# addsub_imm, addsub_ext, addsub_shift, addsub_carry, condcmp_imm, condcmp_reg, condsel, dp_1src, dp_2src, float2fix, float2int, floatcmp, floatccmp, floatsel, floatdp1, floatdp2, floatdp3, floatimm
def get_U(d): return (d >> 29) & 1
def get_V(d): return (d >> 26) & 1
def get_W(d): return (d >> 11) & 1
# def get_a(d): return (d >> 18) & 1	# asimdimm
# def get_a(d): return (d >> 23) & 1	# asisdsamefp16, asisdmiscfp16, asimdsamefp16, asimdmiscfp16
def get_b(d): return (d >> 17) & 1
def get_b40(d): return (d >> 19) & 0x1F
def get_b5(d): return (d >> 31) & 1
def get_c(d): return (d >> 16) & 1
def get_cmode(d): return (d >> 12) & 0xF
# def get_cond(d): return (d >> 0) & 0xF	# condbranch
# def get_cond(d): return (d >> 12) & 0xF	# condcmp_imm, condcmp_reg, condsel, floatccmp, floatsel
def get_d(d): return (d >> 9) & 1
def get_e(d): return (d >> 8) & 1
def get_f(d): return (d >> 7) & 1
def get_g(d): return (d >> 6) & 1
def get_h(d): return (d >> 5) & 1
def get_hw(d): return (d >> 21) & 3
def get_imm12(d): return (d >> 10) & 0xFFF
def get_imm14(d): return (d >> 5) & 0x3FFF
def get_imm16(d): return (d >> 5) & 0xFFFF
def get_imm19(d): return (d >> 5) & 0x7FFFF
def get_imm2(d): return (d >> 12) & 3
def get_imm26(d): return (d >> 0) & 0x3FFFFFF
def get_imm3(d): return (d >> 10) & 7
def get_imm4(d): return (d >> 11) & 0xF
# def get_imm5(d): return (d >> 16) & 0x1F	# condcmp_imm, asimdins, asisdone
# def get_imm5(d): return (d >> 5) & 0x1F	# floatimm
def get_imm6(d): return (d >> 10) & 0x3F
def get_imm7(d): return (d >> 15) & 0x7F
def get_imm8(d): return (d >> 13) & 0xFF
def get_imm9(d): return (d >> 12) & 0x1FF
def get_immb(d): return (d >> 16) & 7
def get_immh(d): return (d >> 19) & 0xF
def get_immhi(d): return (d >> 5) & 0x7FFFF
def get_immlo(d): return (d >> 29) & 3
def get_immr(d): return (d >> 16) & 0x3F
def get_imms(d): return (d >> 10) & 0x3F
def get_len(d): return (d >> 13) & 3
def get_nzcv(d): return (d >> 0) & 0xF
def get_rmode(d): return (d >> 19) & 3
def get_scale(d): return (d >> 10) & 0x3F
def get_sf(d): return (d >> 31) & 1
def get_shift(d): return (d >> 22) & 3
# def get_size(d): return (d >> 10) & 3	# asisdlse, asisdlsep, asisdlso, asisdlsop
# def get_size(d): return (d >> 22) & 3	# asimdall, asimdperm, asisdpair, asisddiff, asisdsame, asisdsame2, asisdmisc, asisdelem, asimddiff, asimdsame, asimdsame2, asimdmisc, asimdelem, cryptoaes, cryptosha3, cryptosha2
# def get_size(d): return (d >> 30) & 3	# memop, ldstexcl, ldst_immpost, ldst_immpre, ldst_pac, ldst_regoff, ldst_unpriv, ldst_unscaled, ldst_pos
def get_type(d): return (d >> 22) & 3


def get_A_s(d): return ((d >> 23) & 1) | (~1 if d & 0x800000 else 0)
def get_CRm_s(d): return ((d >> 8) & 0xF) | (~0xF if d & 0x800 else 0)
def get_CRn_s(d): return ((d >> 12) & 0xF) | (~0xF if d & 0x8000 else 0)
def get_H_s(d): return ((d >> 11) & 1) | (~1 if d & 0x800 else 0)
# def get_L_s(d): return ((d >> 21) & 1) | (~1 if d & 0x200000 else 0)
# def get_L_s(d): return ((d >> 22) & 1) | (~1 if d & 0x400000 else 0)
def get_LL_s(d): return ((d >> 0) & 3) | (~3 if d & 2 else 0)
# def get_M_s(d): return ((d >> 20) & 1) | (~1 if d & 0x100000 else 0)
# def get_M_s(d): return ((d >> 23) & 1) | (~1 if d & 0x800000 else 0)
# def get_M_s(d): return ((d >> 31) & 1) | (~1 if d & 0x80000000 else 0)
# def get_N_s(d): return ((d >> 21) & 1) | (~1 if d & 0x200000 else 0)
# def get_N_s(d): return ((d >> 22) & 1) | (~1 if d & 0x400000 else 0)
def get_O_s(d): return ((d >> 14) & 1) | (~1 if d & 0x4000 else 0)
def get_Op0_s(d): return ((d >> 21) & 3) | (~3 if d & 0x400000 else 0)
def get_Q_s(d): return ((d >> 30) & 1) | (~1 if d & 0x40000000 else 0)
# def get_R_s(d): return ((d >> 21) & 1) | (~1 if d & 0x200000 else 0)
# def get_R_s(d): return ((d >> 22) & 1) | (~1 if d & 0x400000 else 0)
def get_Ra_s(d): return ((d >> 10) & 0x1F) | (~0x1F if d & 0x4000 else 0)
def get_Rd_s(d): return ((d >> 0) & 0x1F) | (~0x1F if d & 0x10 else 0)
# def get_Rm_s(d): return ((d >> 16) & 0x1F) | (~0x1F if d & 0x100000 else 0)
# def get_Rm_s(d): return ((d >> 16) & 0xF) | (~0xF if d & 0x80000 else 0)
def get_Rn_s(d): return ((d >> 5) & 0x1F) | (~0x1F if d & 0x200 else 0)
def get_Rs_s(d): return ((d >> 16) & 0x1F) | (~0x1F if d & 0x100000 else 0)
def get_Rt_s(d): return ((d >> 0) & 0x1F) | (~0x1F if d & 0x10 else 0)
def get_Rt2_s(d): return ((d >> 10) & 0x1F) | (~0x1F if d & 0x4000 else 0)
# def get_S_s(d): return ((d >> 12) & 1) | (~1 if d & 0x1000 else 0)
# def get_S_s(d): return ((d >> 22) & 1) | (~1 if d & 0x400000 else 0)
# def get_S_s(d): return ((d >> 29) & 1) | (~1 if d & 0x20000000 else 0)
def get_U_s(d): return ((d >> 29) & 1) | (~1 if d & 0x20000000 else 0)
def get_V_s(d): return ((d >> 26) & 1) | (~1 if d & 0x4000000 else 0)
def get_W_s(d): return ((d >> 11) & 1) | (~1 if d & 0x800 else 0)
# def get_a_s(d): return ((d >> 18) & 1) | (~1 if d & 0x40000 else 0)
# def get_a_s(d): return ((d >> 23) & 1) | (~1 if d & 0x800000 else 0)
def get_b_s(d): return ((d >> 17) & 1) | (~1 if d & 0x20000 else 0)
def get_b40_s(d): return ((d >> 19) & 0x1F) | (~0x1F if d & 0x800000 else 0)
def get_b5_s(d): return ((d >> 31) & 1) | (~1 if d & 0x80000000 else 0)
def get_c_s(d): return ((d >> 16) & 1) | (~1 if d & 0x10000 else 0)
def get_cmode_s(d): return ((d >> 12) & 0xF) | (~0xF if d & 0x8000 else 0)
# def get_cond_s(d): return ((d >> 0) & 0xF) | (~0xF if d & 8 else 0)
# def get_cond_s(d): return ((d >> 12) & 0xF) | (~0xF if d & 0x8000 else 0)
def get_d_s(d): return ((d >> 9) & 1) | (~1 if d & 0x200 else 0)
def get_e_s(d): return ((d >> 8) & 1) | (~1 if d & 0x100 else 0)
def get_f_s(d): return ((d >> 7) & 1) | (~1 if d & 0x80 else 0)
def get_g_s(d): return ((d >> 6) & 1) | (~1 if d & 0x40 else 0)
def get_h_s(d): return ((d >> 5) & 1) | (~1 if d & 0x20 else 0)
def get_hw_s(d): return ((d >> 21) & 3) | (~3 if d & 0x400000 else 0)
def get_imm12_s(d): return ((d >> 10) & 0xFFF) | (~0xFFF if d & 0x200000 else 0)
def get_imm14_s(d): return ((d >> 5) & 0x3FFF) | (~0x3FFF if d & 0x40000 else 0)
def get_imm16_s(d): return ((d >> 5) & 0xFFFF) | (~0xFFFF if d & 0x100000 else 0)
def get_imm19_s(d): return ((d >> 5) & 0x7FFFF) | (~0x7FFFF if d & 0x800000 else 0)
def get_imm2_s(d): return ((d >> 12) & 3) | (~3 if d & 0x2000 else 0)
def get_imm26_s(d): return ((d >> 0) & 0x3FFFFFF) | (~0x3FFFFFF if d & 0x2000000 else 0)
def get_imm3_s(d): return ((d >> 10) & 7) | (~7 if d & 0x1000 else 0)
def get_imm4_s(d): return ((d >> 11) & 0xF) | (~0xF if d & 0x4000 else 0)
# def get_imm5_s(d): return ((d >> 16) & 0x1F) | (~0x1F if d & 0x100000 else 0)
# def get_imm5_s(d): return ((d >> 5) & 0x1F) | (~0x1F if d & 0x200 else 0)
def get_imm6_s(d): return ((d >> 10) & 0x3F) | (~0x3F if d & 0x8000 else 0)
def get_imm7_s(d): return ((d >> 15) & 0x7F) | (~0x7F if d & 0x200000 else 0)
def get_imm8_s(d): return ((d >> 13) & 0xFF) | (~0xFF if d & 0x100000 else 0)
def get_imm9_s(d): return ((d >> 12) & 0x1FF) | (~0x1FF if d & 0x100000 else 0)
def get_immb_s(d): return ((d >> 16) & 7) | (~7 if d & 0x40000 else 0)
def get_immh_s(d): return ((d >> 19) & 0xF) | (~0xF if d & 0x400000 else 0)
def get_immhi_s(d): return ((d >> 5) & 0x7FFFF) | (~0x7FFFF if d & 0x800000 else 0)
def get_immlo_s(d): return ((d >> 29) & 3) | (~3 if d & 0x40000000 else 0)
def get_immr_s(d): return ((d >> 16) & 0x3F) | (~0x3F if d & 0x200000 else 0)
def get_imms_s(d): return ((d >> 10) & 0x3F) | (~0x3F if d & 0x8000 else 0)
def get_len_s(d): return ((d >> 13) & 3) | (~3 if d & 0x4000 else 0)
def get_nzcv_s(d): return ((d >> 0) & 0xF) | (~0xF if d & 8 else 0)
def get_rmode_s(d): return ((d >> 19) & 3) | (~3 if d & 0x100000 else 0)
def get_scale_s(d): return ((d >> 10) & 0x3F) | (~0x3F if d & 0x8000 else 0)
def get_sf_s(d): return ((d >> 31) & 1) | (~1 if d & 0x80000000 else 0)
def get_shift_s(d): return ((d >> 22) & 3) | (~3 if d & 0x800000 else 0)
# def get_size_s(d): return ((d >> 10) & 3) | (~3 if d & 0x800 else 0)
# def get_size_s(d): return ((d >> 22) & 3) | (~3 if d & 0x800000 else 0)
# def get_size_s(d): return ((d >> 30) & 3) | (~3 if d & 0x80000000 else 0)
def get_type_s(d): return ((d >> 22) & 3) | (~3 if d & 0x800000 else 0)


def decode_UNDEFINED(d):
    raise Exception("undefined instruction")

def decode_root(d):
    assert (d & 0x00000000) == 0x00000000
    op0    = (d >> 25) & 0xF
    if (d & 0x0e000000) == 0x0a000000: return decode_dataproc_register(d)
    if (d & 0x0e000000) == 0x0e000000: return decode_dataproc_simd(d)
    if (d & 0x1c000000) == 0x10000000: return decode_dataproc_immediate(d)
    if (d & 0x1c000000) == 0x14000000: return decode_branch_and_sys(d)
    if (d & 0x0a000000) == 0x08000000: return decode_load_and_store(d)
    return decode_UNDEFINED(d)

def decode_dataproc_immediate(d):
    assert (d & 0x1c000000) == 0x10000000
    op0    = (d >> 23) & 7
    if (d & 0x1f800000) == 0x12000000: return decode_log_imm(d)
    if (d & 0x1f800000) == 0x12800000: return decode_movewide(d)
    if (d & 0x1f800000) == 0x13000000: return decode_bitfield(d)
    if (d & 0x1f800000) == 0x13800000: return decode_extract(d)
    if (d & 0x1f000000) == 0x10000000: return decode_pcreladdr(d)
    if (d & 0x1f000000) == 0x11000000: return decode_addsub_imm(d)
    return decode_UNDEFINED(d)

def decode_branch_and_sys(d):
    assert (d & 0x1c000000) == 0x14000000
    op0    = (d >> 29) & 7
    op1    = (d >> 22) & 0xF
    if (d & 0xffc00000) == 0xd5000000: return decode_system(d)
    if (d & 0xff000000) == 0xd4000000: return decode_exception(d)
    if (d & 0xfe000000) == 0x54000000: return decode_condbranch(d)
    if (d & 0xfe000000) == 0xd6000000: return decode_branch_reg(d)
    if (d & 0x7e000000) == 0x34000000: return decode_compbranch(d)
    if (d & 0x7e000000) == 0x36000000: return decode_testbranch(d)
    if (d & 0x7c000000) == 0x14000000: return decode_branch_imm(d)
    return decode_UNDEFINED(d)

def decode_load_and_store(d):
    assert (d & 0x0a000000) == 0x08000000
    op0    = (d >> 31) & 1
    op1    = (d >> 28) & 3
    op2    = (d >> 26) & 1
    op3    = (d >> 23) & 3
    op4    = (d >> 16) & 0x3F
    op5    = (d >> 10) & 3
    if (d & 0xbfbf0000) == 0x0c000000: return decode_asisdlse(d)
    if (d & 0xbf9f0000) == 0x0d000000: return decode_asisdlso(d)
    if (d & 0xbfa00000) == 0x0c800000: return decode_asisdlsep(d)
    if (d & 0x3b200c00) == 0x38000000: return decode_ldst_unscaled(d)
    if (d & 0x3b200c00) == 0x38000400: return decode_ldst_immpost(d)
    if (d & 0x3b200c00) == 0x38000800: return decode_ldst_unpriv(d)
    if (d & 0x3b200c00) == 0x38000c00: return decode_ldst_immpre(d)
    if (d & 0x3b200c00) == 0x38200000: return decode_memop(d)
    if (d & 0x3b200c00) == 0x38200800: return decode_ldst_regoff(d)
    if (d & 0xbf800000) == 0x0d800000: return decode_asisdlsop(d)
    if (d & 0x3b200400) == 0x38200400: return decode_ldst_pac(d)
    if (d & 0x3b800000) == 0x28000000: return decode_ldstnapair_offs(d)
    if (d & 0x3b800000) == 0x28800000: return decode_ldstpair_post(d)
    if (d & 0x3b800000) == 0x29000000: return decode_ldstpair_off(d)
    if (d & 0x3b800000) == 0x29800000: return decode_ldstpair_pre(d)
    if (d & 0x3f000000) == 0x08000000: return decode_ldstexcl(d)
    if (d & 0x3b000000) == 0x18000000: return decode_loadlit(d)
    if (d & 0x3b000000) == 0x39000000: return decode_ldst_pos(d)
    return decode_UNDEFINED(d)

def decode_dataproc_register(d):
    assert (d & 0x0e000000) == 0x0a000000
    op0    = (d >> 30) & 1
    op1    = (d >> 28) & 1
    op2    = (d >> 21) & 0xF
    op3    = (d >> 11) & 1
    if (d & 0x1fe00800) == 0x1a400000: return decode_condcmp_reg(d)
    if (d & 0x1fe00800) == 0x1a400800: return decode_condcmp_imm(d)
    if (d & 0x5fe00000) == 0x1ac00000: return decode_dp_2src(d)
    if (d & 0x5fe00000) == 0x5ac00000: return decode_dp_1src(d)
    if (d & 0x1fe00000) == 0x1a000000: return decode_addsub_carry(d)
    if (d & 0x1fe00000) == 0x1a800000: return decode_condsel(d)
    if (d & 0x1f200000) == 0x0b000000: return decode_addsub_shift(d)
    if (d & 0x1f200000) == 0x0b200000: return decode_addsub_ext(d)
    if (d & 0x1f000000) == 0x0a000000: return decode_log_shift(d)
    if (d & 0x1f000000) == 0x1b000000: return decode_dp_3src(d)
    return decode_UNDEFINED(d)

def decode_dataproc_simd(d):
    assert (d & 0x0e000000) == 0x0e000000
    op0    = (d >> 28) & 0xF
    op1    = (d >> 23) & 3
    op2    = (d >> 19) & 0xF
    op3    = (d >> 10) & 0x1FF
    if (d & 0xfffff000) == 0xcec08000: return decode_cryptosha512_2(d)
    if (d & 0xdf7e0c00) == 0x5e780800: return decode_asisdmiscfp16(d)
    if (d & 0xff3e0c00) == 0x4e280800: return decode_cryptoaes(d)
    if (d & 0xff3e0c00) == 0x5e280800: return decode_cryptosha2(d)
    if (d & 0x9f7e0c00) == 0x0e780800: return decode_asimdmiscfp16(d)
    if (d & 0xdf3e0c00) == 0x5e200800: return decode_asisdmisc(d)
    if (d & 0xdf3e0c00) == 0x5e300800: return decode_asisdpair(d)
    if (d & 0xffe0b000) == 0xce608000: return decode_cryptosha512_3(d)
    if (d & 0x5f20fc00) == 0x1e200000: return decode_float2int(d)
    if (d & 0x9f3e0c00) == 0x0e200800: return decode_asimdmisc(d)
    if (d & 0x9f3e0c00) == 0x0e300800: return decode_asimdall(d)
    if (d & 0xffe0c000) == 0xce408000: return decode_crypto3_imm2(d)
    if (d & 0x5f207c00) == 0x1e204000: return decode_floatdp1(d)
    if (d & 0x9ff80400) == 0x0f000400: return decode_asimdimm(d)
    if (d & 0xdf60c400) == 0x5e400400: return decode_asisdsamefp16(d)
    if (d & 0xdfe08400) == 0x5e000400: return decode_asisdone(d)
    if (d & 0xff208c00) == 0x5e000000: return decode_cryptosha3(d)
    if (d & 0x5f203c00) == 0x1e202000: return decode_floatcmp(d)
    if (d & 0x9f60c400) == 0x0e400400: return decode_asimdsamefp16(d)
    if (d & 0x9fe08400) == 0x0e000400: return decode_asimdins(d)
    if (d & 0xbf208c00) == 0x0e000000: return decode_asimdtbl(d)
    if (d & 0xbf208c00) == 0x0e000800: return decode_asimdperm(d)
    if (d & 0xffe00000) == 0xce800000: return decode_crypto3_imm6(d)
    if (d & 0x5f201c00) == 0x1e201000: return decode_floatimm(d)
    if (d & 0xbf208400) == 0x2e000000: return decode_asimdext(d)
    if (d & 0xdf200c00) == 0x5e200000: return decode_asisddiff(d)
    if (d & 0xdf208400) == 0x5e008400: return decode_asisdsame2(d)
    if (d & 0xff808000) == 0xce000000: return decode_crypto4(d)
    if (d & 0x5f200c00) == 0x1e200400: return decode_floatccmp(d)
    if (d & 0x5f200c00) == 0x1e200800: return decode_floatdp2(d)
    if (d & 0x5f200c00) == 0x1e200c00: return decode_floatsel(d)
    if (d & 0x9f200c00) == 0x0e200000: return decode_asimddiff(d)
    if (d & 0x9f208400) == 0x0e008400: return decode_asimdsame2(d)
    if (d & 0xdf200400) == 0x5e200400: return decode_asisdsame(d)
    if (d & 0xdf800400) == 0x5f000400: return decode_asisdshf(d)
    if (d & 0x9f200400) == 0x0e200400: return decode_asimdsame(d)
    if (d & 0xdf000400) == 0x5f000000: return decode_asisdelem(d)
    if (d & 0x5f200000) == 0x1e000000: return decode_float2fix(d)
    if (d & 0x9f000400) == 0x0f000000: return decode_asimdelem(d)
    if (d & 0x5f000000) == 0x1f000000: return decode_floatdp3(d)
    if (d & 0x9f800400) == 0x0f000400 and (d & 0x780000) != 0x000000: return decode_asimdshf(d)
    return decode_UNDEFINED(d)

def decode_compbranch(d):
    assert (d & 0x7e000000) == 0x34000000
    Rt     = (d >> 0) & 0x1F
    imm19  = (d >> 5) & 0x7FFFF
    op     = (d >> 24) & 1
    sf     = (d >> 31) & 1
    if (d & 0xff000000) == 0x34000000: return ('CBZ_32_compbranch', {'Rt': Rt, 'imm19': imm19})
    if (d & 0xff000000) == 0x35000000: return ('CBNZ_32_compbranch', {'Rt': Rt, 'imm19': imm19})
    if (d & 0xff000000) == 0xb4000000: return ('CBZ_64_compbranch', {'Rt': Rt, 'imm19': imm19})
    if (d & 0xff000000) == 0xb5000000: return ('CBNZ_64_compbranch', {'Rt': Rt, 'imm19': imm19})
    return decode_UNDEFINED(d)

def decode_condbranch(d):
    assert (d & 0xfe000000) == 0x54000000
    cond   = (d >> 0) & 0xF
    imm19  = (d >> 5) & 0x7FFFF
    o0     = (d >> 4) & 1
    o1     = (d >> 24) & 1
    if (d & 0xff000010) == 0x54000000: return ('B_only_condbranch', {'cond': cond, 'imm19': imm19})
    return decode_UNDEFINED(d)

def decode_exception(d):
    assert (d & 0xff000000) == 0xd4000000
    LL     = (d >> 0) & 3
    imm16  = (d >> 5) & 0xFFFF
    op2    = (d >> 2) & 7
    opc    = (d >> 21) & 7
    if (d & 0xffe0001f) == 0xd4000001: return ('SVC_EX_exception', {'imm16': imm16})
    if (d & 0xffe0001f) == 0xd4000002: return ('HVC_EX_exception', {'imm16': imm16})
    if (d & 0xffe0001f) == 0xd4000003: return ('SMC_EX_exception', {'imm16': imm16})
    if (d & 0xffe0001f) == 0xd4200000: return ('BRK_EX_exception', {'imm16': imm16})
    if (d & 0xffe0001f) == 0xd4400000: return ('HLT_EX_exception', {'imm16': imm16})
    if (d & 0xffe0001f) == 0xd4a00001: return ('DCPS1_DC_exception', {'imm16': imm16})
    if (d & 0xffe0001f) == 0xd4a00002: return ('DCPS2_DC_exception', {'imm16': imm16})
    if (d & 0xffe0001f) == 0xd4a00003: return ('DCPS3_DC_exception', {'imm16': imm16})
    return decode_UNDEFINED(d)

def decode_system(d):
    assert (d & 0xffc00000) == 0xd5000000
    CRm    = (d >> 8) & 0xF
    CRn    = (d >> 12) & 0xF
    L      = (d >> 21) & 1
    Rt     = (d >> 0) & 0x1F
    op0    = (d >> 19) & 3
    op1    = (d >> 16) & 7
    op2    = (d >> 5) & 7
    if (d & 0xffffffff) == 0xd503201f: return ('NOP_HI_system', {})
    if (d & 0xffffffff) == 0xd503203f: return ('YIELD_HI_system', {})
    if (d & 0xffffffff) == 0xd503205f: return ('WFE_HI_system', {})
    if (d & 0xffffffff) == 0xd503207f: return ('WFI_HI_system', {})
    if (d & 0xffffffff) == 0xd503209f: return ('SEV_HI_system', {})
    if (d & 0xffffffff) == 0xd50320bf: return ('SEVL_HI_system', {})
    if (d & 0xffffffff) == 0xd50320ff: return ('XPACLRI_HI_system', {})
    if (d & 0xffffffff) == 0xd503211f: return ('PACIA1716_HI_system', {})
    if (d & 0xffffffff) == 0xd503215f: return ('PACIB1716_HI_system', {})
    if (d & 0xffffffff) == 0xd503219f: return ('AUTIA1716_HI_system', {})
    if (d & 0xffffffff) == 0xd50321df: return ('AUTIB1716_HI_system', {})
    if (d & 0xffffffff) == 0xd503221f: return ('ESB_HI_system', {})
    if (d & 0xffffffff) == 0xd503223f: return ('PSB_HC_system', {})
    if (d & 0xffffffff) == 0xd503231f: return ('PACIAZ_HI_system', {})
    if (d & 0xffffffff) == 0xd503233f: return ('PACIASP_HI_system', {})
    if (d & 0xffffffff) == 0xd503235f: return ('PACIBZ_HI_system', {})
    if (d & 0xffffffff) == 0xd503237f: return ('PACIBSP_HI_system', {})
    if (d & 0xffffffff) == 0xd503239f: return ('AUTIAZ_HI_system', {})
    if (d & 0xffffffff) == 0xd50323bf: return ('AUTIASP_HI_system', {})
    if (d & 0xffffffff) == 0xd50323df: return ('AUTIBZ_HI_system', {})
    if (d & 0xffffffff) == 0xd50323ff: return ('AUTIBSP_HI_system', {})
    if (d & 0xffffffdf) == 0xd50320df: return ('HINT_1', {'op2': op2})
    if (d & 0xfffff0ff) == 0xd503305f: return ('CLREX_BN_system', {'CRm': CRm})
    if (d & 0xfffff0ff) == 0xd503309f: return ('DSB_BO_system', {'CRm': CRm})
    if (d & 0xfffff0ff) == 0xd50330bf: return ('DMB_BO_system', {'CRm': CRm})
    if (d & 0xfffff0ff) == 0xd50330df: return ('ISB_BI_system', {'CRm': CRm})
    if (d & 0xfff8f01f) == 0xd500401f: return ('MSR_SI_system', {'CRm': CRm, 'op1': op1, 'op2': op2})
    if (d & 0xfff80000) == 0xd5080000: return ('SYS_CR_system', {'CRm': CRm, 'CRn': CRn, 'Rt': Rt, 'op1': op1, 'op2': op2})
    if (d & 0xfff80000) == 0xd5280000: return ('SYSL_RC_system', {'CRm': CRm, 'CRn': CRn, 'Rt': Rt, 'op1': op1, 'op2': op2})
    if (d & 0xfff00000) == 0xd5100000: return ('MSR_SR_system', {'CRm': CRm, 'CRn': CRn, 'Rt': Rt, 'op0': op0, 'op1': op1, 'op2': op2})
    if (d & 0xfff00000) == 0xd5300000: return ('MRS_RS_system', {'CRm': CRm, 'CRn': CRn, 'Rt': Rt, 'op0': op0, 'op1': op1, 'op2': op2})
    if (d & 0xffffff1f) == 0xd503221f and (d & 0x0000c0) != 0x000000: return ('HINT_3', {'op2': op2})
    if (d & 0xfffff01f) == 0xd503201f and (d & 0x000d00) != 0x000000: return ('HINT_2', {'CRm': CRm, 'op2': op2})
    return decode_UNDEFINED(d)

def decode_testbranch(d):
    assert (d & 0x7e000000) == 0x36000000
    Rt     = (d >> 0) & 0x1F
    b40    = (d >> 19) & 0x1F
    b5     = (d >> 31) & 1
    imm14  = (d >> 5) & 0x3FFF
    op     = (d >> 24) & 1
    if (d & 0x7f000000) == 0x36000000: return ('TBZ_only_testbranch', {'Rt': Rt, 'b40': b40, 'b5': b5, 'imm14': imm14})
    if (d & 0x7f000000) == 0x37000000: return ('TBNZ_only_testbranch', {'Rt': Rt, 'b40': b40, 'b5': b5, 'imm14': imm14})
    return decode_UNDEFINED(d)

def decode_branch_imm(d):
    assert (d & 0x7c000000) == 0x14000000
    imm26  = (d >> 0) & 0x3FFFFFF
    op     = (d >> 31) & 1
    if (d & 0xfc000000) == 0x14000000: return ('B_only_branch_imm', {'imm26': imm26})
    if (d & 0xfc000000) == 0x94000000: return ('BL_only_branch_imm', {'imm26': imm26})
    return decode_UNDEFINED(d)

def decode_branch_reg(d):
    assert (d & 0xfe000000) == 0xd6000000
    Rn     = (d >> 5) & 0x1F
    op2    = (d >> 16) & 0x1F
    op3    = (d >> 10) & 0x3F
    op4    = (d >> 0) & 0x1F
    opc    = (d >> 21) & 0xF
    if (d & 0xffffffff) == 0xd65f0bff: return ('RETAA_64E_branch_reg', {})
    if (d & 0xffffffff) == 0xd65f0fff: return ('RETAB_64E_branch_reg', {})
    if (d & 0xffffffff) == 0xd69f03e0: return ('ERET_64E_branch_reg', {})
    if (d & 0xffffffff) == 0xd69f0bff: return ('ERETAA_64E_branch_reg', {})
    if (d & 0xffffffff) == 0xd69f0fff: return ('ERETAB_64E_branch_reg', {})
    if (d & 0xffffffff) == 0xd6bf03e0: return ('DRPS_64E_branch_reg', {})
    if (d & 0xfffffc1f) == 0xd61f0000: return ('BR_64_branch_reg', {'Rn': Rn})
    if (d & 0xfffffc1f) == 0xd61f081f: return ('BRAAZ_64_branch_reg', {'Rn': Rn})
    if (d & 0xfffffc1f) == 0xd61f0c1f: return ('BRABZ_64_branch_reg', {'Rn': Rn})
    if (d & 0xfffffc1f) == 0xd63f0000: return ('BLR_64_branch_reg', {'Rn': Rn})
    if (d & 0xfffffc1f) == 0xd63f081f: return ('BLRAAZ_64_branch_reg', {'Rn': Rn})
    if (d & 0xfffffc1f) == 0xd63f0c1f: return ('BLRABZ_64_branch_reg', {'Rn': Rn})
    if (d & 0xfffffc1f) == 0xd65f0000: return ('RET_64R_branch_reg', {'Rn': Rn})
    if (d & 0xfffffc00) == 0xd71f0800: return ('BRAA_64P_branch_reg', {'Rn': Rn, 'op4': op4})
    if (d & 0xfffffc00) == 0xd71f0c00: return ('BRAB_64P_branch_reg', {'Rn': Rn, 'op4': op4})
    if (d & 0xfffffc00) == 0xd73f0800: return ('BLRAA_64P_branch_reg', {'Rn': Rn, 'op4': op4})
    if (d & 0xfffffc00) == 0xd73f0c00: return ('BLRAB_64P_branch_reg', {'Rn': Rn, 'op4': op4})
    return decode_UNDEFINED(d)

def decode_asisdlse(d):
    assert (d & 0xbfbf0000) == 0x0c000000
    L      = (d >> 22) & 1
    Q      = (d >> 30) & 1
    Rn     = (d >> 5) & 0x1F
    Rt     = (d >> 0) & 0x1F
    opcode = (d >> 12) & 0xF
    size   = (d >> 10) & 3
    if (d & 0xbffff000) == 0x0c000000: return ('ST4_asisdlse_R4', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbffff000) == 0x0c002000: return ('ST1_asisdlse_R4_4v', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbffff000) == 0x0c004000: return ('ST3_asisdlse_R3', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbffff000) == 0x0c006000: return ('ST1_asisdlse_R3_3v', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbffff000) == 0x0c007000: return ('ST1_asisdlse_R1_1v', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbffff000) == 0x0c008000: return ('ST2_asisdlse_R2', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbffff000) == 0x0c00a000: return ('ST1_asisdlse_R2_2v', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbffff000) == 0x0c400000: return ('LD4_asisdlse_R4', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbffff000) == 0x0c402000: return ('LD1_asisdlse_R4_4v', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbffff000) == 0x0c404000: return ('LD3_asisdlse_R3', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbffff000) == 0x0c406000: return ('LD1_asisdlse_R3_3v', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbffff000) == 0x0c407000: return ('LD1_asisdlse_R1_1v', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbffff000) == 0x0c408000: return ('LD2_asisdlse_R2', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbffff000) == 0x0c40a000: return ('LD1_asisdlse_R2_2v', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    return decode_UNDEFINED(d)

def decode_asisdlsep(d):
    assert (d & 0xbfa00000) == 0x0c800000
    L      = (d >> 22) & 1
    Q      = (d >> 30) & 1
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    Rt     = (d >> 0) & 0x1F
    opcode = (d >> 12) & 0xF
    size   = (d >> 10) & 3
    if (d & 0xbffff000) == 0x0c9f0000: return ('ST4_asisdlsep_I4_i', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbffff000) == 0x0c9f2000: return ('ST1_asisdlsep_I4_i4', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbffff000) == 0x0c9f4000: return ('ST3_asisdlsep_I3_i', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbffff000) == 0x0c9f6000: return ('ST1_asisdlsep_I3_i3', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbffff000) == 0x0c9f7000: return ('ST1_asisdlsep_I1_i1', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbffff000) == 0x0c9f8000: return ('ST2_asisdlsep_I2_i', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbffff000) == 0x0c9fa000: return ('ST1_asisdlsep_I2_i2', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbffff000) == 0x0cdf0000: return ('LD4_asisdlsep_I4_i', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbffff000) == 0x0cdf2000: return ('LD1_asisdlsep_I4_i4', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbffff000) == 0x0cdf4000: return ('LD3_asisdlsep_I3_i', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbffff000) == 0x0cdf6000: return ('LD1_asisdlsep_I3_i3', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbffff000) == 0x0cdf7000: return ('LD1_asisdlsep_I1_i1', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbffff000) == 0x0cdf8000: return ('LD2_asisdlsep_I2_i', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbffff000) == 0x0cdfa000: return ('LD1_asisdlsep_I2_i2', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbfe0f000) == 0x0c800000 and (d & 0x1f0000) != 0x1f0000: return ('ST4_asisdlsep_R4_r', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbfe0f000) == 0x0c802000 and (d & 0x1f0000) != 0x1f0000: return ('ST1_asisdlsep_R4_r4', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbfe0f000) == 0x0c804000 and (d & 0x1f0000) != 0x1f0000: return ('ST3_asisdlsep_R3_r', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbfe0f000) == 0x0c806000 and (d & 0x1f0000) != 0x1f0000: return ('ST1_asisdlsep_R3_r3', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbfe0f000) == 0x0c807000 and (d & 0x1f0000) != 0x1f0000: return ('ST1_asisdlsep_R1_r1', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbfe0f000) == 0x0c808000 and (d & 0x1f0000) != 0x1f0000: return ('ST2_asisdlsep_R2_r', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbfe0f000) == 0x0c80a000 and (d & 0x1f0000) != 0x1f0000: return ('ST1_asisdlsep_R2_r2', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbfe0f000) == 0x0cc00000 and (d & 0x1f0000) != 0x1f0000: return ('LD4_asisdlsep_R4_r', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbfe0f000) == 0x0cc02000 and (d & 0x1f0000) != 0x1f0000: return ('LD1_asisdlsep_R4_r4', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbfe0f000) == 0x0cc04000 and (d & 0x1f0000) != 0x1f0000: return ('LD3_asisdlsep_R3_r', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbfe0f000) == 0x0cc06000 and (d & 0x1f0000) != 0x1f0000: return ('LD1_asisdlsep_R3_r3', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbfe0f000) == 0x0cc07000 and (d & 0x1f0000) != 0x1f0000: return ('LD1_asisdlsep_R1_r1', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbfe0f000) == 0x0cc08000 and (d & 0x1f0000) != 0x1f0000: return ('LD2_asisdlsep_R2_r', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbfe0f000) == 0x0cc0a000 and (d & 0x1f0000) != 0x1f0000: return ('LD1_asisdlsep_R2_r2', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'size': size})
    return decode_UNDEFINED(d)

def decode_asisdlso(d):
    assert (d & 0xbf9f0000) == 0x0d000000
    L      = (d >> 22) & 1
    Q      = (d >> 30) & 1
    R      = (d >> 21) & 1
    Rn     = (d >> 5) & 0x1F
    Rt     = (d >> 0) & 0x1F
    S      = (d >> 12) & 1
    opcode = (d >> 13) & 7
    size   = (d >> 10) & 3
    if (d & 0xbffffc00) == 0x0d008400: return ('ST1_asisdlso_D1_1d', {'Q': Q, 'Rn': Rn, 'Rt': Rt})
    if (d & 0xbffffc00) == 0x0d00a400: return ('ST3_asisdlso_D3_3d', {'Q': Q, 'Rn': Rn, 'Rt': Rt})
    if (d & 0xbffffc00) == 0x0d208400: return ('ST2_asisdlso_D2_2d', {'Q': Q, 'Rn': Rn, 'Rt': Rt})
    if (d & 0xbffffc00) == 0x0d20a400: return ('ST4_asisdlso_D4_4d', {'Q': Q, 'Rn': Rn, 'Rt': Rt})
    if (d & 0xbffffc00) == 0x0d408400: return ('LD1_asisdlso_D1_1d', {'Q': Q, 'Rn': Rn, 'Rt': Rt})
    if (d & 0xbffffc00) == 0x0d40a400: return ('LD3_asisdlso_D3_3d', {'Q': Q, 'Rn': Rn, 'Rt': Rt})
    if (d & 0xbffffc00) == 0x0d608400: return ('LD2_asisdlso_D2_2d', {'Q': Q, 'Rn': Rn, 'Rt': Rt})
    if (d & 0xbffffc00) == 0x0d60a400: return ('LD4_asisdlso_D4_4d', {'Q': Q, 'Rn': Rn, 'Rt': Rt})
    if (d & 0xbfffec00) == 0x0d008000: return ('ST1_asisdlso_S1_1s', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S})
    if (d & 0xbfffec00) == 0x0d00a000: return ('ST3_asisdlso_S3_3s', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S})
    if (d & 0xbfffec00) == 0x0d208000: return ('ST2_asisdlso_S2_2s', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S})
    if (d & 0xbfffec00) == 0x0d20a000: return ('ST4_asisdlso_S4_4s', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S})
    if (d & 0xbfffec00) == 0x0d408000: return ('LD1_asisdlso_S1_1s', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S})
    if (d & 0xbfffec00) == 0x0d40a000: return ('LD3_asisdlso_S3_3s', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S})
    if (d & 0xbfffec00) == 0x0d608000: return ('LD2_asisdlso_S2_2s', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S})
    if (d & 0xbfffec00) == 0x0d60a000: return ('LD4_asisdlso_S4_4s', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S})
    if (d & 0xbfffe400) == 0x0d004000: return ('ST1_asisdlso_H1_1h', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfffe400) == 0x0d006000: return ('ST3_asisdlso_H3_3h', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfffe400) == 0x0d204000: return ('ST2_asisdlso_H2_2h', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfffe400) == 0x0d206000: return ('ST4_asisdlso_H4_4h', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfffe400) == 0x0d404000: return ('LD1_asisdlso_H1_1h', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfffe400) == 0x0d406000: return ('LD3_asisdlso_H3_3h', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfffe400) == 0x0d604000: return ('LD2_asisdlso_H2_2h', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfffe400) == 0x0d606000: return ('LD4_asisdlso_H4_4h', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbffff000) == 0x0d40c000: return ('LD1R_asisdlso_R1', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbffff000) == 0x0d40e000: return ('LD3R_asisdlso_R3', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbffff000) == 0x0d60c000: return ('LD2R_asisdlso_R2', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbffff000) == 0x0d60e000: return ('LD4R_asisdlso_R4', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbfffe000) == 0x0d000000: return ('ST1_asisdlso_B1_1b', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfffe000) == 0x0d002000: return ('ST3_asisdlso_B3_3b', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfffe000) == 0x0d200000: return ('ST2_asisdlso_B2_2b', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfffe000) == 0x0d202000: return ('ST4_asisdlso_B4_4b', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfffe000) == 0x0d400000: return ('LD1_asisdlso_B1_1b', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfffe000) == 0x0d402000: return ('LD3_asisdlso_B3_3b', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfffe000) == 0x0d600000: return ('LD2_asisdlso_B2_2b', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfffe000) == 0x0d602000: return ('LD4_asisdlso_B4_4b', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    return decode_UNDEFINED(d)

def decode_asisdlsop(d):
    assert (d & 0xbf800000) == 0x0d800000
    L      = (d >> 22) & 1
    Q      = (d >> 30) & 1
    R      = (d >> 21) & 1
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    Rt     = (d >> 0) & 0x1F
    S      = (d >> 12) & 1
    opcode = (d >> 13) & 7
    size   = (d >> 10) & 3
    if (d & 0xbffffc00) == 0x0d9f8400: return ('ST1_asisdlsop_D1_i1d', {'Q': Q, 'Rn': Rn, 'Rt': Rt})
    if (d & 0xbffffc00) == 0x0d9fa400: return ('ST3_asisdlsop_D3_i3d', {'Q': Q, 'Rn': Rn, 'Rt': Rt})
    if (d & 0xbffffc00) == 0x0dbf8400: return ('ST2_asisdlsop_D2_i2d', {'Q': Q, 'Rn': Rn, 'Rt': Rt})
    if (d & 0xbffffc00) == 0x0dbfa400: return ('ST4_asisdlsop_D4_i4d', {'Q': Q, 'Rn': Rn, 'Rt': Rt})
    if (d & 0xbffffc00) == 0x0ddf8400: return ('LD1_asisdlsop_D1_i1d', {'Q': Q, 'Rn': Rn, 'Rt': Rt})
    if (d & 0xbffffc00) == 0x0ddfa400: return ('LD3_asisdlsop_D3_i3d', {'Q': Q, 'Rn': Rn, 'Rt': Rt})
    if (d & 0xbffffc00) == 0x0dff8400: return ('LD2_asisdlsop_D2_i2d', {'Q': Q, 'Rn': Rn, 'Rt': Rt})
    if (d & 0xbffffc00) == 0x0dffa400: return ('LD4_asisdlsop_D4_i4d', {'Q': Q, 'Rn': Rn, 'Rt': Rt})
    if (d & 0xbfffec00) == 0x0d9f8000: return ('ST1_asisdlsop_S1_i1s', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S})
    if (d & 0xbfffec00) == 0x0d9fa000: return ('ST3_asisdlsop_S3_i3s', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S})
    if (d & 0xbfffec00) == 0x0dbf8000: return ('ST2_asisdlsop_S2_i2s', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S})
    if (d & 0xbfffec00) == 0x0dbfa000: return ('ST4_asisdlsop_S4_i4s', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S})
    if (d & 0xbfffec00) == 0x0ddf8000: return ('LD1_asisdlsop_S1_i1s', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S})
    if (d & 0xbfffec00) == 0x0ddfa000: return ('LD3_asisdlsop_S3_i3s', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S})
    if (d & 0xbfffec00) == 0x0dff8000: return ('LD2_asisdlsop_S2_i2s', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S})
    if (d & 0xbfffec00) == 0x0dffa000: return ('LD4_asisdlsop_S4_i4s', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S})
    if (d & 0xbfffe400) == 0x0d9f4000: return ('ST1_asisdlsop_H1_i1h', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfffe400) == 0x0d9f6000: return ('ST3_asisdlsop_H3_i3h', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfffe400) == 0x0dbf4000: return ('ST2_asisdlsop_H2_i2h', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfffe400) == 0x0dbf6000: return ('ST4_asisdlsop_H4_i4h', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfffe400) == 0x0ddf4000: return ('LD1_asisdlsop_H1_i1h', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfffe400) == 0x0ddf6000: return ('LD3_asisdlsop_H3_i3h', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfffe400) == 0x0dff4000: return ('LD2_asisdlsop_H2_i2h', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfffe400) == 0x0dff6000: return ('LD4_asisdlsop_H4_i4h', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbffff000) == 0x0ddfc000: return ('LD1R_asisdlsop_R1_i', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbffff000) == 0x0ddfe000: return ('LD3R_asisdlsop_R3_i', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbffff000) == 0x0dffc000: return ('LD2R_asisdlsop_R2_i', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbffff000) == 0x0dffe000: return ('LD4R_asisdlsop_R4_i', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbfffe000) == 0x0d9f0000: return ('ST1_asisdlsop_B1_i1b', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfffe000) == 0x0d9f2000: return ('ST3_asisdlsop_B3_i3b', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfffe000) == 0x0dbf0000: return ('ST2_asisdlsop_B2_i2b', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfffe000) == 0x0dbf2000: return ('ST4_asisdlsop_B4_i4b', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfffe000) == 0x0ddf0000: return ('LD1_asisdlsop_B1_i1b', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfffe000) == 0x0ddf2000: return ('LD3_asisdlsop_B3_i3b', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfffe000) == 0x0dff0000: return ('LD2_asisdlsop_B2_i2b', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfffe000) == 0x0dff2000: return ('LD4_asisdlsop_B4_i4b', {'Q': Q, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfe0fc00) == 0x0d808400 and (d & 0x1f0000) != 0x1f0000: return ('ST1_asisdlsop_DX1_r1d', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt})
    if (d & 0xbfe0fc00) == 0x0d80a400 and (d & 0x1f0000) != 0x1f0000: return ('ST3_asisdlsop_DX3_r3d', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt})
    if (d & 0xbfe0fc00) == 0x0da08400 and (d & 0x1f0000) != 0x1f0000: return ('ST2_asisdlsop_DX2_r2d', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt})
    if (d & 0xbfe0fc00) == 0x0da0a400 and (d & 0x1f0000) != 0x1f0000: return ('ST4_asisdlsop_DX4_r4d', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt})
    if (d & 0xbfe0fc00) == 0x0dc08400 and (d & 0x1f0000) != 0x1f0000: return ('LD1_asisdlsop_DX1_r1d', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt})
    if (d & 0xbfe0fc00) == 0x0dc0a400 and (d & 0x1f0000) != 0x1f0000: return ('LD3_asisdlsop_DX3_r3d', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt})
    if (d & 0xbfe0fc00) == 0x0de08400 and (d & 0x1f0000) != 0x1f0000: return ('LD2_asisdlsop_DX2_r2d', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt})
    if (d & 0xbfe0fc00) == 0x0de0a400 and (d & 0x1f0000) != 0x1f0000: return ('LD4_asisdlsop_DX4_r4d', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt})
    if (d & 0xbfe0ec00) == 0x0d808000 and (d & 0x1f0000) != 0x1f0000: return ('ST1_asisdlsop_SX1_r1s', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S})
    if (d & 0xbfe0ec00) == 0x0d80a000 and (d & 0x1f0000) != 0x1f0000: return ('ST3_asisdlsop_SX3_r3s', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S})
    if (d & 0xbfe0ec00) == 0x0da08000 and (d & 0x1f0000) != 0x1f0000: return ('ST2_asisdlsop_SX2_r2s', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S})
    if (d & 0xbfe0ec00) == 0x0da0a000 and (d & 0x1f0000) != 0x1f0000: return ('ST4_asisdlsop_SX4_r4s', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S})
    if (d & 0xbfe0ec00) == 0x0dc08000 and (d & 0x1f0000) != 0x1f0000: return ('LD1_asisdlsop_SX1_r1s', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S})
    if (d & 0xbfe0ec00) == 0x0dc0a000 and (d & 0x1f0000) != 0x1f0000: return ('LD3_asisdlsop_SX3_r3s', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S})
    if (d & 0xbfe0ec00) == 0x0de08000 and (d & 0x1f0000) != 0x1f0000: return ('LD2_asisdlsop_SX2_r2s', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S})
    if (d & 0xbfe0ec00) == 0x0de0a000 and (d & 0x1f0000) != 0x1f0000: return ('LD4_asisdlsop_SX4_r4s', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S})
    if (d & 0xbfe0e400) == 0x0d804000 and (d & 0x1f0000) != 0x1f0000: return ('ST1_asisdlsop_HX1_r1h', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfe0e400) == 0x0d806000 and (d & 0x1f0000) != 0x1f0000: return ('ST3_asisdlsop_HX3_r3h', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfe0e400) == 0x0da04000 and (d & 0x1f0000) != 0x1f0000: return ('ST2_asisdlsop_HX2_r2h', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfe0e400) == 0x0da06000 and (d & 0x1f0000) != 0x1f0000: return ('ST4_asisdlsop_HX4_r4h', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfe0e400) == 0x0dc04000 and (d & 0x1f0000) != 0x1f0000: return ('LD1_asisdlsop_HX1_r1h', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfe0e400) == 0x0dc06000 and (d & 0x1f0000) != 0x1f0000: return ('LD3_asisdlsop_HX3_r3h', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfe0e400) == 0x0de04000 and (d & 0x1f0000) != 0x1f0000: return ('LD2_asisdlsop_HX2_r2h', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfe0e400) == 0x0de06000 and (d & 0x1f0000) != 0x1f0000: return ('LD4_asisdlsop_HX4_r4h', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfe0f000) == 0x0dc0c000 and (d & 0x1f0000) != 0x1f0000: return ('LD1R_asisdlsop_RX1_r', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbfe0f000) == 0x0dc0e000 and (d & 0x1f0000) != 0x1f0000: return ('LD3R_asisdlsop_RX3_r', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbfe0f000) == 0x0de0c000 and (d & 0x1f0000) != 0x1f0000: return ('LD2R_asisdlsop_RX2_r', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbfe0f000) == 0x0de0e000 and (d & 0x1f0000) != 0x1f0000: return ('LD4R_asisdlsop_RX4_r', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'size': size})
    if (d & 0xbfe0e000) == 0x0d800000 and (d & 0x1f0000) != 0x1f0000: return ('ST1_asisdlsop_BX1_r1b', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfe0e000) == 0x0d802000 and (d & 0x1f0000) != 0x1f0000: return ('ST3_asisdlsop_BX3_r3b', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfe0e000) == 0x0da00000 and (d & 0x1f0000) != 0x1f0000: return ('ST2_asisdlsop_BX2_r2b', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfe0e000) == 0x0da02000 and (d & 0x1f0000) != 0x1f0000: return ('ST4_asisdlsop_BX4_r4b', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfe0e000) == 0x0dc00000 and (d & 0x1f0000) != 0x1f0000: return ('LD1_asisdlsop_BX1_r1b', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfe0e000) == 0x0dc02000 and (d & 0x1f0000) != 0x1f0000: return ('LD3_asisdlsop_BX3_r3b', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfe0e000) == 0x0de00000 and (d & 0x1f0000) != 0x1f0000: return ('LD2_asisdlsop_BX2_r2b', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    if (d & 0xbfe0e000) == 0x0de02000 and (d & 0x1f0000) != 0x1f0000: return ('LD4_asisdlsop_BX4_r4b', {'Q': Q, 'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'size': size})
    return decode_UNDEFINED(d)

def decode_memop(d):
    assert (d & 0x3b200c00) == 0x38200000
    A      = (d >> 23) & 1
    R      = (d >> 22) & 1
    Rn     = (d >> 5) & 0x1F
    Rs     = (d >> 16) & 0x1F
    Rt     = (d >> 0) & 0x1F
    V      = (d >> 26) & 1
    o3     = (d >> 15) & 1
    opc    = (d >> 12) & 7
    size   = (d >> 30) & 3
    if (d & 0xffe0fc1f) == 0x3820001f: return ('STADDB_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0x3820101f: return ('STCLRB_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0x3820201f: return ('STEORB_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0x3820301f: return ('STSETB_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0x3820401f: return ('STSMAXB_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0x3820501f: return ('STSMINB_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0x3820601f: return ('STUMAXB_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0x3820701f: return ('STUMINB_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0x3860001f: return ('STADDLB_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0x3860101f: return ('STCLRLB_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0x3860201f: return ('STEORLB_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0x3860301f: return ('STSETLB_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0x3860401f: return ('STSMAXLB_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0x3860501f: return ('STSMINLB_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0x3860601f: return ('STUMAXLB_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0x3860701f: return ('STUMINLB_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0x7820001f: return ('STADDH_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0x7820101f: return ('STCLRH_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0x7820201f: return ('STEORH_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0x7820301f: return ('STSETH_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0x7820401f: return ('STSMAXH_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0x7820501f: return ('STSMINH_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0x7820601f: return ('STUMAXH_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0x7820701f: return ('STUMINH_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0x7860001f: return ('STADDLH_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0x7860101f: return ('STCLRLH_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0x7860201f: return ('STEORLH_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0x7860301f: return ('STSETLH_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0x7860401f: return ('STSMAXLH_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0x7860501f: return ('STSMINLH_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0x7860601f: return ('STUMAXLH_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0x7860701f: return ('STUMINLH_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0xb820001f: return ('STADD_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0xb820101f: return ('STCLR_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0xb820201f: return ('STEOR_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0xb820301f: return ('STSET_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0xb820401f: return ('STSMAX_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0xb820501f: return ('STSMIN_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0xb820601f: return ('STUMAX_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0xb820701f: return ('STUMIN_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0xb860001f: return ('STADDL_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0xb860101f: return ('STCLRL_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0xb860201f: return ('STEORL_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0xb860301f: return ('STSETL_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0xb860401f: return ('STSMAXL_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0xb860501f: return ('STSMINL_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0xb860601f: return ('STUMAXL_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0xb860701f: return ('STUMINL_32S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0xf820001f: return ('STADD_64S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0xf820101f: return ('STCLR_64S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0xf820201f: return ('STEOR_64S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0xf820301f: return ('STSET_64S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0xf820401f: return ('STSMAX_64S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0xf820501f: return ('STSMIN_64S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0xf820601f: return ('STUMAX_64S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0xf820701f: return ('STUMIN_64S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0xf860001f: return ('STADDL_64S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0xf860101f: return ('STCLRL_64S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0xf860201f: return ('STEORL_64S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0xf860301f: return ('STSETL_64S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0xf860401f: return ('STSMAXL_64S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0xf860501f: return ('STSMINL_64S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0xf860601f: return ('STUMAXL_64S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc1f) == 0xf860701f: return ('STUMINL_64S_memop', {'Rn': Rn, 'Rs': Rs})
    if (d & 0xffe0fc00) == 0x38208000: return ('SWPB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38608000: return ('SWPLB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38a00000: return ('LDADDAB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38a01000: return ('LDCLRAB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38a02000: return ('LDEORAB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38a03000: return ('LDSETAB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38a04000: return ('LDSMAXAB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38a05000: return ('LDSMINAB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38a06000: return ('LDUMAXAB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38a07000: return ('LDUMINAB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38a08000: return ('SWPAB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38a0c000: return ('LDAPRB_32L_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38e00000: return ('LDADDALB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38e01000: return ('LDCLRALB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38e02000: return ('LDEORALB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38e03000: return ('LDSETALB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38e04000: return ('LDSMAXALB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38e05000: return ('LDSMINALB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38e06000: return ('LDUMAXALB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38e07000: return ('LDUMINALB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38e08000: return ('SWPALB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78208000: return ('SWPH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78608000: return ('SWPLH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78a00000: return ('LDADDAH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78a01000: return ('LDCLRAH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78a02000: return ('LDEORAH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78a03000: return ('LDSETAH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78a04000: return ('LDSMAXAH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78a05000: return ('LDSMINAH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78a06000: return ('LDUMAXAH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78a07000: return ('LDUMINAH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78a08000: return ('SWPAH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78a0c000: return ('LDAPRH_32L_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78e00000: return ('LDADDALH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78e01000: return ('LDCLRALH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78e02000: return ('LDEORALH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78e03000: return ('LDSETALH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78e04000: return ('LDSMAXALH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78e05000: return ('LDSMINALH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78e06000: return ('LDUMAXALH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78e07000: return ('LDUMINALH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78e08000: return ('SWPALH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8208000: return ('SWP_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8608000: return ('SWPL_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8a00000: return ('LDADDA_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8a01000: return ('LDCLRA_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8a02000: return ('LDEORA_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8a03000: return ('LDSETA_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8a04000: return ('LDSMAXA_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8a05000: return ('LDSMINA_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8a06000: return ('LDUMAXA_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8a07000: return ('LDUMINA_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8a08000: return ('SWPA_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8a0c000: return ('LDAPR_32L_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8e00000: return ('LDADDAL_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8e01000: return ('LDCLRAL_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8e02000: return ('LDEORAL_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8e03000: return ('LDSETAL_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8e04000: return ('LDSMAXAL_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8e05000: return ('LDSMINAL_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8e06000: return ('LDUMAXAL_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8e07000: return ('LDUMINAL_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8e08000: return ('SWPAL_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8208000: return ('SWP_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8608000: return ('SWPL_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8a00000: return ('LDADDA_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8a01000: return ('LDCLRA_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8a02000: return ('LDEORA_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8a03000: return ('LDSETA_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8a04000: return ('LDSMAXA_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8a05000: return ('LDSMINA_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8a06000: return ('LDUMAXA_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8a07000: return ('LDUMINA_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8a08000: return ('SWPA_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8a0c000: return ('LDAPR_64L_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8e00000: return ('LDADDAL_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8e01000: return ('LDCLRAL_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8e02000: return ('LDEORAL_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8e03000: return ('LDSETAL_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8e04000: return ('LDSMAXAL_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8e05000: return ('LDSMINAL_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8e06000: return ('LDUMAXAL_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8e07000: return ('LDUMINAL_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8e08000: return ('SWPAL_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38200000 and (d & 0x00001f) != 0x00001f: return ('LDADDB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38201000 and (d & 0x00001f) != 0x00001f: return ('LDCLRB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38202000 and (d & 0x00001f) != 0x00001f: return ('LDEORB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38203000 and (d & 0x00001f) != 0x00001f: return ('LDSETB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38204000 and (d & 0x00001f) != 0x00001f: return ('LDSMAXB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38205000 and (d & 0x00001f) != 0x00001f: return ('LDSMINB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38206000 and (d & 0x00001f) != 0x00001f: return ('LDUMAXB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38207000 and (d & 0x00001f) != 0x00001f: return ('LDUMINB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38600000 and (d & 0x00001f) != 0x00001f: return ('LDADDLB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38601000 and (d & 0x00001f) != 0x00001f: return ('LDCLRLB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38602000 and (d & 0x00001f) != 0x00001f: return ('LDEORLB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38603000 and (d & 0x00001f) != 0x00001f: return ('LDSETLB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38604000 and (d & 0x00001f) != 0x00001f: return ('LDSMAXLB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38605000 and (d & 0x00001f) != 0x00001f: return ('LDSMINLB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38606000 and (d & 0x00001f) != 0x00001f: return ('LDUMAXLB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x38607000 and (d & 0x00001f) != 0x00001f: return ('LDUMINLB_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78200000 and (d & 0x00001f) != 0x00001f: return ('LDADDH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78201000 and (d & 0x00001f) != 0x00001f: return ('LDCLRH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78202000 and (d & 0x00001f) != 0x00001f: return ('LDEORH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78203000 and (d & 0x00001f) != 0x00001f: return ('LDSETH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78204000 and (d & 0x00001f) != 0x00001f: return ('LDSMAXH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78205000 and (d & 0x00001f) != 0x00001f: return ('LDSMINH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78206000 and (d & 0x00001f) != 0x00001f: return ('LDUMAXH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78207000 and (d & 0x00001f) != 0x00001f: return ('LDUMINH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78600000 and (d & 0x00001f) != 0x00001f: return ('LDADDLH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78601000 and (d & 0x00001f) != 0x00001f: return ('LDCLRLH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78602000 and (d & 0x00001f) != 0x00001f: return ('LDEORLH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78603000 and (d & 0x00001f) != 0x00001f: return ('LDSETLH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78604000 and (d & 0x00001f) != 0x00001f: return ('LDSMAXLH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78605000 and (d & 0x00001f) != 0x00001f: return ('LDSMINLH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78606000 and (d & 0x00001f) != 0x00001f: return ('LDUMAXLH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x78607000 and (d & 0x00001f) != 0x00001f: return ('LDUMINLH_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8200000 and (d & 0x00001f) != 0x00001f: return ('LDADD_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8201000 and (d & 0x00001f) != 0x00001f: return ('LDCLR_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8202000 and (d & 0x00001f) != 0x00001f: return ('LDEOR_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8203000 and (d & 0x00001f) != 0x00001f: return ('LDSET_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8204000 and (d & 0x00001f) != 0x00001f: return ('LDSMAX_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8205000 and (d & 0x00001f) != 0x00001f: return ('LDSMIN_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8206000 and (d & 0x00001f) != 0x00001f: return ('LDUMAX_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8207000 and (d & 0x00001f) != 0x00001f: return ('LDUMIN_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8600000 and (d & 0x00001f) != 0x00001f: return ('LDADDL_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8601000 and (d & 0x00001f) != 0x00001f: return ('LDCLRL_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8602000 and (d & 0x00001f) != 0x00001f: return ('LDEORL_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8603000 and (d & 0x00001f) != 0x00001f: return ('LDSETL_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8604000 and (d & 0x00001f) != 0x00001f: return ('LDSMAXL_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8605000 and (d & 0x00001f) != 0x00001f: return ('LDSMINL_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8606000 and (d & 0x00001f) != 0x00001f: return ('LDUMAXL_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xb8607000 and (d & 0x00001f) != 0x00001f: return ('LDUMINL_32_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8200000 and (d & 0x00001f) != 0x00001f: return ('LDADD_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8201000 and (d & 0x00001f) != 0x00001f: return ('LDCLR_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8202000 and (d & 0x00001f) != 0x00001f: return ('LDEOR_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8203000 and (d & 0x00001f) != 0x00001f: return ('LDSET_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8204000 and (d & 0x00001f) != 0x00001f: return ('LDSMAX_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8205000 and (d & 0x00001f) != 0x00001f: return ('LDSMIN_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8206000 and (d & 0x00001f) != 0x00001f: return ('LDUMAX_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8207000 and (d & 0x00001f) != 0x00001f: return ('LDUMIN_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8600000 and (d & 0x00001f) != 0x00001f: return ('LDADDL_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8601000 and (d & 0x00001f) != 0x00001f: return ('LDCLRL_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8602000 and (d & 0x00001f) != 0x00001f: return ('LDEORL_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8603000 and (d & 0x00001f) != 0x00001f: return ('LDSETL_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8604000 and (d & 0x00001f) != 0x00001f: return ('LDSMAXL_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8605000 and (d & 0x00001f) != 0x00001f: return ('LDSMINL_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8606000 and (d & 0x00001f) != 0x00001f: return ('LDUMAXL_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xf8607000 and (d & 0x00001f) != 0x00001f: return ('LDUMINL_64_memop', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    return decode_UNDEFINED(d)

def decode_loadlit(d):
    assert (d & 0x3b000000) == 0x18000000
    Rt     = (d >> 0) & 0x1F
    V      = (d >> 26) & 1
    imm19  = (d >> 5) & 0x7FFFF
    opc    = (d >> 30) & 3
    if (d & 0xff000000) == 0x18000000: return ('LDR_32_loadlit', {'Rt': Rt, 'imm19': imm19})
    if (d & 0xff000000) == 0x1c000000: return ('LDR_S_loadlit', {'Rt': Rt, 'imm19': imm19})
    if (d & 0xff000000) == 0x58000000: return ('LDR_64_loadlit', {'Rt': Rt, 'imm19': imm19})
    if (d & 0xff000000) == 0x5c000000: return ('LDR_D_loadlit', {'Rt': Rt, 'imm19': imm19})
    if (d & 0xff000000) == 0x98000000: return ('LDRSW_64_loadlit', {'Rt': Rt, 'imm19': imm19})
    if (d & 0xff000000) == 0x9c000000: return ('LDR_Q_loadlit', {'Rt': Rt, 'imm19': imm19})
    if (d & 0xff000000) == 0xd8000000: return ('PRFM_P_loadlit', {'Rt': Rt, 'imm19': imm19})
    return decode_UNDEFINED(d)

def decode_ldstexcl(d):
    assert (d & 0x3f000000) == 0x08000000
    L      = (d >> 22) & 1
    Rn     = (d >> 5) & 0x1F
    Rs     = (d >> 16) & 0x1F
    Rt     = (d >> 0) & 0x1F
    Rt2    = (d >> 10) & 0x1F
    o0     = (d >> 15) & 1
    o1     = (d >> 21) & 1
    o2     = (d >> 23) & 1
    size   = (d >> 30) & 3
    if (d & 0xffe0fc00) == 0x08207c00: return ('CASP_CP32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x0820fc00: return ('CASPL_CP32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x08607c00: return ('CASPA_CP32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x0860fc00: return ('CASPAL_CP32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x08a07c00: return ('CASB_C32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x08a0fc00: return ('CASLB_C32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x08e07c00: return ('CASAB_C32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x08e0fc00: return ('CASALB_C32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x48207c00: return ('CASP_CP64_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x4820fc00: return ('CASPL_CP64_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x48607c00: return ('CASPA_CP64_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x4860fc00: return ('CASPAL_CP64_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x48a07c00: return ('CASH_C32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x48a0fc00: return ('CASLH_C32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x48e07c00: return ('CASAH_C32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x48e0fc00: return ('CASALH_C32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x88a07c00: return ('CAS_C32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x88a0fc00: return ('CASL_C32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x88e07c00: return ('CASA_C32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0x88e0fc00: return ('CASAL_C32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xc8a07c00: return ('CAS_C64_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xc8a0fc00: return ('CASL_C64_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xc8e07c00: return ('CASA_C64_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe0fc00) == 0xc8e0fc00: return ('CASAL_C64_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt})
    if (d & 0xffe08000) == 0x08000000: return ('STXRB_SR32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0x08008000: return ('STLXRB_SR32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0x08400000: return ('LDXRB_LR32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0x08408000: return ('LDAXRB_LR32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0x08800000: return ('STLLRB_SL32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0x08808000: return ('STLRB_SL32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0x08c00000: return ('LDLARB_LR32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0x08c08000: return ('LDARB_LR32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0x48000000: return ('STXRH_SR32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0x48008000: return ('STLXRH_SR32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0x48400000: return ('LDXRH_LR32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0x48408000: return ('LDAXRH_LR32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0x48800000: return ('STLLRH_SL32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0x48808000: return ('STLRH_SL32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0x48c00000: return ('LDLARH_LR32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0x48c08000: return ('LDARH_LR32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0x88000000: return ('STXR_SR32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0x88008000: return ('STLXR_SR32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0x88200000: return ('STXP_SP32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0x88208000: return ('STLXP_SP32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0x88400000: return ('LDXR_LR32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0x88408000: return ('LDAXR_LR32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0x88600000: return ('LDXP_LP32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0x88608000: return ('LDAXP_LP32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0x88800000: return ('STLLR_SL32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0x88808000: return ('STLR_SL32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0x88c00000: return ('LDLAR_LR32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0x88c08000: return ('LDAR_LR32_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0xc8000000: return ('STXR_SR64_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0xc8008000: return ('STLXR_SR64_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0xc8200000: return ('STXP_SP64_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0xc8208000: return ('STLXP_SP64_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0xc8400000: return ('LDXR_LR64_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0xc8408000: return ('LDAXR_LR64_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0xc8600000: return ('LDXP_LP64_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0xc8608000: return ('LDAXP_LP64_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0xc8800000: return ('STLLR_SL64_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0xc8808000: return ('STLR_SL64_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0xc8c00000: return ('LDLAR_LR64_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    if (d & 0xffe08000) == 0xc8c08000: return ('LDAR_LR64_ldstexcl', {'Rn': Rn, 'Rs': Rs, 'Rt': Rt, 'Rt2': Rt2})
    return decode_UNDEFINED(d)

def decode_ldstnapair_offs(d):
    assert (d & 0x3b800000) == 0x28000000
    L      = (d >> 22) & 1
    Rn     = (d >> 5) & 0x1F
    Rt     = (d >> 0) & 0x1F
    Rt2    = (d >> 10) & 0x1F
    V      = (d >> 26) & 1
    imm7   = (d >> 15) & 0x7F
    opc    = (d >> 30) & 3
    if (d & 0xffc00000) == 0x28000000: return ('STNP_32_ldstnapair_offs', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0x28400000: return ('LDNP_32_ldstnapair_offs', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0x2c000000: return ('STNP_S_ldstnapair_offs', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0x2c400000: return ('LDNP_S_ldstnapair_offs', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0x6c000000: return ('STNP_D_ldstnapair_offs', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0x6c400000: return ('LDNP_D_ldstnapair_offs', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0xa8000000: return ('STNP_64_ldstnapair_offs', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0xa8400000: return ('LDNP_64_ldstnapair_offs', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0xac000000: return ('STNP_Q_ldstnapair_offs', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0xac400000: return ('LDNP_Q_ldstnapair_offs', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    return decode_UNDEFINED(d)

def decode_ldst_immpost(d):
    assert (d & 0x3b200c00) == 0x38000400
    Rn     = (d >> 5) & 0x1F
    Rt     = (d >> 0) & 0x1F
    V      = (d >> 26) & 1
    imm9   = (d >> 12) & 0x1FF
    opc    = (d >> 22) & 3
    size   = (d >> 30) & 3
    if (d & 0xffe00c00) == 0x38000400: return ('STRB_32_ldst_immpost', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x38400400: return ('LDRB_32_ldst_immpost', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x38800400: return ('LDRSB_64_ldst_immpost', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x38c00400: return ('LDRSB_32_ldst_immpost', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x3c000400: return ('STR_B_ldst_immpost', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x3c400400: return ('LDR_B_ldst_immpost', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x3c800400: return ('STR_Q_ldst_immpost', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x3cc00400: return ('LDR_Q_ldst_immpost', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x78000400: return ('STRH_32_ldst_immpost', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x78400400: return ('LDRH_32_ldst_immpost', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x78800400: return ('LDRSH_64_ldst_immpost', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x78c00400: return ('LDRSH_32_ldst_immpost', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x7c000400: return ('STR_H_ldst_immpost', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x7c400400: return ('LDR_H_ldst_immpost', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xb8000400: return ('STR_32_ldst_immpost', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xb8400400: return ('LDR_32_ldst_immpost', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xb8800400: return ('LDRSW_64_ldst_immpost', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xbc000400: return ('STR_S_ldst_immpost', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xbc400400: return ('LDR_S_ldst_immpost', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xf8000400: return ('STR_64_ldst_immpost', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xf8400400: return ('LDR_64_ldst_immpost', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xfc000400: return ('STR_D_ldst_immpost', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xfc400400: return ('LDR_D_ldst_immpost', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    return decode_UNDEFINED(d)

def decode_ldst_immpre(d):
    assert (d & 0x3b200c00) == 0x38000c00
    Rn     = (d >> 5) & 0x1F
    Rt     = (d >> 0) & 0x1F
    V      = (d >> 26) & 1
    imm9   = (d >> 12) & 0x1FF
    opc    = (d >> 22) & 3
    size   = (d >> 30) & 3
    if (d & 0xffe00c00) == 0x38000c00: return ('STRB_32_ldst_immpre', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x38400c00: return ('LDRB_32_ldst_immpre', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x38800c00: return ('LDRSB_64_ldst_immpre', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x38c00c00: return ('LDRSB_32_ldst_immpre', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x3c000c00: return ('STR_B_ldst_immpre', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x3c400c00: return ('LDR_B_ldst_immpre', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x3c800c00: return ('STR_Q_ldst_immpre', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x3cc00c00: return ('LDR_Q_ldst_immpre', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x78000c00: return ('STRH_32_ldst_immpre', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x78400c00: return ('LDRH_32_ldst_immpre', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x78800c00: return ('LDRSH_64_ldst_immpre', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x78c00c00: return ('LDRSH_32_ldst_immpre', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x7c000c00: return ('STR_H_ldst_immpre', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x7c400c00: return ('LDR_H_ldst_immpre', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xb8000c00: return ('STR_32_ldst_immpre', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xb8400c00: return ('LDR_32_ldst_immpre', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xb8800c00: return ('LDRSW_64_ldst_immpre', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xbc000c00: return ('STR_S_ldst_immpre', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xbc400c00: return ('LDR_S_ldst_immpre', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xf8000c00: return ('STR_64_ldst_immpre', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xf8400c00: return ('LDR_64_ldst_immpre', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xfc000c00: return ('STR_D_ldst_immpre', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xfc400c00: return ('LDR_D_ldst_immpre', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    return decode_UNDEFINED(d)

def decode_ldst_pac(d):
    assert (d & 0x3b200400) == 0x38200400
    M      = (d >> 23) & 1
    Rn     = (d >> 5) & 0x1F
    Rt     = (d >> 0) & 0x1F
    S      = (d >> 22) & 1
    V      = (d >> 26) & 1
    W      = (d >> 11) & 1
    imm9   = (d >> 12) & 0x1FF
    size   = (d >> 30) & 3
    if (d & 0xfba00c00) == 0xf8200400: return ('LDRAA_64_ldst_pac', {'Rn': Rn, 'Rt': Rt, 'S': S, 'V': V, 'imm9': imm9})
    if (d & 0xfba00c00) == 0xf8200c00: return ('LDRAA_64W_ldst_pac', {'Rn': Rn, 'Rt': Rt, 'S': S, 'V': V, 'imm9': imm9})
    if (d & 0xfba00c00) == 0xf8a00400: return ('LDRAB_64_ldst_pac', {'Rn': Rn, 'Rt': Rt, 'S': S, 'V': V, 'imm9': imm9})
    if (d & 0xfba00c00) == 0xf8a00c00: return ('LDRAB_64W_ldst_pac', {'Rn': Rn, 'Rt': Rt, 'S': S, 'V': V, 'imm9': imm9})
    return decode_UNDEFINED(d)

def decode_ldst_regoff(d):
    assert (d & 0x3b200c00) == 0x38200800
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    Rt     = (d >> 0) & 0x1F
    S      = (d >> 12) & 1
    V      = (d >> 26) & 1
    opc    = (d >> 22) & 3
    option = (d >> 13) & 7
    size   = (d >> 30) & 3
    if (d & 0xffe0ec00) == 0x38206800: return ('STRB_32BL_ldst_regoff', {'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S})
    if (d & 0xffe0ec00) == 0x38606800: return ('LDRB_32BL_ldst_regoff', {'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S})
    if (d & 0xffe0ec00) == 0x38a06800: return ('LDRSB_64BL_ldst_regoff', {'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S})
    if (d & 0xffe0ec00) == 0x38e06800: return ('LDRSB_32BL_ldst_regoff', {'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S})
    if (d & 0xffe0ec00) == 0x3c206800: return ('STR_BL_ldst_regoff', {'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S})
    if (d & 0xffe0ec00) == 0x3c606800: return ('LDR_BL_ldst_regoff', {'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S})
    if (d & 0xffe00c00) == 0x3ca00800: return ('STR_Q_ldst_regoff', {'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'option': option})
    if (d & 0xffe00c00) == 0x3ce00800: return ('LDR_Q_ldst_regoff', {'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'option': option})
    if (d & 0xffe00c00) == 0x78200800: return ('STRH_32_ldst_regoff', {'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'option': option})
    if (d & 0xffe00c00) == 0x78600800: return ('LDRH_32_ldst_regoff', {'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'option': option})
    if (d & 0xffe00c00) == 0x78a00800: return ('LDRSH_64_ldst_regoff', {'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'option': option})
    if (d & 0xffe00c00) == 0x78e00800: return ('LDRSH_32_ldst_regoff', {'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'option': option})
    if (d & 0xffe00c00) == 0x7c200800: return ('STR_H_ldst_regoff', {'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'option': option})
    if (d & 0xffe00c00) == 0x7c600800: return ('LDR_H_ldst_regoff', {'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'option': option})
    if (d & 0xffe00c00) == 0xb8200800: return ('STR_32_ldst_regoff', {'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'option': option})
    if (d & 0xffe00c00) == 0xb8600800: return ('LDR_32_ldst_regoff', {'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'option': option})
    if (d & 0xffe00c00) == 0xb8a00800: return ('LDRSW_64_ldst_regoff', {'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'option': option})
    if (d & 0xffe00c00) == 0xbc200800: return ('STR_S_ldst_regoff', {'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'option': option})
    if (d & 0xffe00c00) == 0xbc600800: return ('LDR_S_ldst_regoff', {'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'option': option})
    if (d & 0xffe00c00) == 0xf8200800: return ('STR_64_ldst_regoff', {'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'option': option})
    if (d & 0xffe00c00) == 0xf8600800: return ('LDR_64_ldst_regoff', {'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'option': option})
    if (d & 0xffe00c00) == 0xf8a00800: return ('PRFM_P_ldst_regoff', {'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'option': option})
    if (d & 0xffe00c00) == 0xfc200800: return ('STR_D_ldst_regoff', {'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'option': option})
    if (d & 0xffe00c00) == 0xfc600800: return ('LDR_D_ldst_regoff', {'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'option': option})
    if (d & 0xffe00c00) == 0x38200800 and (d & 0x00e000) != 0x006000: return ('STRB_32B_ldst_regoff', {'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'option': option})
    if (d & 0xffe00c00) == 0x38600800 and (d & 0x00e000) != 0x006000: return ('LDRB_32B_ldst_regoff', {'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'option': option})
    if (d & 0xffe00c00) == 0x38a00800 and (d & 0x00e000) != 0x006000: return ('LDRSB_64B_ldst_regoff', {'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'option': option})
    if (d & 0xffe00c00) == 0x38e00800 and (d & 0x00e000) != 0x006000: return ('LDRSB_32B_ldst_regoff', {'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'option': option})
    if (d & 0xffe00c00) == 0x3c200800 and (d & 0x00e000) != 0x006000: return ('STR_B_ldst_regoff', {'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'option': option})
    if (d & 0xffe00c00) == 0x3c600800 and (d & 0x00e000) != 0x006000: return ('LDR_B_ldst_regoff', {'Rm': Rm, 'Rn': Rn, 'Rt': Rt, 'S': S, 'option': option})
    return decode_UNDEFINED(d)

def decode_ldst_unpriv(d):
    assert (d & 0x3b200c00) == 0x38000800
    Rn     = (d >> 5) & 0x1F
    Rt     = (d >> 0) & 0x1F
    V      = (d >> 26) & 1
    imm9   = (d >> 12) & 0x1FF
    opc    = (d >> 22) & 3
    size   = (d >> 30) & 3
    if (d & 0xffe00c00) == 0x38000800: return ('STTRB_32_ldst_unpriv', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x38400800: return ('LDTRB_32_ldst_unpriv', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x38800800: return ('LDTRSB_64_ldst_unpriv', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x38c00800: return ('LDTRSB_32_ldst_unpriv', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x78000800: return ('STTRH_32_ldst_unpriv', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x78400800: return ('LDTRH_32_ldst_unpriv', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x78800800: return ('LDTRSH_64_ldst_unpriv', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x78c00800: return ('LDTRSH_32_ldst_unpriv', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xb8000800: return ('STTR_32_ldst_unpriv', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xb8400800: return ('LDTR_32_ldst_unpriv', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xb8800800: return ('LDTRSW_64_ldst_unpriv', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xf8000800: return ('STTR_64_ldst_unpriv', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xf8400800: return ('LDTR_64_ldst_unpriv', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    return decode_UNDEFINED(d)

def decode_ldst_unscaled(d):
    assert (d & 0x3b200c00) == 0x38000000
    Rn     = (d >> 5) & 0x1F
    Rt     = (d >> 0) & 0x1F
    V      = (d >> 26) & 1
    imm9   = (d >> 12) & 0x1FF
    opc    = (d >> 22) & 3
    size   = (d >> 30) & 3
    if (d & 0xffe00c00) == 0x38000000: return ('STURB_32_ldst_unscaled', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x38400000: return ('LDURB_32_ldst_unscaled', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x38800000: return ('LDURSB_64_ldst_unscaled', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x38c00000: return ('LDURSB_32_ldst_unscaled', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x3c000000: return ('STUR_B_ldst_unscaled', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x3c400000: return ('LDUR_B_ldst_unscaled', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x3c800000: return ('STUR_Q_ldst_unscaled', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x3cc00000: return ('LDUR_Q_ldst_unscaled', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x78000000: return ('STURH_32_ldst_unscaled', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x78400000: return ('LDURH_32_ldst_unscaled', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x78800000: return ('LDURSH_64_ldst_unscaled', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x78c00000: return ('LDURSH_32_ldst_unscaled', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x7c000000: return ('STUR_H_ldst_unscaled', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0x7c400000: return ('LDUR_H_ldst_unscaled', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xb8000000: return ('STUR_32_ldst_unscaled', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xb8400000: return ('LDUR_32_ldst_unscaled', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xb8800000: return ('LDURSW_64_ldst_unscaled', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xbc000000: return ('STUR_S_ldst_unscaled', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xbc400000: return ('LDUR_S_ldst_unscaled', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xf8000000: return ('STUR_64_ldst_unscaled', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xf8400000: return ('LDUR_64_ldst_unscaled', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xf8800000: return ('PRFUM_P_ldst_unscaled', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xfc000000: return ('STUR_D_ldst_unscaled', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    if (d & 0xffe00c00) == 0xfc400000: return ('LDUR_D_ldst_unscaled', {'Rn': Rn, 'Rt': Rt, 'imm9': imm9})
    return decode_UNDEFINED(d)

def decode_ldst_pos(d):
    assert (d & 0x3b000000) == 0x39000000
    Rn     = (d >> 5) & 0x1F
    Rt     = (d >> 0) & 0x1F
    V      = (d >> 26) & 1
    imm12  = (d >> 10) & 0xFFF
    opc    = (d >> 22) & 3
    size   = (d >> 30) & 3
    if (d & 0xffc00000) == 0x39000000: return ('STRB_32_ldst_pos', {'Rn': Rn, 'Rt': Rt, 'imm12': imm12})
    if (d & 0xffc00000) == 0x39400000: return ('LDRB_32_ldst_pos', {'Rn': Rn, 'Rt': Rt, 'imm12': imm12})
    if (d & 0xffc00000) == 0x39800000: return ('LDRSB_64_ldst_pos', {'Rn': Rn, 'Rt': Rt, 'imm12': imm12})
    if (d & 0xffc00000) == 0x39c00000: return ('LDRSB_32_ldst_pos', {'Rn': Rn, 'Rt': Rt, 'imm12': imm12})
    if (d & 0xffc00000) == 0x3d000000: return ('STR_B_ldst_pos', {'Rn': Rn, 'Rt': Rt, 'imm12': imm12})
    if (d & 0xffc00000) == 0x3d400000: return ('LDR_B_ldst_pos', {'Rn': Rn, 'Rt': Rt, 'imm12': imm12})
    if (d & 0xffc00000) == 0x3d800000: return ('STR_Q_ldst_pos', {'Rn': Rn, 'Rt': Rt, 'imm12': imm12})
    if (d & 0xffc00000) == 0x3dc00000: return ('LDR_Q_ldst_pos', {'Rn': Rn, 'Rt': Rt, 'imm12': imm12})
    if (d & 0xffc00000) == 0x79000000: return ('STRH_32_ldst_pos', {'Rn': Rn, 'Rt': Rt, 'imm12': imm12})
    if (d & 0xffc00000) == 0x79400000: return ('LDRH_32_ldst_pos', {'Rn': Rn, 'Rt': Rt, 'imm12': imm12})
    if (d & 0xffc00000) == 0x79800000: return ('LDRSH_64_ldst_pos', {'Rn': Rn, 'Rt': Rt, 'imm12': imm12})
    if (d & 0xffc00000) == 0x79c00000: return ('LDRSH_32_ldst_pos', {'Rn': Rn, 'Rt': Rt, 'imm12': imm12})
    if (d & 0xffc00000) == 0x7d000000: return ('STR_H_ldst_pos', {'Rn': Rn, 'Rt': Rt, 'imm12': imm12})
    if (d & 0xffc00000) == 0x7d400000: return ('LDR_H_ldst_pos', {'Rn': Rn, 'Rt': Rt, 'imm12': imm12})
    if (d & 0xffc00000) == 0xb9000000: return ('STR_32_ldst_pos', {'Rn': Rn, 'Rt': Rt, 'imm12': imm12})
    if (d & 0xffc00000) == 0xb9400000: return ('LDR_32_ldst_pos', {'Rn': Rn, 'Rt': Rt, 'imm12': imm12})
    if (d & 0xffc00000) == 0xb9800000: return ('LDRSW_64_ldst_pos', {'Rn': Rn, 'Rt': Rt, 'imm12': imm12})
    if (d & 0xffc00000) == 0xbd000000: return ('STR_S_ldst_pos', {'Rn': Rn, 'Rt': Rt, 'imm12': imm12})
    if (d & 0xffc00000) == 0xbd400000: return ('LDR_S_ldst_pos', {'Rn': Rn, 'Rt': Rt, 'imm12': imm12})
    if (d & 0xffc00000) == 0xf9000000: return ('STR_64_ldst_pos', {'Rn': Rn, 'Rt': Rt, 'imm12': imm12})
    if (d & 0xffc00000) == 0xf9400000: return ('LDR_64_ldst_pos', {'Rn': Rn, 'Rt': Rt, 'imm12': imm12})
    if (d & 0xffc00000) == 0xf9800000: return ('PRFM_P_ldst_pos', {'Rn': Rn, 'Rt': Rt, 'imm12': imm12})
    if (d & 0xffc00000) == 0xfd000000: return ('STR_D_ldst_pos', {'Rn': Rn, 'Rt': Rt, 'imm12': imm12})
    if (d & 0xffc00000) == 0xfd400000: return ('LDR_D_ldst_pos', {'Rn': Rn, 'Rt': Rt, 'imm12': imm12})
    return decode_UNDEFINED(d)

def decode_ldstpair_off(d):
    assert (d & 0x3b800000) == 0x29000000
    L      = (d >> 22) & 1
    Rn     = (d >> 5) & 0x1F
    Rt     = (d >> 0) & 0x1F
    Rt2    = (d >> 10) & 0x1F
    V      = (d >> 26) & 1
    imm7   = (d >> 15) & 0x7F
    opc    = (d >> 30) & 3
    if (d & 0xffc00000) == 0x29000000: return ('STP_32_ldstpair_off', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0x29400000: return ('LDP_32_ldstpair_off', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0x2d000000: return ('STP_S_ldstpair_off', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0x2d400000: return ('LDP_S_ldstpair_off', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0x69400000: return ('LDPSW_64_ldstpair_off', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0x6d000000: return ('STP_D_ldstpair_off', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0x6d400000: return ('LDP_D_ldstpair_off', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0xa9000000: return ('STP_64_ldstpair_off', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0xa9400000: return ('LDP_64_ldstpair_off', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0xad000000: return ('STP_Q_ldstpair_off', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0xad400000: return ('LDP_Q_ldstpair_off', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    return decode_UNDEFINED(d)

def decode_ldstpair_post(d):
    assert (d & 0x3b800000) == 0x28800000
    L      = (d >> 22) & 1
    Rn     = (d >> 5) & 0x1F
    Rt     = (d >> 0) & 0x1F
    Rt2    = (d >> 10) & 0x1F
    V      = (d >> 26) & 1
    imm7   = (d >> 15) & 0x7F
    opc    = (d >> 30) & 3
    if (d & 0xffc00000) == 0x28800000: return ('STP_32_ldstpair_post', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0x28c00000: return ('LDP_32_ldstpair_post', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0x2c800000: return ('STP_S_ldstpair_post', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0x2cc00000: return ('LDP_S_ldstpair_post', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0x68c00000: return ('LDPSW_64_ldstpair_post', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0x6c800000: return ('STP_D_ldstpair_post', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0x6cc00000: return ('LDP_D_ldstpair_post', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0xa8800000: return ('STP_64_ldstpair_post', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0xa8c00000: return ('LDP_64_ldstpair_post', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0xac800000: return ('STP_Q_ldstpair_post', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0xacc00000: return ('LDP_Q_ldstpair_post', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    return decode_UNDEFINED(d)

def decode_ldstpair_pre(d):
    assert (d & 0x3b800000) == 0x29800000
    L      = (d >> 22) & 1
    Rn     = (d >> 5) & 0x1F
    Rt     = (d >> 0) & 0x1F
    Rt2    = (d >> 10) & 0x1F
    V      = (d >> 26) & 1
    imm7   = (d >> 15) & 0x7F
    opc    = (d >> 30) & 3
    if (d & 0xffc00000) == 0x29800000: return ('STP_32_ldstpair_pre', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0x29c00000: return ('LDP_32_ldstpair_pre', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0x2d800000: return ('STP_S_ldstpair_pre', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0x2dc00000: return ('LDP_S_ldstpair_pre', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0x69c00000: return ('LDPSW_64_ldstpair_pre', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0x6d800000: return ('STP_D_ldstpair_pre', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0x6dc00000: return ('LDP_D_ldstpair_pre', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0xa9800000: return ('STP_64_ldstpair_pre', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0xa9c00000: return ('LDP_64_ldstpair_pre', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0xad800000: return ('STP_Q_ldstpair_pre', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    if (d & 0xffc00000) == 0xadc00000: return ('LDP_Q_ldstpair_pre', {'Rn': Rn, 'Rt': Rt, 'Rt2': Rt2, 'imm7': imm7})
    return decode_UNDEFINED(d)

def decode_addsub_imm(d):
    assert (d & 0x1f000000) == 0x11000000
    Rd     = (d >> 0) & 0x1F
    Rn     = (d >> 5) & 0x1F
    S      = (d >> 29) & 1
    imm12  = (d >> 10) & 0xFFF
    op     = (d >> 30) & 1
    sf     = (d >> 31) & 1
    shift  = (d >> 22) & 3
    if (d & 0xff000000) == 0x11000000: return ('ADD_32_addsub_imm', {'Rd': Rd, 'Rn': Rn, 'imm12': imm12, 'shift': shift})
    if (d & 0xff000000) == 0x31000000: return ('ADDS_32S_addsub_imm', {'Rd': Rd, 'Rn': Rn, 'imm12': imm12, 'shift': shift})
    if (d & 0xff000000) == 0x51000000: return ('SUB_32_addsub_imm', {'Rd': Rd, 'Rn': Rn, 'imm12': imm12, 'shift': shift})
    if (d & 0xff000000) == 0x71000000: return ('SUBS_32S_addsub_imm', {'Rd': Rd, 'Rn': Rn, 'imm12': imm12, 'shift': shift})
    if (d & 0xff000000) == 0x91000000: return ('ADD_64_addsub_imm', {'Rd': Rd, 'Rn': Rn, 'imm12': imm12, 'shift': shift})
    if (d & 0xff000000) == 0xb1000000: return ('ADDS_64S_addsub_imm', {'Rd': Rd, 'Rn': Rn, 'imm12': imm12, 'shift': shift})
    if (d & 0xff000000) == 0xd1000000: return ('SUB_64_addsub_imm', {'Rd': Rd, 'Rn': Rn, 'imm12': imm12, 'shift': shift})
    if (d & 0xff000000) == 0xf1000000: return ('SUBS_64S_addsub_imm', {'Rd': Rd, 'Rn': Rn, 'imm12': imm12, 'shift': shift})
    return decode_UNDEFINED(d)

def decode_bitfield(d):
    assert (d & 0x1f800000) == 0x13000000
    N      = (d >> 22) & 1
    Rd     = (d >> 0) & 0x1F
    Rn     = (d >> 5) & 0x1F
    immr   = (d >> 16) & 0x3F
    imms   = (d >> 10) & 0x3F
    opc    = (d >> 29) & 3
    sf     = (d >> 31) & 1
    if (d & 0xffc00000) == 0x13000000: return ('SBFM_32M_bitfield', {'Rd': Rd, 'Rn': Rn, 'immr': immr, 'imms': imms})
    if (d & 0xffc00000) == 0x33000000: return ('BFM_32M_bitfield', {'Rd': Rd, 'Rn': Rn, 'immr': immr, 'imms': imms})
    if (d & 0xffc00000) == 0x53000000: return ('UBFM_32M_bitfield', {'Rd': Rd, 'Rn': Rn, 'immr': immr, 'imms': imms})
    if (d & 0xffc00000) == 0x93400000: return ('SBFM_64M_bitfield', {'Rd': Rd, 'Rn': Rn, 'immr': immr, 'imms': imms})
    if (d & 0xffc00000) == 0xb3400000: return ('BFM_64M_bitfield', {'Rd': Rd, 'Rn': Rn, 'immr': immr, 'imms': imms})
    if (d & 0xffc00000) == 0xd3400000: return ('UBFM_64M_bitfield', {'Rd': Rd, 'Rn': Rn, 'immr': immr, 'imms': imms})
    return decode_UNDEFINED(d)

def decode_extract(d):
    assert (d & 0x1f800000) == 0x13800000
    N      = (d >> 22) & 1
    Rd     = (d >> 0) & 0x1F
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    imms   = (d >> 10) & 0x3F
    o0     = (d >> 21) & 1
    op21   = (d >> 29) & 3
    sf     = (d >> 31) & 1
    if (d & 0xffe08000) == 0x13800000: return ('EXTR_32_extract', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imms': imms})
    if (d & 0xffe00000) == 0x93c00000: return ('EXTR_64_extract', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imms': imms})
    return decode_UNDEFINED(d)

def decode_log_imm(d):
    assert (d & 0x1f800000) == 0x12000000
    N      = (d >> 22) & 1
    Rd     = (d >> 0) & 0x1F
    Rn     = (d >> 5) & 0x1F
    immr   = (d >> 16) & 0x3F
    imms   = (d >> 10) & 0x3F
    opc    = (d >> 29) & 3
    sf     = (d >> 31) & 1
    if (d & 0xffc00000) == 0x12000000: return ('AND_32_log_imm', {'Rd': Rd, 'Rn': Rn, 'immr': immr, 'imms': imms})
    if (d & 0xffc00000) == 0x32000000: return ('ORR_32_log_imm', {'Rd': Rd, 'Rn': Rn, 'immr': immr, 'imms': imms})
    if (d & 0xffc00000) == 0x52000000: return ('EOR_32_log_imm', {'Rd': Rd, 'Rn': Rn, 'immr': immr, 'imms': imms})
    if (d & 0xffc00000) == 0x72000000: return ('ANDS_32S_log_imm', {'Rd': Rd, 'Rn': Rn, 'immr': immr, 'imms': imms})
    if (d & 0xff800000) == 0x92000000: return ('AND_64_log_imm', {'N': N, 'Rd': Rd, 'Rn': Rn, 'immr': immr, 'imms': imms})
    if (d & 0xff800000) == 0xb2000000: return ('ORR_64_log_imm', {'N': N, 'Rd': Rd, 'Rn': Rn, 'immr': immr, 'imms': imms})
    if (d & 0xff800000) == 0xd2000000: return ('EOR_64_log_imm', {'N': N, 'Rd': Rd, 'Rn': Rn, 'immr': immr, 'imms': imms})
    if (d & 0xff800000) == 0xf2000000: return ('ANDS_64S_log_imm', {'N': N, 'Rd': Rd, 'Rn': Rn, 'immr': immr, 'imms': imms})
    return decode_UNDEFINED(d)

def decode_movewide(d):
    assert (d & 0x1f800000) == 0x12800000
    Rd     = (d >> 0) & 0x1F
    hw     = (d >> 21) & 3
    imm16  = (d >> 5) & 0xFFFF
    opc    = (d >> 29) & 3
    sf     = (d >> 31) & 1
    if (d & 0xff800000) == 0x12800000: return ('MOVN_32_movewide', {'Rd': Rd, 'hw': hw, 'imm16': imm16})
    if (d & 0xff800000) == 0x52800000: return ('MOVZ_32_movewide', {'Rd': Rd, 'hw': hw, 'imm16': imm16})
    if (d & 0xff800000) == 0x72800000: return ('MOVK_32_movewide', {'Rd': Rd, 'hw': hw, 'imm16': imm16})
    if (d & 0xff800000) == 0x92800000: return ('MOVN_64_movewide', {'Rd': Rd, 'hw': hw, 'imm16': imm16})
    if (d & 0xff800000) == 0xd2800000: return ('MOVZ_64_movewide', {'Rd': Rd, 'hw': hw, 'imm16': imm16})
    if (d & 0xff800000) == 0xf2800000: return ('MOVK_64_movewide', {'Rd': Rd, 'hw': hw, 'imm16': imm16})
    return decode_UNDEFINED(d)

def decode_pcreladdr(d):
    assert (d & 0x1f000000) == 0x10000000
    Rd     = (d >> 0) & 0x1F
    immhi  = (d >> 5) & 0x7FFFF
    immlo  = (d >> 29) & 3
    op     = (d >> 31) & 1
    if (d & 0x9f000000) == 0x10000000: return ('ADR_only_pcreladdr', {'Rd': Rd, 'immhi': immhi, 'immlo': immlo})
    if (d & 0x9f000000) == 0x90000000: return ('ADRP_only_pcreladdr', {'Rd': Rd, 'immhi': immhi, 'immlo': immlo})
    return decode_UNDEFINED(d)

def decode_addsub_ext(d):
    assert (d & 0x1f200000) == 0x0b200000
    Rd     = (d >> 0) & 0x1F
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    S      = (d >> 29) & 1
    imm3   = (d >> 10) & 7
    op     = (d >> 30) & 1
    opt    = (d >> 22) & 3
    option = (d >> 13) & 7
    sf     = (d >> 31) & 1
    if (d & 0xffe00000) == 0x0b200000: return ('ADD_32_addsub_ext', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm3': imm3, 'option': option})
    if (d & 0xffe00000) == 0x2b200000: return ('ADDS_32S_addsub_ext', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm3': imm3, 'option': option})
    if (d & 0xffe00000) == 0x4b200000: return ('SUB_32_addsub_ext', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm3': imm3, 'option': option})
    if (d & 0xffe00000) == 0x6b200000: return ('SUBS_32S_addsub_ext', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm3': imm3, 'option': option})
    if (d & 0xffe00000) == 0x8b200000: return ('ADD_64_addsub_ext', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm3': imm3, 'option': option})
    if (d & 0xffe00000) == 0xab200000: return ('ADDS_64S_addsub_ext', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm3': imm3, 'option': option})
    if (d & 0xffe00000) == 0xcb200000: return ('SUB_64_addsub_ext', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm3': imm3, 'option': option})
    if (d & 0xffe00000) == 0xeb200000: return ('SUBS_64S_addsub_ext', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm3': imm3, 'option': option})
    return decode_UNDEFINED(d)

def decode_addsub_shift(d):
    assert (d & 0x1f200000) == 0x0b000000
    Rd     = (d >> 0) & 0x1F
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    S      = (d >> 29) & 1
    imm6   = (d >> 10) & 0x3F
    op     = (d >> 30) & 1
    sf     = (d >> 31) & 1
    shift  = (d >> 22) & 3
    if (d & 0xff200000) == 0x0b000000: return ('ADD_32_addsub_shift', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm6': imm6, 'shift': shift})
    if (d & 0xff200000) == 0x2b000000: return ('ADDS_32_addsub_shift', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm6': imm6, 'shift': shift})
    if (d & 0xff200000) == 0x4b000000: return ('SUB_32_addsub_shift', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm6': imm6, 'shift': shift})
    if (d & 0xff200000) == 0x6b000000: return ('SUBS_32_addsub_shift', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm6': imm6, 'shift': shift})
    if (d & 0xff200000) == 0x8b000000: return ('ADD_64_addsub_shift', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm6': imm6, 'shift': shift})
    if (d & 0xff200000) == 0xab000000: return ('ADDS_64_addsub_shift', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm6': imm6, 'shift': shift})
    if (d & 0xff200000) == 0xcb000000: return ('SUB_64_addsub_shift', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm6': imm6, 'shift': shift})
    if (d & 0xff200000) == 0xeb000000: return ('SUBS_64_addsub_shift', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm6': imm6, 'shift': shift})
    return decode_UNDEFINED(d)

def decode_addsub_carry(d):
    assert (d & 0x1fe00000) == 0x1a000000
    Rd     = (d >> 0) & 0x1F
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    S      = (d >> 29) & 1
    op     = (d >> 30) & 1
    opcode2 = (d >> 10) & 0x3F
    sf     = (d >> 31) & 1
    if (d & 0xffe0fc00) == 0x1a000000: return ('ADC_32_addsub_carry', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x3a000000: return ('ADCS_32_addsub_carry', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x5a000000: return ('SBC_32_addsub_carry', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x7a000000: return ('SBCS_32_addsub_carry', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x9a000000: return ('ADC_64_addsub_carry', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0xba000000: return ('ADCS_64_addsub_carry', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0xda000000: return ('SBC_64_addsub_carry', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0xfa000000: return ('SBCS_64_addsub_carry', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    return decode_UNDEFINED(d)

def decode_condcmp_imm(d):
    assert (d & 0x1fe00800) == 0x1a400800
    Rn     = (d >> 5) & 0x1F
    S      = (d >> 29) & 1
    cond   = (d >> 12) & 0xF
    imm5   = (d >> 16) & 0x1F
    nzcv   = (d >> 0) & 0xF
    o2     = (d >> 10) & 1
    o3     = (d >> 4) & 1
    op     = (d >> 30) & 1
    sf     = (d >> 31) & 1
    if (d & 0xffe00c10) == 0x3a400800: return ('CCMN_32_condcmp_imm', {'Rn': Rn, 'cond': cond, 'imm5': imm5, 'nzcv': nzcv})
    if (d & 0xffe00c10) == 0x7a400800: return ('CCMP_32_condcmp_imm', {'Rn': Rn, 'cond': cond, 'imm5': imm5, 'nzcv': nzcv})
    if (d & 0xffe00c10) == 0xba400800: return ('CCMN_64_condcmp_imm', {'Rn': Rn, 'cond': cond, 'imm5': imm5, 'nzcv': nzcv})
    if (d & 0xffe00c10) == 0xfa400800: return ('CCMP_64_condcmp_imm', {'Rn': Rn, 'cond': cond, 'imm5': imm5, 'nzcv': nzcv})
    return decode_UNDEFINED(d)

def decode_condcmp_reg(d):
    assert (d & 0x1fe00800) == 0x1a400000
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    S      = (d >> 29) & 1
    cond   = (d >> 12) & 0xF
    nzcv   = (d >> 0) & 0xF
    o2     = (d >> 10) & 1
    o3     = (d >> 4) & 1
    op     = (d >> 30) & 1
    sf     = (d >> 31) & 1
    if (d & 0xffe00c10) == 0x3a400000: return ('CCMN_32_condcmp_reg', {'Rm': Rm, 'Rn': Rn, 'cond': cond, 'nzcv': nzcv})
    if (d & 0xffe00c10) == 0x7a400000: return ('CCMP_32_condcmp_reg', {'Rm': Rm, 'Rn': Rn, 'cond': cond, 'nzcv': nzcv})
    if (d & 0xffe00c10) == 0xba400000: return ('CCMN_64_condcmp_reg', {'Rm': Rm, 'Rn': Rn, 'cond': cond, 'nzcv': nzcv})
    if (d & 0xffe00c10) == 0xfa400000: return ('CCMP_64_condcmp_reg', {'Rm': Rm, 'Rn': Rn, 'cond': cond, 'nzcv': nzcv})
    return decode_UNDEFINED(d)

def decode_condsel(d):
    assert (d & 0x1fe00000) == 0x1a800000
    Rd     = (d >> 0) & 0x1F
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    S      = (d >> 29) & 1
    cond   = (d >> 12) & 0xF
    op     = (d >> 30) & 1
    op2    = (d >> 10) & 3
    sf     = (d >> 31) & 1
    if (d & 0xffe00c00) == 0x1a800000: return ('CSEL_32_condsel', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'cond': cond})
    if (d & 0xffe00c00) == 0x1a800400: return ('CSINC_32_condsel', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'cond': cond})
    if (d & 0xffe00c00) == 0x5a800000: return ('CSINV_32_condsel', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'cond': cond})
    if (d & 0xffe00c00) == 0x5a800400: return ('CSNEG_32_condsel', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'cond': cond})
    if (d & 0xffe00c00) == 0x9a800000: return ('CSEL_64_condsel', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'cond': cond})
    if (d & 0xffe00c00) == 0x9a800400: return ('CSINC_64_condsel', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'cond': cond})
    if (d & 0xffe00c00) == 0xda800000: return ('CSINV_64_condsel', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'cond': cond})
    if (d & 0xffe00c00) == 0xda800400: return ('CSNEG_64_condsel', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'cond': cond})
    return decode_UNDEFINED(d)

def decode_dp_1src(d):
    assert (d & 0x5fe00000) == 0x5ac00000
    Rd     = (d >> 0) & 0x1F
    Rn     = (d >> 5) & 0x1F
    S      = (d >> 29) & 1
    opcode = (d >> 10) & 0x3F
    opcode2 = (d >> 16) & 0x1F
    sf     = (d >> 31) & 1
    if (d & 0xffffffe0) == 0xdac123e0: return ('PACIZA_64Z_dp_1src', {'Rd': Rd})
    if (d & 0xffffffe0) == 0xdac127e0: return ('PACIZB_64Z_dp_1src', {'Rd': Rd})
    if (d & 0xffffffe0) == 0xdac12be0: return ('PACDZA_64Z_dp_1src', {'Rd': Rd})
    if (d & 0xffffffe0) == 0xdac12fe0: return ('PACDZB_64Z_dp_1src', {'Rd': Rd})
    if (d & 0xffffffe0) == 0xdac133e0: return ('AUTIZA_64Z_dp_1src', {'Rd': Rd})
    if (d & 0xffffffe0) == 0xdac137e0: return ('AUTIZB_64Z_dp_1src', {'Rd': Rd})
    if (d & 0xffffffe0) == 0xdac13be0: return ('AUTDZA_64Z_dp_1src', {'Rd': Rd})
    if (d & 0xffffffe0) == 0xdac13fe0: return ('AUTDZB_64Z_dp_1src', {'Rd': Rd})
    if (d & 0xffffffe0) == 0xdac143e0: return ('XPACI_64Z_dp_1src', {'Rd': Rd})
    if (d & 0xffffffe0) == 0xdac147e0: return ('XPACD_64Z_dp_1src', {'Rd': Rd})
    if (d & 0xfffffc00) == 0x5ac00000: return ('RBIT_32_dp_1src', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x5ac00400: return ('REV16_32_dp_1src', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x5ac00800: return ('REV_32_dp_1src', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x5ac01000: return ('CLZ_32_dp_1src', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x5ac01400: return ('CLS_32_dp_1src', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0xdac00000: return ('RBIT_64_dp_1src', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0xdac00400: return ('REV16_64_dp_1src', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0xdac00800: return ('REV32_64_dp_1src', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0xdac00c00: return ('REV_64_dp_1src', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0xdac01000: return ('CLZ_64_dp_1src', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0xdac01400: return ('CLS_64_dp_1src', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0xdac10000: return ('PACIA_64P_dp_1src', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0xdac10400: return ('PACIB_64P_dp_1src', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0xdac10800: return ('PACDA_64P_dp_1src', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0xdac10c00: return ('PACDB_64P_dp_1src', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0xdac11000: return ('AUTIA_64P_dp_1src', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0xdac11400: return ('AUTIB_64P_dp_1src', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0xdac11800: return ('AUTDA_64P_dp_1src', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0xdac11c00: return ('AUTDB_64P_dp_1src', {'Rd': Rd, 'Rn': Rn})
    return decode_UNDEFINED(d)

def decode_dp_2src(d):
    assert (d & 0x5fe00000) == 0x1ac00000
    Rd     = (d >> 0) & 0x1F
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    S      = (d >> 29) & 1
    opcode = (d >> 10) & 0x3F
    sf     = (d >> 31) & 1
    if (d & 0xffe0fc00) == 0x1ac00800: return ('UDIV_32_dp_2src', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1ac00c00: return ('SDIV_32_dp_2src', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1ac02000: return ('LSLV_32_dp_2src', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1ac02400: return ('LSRV_32_dp_2src', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1ac02800: return ('ASRV_32_dp_2src', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1ac02c00: return ('RORV_32_dp_2src', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1ac04000: return ('CRC32B_32C_dp_2src', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1ac04400: return ('CRC32H_32C_dp_2src', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1ac04800: return ('CRC32W_32C_dp_2src', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1ac05000: return ('CRC32CB_32C_dp_2src', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1ac05400: return ('CRC32CH_32C_dp_2src', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1ac05800: return ('CRC32CW_32C_dp_2src', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x9ac00800: return ('UDIV_64_dp_2src', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x9ac00c00: return ('SDIV_64_dp_2src', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x9ac02000: return ('LSLV_64_dp_2src', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x9ac02400: return ('LSRV_64_dp_2src', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x9ac02800: return ('ASRV_64_dp_2src', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x9ac02c00: return ('RORV_64_dp_2src', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x9ac03000: return ('PACGA_64P_dp_2src', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x9ac04c00: return ('CRC32X_64C_dp_2src', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x9ac05c00: return ('CRC32CX_64C_dp_2src', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    return decode_UNDEFINED(d)

def decode_dp_3src(d):
    assert (d & 0x1f000000) == 0x1b000000
    Ra     = (d >> 10) & 0x1F
    Rd     = (d >> 0) & 0x1F
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    o0     = (d >> 15) & 1
    op31   = (d >> 21) & 7
    op54   = (d >> 29) & 3
    sf     = (d >> 31) & 1
    if (d & 0xffe08000) == 0x1b000000: return ('MADD_32A_dp_3src', {'Ra': Ra, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe08000) == 0x1b008000: return ('MSUB_32A_dp_3src', {'Ra': Ra, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe08000) == 0x9b000000: return ('MADD_64A_dp_3src', {'Ra': Ra, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe08000) == 0x9b008000: return ('MSUB_64A_dp_3src', {'Ra': Ra, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe08000) == 0x9b200000: return ('SMADDL_64WA_dp_3src', {'Ra': Ra, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe08000) == 0x9b208000: return ('SMSUBL_64WA_dp_3src', {'Ra': Ra, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe08000) == 0x9b400000: return ('SMULH_64_dp_3src', {'Ra': Ra, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe08000) == 0x9ba00000: return ('UMADDL_64WA_dp_3src', {'Ra': Ra, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe08000) == 0x9ba08000: return ('UMSUBL_64WA_dp_3src', {'Ra': Ra, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe08000) == 0x9bc00000: return ('UMULH_64_dp_3src', {'Ra': Ra, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    return decode_UNDEFINED(d)

def decode_log_shift(d):
    assert (d & 0x1f000000) == 0x0a000000
    N      = (d >> 21) & 1
    Rd     = (d >> 0) & 0x1F
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    imm6   = (d >> 10) & 0x3F
    opc    = (d >> 29) & 3
    sf     = (d >> 31) & 1
    shift  = (d >> 22) & 3
    if (d & 0xff200000) == 0x0a000000: return ('AND_32_log_shift', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm6': imm6, 'shift': shift})
    if (d & 0xff200000) == 0x0a200000: return ('BIC_32_log_shift', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm6': imm6, 'shift': shift})
    if (d & 0xff200000) == 0x2a000000: return ('ORR_32_log_shift', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm6': imm6, 'shift': shift})
    if (d & 0xff200000) == 0x2a200000: return ('ORN_32_log_shift', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm6': imm6, 'shift': shift})
    if (d & 0xff200000) == 0x4a000000: return ('EOR_32_log_shift', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm6': imm6, 'shift': shift})
    if (d & 0xff200000) == 0x4a200000: return ('EON_32_log_shift', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm6': imm6, 'shift': shift})
    if (d & 0xff200000) == 0x6a000000: return ('ANDS_32_log_shift', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm6': imm6, 'shift': shift})
    if (d & 0xff200000) == 0x6a200000: return ('BICS_32_log_shift', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm6': imm6, 'shift': shift})
    if (d & 0xff200000) == 0x8a000000: return ('AND_64_log_shift', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm6': imm6, 'shift': shift})
    if (d & 0xff200000) == 0x8a200000: return ('BIC_64_log_shift', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm6': imm6, 'shift': shift})
    if (d & 0xff200000) == 0xaa000000: return ('ORR_64_log_shift', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm6': imm6, 'shift': shift})
    if (d & 0xff200000) == 0xaa200000: return ('ORN_64_log_shift', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm6': imm6, 'shift': shift})
    if (d & 0xff200000) == 0xca000000: return ('EOR_64_log_shift', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm6': imm6, 'shift': shift})
    if (d & 0xff200000) == 0xca200000: return ('EON_64_log_shift', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm6': imm6, 'shift': shift})
    if (d & 0xff200000) == 0xea000000: return ('ANDS_64_log_shift', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm6': imm6, 'shift': shift})
    if (d & 0xff200000) == 0xea200000: return ('BICS_64_log_shift', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm6': imm6, 'shift': shift})
    return decode_UNDEFINED(d)

def decode_asimdall(d):
    assert (d & 0x9f3e0c00) == 0x0e300800
    Q      = (d >> 30) & 1
    Rd     = (d >> 0) & 0x1F
    Rn     = (d >> 5) & 0x1F
    U      = (d >> 29) & 1
    opcode = (d >> 12) & 0x1F
    size   = (d >> 22) & 3
    if (d & 0xbffffc00) == 0x0e30c800: return ('FMAXNMV_asimdall_only_H', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbffffc00) == 0x0e30f800: return ('FMAXV_asimdall_only_H', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbffffc00) == 0x0eb0c800: return ('FMINNMV_asimdall_only_H', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbffffc00) == 0x0eb0f800: return ('FMINV_asimdall_only_H', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbfbffc00) == 0x2e30c800: return ('FMAXNMV_asimdall_only_SD', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x2e30f800: return ('FMAXV_asimdall_only_SD', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x2eb0c800: return ('FMINNMV_asimdall_only_SD', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x2eb0f800: return ('FMINV_asimdall_only_SD', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x0e303800: return ('SADDLV_asimdall_only', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x0e30a800: return ('SMAXV_asimdall_only', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x0e31a800: return ('SMINV_asimdall_only', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x0e31b800: return ('ADDV_asimdall_only', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x2e303800: return ('UADDLV_asimdall_only', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x2e30a800: return ('UMAXV_asimdall_only', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x2e31a800: return ('UMINV_asimdall_only', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    return decode_UNDEFINED(d)

def decode_asimdins(d):
    assert (d & 0x9fe08400) == 0x0e000400
    Q      = (d >> 30) & 1
    Rd     = (d >> 0) & 0x1F
    Rn     = (d >> 5) & 0x1F
    imm4   = (d >> 11) & 0xF
    imm5   = (d >> 16) & 0x1F
    op     = (d >> 29) & 1
    if (d & 0xffeffc00) == 0x4e083c00: return ('UMOV_asimdins_X_x', {'Rd': Rd, 'Rn': Rn, 'imm5': imm5})
    if (d & 0xffe0fc00) == 0x0e002c00: return ('SMOV_asimdins_W_w', {'Rd': Rd, 'Rn': Rn, 'imm5': imm5})
    if (d & 0xffe0fc00) == 0x0e003c00: return ('UMOV_asimdins_W_w', {'Rd': Rd, 'Rn': Rn, 'imm5': imm5})
    if (d & 0xffe0fc00) == 0x4e001c00: return ('INS_asimdins_IR_r', {'Rd': Rd, 'Rn': Rn, 'imm5': imm5})
    if (d & 0xffe0fc00) == 0x4e002c00: return ('SMOV_asimdins_X_x', {'Rd': Rd, 'Rn': Rn, 'imm5': imm5})
    if (d & 0xbfe0fc00) == 0x0e000400: return ('DUP_asimdins_DV_v', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'imm5': imm5})
    if (d & 0xbfe0fc00) == 0x0e000c00: return ('DUP_asimdins_DR_r', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'imm5': imm5})
    if (d & 0xffe08400) == 0x6e000400: return ('INS_asimdins_IV_v', {'Rd': Rd, 'Rn': Rn, 'imm4': imm4, 'imm5': imm5})
    return decode_UNDEFINED(d)

def decode_asimdext(d):
    assert (d & 0xbf208400) == 0x2e000000
    Q      = (d >> 30) & 1
    Rd     = (d >> 0) & 0x1F
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    imm4   = (d >> 11) & 0xF
    op2    = (d >> 22) & 3
    if (d & 0xbfe08400) == 0x2e000000: return ('EXT_asimdext_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm4': imm4})
    return decode_UNDEFINED(d)

def decode_asimdimm(v):
    assert (v & 0x9ff80400) == 0x0f000400
    Q      = (v >> 30) & 1
    Rd     = (v >> 0) & 0x1F
    a      = (v >> 18) & 1
    b      = (v >> 17) & 1
    c      = (v >> 16) & 1
    cmode  = (v >> 12) & 0xF
    d      = (v >> 9) & 1
    e      = (v >> 8) & 1
    f      = (v >> 7) & 1
    g      = (v >> 6) & 1
    h      = (v >> 5) & 1
    o2     = (v >> 11) & 1
    op     = (v >> 29) & 1
    if (v & 0xfff8fc00) == 0x2f00e400: return ('MOVI_asimdimm_D_ds', {'Rd': Rd, 'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h})
    if (v & 0xfff8fc00) == 0x6f00e400: return ('MOVI_asimdimm_D2_d', {'Rd': Rd, 'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h})
    if (v & 0xfff8fc00) == 0x6f00f400: return ('FMOV_asimdimm_D2_d', {'Rd': Rd, 'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h})
    if (v & 0xbff8fc00) == 0x0f00e400: return ('MOVI_asimdimm_N_b', {'Q': Q, 'Rd': Rd, 'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h})
    if (v & 0xbff8fc00) == 0x0f00f400: return ('FMOV_asimdimm_S_s', {'Q': Q, 'Rd': Rd, 'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h})
    if (v & 0xbff8fc00) == 0x0f00fc00: return ('FMOV_asimdimm_H_h', {'Q': Q, 'Rd': Rd, 'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h})
    if (v & 0xbff8dc00) == 0x0f008400: return ('MOVI_asimdimm_L_hl', {'Q': Q, 'Rd': Rd, 'a': a, 'b': b, 'c': c, 'cmode': cmode, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h})
    if (v & 0xbff8dc00) == 0x0f009400: return ('ORR_asimdimm_L_hl', {'Q': Q, 'Rd': Rd, 'a': a, 'b': b, 'c': c, 'cmode': cmode, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h})
    if (v & 0xbff8dc00) == 0x2f008400: return ('MVNI_asimdimm_L_hl', {'Q': Q, 'Rd': Rd, 'a': a, 'b': b, 'c': c, 'cmode': cmode, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h})
    if (v & 0xbff8dc00) == 0x2f009400: return ('BIC_asimdimm_L_hl', {'Q': Q, 'Rd': Rd, 'a': a, 'b': b, 'c': c, 'cmode': cmode, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h})
    if (v & 0xbff8ec00) == 0x0f00c400: return ('MOVI_asimdimm_M_sm', {'Q': Q, 'Rd': Rd, 'a': a, 'b': b, 'c': c, 'cmode': cmode, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h})
    if (v & 0xbff8ec00) == 0x2f00c400: return ('MVNI_asimdimm_M_sm', {'Q': Q, 'Rd': Rd, 'a': a, 'b': b, 'c': c, 'cmode': cmode, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h})
    if (v & 0xbff89c00) == 0x0f000400: return ('MOVI_asimdimm_L_sl', {'Q': Q, 'Rd': Rd, 'a': a, 'b': b, 'c': c, 'cmode': cmode, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h})
    if (v & 0xbff89c00) == 0x0f001400: return ('ORR_asimdimm_L_sl', {'Q': Q, 'Rd': Rd, 'a': a, 'b': b, 'c': c, 'cmode': cmode, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h})
    if (v & 0xbff89c00) == 0x2f000400: return ('MVNI_asimdimm_L_sl', {'Q': Q, 'Rd': Rd, 'a': a, 'b': b, 'c': c, 'cmode': cmode, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h})
    if (v & 0xbff89c00) == 0x2f001400: return ('BIC_asimdimm_L_sl', {'Q': Q, 'Rd': Rd, 'a': a, 'b': b, 'c': c, 'cmode': cmode, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h})
    return decode_UNDEFINED(v)

def decode_asimdperm(d):
    assert (d & 0xbf208c00) == 0x0e000800
    Q      = (d >> 30) & 1
    Rd     = (d >> 0) & 0x1F
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    opcode = (d >> 12) & 7
    size   = (d >> 22) & 3
    if (d & 0xbf20fc00) == 0x0e001800: return ('UZP1_asimdperm_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e002800: return ('TRN1_asimdperm_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e003800: return ('ZIP1_asimdperm_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e005800: return ('UZP2_asimdperm_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e006800: return ('TRN2_asimdperm_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e007800: return ('ZIP2_asimdperm_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    return decode_UNDEFINED(d)

def decode_asisdone(d):
    assert (d & 0xdfe08400) == 0x5e000400
    Rd     = (d >> 0) & 0x1F
    Rn     = (d >> 5) & 0x1F
    imm4   = (d >> 11) & 0xF
    imm5   = (d >> 16) & 0x1F
    op     = (d >> 29) & 1
    if (d & 0xffe0fc00) == 0x5e000400: return ('DUP_asisdone_only', {'Rd': Rd, 'Rn': Rn, 'imm5': imm5})
    return decode_UNDEFINED(d)

def decode_asisdpair(d):
    assert (d & 0xdf3e0c00) == 0x5e300800
    Rd     = (d >> 0) & 0x1F
    Rn     = (d >> 5) & 0x1F
    U      = (d >> 29) & 1
    opcode = (d >> 12) & 0x1F
    size   = (d >> 22) & 3
    if (d & 0xfffffc00) == 0x5e30c800: return ('FMAXNMP_asisdpair_only_H', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x5e30d800: return ('FADDP_asisdpair_only_H', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x5e30f800: return ('FMAXP_asisdpair_only_H', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x5eb0c800: return ('FMINNMP_asisdpair_only_H', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x5eb0f800: return ('FMINP_asisdpair_only_H', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xffbffc00) == 0x7e30c800: return ('FMAXNMP_asisdpair_only_SD', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xffbffc00) == 0x7e30d800: return ('FADDP_asisdpair_only_SD', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xffbffc00) == 0x7e30f800: return ('FMAXP_asisdpair_only_SD', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xffbffc00) == 0x7eb0c800: return ('FMINNMP_asisdpair_only_SD', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xffbffc00) == 0x7eb0f800: return ('FMINP_asisdpair_only_SD', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xff3ffc00) == 0x5e31b800: return ('ADDP_asisdpair_only', {'Rd': Rd, 'Rn': Rn, 'size': size})
    return decode_UNDEFINED(d)

def decode_asisdshf(d):
    assert (d & 0xdf800400) == 0x5f000400
    Rd     = (d >> 0) & 0x1F
    Rn     = (d >> 5) & 0x1F
    U      = (d >> 29) & 1
    immb   = (d >> 16) & 7
    immh   = (d >> 19) & 0xF
    opcode = (d >> 11) & 0x1F
    if (d & 0xff80fc00) == 0x5f000400 and (d & 0x780000) != 0x000000: return ('SSHR_asisdshf_R', {'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xff80fc00) == 0x5f001400 and (d & 0x780000) != 0x000000: return ('SSRA_asisdshf_R', {'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xff80fc00) == 0x5f002400 and (d & 0x780000) != 0x000000: return ('SRSHR_asisdshf_R', {'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xff80fc00) == 0x5f003400 and (d & 0x780000) != 0x000000: return ('SRSRA_asisdshf_R', {'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xff80fc00) == 0x5f005400 and (d & 0x780000) != 0x000000: return ('SHL_asisdshf_R', {'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xff80fc00) == 0x5f007400 and (d & 0x780000) != 0x000000: return ('SQSHL_asisdshf_R', {'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xff80fc00) == 0x5f009400 and (d & 0x780000) != 0x000000: return ('SQSHRN_asisdshf_N', {'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xff80fc00) == 0x5f009c00 and (d & 0x780000) != 0x000000: return ('SQRSHRN_asisdshf_N', {'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xff80fc00) == 0x5f00e400 and (d & 0x780000) != 0x000000: return ('SCVTF_asisdshf_C', {'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xff80fc00) == 0x5f00fc00 and (d & 0x780000) != 0x000000: return ('FCVTZS_asisdshf_C', {'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xff80fc00) == 0x7f000400 and (d & 0x780000) != 0x000000: return ('USHR_asisdshf_R', {'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xff80fc00) == 0x7f001400 and (d & 0x780000) != 0x000000: return ('USRA_asisdshf_R', {'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xff80fc00) == 0x7f002400 and (d & 0x780000) != 0x000000: return ('URSHR_asisdshf_R', {'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xff80fc00) == 0x7f003400 and (d & 0x780000) != 0x000000: return ('URSRA_asisdshf_R', {'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xff80fc00) == 0x7f004400 and (d & 0x780000) != 0x000000: return ('SRI_asisdshf_R', {'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xff80fc00) == 0x7f005400 and (d & 0x780000) != 0x000000: return ('SLI_asisdshf_R', {'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xff80fc00) == 0x7f006400 and (d & 0x780000) != 0x000000: return ('SQSHLU_asisdshf_R', {'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xff80fc00) == 0x7f007400 and (d & 0x780000) != 0x000000: return ('UQSHL_asisdshf_R', {'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xff80fc00) == 0x7f008400 and (d & 0x780000) != 0x000000: return ('SQSHRUN_asisdshf_N', {'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xff80fc00) == 0x7f008c00 and (d & 0x780000) != 0x000000: return ('SQRSHRUN_asisdshf_N', {'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xff80fc00) == 0x7f009400 and (d & 0x780000) != 0x000000: return ('UQSHRN_asisdshf_N', {'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xff80fc00) == 0x7f009c00 and (d & 0x780000) != 0x000000: return ('UQRSHRN_asisdshf_N', {'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xff80fc00) == 0x7f00e400 and (d & 0x780000) != 0x000000: return ('UCVTF_asisdshf_C', {'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xff80fc00) == 0x7f00fc00 and (d & 0x780000) != 0x000000: return ('FCVTZU_asisdshf_C', {'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    return decode_UNDEFINED(d)

def decode_asisddiff(d):
    assert (d & 0xdf200c00) == 0x5e200000
    Rd     = (d >> 0) & 0x1F
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    U      = (d >> 29) & 1
    opcode = (d >> 12) & 0xF
    size   = (d >> 22) & 3
    if (d & 0xff20fc00) == 0x5e209000: return ('SQDMLAL_asisddiff_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff20fc00) == 0x5e20b000: return ('SQDMLSL_asisddiff_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff20fc00) == 0x5e20d000: return ('SQDMULL_asisddiff_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    return decode_UNDEFINED(d)

def decode_asisdsame(d):
    assert (d & 0xdf200400) == 0x5e200400
    Rd     = (d >> 0) & 0x1F
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    U      = (d >> 29) & 1
    opcode = (d >> 11) & 0x1F
    size   = (d >> 22) & 3
    if (d & 0xffa0fc00) == 0x5e20dc00: return ('FMULX_asisdsame_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xffa0fc00) == 0x5e20e400: return ('FCMEQ_asisdsame_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xffa0fc00) == 0x5e20fc00: return ('FRECPS_asisdsame_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xffa0fc00) == 0x5ea0fc00: return ('FRSQRTS_asisdsame_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xffa0fc00) == 0x7e20e400: return ('FCMGE_asisdsame_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xffa0fc00) == 0x7e20ec00: return ('FACGE_asisdsame_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xffa0fc00) == 0x7ea0d400: return ('FABD_asisdsame_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xffa0fc00) == 0x7ea0e400: return ('FCMGT_asisdsame_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xffa0fc00) == 0x7ea0ec00: return ('FACGT_asisdsame_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff20fc00) == 0x5e200c00: return ('SQADD_asisdsame_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff20fc00) == 0x5e202c00: return ('SQSUB_asisdsame_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff20fc00) == 0x5e203400: return ('CMGT_asisdsame_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff20fc00) == 0x5e203c00: return ('CMGE_asisdsame_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff20fc00) == 0x5e204400: return ('SSHL_asisdsame_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff20fc00) == 0x5e204c00: return ('SQSHL_asisdsame_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff20fc00) == 0x5e205400: return ('SRSHL_asisdsame_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff20fc00) == 0x5e205c00: return ('SQRSHL_asisdsame_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff20fc00) == 0x5e208400: return ('ADD_asisdsame_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff20fc00) == 0x5e208c00: return ('CMTST_asisdsame_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff20fc00) == 0x5e20b400: return ('SQDMULH_asisdsame_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff20fc00) == 0x7e200c00: return ('UQADD_asisdsame_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff20fc00) == 0x7e202c00: return ('UQSUB_asisdsame_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff20fc00) == 0x7e203400: return ('CMHI_asisdsame_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff20fc00) == 0x7e203c00: return ('CMHS_asisdsame_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff20fc00) == 0x7e204400: return ('USHL_asisdsame_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff20fc00) == 0x7e204c00: return ('UQSHL_asisdsame_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff20fc00) == 0x7e205400: return ('URSHL_asisdsame_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff20fc00) == 0x7e205c00: return ('UQRSHL_asisdsame_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff20fc00) == 0x7e208400: return ('SUB_asisdsame_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff20fc00) == 0x7e208c00: return ('CMEQ_asisdsame_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff20fc00) == 0x7e20b400: return ('SQRDMULH_asisdsame_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    return decode_UNDEFINED(d)

def decode_asisdsamefp16(d):
    assert (d & 0xdf60c400) == 0x5e400400
    Rd     = (d >> 0) & 0x1F
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    U      = (d >> 29) & 1
    a      = (d >> 23) & 1
    opcode = (d >> 11) & 7
    if (d & 0xffe0fc00) == 0x5e401c00: return ('FMULX_asisdsamefp16_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x5e402400: return ('FCMEQ_asisdsamefp16_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x5e403c00: return ('FRECPS_asisdsamefp16_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x5ec03c00: return ('FRSQRTS_asisdsamefp16_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x7e402400: return ('FCMGE_asisdsamefp16_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x7e402c00: return ('FACGE_asisdsamefp16_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x7ec01400: return ('FABD_asisdsamefp16_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x7ec02400: return ('FCMGT_asisdsamefp16_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x7ec02c00: return ('FACGT_asisdsamefp16_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    return decode_UNDEFINED(d)

def decode_asisdsame2(d):
    assert (d & 0xdf208400) == 0x5e008400
    Rd     = (d >> 0) & 0x1F
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    U      = (d >> 29) & 1
    opcode = (d >> 11) & 0xF
    size   = (d >> 22) & 3
    if (d & 0xff20fc00) == 0x7e008400: return ('SQRDMLAH_asisdsame2_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff20fc00) == 0x7e008c00: return ('SQRDMLSH_asisdsame2_only', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    return decode_UNDEFINED(d)

def decode_asisdmisc(d):
    assert (d & 0xdf3e0c00) == 0x5e200800
    Rd     = (d >> 0) & 0x1F
    Rn     = (d >> 5) & 0x1F
    U      = (d >> 29) & 1
    opcode = (d >> 12) & 0x1F
    size   = (d >> 22) & 3
    if (d & 0xffbffc00) == 0x5e21a800: return ('FCVTNS_asisdmisc_R', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xffbffc00) == 0x5e21b800: return ('FCVTMS_asisdmisc_R', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xffbffc00) == 0x5e21c800: return ('FCVTAS_asisdmisc_R', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xffbffc00) == 0x5e21d800: return ('SCVTF_asisdmisc_R', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xffbffc00) == 0x5ea0c800: return ('FCMGT_asisdmisc_FZ', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xffbffc00) == 0x5ea0d800: return ('FCMEQ_asisdmisc_FZ', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xffbffc00) == 0x5ea0e800: return ('FCMLT_asisdmisc_FZ', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xffbffc00) == 0x5ea1a800: return ('FCVTPS_asisdmisc_R', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xffbffc00) == 0x5ea1b800: return ('FCVTZS_asisdmisc_R', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xffbffc00) == 0x5ea1d800: return ('FRECPE_asisdmisc_R', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xffbffc00) == 0x5ea1f800: return ('FRECPX_asisdmisc_R', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xffbffc00) == 0x7e216800: return ('FCVTXN_asisdmisc_N', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xffbffc00) == 0x7e21a800: return ('FCVTNU_asisdmisc_R', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xffbffc00) == 0x7e21b800: return ('FCVTMU_asisdmisc_R', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xffbffc00) == 0x7e21c800: return ('FCVTAU_asisdmisc_R', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xffbffc00) == 0x7e21d800: return ('UCVTF_asisdmisc_R', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xffbffc00) == 0x7ea0c800: return ('FCMGE_asisdmisc_FZ', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xffbffc00) == 0x7ea0d800: return ('FCMLE_asisdmisc_FZ', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xffbffc00) == 0x7ea1a800: return ('FCVTPU_asisdmisc_R', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xffbffc00) == 0x7ea1b800: return ('FCVTZU_asisdmisc_R', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xffbffc00) == 0x7ea1d800: return ('FRSQRTE_asisdmisc_R', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xff3ffc00) == 0x5e203800: return ('SUQADD_asisdmisc_R', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xff3ffc00) == 0x5e207800: return ('SQABS_asisdmisc_R', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xff3ffc00) == 0x5e208800: return ('CMGT_asisdmisc_Z', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xff3ffc00) == 0x5e209800: return ('CMEQ_asisdmisc_Z', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xff3ffc00) == 0x5e20a800: return ('CMLT_asisdmisc_Z', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xff3ffc00) == 0x5e20b800: return ('ABS_asisdmisc_R', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xff3ffc00) == 0x5e214800: return ('SQXTN_asisdmisc_N', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xff3ffc00) == 0x7e203800: return ('USQADD_asisdmisc_R', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xff3ffc00) == 0x7e207800: return ('SQNEG_asisdmisc_R', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xff3ffc00) == 0x7e208800: return ('CMGE_asisdmisc_Z', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xff3ffc00) == 0x7e209800: return ('CMLE_asisdmisc_Z', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xff3ffc00) == 0x7e20b800: return ('NEG_asisdmisc_R', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xff3ffc00) == 0x7e212800: return ('SQXTUN_asisdmisc_N', {'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xff3ffc00) == 0x7e214800: return ('UQXTN_asisdmisc_N', {'Rd': Rd, 'Rn': Rn, 'size': size})
    return decode_UNDEFINED(d)

def decode_asisdmiscfp16(d):
    assert (d & 0xdf7e0c00) == 0x5e780800
    Rd     = (d >> 0) & 0x1F
    Rn     = (d >> 5) & 0x1F
    U      = (d >> 29) & 1
    a      = (d >> 23) & 1
    opcode = (d >> 12) & 0x1F
    if (d & 0xfffffc00) == 0x5e79a800: return ('FCVTNS_asisdmiscfp16_R', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x5e79b800: return ('FCVTMS_asisdmiscfp16_R', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x5e79c800: return ('FCVTAS_asisdmiscfp16_R', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x5e79d800: return ('SCVTF_asisdmiscfp16_R', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x5ef8c800: return ('FCMGT_asisdmiscfp16_FZ', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x5ef8d800: return ('FCMEQ_asisdmiscfp16_FZ', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x5ef8e800: return ('FCMLT_asisdmiscfp16_FZ', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x5ef9a800: return ('FCVTPS_asisdmiscfp16_R', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x5ef9b800: return ('FCVTZS_asisdmiscfp16_R', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x5ef9d800: return ('FRECPE_asisdmiscfp16_R', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x5ef9f800: return ('FRECPX_asisdmiscfp16_R', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x7e79a800: return ('FCVTNU_asisdmiscfp16_R', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x7e79b800: return ('FCVTMU_asisdmiscfp16_R', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x7e79c800: return ('FCVTAU_asisdmiscfp16_R', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x7e79d800: return ('UCVTF_asisdmiscfp16_R', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x7ef8c800: return ('FCMGE_asisdmiscfp16_FZ', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x7ef8d800: return ('FCMLE_asisdmiscfp16_FZ', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x7ef9a800: return ('FCVTPU_asisdmiscfp16_R', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x7ef9b800: return ('FCVTZU_asisdmiscfp16_R', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x7ef9d800: return ('FRSQRTE_asisdmiscfp16_R', {'Rd': Rd, 'Rn': Rn})
    return decode_UNDEFINED(d)

def decode_asisdelem(d):
    assert (d & 0xdf000400) == 0x5f000000
    H      = (d >> 11) & 1
    L      = (d >> 21) & 1
    M      = (d >> 20) & 1
    Rd     = (d >> 0) & 0x1F
    Rm     = (d >> 16) & 0xF
    Rn     = (d >> 5) & 0x1F
    U      = (d >> 29) & 1
    opcode = (d >> 12) & 0xF
    size   = (d >> 22) & 3
    if (d & 0xffc0f400) == 0x5f001000: return ('FMLA_asisdelem_RH_H', {'H': H, 'L': L, 'M': M, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffc0f400) == 0x5f005000: return ('FMLS_asisdelem_RH_H', {'H': H, 'L': L, 'M': M, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffc0f400) == 0x5f009000: return ('FMUL_asisdelem_RH_H', {'H': H, 'L': L, 'M': M, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffc0f400) == 0x7f009000: return ('FMULX_asisdelem_RH_H', {'H': H, 'L': L, 'M': M, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xff80f400) == 0x5f801000: return ('FMLA_asisdelem_R_SD', {'H': H, 'L': L, 'M': M, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff80f400) == 0x5f805000: return ('FMLS_asisdelem_R_SD', {'H': H, 'L': L, 'M': M, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff80f400) == 0x5f809000: return ('FMUL_asisdelem_R_SD', {'H': H, 'L': L, 'M': M, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff80f400) == 0x7f809000: return ('FMULX_asisdelem_R_SD', {'H': H, 'L': L, 'M': M, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff00f400) == 0x5f003000: return ('SQDMLAL_asisdelem_L', {'H': H, 'L': L, 'M': M, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff00f400) == 0x5f007000: return ('SQDMLSL_asisdelem_L', {'H': H, 'L': L, 'M': M, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff00f400) == 0x5f00b000: return ('SQDMULL_asisdelem_L', {'H': H, 'L': L, 'M': M, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff00f400) == 0x5f00c000: return ('SQDMULH_asisdelem_R', {'H': H, 'L': L, 'M': M, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff00f400) == 0x5f00d000: return ('SQRDMULH_asisdelem_R', {'H': H, 'L': L, 'M': M, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff00f400) == 0x7f00d000: return ('SQRDMLAH_asisdelem_R', {'H': H, 'L': L, 'M': M, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xff00f400) == 0x7f00f000: return ('SQRDMLSH_asisdelem_R', {'H': H, 'L': L, 'M': M, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    return decode_UNDEFINED(d)

def decode_asimdshf(d):
    assert (d & 0x9f800400) == 0x0f000400 and (d & 0x780000) != 0x000000
    Q      = (d >> 30) & 1
    Rd     = (d >> 0) & 0x1F
    Rn     = (d >> 5) & 0x1F
    U      = (d >> 29) & 1
    immb   = (d >> 16) & 7
    immh   = (d >> 19) & 0xF
    opcode = (d >> 11) & 0x1F
    if (d & 0xbf80fc00) == 0x0f000400 and (d & 0x780000) != 0x000000: return ('SSHR_asimdshf_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xbf80fc00) == 0x0f001400 and (d & 0x780000) != 0x000000: return ('SSRA_asimdshf_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xbf80fc00) == 0x0f002400 and (d & 0x780000) != 0x000000: return ('SRSHR_asimdshf_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xbf80fc00) == 0x0f003400 and (d & 0x780000) != 0x000000: return ('SRSRA_asimdshf_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xbf80fc00) == 0x0f005400 and (d & 0x780000) != 0x000000: return ('SHL_asimdshf_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xbf80fc00) == 0x0f007400 and (d & 0x780000) != 0x000000: return ('SQSHL_asimdshf_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xbf80fc00) == 0x0f008400 and (d & 0x780000) != 0x000000: return ('SHRN_asimdshf_N', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xbf80fc00) == 0x0f008c00 and (d & 0x780000) != 0x000000: return ('RSHRN_asimdshf_N', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xbf80fc00) == 0x0f009400 and (d & 0x780000) != 0x000000: return ('SQSHRN_asimdshf_N', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xbf80fc00) == 0x0f009c00 and (d & 0x780000) != 0x000000: return ('SQRSHRN_asimdshf_N', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xbf80fc00) == 0x0f00a400 and (d & 0x780000) != 0x000000: return ('SSHLL_asimdshf_L', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xbf80fc00) == 0x0f00e400 and (d & 0x780000) != 0x000000: return ('SCVTF_asimdshf_C', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xbf80fc00) == 0x0f00fc00 and (d & 0x780000) != 0x000000: return ('FCVTZS_asimdshf_C', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xbf80fc00) == 0x2f000400 and (d & 0x780000) != 0x000000: return ('USHR_asimdshf_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xbf80fc00) == 0x2f001400 and (d & 0x780000) != 0x000000: return ('USRA_asimdshf_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xbf80fc00) == 0x2f002400 and (d & 0x780000) != 0x000000: return ('URSHR_asimdshf_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xbf80fc00) == 0x2f003400 and (d & 0x780000) != 0x000000: return ('URSRA_asimdshf_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xbf80fc00) == 0x2f004400 and (d & 0x780000) != 0x000000: return ('SRI_asimdshf_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xbf80fc00) == 0x2f005400 and (d & 0x780000) != 0x000000: return ('SLI_asimdshf_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xbf80fc00) == 0x2f006400 and (d & 0x780000) != 0x000000: return ('SQSHLU_asimdshf_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xbf80fc00) == 0x2f007400 and (d & 0x780000) != 0x000000: return ('UQSHL_asimdshf_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xbf80fc00) == 0x2f008400 and (d & 0x780000) != 0x000000: return ('SQSHRUN_asimdshf_N', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xbf80fc00) == 0x2f008c00 and (d & 0x780000) != 0x000000: return ('SQRSHRUN_asimdshf_N', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xbf80fc00) == 0x2f009400 and (d & 0x780000) != 0x000000: return ('UQSHRN_asimdshf_N', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xbf80fc00) == 0x2f009c00 and (d & 0x780000) != 0x000000: return ('UQRSHRN_asimdshf_N', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xbf80fc00) == 0x2f00a400 and (d & 0x780000) != 0x000000: return ('USHLL_asimdshf_L', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xbf80fc00) == 0x2f00e400 and (d & 0x780000) != 0x000000: return ('UCVTF_asimdshf_C', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    if (d & 0xbf80fc00) == 0x2f00fc00 and (d & 0x780000) != 0x000000: return ('FCVTZU_asimdshf_C', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'immb': immb, 'immh': immh})
    return decode_UNDEFINED(d)

def decode_asimdtbl(d):
    assert (d & 0xbf208c00) == 0x0e000000
    Q      = (d >> 30) & 1
    Rd     = (d >> 0) & 0x1F
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    len    = (d >> 13) & 3
    op     = (d >> 12) & 1
    op2    = (d >> 22) & 3
    if (d & 0xbfe0fc00) == 0x0e000000: return ('TBL_asimdtbl_L1_1', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x0e001000: return ('TBX_asimdtbl_L1_1', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x0e002000: return ('TBL_asimdtbl_L2_2', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x0e003000: return ('TBX_asimdtbl_L2_2', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x0e004000: return ('TBL_asimdtbl_L3_3', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x0e005000: return ('TBX_asimdtbl_L3_3', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x0e006000: return ('TBL_asimdtbl_L4_4', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x0e007000: return ('TBX_asimdtbl_L4_4', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    return decode_UNDEFINED(d)

def decode_asimddiff(d):
    assert (d & 0x9f200c00) == 0x0e200000
    Q      = (d >> 30) & 1
    Rd     = (d >> 0) & 0x1F
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    U      = (d >> 29) & 1
    opcode = (d >> 12) & 0xF
    size   = (d >> 22) & 3
    if (d & 0xbf20fc00) == 0x0e200000: return ('SADDL_asimddiff_L', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e201000: return ('SADDW_asimddiff_W', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e202000: return ('SSUBL_asimddiff_L', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e203000: return ('SSUBW_asimddiff_W', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e204000: return ('ADDHN_asimddiff_N', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e205000: return ('SABAL_asimddiff_L', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e206000: return ('SUBHN_asimddiff_N', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e207000: return ('SABDL_asimddiff_L', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e208000: return ('SMLAL_asimddiff_L', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e209000: return ('SQDMLAL_asimddiff_L', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e20a000: return ('SMLSL_asimddiff_L', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e20b000: return ('SQDMLSL_asimddiff_L', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e20c000: return ('SMULL_asimddiff_L', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e20d000: return ('SQDMULL_asimddiff_L', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e20e000: return ('PMULL_asimddiff_L', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e200000: return ('UADDL_asimddiff_L', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e201000: return ('UADDW_asimddiff_W', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e202000: return ('USUBL_asimddiff_L', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e203000: return ('USUBW_asimddiff_W', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e204000: return ('RADDHN_asimddiff_N', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e205000: return ('UABAL_asimddiff_L', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e206000: return ('RSUBHN_asimddiff_N', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e207000: return ('UABDL_asimddiff_L', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e208000: return ('UMLAL_asimddiff_L', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e20a000: return ('UMLSL_asimddiff_L', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e20c000: return ('UMULL_asimddiff_L', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    return decode_UNDEFINED(d)

def decode_asimdsame(d):
    assert (d & 0x9f200400) == 0x0e200400
    Q      = (d >> 30) & 1
    Rd     = (d >> 0) & 0x1F
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    U      = (d >> 29) & 1
    opcode = (d >> 11) & 0x1F
    size   = (d >> 22) & 3
    if (d & 0xbfe0fc00) == 0x0e201c00: return ('AND_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x0e601c00: return ('BIC_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x0ea01c00: return ('ORR_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x0ee01c00: return ('ORN_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x2e201c00: return ('EOR_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x2e601c00: return ('BSL_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x2ea01c00: return ('BIT_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x2ee01c00: return ('BIF_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfa0fc00) == 0x0e20c400: return ('FMAXNM_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbfa0fc00) == 0x0e20cc00: return ('FMLA_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbfa0fc00) == 0x0e20d400: return ('FADD_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbfa0fc00) == 0x0e20dc00: return ('FMULX_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbfa0fc00) == 0x0e20e400: return ('FCMEQ_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbfa0fc00) == 0x0e20f400: return ('FMAX_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbfa0fc00) == 0x0e20fc00: return ('FRECPS_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbfa0fc00) == 0x0ea0c400: return ('FMINNM_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbfa0fc00) == 0x0ea0cc00: return ('FMLS_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbfa0fc00) == 0x0ea0d400: return ('FSUB_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbfa0fc00) == 0x0ea0f400: return ('FMIN_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbfa0fc00) == 0x0ea0fc00: return ('FRSQRTS_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbfa0fc00) == 0x2e20c400: return ('FMAXNMP_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbfa0fc00) == 0x2e20d400: return ('FADDP_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbfa0fc00) == 0x2e20dc00: return ('FMUL_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbfa0fc00) == 0x2e20e400: return ('FCMGE_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbfa0fc00) == 0x2e20ec00: return ('FACGE_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbfa0fc00) == 0x2e20f400: return ('FMAXP_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbfa0fc00) == 0x2e20fc00: return ('FDIV_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbfa0fc00) == 0x2ea0c400: return ('FMINNMP_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbfa0fc00) == 0x2ea0d400: return ('FABD_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbfa0fc00) == 0x2ea0e400: return ('FCMGT_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbfa0fc00) == 0x2ea0ec00: return ('FACGT_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbfa0fc00) == 0x2ea0f400: return ('FMINP_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e200400: return ('SHADD_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e200c00: return ('SQADD_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e201400: return ('SRHADD_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e202400: return ('SHSUB_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e202c00: return ('SQSUB_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e203400: return ('CMGT_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e203c00: return ('CMGE_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e204400: return ('SSHL_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e204c00: return ('SQSHL_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e205400: return ('SRSHL_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e205c00: return ('SQRSHL_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e206400: return ('SMAX_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e206c00: return ('SMIN_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e207400: return ('SABD_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e207c00: return ('SABA_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e208400: return ('ADD_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e208c00: return ('CMTST_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e209400: return ('MLA_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e209c00: return ('MUL_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e20a400: return ('SMAXP_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e20ac00: return ('SMINP_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e20b400: return ('SQDMULH_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x0e20bc00: return ('ADDP_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e200400: return ('UHADD_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e200c00: return ('UQADD_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e201400: return ('URHADD_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e202400: return ('UHSUB_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e202c00: return ('UQSUB_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e203400: return ('CMHI_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e203c00: return ('CMHS_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e204400: return ('USHL_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e204c00: return ('UQSHL_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e205400: return ('URSHL_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e205c00: return ('UQRSHL_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e206400: return ('UMAX_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e206c00: return ('UMIN_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e207400: return ('UABD_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e207c00: return ('UABA_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e208400: return ('SUB_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e208c00: return ('CMEQ_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e209400: return ('MLS_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e209c00: return ('PMUL_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e20a400: return ('UMAXP_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e20ac00: return ('UMINP_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e20b400: return ('SQRDMULH_asimdsame_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    return decode_UNDEFINED(d)

def decode_asimdsamefp16(d):
    assert (d & 0x9f60c400) == 0x0e400400
    Q      = (d >> 30) & 1
    Rd     = (d >> 0) & 0x1F
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    U      = (d >> 29) & 1
    a      = (d >> 23) & 1
    opcode = (d >> 11) & 7
    if (d & 0xbfe0fc00) == 0x0e400400: return ('FMAXNM_asimdsamefp16_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x0e400c00: return ('FMLA_asimdsamefp16_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x0e401400: return ('FADD_asimdsamefp16_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x0e401c00: return ('FMULX_asimdsamefp16_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x0e402400: return ('FCMEQ_asimdsamefp16_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x0e403400: return ('FMAX_asimdsamefp16_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x0e403c00: return ('FRECPS_asimdsamefp16_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x0ec00400: return ('FMINNM_asimdsamefp16_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x0ec00c00: return ('FMLS_asimdsamefp16_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x0ec01400: return ('FSUB_asimdsamefp16_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x0ec03400: return ('FMIN_asimdsamefp16_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x0ec03c00: return ('FRSQRTS_asimdsamefp16_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x2e400400: return ('FMAXNMP_asimdsamefp16_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x2e401400: return ('FADDP_asimdsamefp16_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x2e401c00: return ('FMUL_asimdsamefp16_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x2e402400: return ('FCMGE_asimdsamefp16_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x2e402c00: return ('FACGE_asimdsamefp16_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x2e403400: return ('FMAXP_asimdsamefp16_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x2e403c00: return ('FDIV_asimdsamefp16_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x2ec00400: return ('FMINNMP_asimdsamefp16_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x2ec01400: return ('FABD_asimdsamefp16_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x2ec02400: return ('FCMGT_asimdsamefp16_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x2ec02c00: return ('FACGT_asimdsamefp16_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfe0fc00) == 0x2ec03400: return ('FMINP_asimdsamefp16_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    return decode_UNDEFINED(d)

def decode_asimdsame2(d):
    assert (d & 0x9f208400) == 0x0e008400
    Q      = (d >> 30) & 1
    Rd     = (d >> 0) & 0x1F
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    U      = (d >> 29) & 1
    opcode = (d >> 11) & 0xF
    size   = (d >> 22) & 3
    if (d & 0xbf20fc00) == 0x0e009400: return ('SDOT_asimdsame2_D', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e008400: return ('SQRDMLAH_asimdsame2_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e008c00: return ('SQRDMLSH_asimdsame2_only', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20fc00) == 0x2e009400: return ('UDOT_asimdsame2_D', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf20ec00) == 0x2e00e400: return ('FCADD_asimdsame2_C', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'opcode': opcode, 'size': size})
    if (d & 0xbf20e400) == 0x2e00c400: return ('FCMLA_asimdsame2_C', {'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'opcode': opcode, 'size': size})
    return decode_UNDEFINED(d)

def decode_asimdmisc(d):
    assert (d & 0x9f3e0c00) == 0x0e200800
    Q      = (d >> 30) & 1
    Rd     = (d >> 0) & 0x1F
    Rn     = (d >> 5) & 0x1F
    U      = (d >> 29) & 1
    opcode = (d >> 12) & 0x1F
    size   = (d >> 22) & 3
    if (d & 0xbffffc00) == 0x2e205800: return ('NOT_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbffffc00) == 0x2e605800: return ('RBIT_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbfbffc00) == 0x0e216800: return ('FCVTN_asimdmisc_N', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x0e217800: return ('FCVTL_asimdmisc_L', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x0e218800: return ('FRINTN_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x0e219800: return ('FRINTM_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x0e21a800: return ('FCVTNS_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x0e21b800: return ('FCVTMS_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x0e21c800: return ('FCVTAS_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x0e21d800: return ('SCVTF_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x0ea0c800: return ('FCMGT_asimdmisc_FZ', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x0ea0d800: return ('FCMEQ_asimdmisc_FZ', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x0ea0e800: return ('FCMLT_asimdmisc_FZ', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x0ea0f800: return ('FABS_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x0ea18800: return ('FRINTP_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x0ea19800: return ('FRINTZ_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x0ea1a800: return ('FCVTPS_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x0ea1b800: return ('FCVTZS_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x0ea1c800: return ('URECPE_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x0ea1d800: return ('FRECPE_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x2e216800: return ('FCVTXN_asimdmisc_N', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x2e218800: return ('FRINTA_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x2e219800: return ('FRINTX_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x2e21a800: return ('FCVTNU_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x2e21b800: return ('FCVTMU_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x2e21c800: return ('FCVTAU_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x2e21d800: return ('UCVTF_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x2ea0c800: return ('FCMGE_asimdmisc_FZ', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x2ea0d800: return ('FCMLE_asimdmisc_FZ', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x2ea0f800: return ('FNEG_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x2ea19800: return ('FRINTI_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x2ea1a800: return ('FCVTPU_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x2ea1b800: return ('FCVTZU_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x2ea1c800: return ('URSQRTE_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x2ea1d800: return ('FRSQRTE_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbfbffc00) == 0x2ea1f800: return ('FSQRT_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x0e200800: return ('REV64_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x0e201800: return ('REV16_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x0e202800: return ('SADDLP_asimdmisc_P', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x0e203800: return ('SUQADD_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x0e204800: return ('CLS_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x0e205800: return ('CNT_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x0e206800: return ('SADALP_asimdmisc_P', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x0e207800: return ('SQABS_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x0e208800: return ('CMGT_asimdmisc_Z', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x0e209800: return ('CMEQ_asimdmisc_Z', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x0e20a800: return ('CMLT_asimdmisc_Z', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x0e20b800: return ('ABS_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x0e212800: return ('XTN_asimdmisc_N', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x0e214800: return ('SQXTN_asimdmisc_N', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x2e200800: return ('REV32_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x2e202800: return ('UADDLP_asimdmisc_P', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x2e203800: return ('USQADD_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x2e204800: return ('CLZ_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x2e206800: return ('UADALP_asimdmisc_P', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x2e207800: return ('SQNEG_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x2e208800: return ('CMGE_asimdmisc_Z', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x2e209800: return ('CMLE_asimdmisc_Z', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x2e20b800: return ('NEG_asimdmisc_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x2e212800: return ('SQXTUN_asimdmisc_N', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x2e213800: return ('SHLL_asimdmisc_S', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    if (d & 0xbf3ffc00) == 0x2e214800: return ('UQXTN_asimdmisc_N', {'Q': Q, 'Rd': Rd, 'Rn': Rn, 'size': size})
    return decode_UNDEFINED(d)

def decode_asimdmiscfp16(d):
    assert (d & 0x9f7e0c00) == 0x0e780800
    Q      = (d >> 30) & 1
    Rd     = (d >> 0) & 0x1F
    Rn     = (d >> 5) & 0x1F
    U      = (d >> 29) & 1
    a      = (d >> 23) & 1
    opcode = (d >> 12) & 0x1F
    if (d & 0xbffffc00) == 0x0e798800: return ('FRINTN_asimdmiscfp16_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbffffc00) == 0x0e799800: return ('FRINTM_asimdmiscfp16_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbffffc00) == 0x0e79a800: return ('FCVTNS_asimdmiscfp16_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbffffc00) == 0x0e79b800: return ('FCVTMS_asimdmiscfp16_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbffffc00) == 0x0e79c800: return ('FCVTAS_asimdmiscfp16_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbffffc00) == 0x0e79d800: return ('SCVTF_asimdmiscfp16_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbffffc00) == 0x0ef8c800: return ('FCMGT_asimdmiscfp16_FZ', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbffffc00) == 0x0ef8d800: return ('FCMEQ_asimdmiscfp16_FZ', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbffffc00) == 0x0ef8e800: return ('FCMLT_asimdmiscfp16_FZ', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbffffc00) == 0x0ef8f800: return ('FABS_asimdmiscfp16_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbffffc00) == 0x0ef98800: return ('FRINTP_asimdmiscfp16_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbffffc00) == 0x0ef99800: return ('FRINTZ_asimdmiscfp16_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbffffc00) == 0x0ef9a800: return ('FCVTPS_asimdmiscfp16_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbffffc00) == 0x0ef9b800: return ('FCVTZS_asimdmiscfp16_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbffffc00) == 0x0ef9d800: return ('FRECPE_asimdmiscfp16_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbffffc00) == 0x2e798800: return ('FRINTA_asimdmiscfp16_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbffffc00) == 0x2e799800: return ('FRINTX_asimdmiscfp16_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbffffc00) == 0x2e79a800: return ('FCVTNU_asimdmiscfp16_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbffffc00) == 0x2e79b800: return ('FCVTMU_asimdmiscfp16_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbffffc00) == 0x2e79c800: return ('FCVTAU_asimdmiscfp16_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbffffc00) == 0x2e79d800: return ('UCVTF_asimdmiscfp16_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbffffc00) == 0x2ef8c800: return ('FCMGE_asimdmiscfp16_FZ', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbffffc00) == 0x2ef8d800: return ('FCMLE_asimdmiscfp16_FZ', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbffffc00) == 0x2ef8f800: return ('FNEG_asimdmiscfp16_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbffffc00) == 0x2ef99800: return ('FRINTI_asimdmiscfp16_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbffffc00) == 0x2ef9a800: return ('FCVTPU_asimdmiscfp16_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbffffc00) == 0x2ef9b800: return ('FCVTZU_asimdmiscfp16_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbffffc00) == 0x2ef9d800: return ('FRSQRTE_asimdmiscfp16_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    if (d & 0xbffffc00) == 0x2ef9f800: return ('FSQRT_asimdmiscfp16_R', {'Q': Q, 'Rd': Rd, 'Rn': Rn})
    return decode_UNDEFINED(d)

def decode_asimdelem(d):
    assert (d & 0x9f000400) == 0x0f000000
    H      = (d >> 11) & 1
    L      = (d >> 21) & 1
    M      = (d >> 20) & 1
    Q      = (d >> 30) & 1
    Rd     = (d >> 0) & 0x1F
    Rm     = (d >> 16) & 0xF
    Rn     = (d >> 5) & 0x1F
    U      = (d >> 29) & 1
    opcode = (d >> 12) & 0xF
    size   = (d >> 22) & 3
    if (d & 0xbfc0f400) == 0x0f001000: return ('FMLA_asimdelem_RH_H', {'H': H, 'L': L, 'M': M, 'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfc0f400) == 0x0f005000: return ('FMLS_asimdelem_RH_H', {'H': H, 'L': L, 'M': M, 'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfc0f400) == 0x0f009000: return ('FMUL_asimdelem_RH_H', {'H': H, 'L': L, 'M': M, 'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbfc0f400) == 0x2f009000: return ('FMULX_asimdelem_RH_H', {'H': H, 'L': L, 'M': M, 'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xbf80f400) == 0x0f801000: return ('FMLA_asimdelem_R_SD', {'H': H, 'L': L, 'M': M, 'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf80f400) == 0x0f805000: return ('FMLS_asimdelem_R_SD', {'H': H, 'L': L, 'M': M, 'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf80f400) == 0x0f809000: return ('FMUL_asimdelem_R_SD', {'H': H, 'L': L, 'M': M, 'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf80f400) == 0x2f809000: return ('FMULX_asimdelem_R_SD', {'H': H, 'L': L, 'M': M, 'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf00f400) == 0x0f002000: return ('SMLAL_asimdelem_L', {'H': H, 'L': L, 'M': M, 'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf00f400) == 0x0f003000: return ('SQDMLAL_asimdelem_L', {'H': H, 'L': L, 'M': M, 'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf00f400) == 0x0f006000: return ('SMLSL_asimdelem_L', {'H': H, 'L': L, 'M': M, 'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf00f400) == 0x0f007000: return ('SQDMLSL_asimdelem_L', {'H': H, 'L': L, 'M': M, 'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf00f400) == 0x0f008000: return ('MUL_asimdelem_R', {'H': H, 'L': L, 'M': M, 'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf00f400) == 0x0f00a000: return ('SMULL_asimdelem_L', {'H': H, 'L': L, 'M': M, 'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf00f400) == 0x0f00b000: return ('SQDMULL_asimdelem_L', {'H': H, 'L': L, 'M': M, 'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf00f400) == 0x0f00c000: return ('SQDMULH_asimdelem_R', {'H': H, 'L': L, 'M': M, 'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf00f400) == 0x0f00d000: return ('SQRDMULH_asimdelem_R', {'H': H, 'L': L, 'M': M, 'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf00f400) == 0x0f00e000: return ('SDOT_asimdelem_D', {'H': H, 'L': L, 'M': M, 'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf00f400) == 0x2f000000: return ('MLA_asimdelem_R', {'H': H, 'L': L, 'M': M, 'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf00f400) == 0x2f002000: return ('UMLAL_asimdelem_L', {'H': H, 'L': L, 'M': M, 'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf00f400) == 0x2f004000: return ('MLS_asimdelem_R', {'H': H, 'L': L, 'M': M, 'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf00f400) == 0x2f006000: return ('UMLSL_asimdelem_L', {'H': H, 'L': L, 'M': M, 'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf00f400) == 0x2f00a000: return ('UMULL_asimdelem_L', {'H': H, 'L': L, 'M': M, 'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf00f400) == 0x2f00d000: return ('SQRDMLAH_asimdelem_R', {'H': H, 'L': L, 'M': M, 'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf00f400) == 0x2f00e000: return ('UDOT_asimdelem_D', {'H': H, 'L': L, 'M': M, 'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbf00f400) == 0x2f00f000: return ('SQRDMLSH_asimdelem_R', {'H': H, 'L': L, 'M': M, 'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'size': size})
    if (d & 0xbfc09400) == 0x2f401000: return ('FCMLA_asimdelem_C_H', {'H': H, 'L': L, 'M': M, 'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'opcode': opcode})
    if (d & 0xbfc09400) == 0x2f801000: return ('FCMLA_asimdelem_C_S', {'H': H, 'L': L, 'M': M, 'Q': Q, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'opcode': opcode})
    return decode_UNDEFINED(d)

def decode_float2fix(d):
    assert (d & 0x5f200000) == 0x1e000000
    Rd     = (d >> 0) & 0x1F
    Rn     = (d >> 5) & 0x1F
    S      = (d >> 29) & 1
    opcode = (d >> 16) & 7
    rmode  = (d >> 19) & 3
    scale  = (d >> 10) & 0x3F
    sf     = (d >> 31) & 1
    type   = (d >> 22) & 3
    if (d & 0xffff0000) == 0x1e020000: return ('SCVTF_S32_float2fix', {'Rd': Rd, 'Rn': Rn, 'scale': scale})
    if (d & 0xffff0000) == 0x1e030000: return ('UCVTF_S32_float2fix', {'Rd': Rd, 'Rn': Rn, 'scale': scale})
    if (d & 0xffff0000) == 0x1e180000: return ('FCVTZS_32S_float2fix', {'Rd': Rd, 'Rn': Rn, 'scale': scale})
    if (d & 0xffff0000) == 0x1e190000: return ('FCVTZU_32S_float2fix', {'Rd': Rd, 'Rn': Rn, 'scale': scale})
    if (d & 0xffff0000) == 0x1e420000: return ('SCVTF_D32_float2fix', {'Rd': Rd, 'Rn': Rn, 'scale': scale})
    if (d & 0xffff0000) == 0x1e430000: return ('UCVTF_D32_float2fix', {'Rd': Rd, 'Rn': Rn, 'scale': scale})
    if (d & 0xffff0000) == 0x1e580000: return ('FCVTZS_32D_float2fix', {'Rd': Rd, 'Rn': Rn, 'scale': scale})
    if (d & 0xffff0000) == 0x1e590000: return ('FCVTZU_32D_float2fix', {'Rd': Rd, 'Rn': Rn, 'scale': scale})
    if (d & 0xffff0000) == 0x1ec20000: return ('SCVTF_H32_float2fix', {'Rd': Rd, 'Rn': Rn, 'scale': scale})
    if (d & 0xffff0000) == 0x1ec30000: return ('UCVTF_H32_float2fix', {'Rd': Rd, 'Rn': Rn, 'scale': scale})
    if (d & 0xffff0000) == 0x1ed80000: return ('FCVTZS_32H_float2fix', {'Rd': Rd, 'Rn': Rn, 'scale': scale})
    if (d & 0xffff0000) == 0x1ed90000: return ('FCVTZU_32H_float2fix', {'Rd': Rd, 'Rn': Rn, 'scale': scale})
    if (d & 0xffff0000) == 0x9e020000: return ('SCVTF_S64_float2fix', {'Rd': Rd, 'Rn': Rn, 'scale': scale})
    if (d & 0xffff0000) == 0x9e030000: return ('UCVTF_S64_float2fix', {'Rd': Rd, 'Rn': Rn, 'scale': scale})
    if (d & 0xffff0000) == 0x9e180000: return ('FCVTZS_64S_float2fix', {'Rd': Rd, 'Rn': Rn, 'scale': scale})
    if (d & 0xffff0000) == 0x9e190000: return ('FCVTZU_64S_float2fix', {'Rd': Rd, 'Rn': Rn, 'scale': scale})
    if (d & 0xffff0000) == 0x9e420000: return ('SCVTF_D64_float2fix', {'Rd': Rd, 'Rn': Rn, 'scale': scale})
    if (d & 0xffff0000) == 0x9e430000: return ('UCVTF_D64_float2fix', {'Rd': Rd, 'Rn': Rn, 'scale': scale})
    if (d & 0xffff0000) == 0x9e580000: return ('FCVTZS_64D_float2fix', {'Rd': Rd, 'Rn': Rn, 'scale': scale})
    if (d & 0xffff0000) == 0x9e590000: return ('FCVTZU_64D_float2fix', {'Rd': Rd, 'Rn': Rn, 'scale': scale})
    if (d & 0xffff0000) == 0x9ec20000: return ('SCVTF_H64_float2fix', {'Rd': Rd, 'Rn': Rn, 'scale': scale})
    if (d & 0xffff0000) == 0x9ec30000: return ('UCVTF_H64_float2fix', {'Rd': Rd, 'Rn': Rn, 'scale': scale})
    if (d & 0xffff0000) == 0x9ed80000: return ('FCVTZS_64H_float2fix', {'Rd': Rd, 'Rn': Rn, 'scale': scale})
    if (d & 0xffff0000) == 0x9ed90000: return ('FCVTZU_64H_float2fix', {'Rd': Rd, 'Rn': Rn, 'scale': scale})
    return decode_UNDEFINED(d)

def decode_float2int(d):
    assert (d & 0x5f20fc00) == 0x1e200000
    Rd     = (d >> 0) & 0x1F
    Rn     = (d >> 5) & 0x1F
    S      = (d >> 29) & 1
    opcode = (d >> 16) & 7
    rmode  = (d >> 19) & 3
    sf     = (d >> 31) & 1
    type   = (d >> 22) & 3
    if (d & 0xfffffc00) == 0x1e200000: return ('FCVTNS_32S_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e210000: return ('FCVTNU_32S_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e220000: return ('SCVTF_S32_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e230000: return ('UCVTF_S32_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e240000: return ('FCVTAS_32S_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e250000: return ('FCVTAU_32S_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e260000: return ('FMOV_32S_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e270000: return ('FMOV_S32_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e280000: return ('FCVTPS_32S_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e290000: return ('FCVTPU_32S_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e300000: return ('FCVTMS_32S_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e310000: return ('FCVTMU_32S_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e380000: return ('FCVTZS_32S_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e390000: return ('FCVTZU_32S_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e600000: return ('FCVTNS_32D_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e610000: return ('FCVTNU_32D_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e620000: return ('SCVTF_D32_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e630000: return ('UCVTF_D32_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e640000: return ('FCVTAS_32D_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e650000: return ('FCVTAU_32D_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e680000: return ('FCVTPS_32D_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e690000: return ('FCVTPU_32D_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e700000: return ('FCVTMS_32D_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e710000: return ('FCVTMU_32D_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e780000: return ('FCVTZS_32D_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e790000: return ('FCVTZU_32D_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e7e0000: return ('FJCVTZS_32D_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1ee00000: return ('FCVTNS_32H_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1ee10000: return ('FCVTNU_32H_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1ee20000: return ('SCVTF_H32_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1ee30000: return ('UCVTF_H32_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1ee40000: return ('FCVTAS_32H_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1ee50000: return ('FCVTAU_32H_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1ee60000: return ('FMOV_32H_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1ee70000: return ('FMOV_H32_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1ee80000: return ('FCVTPS_32H_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1ee90000: return ('FCVTPU_32H_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1ef00000: return ('FCVTMS_32H_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1ef10000: return ('FCVTMU_32H_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1ef80000: return ('FCVTZS_32H_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1ef90000: return ('FCVTZU_32H_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9e200000: return ('FCVTNS_64S_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9e210000: return ('FCVTNU_64S_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9e220000: return ('SCVTF_S64_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9e230000: return ('UCVTF_S64_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9e240000: return ('FCVTAS_64S_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9e250000: return ('FCVTAU_64S_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9e280000: return ('FCVTPS_64S_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9e290000: return ('FCVTPU_64S_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9e300000: return ('FCVTMS_64S_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9e310000: return ('FCVTMU_64S_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9e380000: return ('FCVTZS_64S_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9e390000: return ('FCVTZU_64S_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9e600000: return ('FCVTNS_64D_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9e610000: return ('FCVTNU_64D_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9e620000: return ('SCVTF_D64_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9e630000: return ('UCVTF_D64_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9e640000: return ('FCVTAS_64D_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9e650000: return ('FCVTAU_64D_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9e660000: return ('FMOV_64D_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9e670000: return ('FMOV_D64_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9e680000: return ('FCVTPS_64D_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9e690000: return ('FCVTPU_64D_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9e700000: return ('FCVTMS_64D_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9e710000: return ('FCVTMU_64D_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9e780000: return ('FCVTZS_64D_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9e790000: return ('FCVTZU_64D_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9eae0000: return ('FMOV_64VX_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9eaf0000: return ('FMOV_V64I_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9ee00000: return ('FCVTNS_64H_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9ee10000: return ('FCVTNU_64H_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9ee20000: return ('SCVTF_H64_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9ee30000: return ('UCVTF_H64_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9ee40000: return ('FCVTAS_64H_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9ee50000: return ('FCVTAU_64H_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9ee60000: return ('FMOV_64H_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9ee70000: return ('FMOV_H64_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9ee80000: return ('FCVTPS_64H_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9ee90000: return ('FCVTPU_64H_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9ef00000: return ('FCVTMS_64H_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9ef10000: return ('FCVTMU_64H_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9ef80000: return ('FCVTZS_64H_float2int', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x9ef90000: return ('FCVTZU_64H_float2int', {'Rd': Rd, 'Rn': Rn})
    return decode_UNDEFINED(d)

def decode_cryptoaes(d):
    assert (d & 0xff3e0c00) == 0x4e280800
    Rd     = (d >> 0) & 0x1F
    Rn     = (d >> 5) & 0x1F
    opcode = (d >> 12) & 0x1F
    size   = (d >> 22) & 3
    if (d & 0xfffffc00) == 0x4e284800: return ('AESE_B_cryptoaes', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x4e285800: return ('AESD_B_cryptoaes', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x4e286800: return ('AESMC_B_cryptoaes', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x4e287800: return ('AESIMC_B_cryptoaes', {'Rd': Rd, 'Rn': Rn})
    return decode_UNDEFINED(d)

def decode_crypto4(d):
    assert (d & 0xff808000) == 0xce000000
    Op0    = (d >> 21) & 3
    Ra     = (d >> 10) & 0x1F
    Rd     = (d >> 0) & 0x1F
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    if (d & 0xffe08000) == 0xce000000: return ('EOR3_VVV16_crypto4', {'Ra': Ra, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe08000) == 0xce200000: return ('BCAX_VVV16_crypto4', {'Ra': Ra, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe08000) == 0xce400000: return ('SM3SS1_VVV4_crypto4', {'Ra': Ra, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    return decode_UNDEFINED(d)

def decode_cryptosha3(d):
    assert (d & 0xff208c00) == 0x5e000000
    Rd     = (d >> 0) & 0x1F
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    opcode = (d >> 12) & 7
    size   = (d >> 22) & 3
    if (d & 0xffe0fc00) == 0x5e000000: return ('SHA1C_QSV_cryptosha3', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x5e001000: return ('SHA1P_QSV_cryptosha3', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x5e002000: return ('SHA1M_QSV_cryptosha3', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x5e003000: return ('SHA1SU0_VVV_cryptosha3', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x5e004000: return ('SHA256H_QQV_cryptosha3', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x5e005000: return ('SHA256H2_QQV_cryptosha3', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x5e006000: return ('SHA256SU1_VVV_cryptosha3', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    return decode_UNDEFINED(d)

def decode_cryptosha512_3(d):
    assert (d & 0xffe0b000) == 0xce608000
    O      = (d >> 14) & 1
    Rd     = (d >> 0) & 0x1F
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    opcode = (d >> 10) & 3
    if (d & 0xffe0fc00) == 0xce608000: return ('SHA512H_QQV_cryptosha512_3', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0xce608400: return ('SHA512H2_QQV_cryptosha512_3', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0xce608800: return ('SHA512SU1_VVV2_cryptosha512_3', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0xce608c00: return ('RAX1_VVV2_cryptosha512_3', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0xce60c000: return ('SM3PARTW1_VVV4_cryptosha512_3', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0xce60c400: return ('SM3PARTW2_VVV4_cryptosha512_3', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0xce60c800: return ('SM4EKEY_VVV4_cryptosha512_3', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    return decode_UNDEFINED(d)

def decode_crypto3_imm2(d):
    assert (d & 0xffe0c000) == 0xce408000
    Rd     = (d >> 0) & 0x1F
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    imm2   = (d >> 12) & 3
    opcode = (d >> 10) & 3
    if (d & 0xffe0cc00) == 0xce408000: return ('SM3TT1A_VVV4_crypto3_imm2', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm2': imm2})
    if (d & 0xffe0cc00) == 0xce408400: return ('SM3TT1B_VVV4_crypto3_imm2', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm2': imm2})
    if (d & 0xffe0cc00) == 0xce408800: return ('SM3TT2A_VVV4_crypto3_imm2', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm2': imm2})
    if (d & 0xffe0cc00) == 0xce408c00: return ('SM3TT2B_VVV_crypto3_imm2', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm2': imm2})
    return decode_UNDEFINED(d)

def decode_crypto3_imm6(d):
    assert (d & 0xffe00000) == 0xce800000
    Rd     = (d >> 0) & 0x1F
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    imm6   = (d >> 10) & 0x3F
    if (d & 0xffe00000) == 0xce800000: return ('XAR_VVV2_crypto3_imm6', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'imm6': imm6})
    return decode_UNDEFINED(d)

def decode_cryptosha2(d):
    assert (d & 0xff3e0c00) == 0x5e280800
    Rd     = (d >> 0) & 0x1F
    Rn     = (d >> 5) & 0x1F
    opcode = (d >> 12) & 0x1F
    size   = (d >> 22) & 3
    if (d & 0xfffffc00) == 0x5e280800: return ('SHA1H_SS_cryptosha2', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x5e281800: return ('SHA1SU1_VV_cryptosha2', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x5e282800: return ('SHA256SU0_VV_cryptosha2', {'Rd': Rd, 'Rn': Rn})
    return decode_UNDEFINED(d)

def decode_cryptosha512_2(d):
    assert (d & 0xfffff000) == 0xcec08000
    Rd     = (d >> 0) & 0x1F
    Rn     = (d >> 5) & 0x1F
    opcode = (d >> 10) & 3
    if (d & 0xfffffc00) == 0xcec08000: return ('SHA512SU0_VV2_cryptosha512_2', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0xcec08400: return ('SM4E_VV4_cryptosha512_2', {'Rd': Rd, 'Rn': Rn})
    return decode_UNDEFINED(d)

def decode_floatcmp(d):
    assert (d & 0x5f203c00) == 0x1e202000
    M      = (d >> 31) & 1
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    S      = (d >> 29) & 1
    op     = (d >> 14) & 3
    opcode2 = (d >> 0) & 0x1F
    type   = (d >> 22) & 3
    if (d & 0xffe0fc1f) == 0x1e202000: return ('FCMP_S_floatcmp', {'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc1f) == 0x1e202008: return ('FCMP_SZ_floatcmp', {'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc1f) == 0x1e202010: return ('FCMPE_S_floatcmp', {'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc1f) == 0x1e202018: return ('FCMPE_SZ_floatcmp', {'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc1f) == 0x1e602000: return ('FCMP_D_floatcmp', {'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc1f) == 0x1e602008: return ('FCMP_DZ_floatcmp', {'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc1f) == 0x1e602010: return ('FCMPE_D_floatcmp', {'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc1f) == 0x1e602018: return ('FCMPE_DZ_floatcmp', {'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc1f) == 0x1ee02000: return ('FCMP_H_floatcmp', {'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc1f) == 0x1ee02008: return ('FCMP_HZ_floatcmp', {'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc1f) == 0x1ee02010: return ('FCMPE_H_floatcmp', {'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc1f) == 0x1ee02018: return ('FCMPE_HZ_floatcmp', {'Rm': Rm, 'Rn': Rn})
    return decode_UNDEFINED(d)

def decode_floatccmp(d):
    assert (d & 0x5f200c00) == 0x1e200400
    M      = (d >> 31) & 1
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    S      = (d >> 29) & 1
    cond   = (d >> 12) & 0xF
    nzcv   = (d >> 0) & 0xF
    op     = (d >> 4) & 1
    type   = (d >> 22) & 3
    if (d & 0xffe00c10) == 0x1e200400: return ('FCCMP_S_floatccmp', {'Rm': Rm, 'Rn': Rn, 'cond': cond, 'nzcv': nzcv})
    if (d & 0xffe00c10) == 0x1e200410: return ('FCCMPE_S_floatccmp', {'Rm': Rm, 'Rn': Rn, 'cond': cond, 'nzcv': nzcv})
    if (d & 0xffe00c10) == 0x1e600400: return ('FCCMP_D_floatccmp', {'Rm': Rm, 'Rn': Rn, 'cond': cond, 'nzcv': nzcv})
    if (d & 0xffe00c10) == 0x1e600410: return ('FCCMPE_D_floatccmp', {'Rm': Rm, 'Rn': Rn, 'cond': cond, 'nzcv': nzcv})
    if (d & 0xffe00c10) == 0x1ee00400: return ('FCCMP_H_floatccmp', {'Rm': Rm, 'Rn': Rn, 'cond': cond, 'nzcv': nzcv})
    if (d & 0xffe00c10) == 0x1ee00410: return ('FCCMPE_H_floatccmp', {'Rm': Rm, 'Rn': Rn, 'cond': cond, 'nzcv': nzcv})
    return decode_UNDEFINED(d)

def decode_floatsel(d):
    assert (d & 0x5f200c00) == 0x1e200c00
    M      = (d >> 31) & 1
    Rd     = (d >> 0) & 0x1F
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    S      = (d >> 29) & 1
    cond   = (d >> 12) & 0xF
    type   = (d >> 22) & 3
    if (d & 0xffe00c00) == 0x1e200c00: return ('FCSEL_S_floatsel', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'cond': cond})
    if (d & 0xffe00c00) == 0x1e600c00: return ('FCSEL_D_floatsel', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'cond': cond})
    if (d & 0xffe00c00) == 0x1ee00c00: return ('FCSEL_H_floatsel', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn, 'cond': cond})
    return decode_UNDEFINED(d)

def decode_floatdp1(d):
    assert (d & 0x5f207c00) == 0x1e204000
    M      = (d >> 31) & 1
    Rd     = (d >> 0) & 0x1F
    Rn     = (d >> 5) & 0x1F
    S      = (d >> 29) & 1
    opcode = (d >> 15) & 0x3F
    type   = (d >> 22) & 3
    if (d & 0xfffffc00) == 0x1e204000: return ('FMOV_S_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e20c000: return ('FABS_S_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e214000: return ('FNEG_S_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e21c000: return ('FSQRT_S_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e22c000: return ('FCVT_DS_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e23c000: return ('FCVT_HS_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e244000: return ('FRINTN_S_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e24c000: return ('FRINTP_S_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e254000: return ('FRINTM_S_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e25c000: return ('FRINTZ_S_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e264000: return ('FRINTA_S_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e274000: return ('FRINTX_S_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e27c000: return ('FRINTI_S_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e604000: return ('FMOV_D_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e60c000: return ('FABS_D_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e614000: return ('FNEG_D_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e61c000: return ('FSQRT_D_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e624000: return ('FCVT_SD_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e63c000: return ('FCVT_HD_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e644000: return ('FRINTN_D_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e64c000: return ('FRINTP_D_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e654000: return ('FRINTM_D_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e65c000: return ('FRINTZ_D_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e664000: return ('FRINTA_D_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e674000: return ('FRINTX_D_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1e67c000: return ('FRINTI_D_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1ee04000: return ('FMOV_H_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1ee0c000: return ('FABS_H_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1ee14000: return ('FNEG_H_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1ee1c000: return ('FSQRT_H_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1ee24000: return ('FCVT_SH_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1ee2c000: return ('FCVT_DH_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1ee44000: return ('FRINTN_H_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1ee4c000: return ('FRINTP_H_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1ee54000: return ('FRINTM_H_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1ee5c000: return ('FRINTZ_H_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1ee64000: return ('FRINTA_H_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1ee74000: return ('FRINTX_H_floatdp1', {'Rd': Rd, 'Rn': Rn})
    if (d & 0xfffffc00) == 0x1ee7c000: return ('FRINTI_H_floatdp1', {'Rd': Rd, 'Rn': Rn})
    return decode_UNDEFINED(d)

def decode_floatdp2(d):
    assert (d & 0x5f200c00) == 0x1e200800
    M      = (d >> 31) & 1
    Rd     = (d >> 0) & 0x1F
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    S      = (d >> 29) & 1
    opcode = (d >> 12) & 0xF
    type   = (d >> 22) & 3
    if (d & 0xffe0fc00) == 0x1e200800: return ('FMUL_S_floatdp2', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1e201800: return ('FDIV_S_floatdp2', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1e202800: return ('FADD_S_floatdp2', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1e203800: return ('FSUB_S_floatdp2', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1e204800: return ('FMAX_S_floatdp2', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1e205800: return ('FMIN_S_floatdp2', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1e206800: return ('FMAXNM_S_floatdp2', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1e207800: return ('FMINNM_S_floatdp2', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1e208800: return ('FNMUL_S_floatdp2', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1e600800: return ('FMUL_D_floatdp2', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1e601800: return ('FDIV_D_floatdp2', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1e602800: return ('FADD_D_floatdp2', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1e603800: return ('FSUB_D_floatdp2', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1e604800: return ('FMAX_D_floatdp2', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1e605800: return ('FMIN_D_floatdp2', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1e606800: return ('FMAXNM_D_floatdp2', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1e607800: return ('FMINNM_D_floatdp2', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1e608800: return ('FNMUL_D_floatdp2', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1ee00800: return ('FMUL_H_floatdp2', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1ee01800: return ('FDIV_H_floatdp2', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1ee02800: return ('FADD_H_floatdp2', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1ee03800: return ('FSUB_H_floatdp2', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1ee04800: return ('FMAX_H_floatdp2', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1ee05800: return ('FMIN_H_floatdp2', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1ee06800: return ('FMAXNM_H_floatdp2', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1ee07800: return ('FMINNM_H_floatdp2', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe0fc00) == 0x1ee08800: return ('FNMUL_H_floatdp2', {'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    return decode_UNDEFINED(d)

def decode_floatdp3(d):
    assert (d & 0x5f000000) == 0x1f000000
    M      = (d >> 31) & 1
    Ra     = (d >> 10) & 0x1F
    Rd     = (d >> 0) & 0x1F
    Rm     = (d >> 16) & 0x1F
    Rn     = (d >> 5) & 0x1F
    S      = (d >> 29) & 1
    o0     = (d >> 15) & 1
    o1     = (d >> 21) & 1
    type   = (d >> 22) & 3
    if (d & 0xffe08000) == 0x1f000000: return ('FMADD_S_floatdp3', {'Ra': Ra, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe08000) == 0x1f008000: return ('FMSUB_S_floatdp3', {'Ra': Ra, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe08000) == 0x1f200000: return ('FNMADD_S_floatdp3', {'Ra': Ra, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe08000) == 0x1f208000: return ('FNMSUB_S_floatdp3', {'Ra': Ra, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe08000) == 0x1f400000: return ('FMADD_D_floatdp3', {'Ra': Ra, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe08000) == 0x1f408000: return ('FMSUB_D_floatdp3', {'Ra': Ra, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe08000) == 0x1f600000: return ('FNMADD_D_floatdp3', {'Ra': Ra, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe08000) == 0x1f608000: return ('FNMSUB_D_floatdp3', {'Ra': Ra, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe08000) == 0x1fc00000: return ('FMADD_H_floatdp3', {'Ra': Ra, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe08000) == 0x1fc08000: return ('FMSUB_H_floatdp3', {'Ra': Ra, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe08000) == 0x1fe00000: return ('FNMADD_H_floatdp3', {'Ra': Ra, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    if (d & 0xffe08000) == 0x1fe08000: return ('FNMSUB_H_floatdp3', {'Ra': Ra, 'Rd': Rd, 'Rm': Rm, 'Rn': Rn})
    return decode_UNDEFINED(d)

def decode_floatimm(d):
    assert (d & 0x5f201c00) == 0x1e201000
    M      = (d >> 31) & 1
    Rd     = (d >> 0) & 0x1F
    S      = (d >> 29) & 1
    imm5   = (d >> 5) & 0x1F
    imm8   = (d >> 13) & 0xFF
    type   = (d >> 22) & 3
    if (d & 0xffe01fe0) == 0x1e201000: return ('FMOV_S_floatimm', {'Rd': Rd, 'imm8': imm8})
    if (d & 0xffe01fe0) == 0x1e601000: return ('FMOV_D_floatimm', {'Rd': Rd, 'imm8': imm8})
    if (d & 0xffe01fe0) == 0x1ee01000: return ('FMOV_H_floatimm', {'Rd': Rd, 'imm8': imm8})
    return decode_UNDEFINED(d)
