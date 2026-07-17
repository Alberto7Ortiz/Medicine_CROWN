class  Commands:

    #ADS1256 commands """
    CMD_WAKEUP   = 0b11111111
    CMD_RDATA    = 0b00000001
    CMD_RDTAC    = 0b00000011
    CMD_SDATAC   = 0b00001111
    CMD_RREG     = 0b00010000
    CMD_WREG     = 0b01010000
    CMD_SELFCAL  = 0b11110000
    CMD_SELFOCAL = 0b11110001
    CMD_SELFGCAL = 0b11110010
    CMD_SYSOCAL  = 0b11110011
    CMD_SYSGCAL  = 0b11110100
    CMD_SYNC     = 0b11111100
    CMD_STANDBY  = 0b11111101
    CMD_RESET    = 0b11111110

    # ADS1256 resgister """
    REG_STATUS = 0x00
    REG_MUX    = 0x01
    REG_ADCON  = 0x02
    REG_DRATE  = 0x03
    REG_IO     = 0x04
    REG_OFC0   = 0x05
    REG_OFC1   = 0x06
    REG_OFC2   = 0x07
    REG_FSC0   = 0x08
    REG_FSC1   = 0x09
    REG_FSC2   = 0x0A



    #First configuration
    INI_STATUS = 0b01000111    #(0100) factory programed xxxx, (0 MSB or 1 LSB) order x, (0 auto_cal_dis or 1 auto_cal_enb) ACAL x, (0 dis or 1 enb) BUFFEN x, 1 (read only) DRDY x
    INI_MUX    = 0b00010000    #AIN1 Postive and AIN0 Negative
    INI_ADCON  = 0b00100000    # bit 7 reserved, bit 6-5 CLK(01)Fclkin/1, bit 4-2 Sensor Detect Current Source (00) off, Bits 2-0 Programable Gain Amplifier Setting (000) = 1 
    INI_DRATE  = 0b00000010    #100 SPS 