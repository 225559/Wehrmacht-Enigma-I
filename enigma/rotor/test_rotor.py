import unittest
import rotor

class TestRotor(unittest.TestCase):
    """TestRotor ...
    """

    def test_init(self):
        tt = [
            {"rotor" : 1, "expected" : "EKMFLGDQVZNTOWYHXUSPAIBRCJ"},
            {"rotor" : 2, "expected" : "AJDKSIRUXBLHWTMCQGZNPYFVOE"},
            {"rotor" : 3, "expected" : "BDFHJLCPRTXVZNYEIWGAKMUSQO"},            
        ]
        for tc in tt:
            rtor = rotor.Rotor(tc["rotor"])
            self.assertEqual(tc["expected"], rtor.rotor)

    def test_ring_setting(self):
        tt = [
            # Test all ring settings for rotor I
            {"rotor" : 1, "ring_setting" : 'A', "expected" : "EKMFLGDQVZNTOWYHXUSPAIBRCJ"},
            {"rotor" : 1, "ring_setting" : 'B', "expected" : "KFLNGMHERWAOUPXZIYVTQBJCSD"},
            {"rotor" : 1, "ring_setting" : 'C', "expected" : "ELGMOHNIFSXBPVQYAJZWURCKDT"},
            {"rotor" : 1, "ring_setting" : 'D', "expected" : "UFMHNPIOJGTYCQWRZBKAXVSDLE"},
            {"rotor" : 1, "ring_setting" : 'E', "expected" : "FVGNIOQJPKHUZDRXSACLBYWTEM"},
            {"rotor" : 1, "ring_setting" : 'F', "expected" : "NGWHOJPRKQLIVAESYTBDMCZXUF"},
            {"rotor" : 1, "ring_setting" : 'G', "expected" : "GOHXIPKQSLRMJWBFTZUCENDAYV"},
            {"rotor" : 1, "ring_setting" : 'H', "expected" : "WHPIYJQLRTMSNKXCGUAVDFOEBZ"},
            {"rotor" : 1, "ring_setting" : 'I', "expected" : "AXIQJZKRMSUNTOLYDHVBWEGPFC"},
            {"rotor" : 1, "ring_setting" : 'J', "expected" : "DBYJRKALSNTVOUPMZEIWCXFHQG"},
            {"rotor" : 1, "ring_setting" : 'K', "expected" : "HECZKSLBMTOUWPVQNAFJXDYGIR"},
            {"rotor" : 1, "ring_setting" : 'L', "expected" : "SIFDALTMCNUPVXQWROBGKYEZHJ"},
            {"rotor" : 1, "ring_setting" : 'M', "expected" : "KTJGEBMUNDOVQWYRXSPCHLZFAI"},
            {"rotor" : 1, "ring_setting" : 'N', "expected" : "JLUKHFCNVOEPWRXZSYTQDIMAGB"},
            {"rotor" : 1, "ring_setting" : 'O', "expected" : "CKMVLIGDOWPFQXSYATZUREJNBH"},
            {"rotor" : 1, "ring_setting" : 'P', "expected" : "IDLNWMJHEPXQGRYTZBUAVSFKOC"},
            {"rotor" : 1, "ring_setting" : 'Q', "expected" : "DJEMOXNKIFQYRHSZUACVBWTGLP"},
            {"rotor" : 1, "ring_setting" : 'R', "expected" : "QEKFNPYOLJGRZSITAVBDWCXUHM"},
            {"rotor" : 1, "ring_setting" : 'S', "expected" : "NRFLGOQZPMKHSATJUBWCEXDYVI"},
            {"rotor" : 1, "ring_setting" : 'T', "expected" : "JOSGMHPRAQNLITBUKVCXDFYEZW"},
            {"rotor" : 1, "ring_setting" : 'U', "expected" : "XKPTHNIQSBROMJUCVLWDYEGZFA"},
            {"rotor" : 1, "ring_setting" : 'V', "expected" : "BYLQUIOJRTCSPNKVDWMXEZFHAG"},
            {"rotor" : 1, "ring_setting" : 'W', "expected" : "HCZMRVJPKSUDTQOLWEXNYFAGIB"},
            {"rotor" : 1, "ring_setting" : 'X', "expected" : "CIDANSWKQLTVEURPMXFYOZGBHJ"},
            {"rotor" : 1, "ring_setting" : 'Y', "expected" : "KDJEBOTXLRMUWFVSQNYGZPAHCI"},
            {"rotor" : 1, "ring_setting" : 'Z', "expected" : "JLEKFCPUYMSNVXGWTROZHAQBID"},

            # Test all ring settings for rotor II
            {"rotor" : 2, "ring_setting" : 'A', "expected" : "AJDKSIRUXBLHWTMCQGZNPYFVOE"},
            {"rotor" : 2, "ring_setting" : 'B', "expected" : "FBKELTJSVYCMIXUNDRHAOQZGWP"},
            {"rotor" : 2, "ring_setting" : 'C', "expected" : "QGCLFMUKTWZDNJYVOESIBPRAHX"},
            {"rotor" : 2, "ring_setting" : 'D', "expected" : "YRHDMGNVLUXAEOKZWPFTJCQSBI"},
            {"rotor" : 2, "ring_setting" : 'E', "expected" : "JZSIENHOWMVYBFPLAXQGUKDRTC"},
            {"rotor" : 2, "ring_setting" : 'F', "expected" : "DKATJFOIPXNWZCGQMBYRHVLESU"},
            {"rotor" : 2, "ring_setting" : 'G', "expected" : "VELBUKGPJQYOXADHRNCZSIWMFT"},
            {"rotor" : 2, "ring_setting" : 'H', "expected" : "UWFMCVLHQKRZPYBEISODATJXNG"},
            {"rotor" : 2, "ring_setting" : 'I', "expected" : "HVXGNDWMIRLSAQZCFJTPEBUKYO"},
            {"rotor" : 2, "ring_setting" : 'J', "expected" : "PIWYHOEXNJSMTBRADGKUQFCVLZ"},
            {"rotor" : 2, "ring_setting" : 'K', "expected" : "AQJXZIPFYOKTNUCSBEHLVRGDWM"},
            {"rotor" : 2, "ring_setting" : 'L', "expected" : "NBRKYAJQGZPLUOVDTCFIMWSHEX"},
            {"rotor" : 2, "ring_setting" : 'M', "expected" : "YOCSLZBKRHAQMVPWEUDGJNXTIF"},
            {"rotor" : 2, "ring_setting" : 'N', "expected" : "GZPDTMACLSIBRNWQXFVEHKOYUJ"},
            {"rotor" : 2, "ring_setting" : 'O', "expected" : "KHAQEUNBDMTJCSOXRYGWFILPZV"},
            {"rotor" : 2, "ring_setting" : 'P', "expected" : "WLIBRFVOCENUKDTPYSZHXGJMQA"},
            {"rotor" : 2, "ring_setting" : 'Q', "expected" : "BXMJCSGWPDFOVLEUQZTAIYHKNR"},
            {"rotor" : 2, "ring_setting" : 'R', "expected" : "SCYNKDTHXQEGPWMFVRAUBJZILO"},
            {"rotor" : 2, "ring_setting" : 'S', "expected" : "PTDZOLEUIYRFHQXNGWSBVCKAJM"},
            {"rotor" : 2, "ring_setting" : 'T', "expected" : "NQUEAPMFVJZSGIRYOHXTCWDLBK"},
            {"rotor" : 2, "ring_setting" : 'U', "expected" : "LORVFBQNGWKATHJSZPIYUDXEMC"},
            {"rotor" : 2, "ring_setting" : 'V', "expected" : "DMPSWGCROHXLBUIKTAQJZVEYFN"},
            {"rotor" : 2, "ring_setting" : 'W', "expected" : "OENQTXHDSPIYMCVJLUBRKAWFZG"},
            {"rotor" : 2, "ring_setting" : 'X', "expected" : "HPFORUYIETQJZNDWKMVCSLBXGA"},
            {"rotor" : 2, "ring_setting" : 'Y', "expected" : "BIQGPSVZJFURKAOEXLNWDTMCYH"},
            {"rotor" : 2, "ring_setting" : 'Z', "expected" : "ICJRHQTWAKGVSLBPFYMOXEUNDZ"},

            # Test all ring settings for rotor III
            {"rotor" : 3, "ring_setting" : 'A', "expected" : "BDFHJLCPRTXVZNYEIWGAKMUSQO"},
            {"rotor" : 3, "ring_setting" : 'B', "expected" : "PCEGIKMDQSUYWAOZFJXHBLNVTR"},
            {"rotor" : 3, "ring_setting" : 'C', "expected" : "SQDFHJLNERTVZXBPAGKYICMOWU"},
            {"rotor" : 3, "ring_setting" : 'D', "expected" : "VTREGIKMOFSUWAYCQBHLZJDNPX"},
            {"rotor" : 3, "ring_setting" : 'E', "expected" : "YWUSFHJLNPGTVXBZDRCIMAKEOQ"},
            {"rotor" : 3, "ring_setting" : 'F', "expected" : "RZXVTGIKMOQHUWYCAESDJNBLFP"},
            {"rotor" : 3, "ring_setting" : 'G', "expected" : "QSAYWUHJLNPRIVXZDBFTEKOCMG"},
            {"rotor" : 3, "ring_setting" : 'H', "expected" : "HRTBZXVIKMOQSJWYAECGUFLPDN"},
            {"rotor" : 3, "ring_setting" : 'I', "expected" : "OISUCAYWJLNPRTKXZBFDHVGMQE"},
            {"rotor" : 3, "ring_setting" : 'J', "expected" : "FPJTVDBZXKMOQSULYACGEIWHNR"},
            {"rotor" : 3, "ring_setting" : 'K', "expected" : "SGQKUWECAYLNPRTVMZBDHFJXIO"},
            {"rotor" : 3, "ring_setting" : 'L', "expected" : "PTHRLVXFDBZMOQSUWNACEIGKYJ"},
            {"rotor" : 3, "ring_setting" : 'M', "expected" : "KQUISMWYGECANPRTVXOBDFJHLZ"},
            {"rotor" : 3, "ring_setting" : 'N', "expected" : "ALRVJTNXZHFDBOQSUWYPCEGKIM"},
            {"rotor" : 3, "ring_setting" : 'O', "expected" : "NBMSWKUOYAIGECPRTVXZQDFHLJ"},
            {"rotor" : 3, "ring_setting" : 'P', "expected" : "KOCNTXLVPZBJHFDQSUWYAREGIM"},
            {"rotor" : 3, "ring_setting" : 'Q', "expected" : "NLPDOUYMWQACKIGERTVXZBSFHJ"},
            {"rotor" : 3, "ring_setting" : 'R', "expected" : "KOMQEPVZNXRBDLJHFSUWYACTGI"},
            {"rotor" : 3, "ring_setting" : 'S', "expected" : "JLPNRFQWAOYSCEMKIGTVXZBDUH"},
            {"rotor" : 3, "ring_setting" : 'T', "expected" : "IKMQOSGRXBPZTDFNLJHUWYACEV"},
            {"rotor" : 3, "ring_setting" : 'U', "expected" : "WJLNRPTHSYCQAUEGOMKIVXZBDF"},
            {"rotor" : 3, "ring_setting" : 'V', "expected" : "GXKMOSQUITZDRBVFHPNLJWYACE"},
            {"rotor" : 3, "ring_setting" : 'W', "expected" : "FHYLNPTRVJUAESCWGIQOMKXZBD"},
            {"rotor" : 3, "ring_setting" : 'X', "expected" : "EGIZMOQUSWKVBFTDXHJRPNLYAC"},
            {"rotor" : 3, "ring_setting" : 'Y', "expected" : "DFHJANPRVTXLWCGUEYIKSQOMZB"},
            {"rotor" : 3, "ring_setting" : 'Z', "expected" : "CEGIKBOQSWUYMXDHVFZJLTRPNA"},
        ]
        for tc in tt:
            rtor = rotor.Rotor(tc["rotor"])
            rtor.ring_setting(tc["ring_setting"])
            self.assertEqual(tc["expected"], rtor.rotor)
