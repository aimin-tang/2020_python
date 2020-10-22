from merge_the_tools.src import merge_the_tools
import os
import unittest.mock as mock

def test_merge_the_tools():
    string = 'AABCAAADA'
    k = 3
    result = merge_the_tools.merge_the_tools(string, k)
    assert result == 'AB\nCA\nAD'

def test_merge_the_tools2():
    string = 'BBWMNAKIJIWBHMOZHIMAXVIGQQYZWMOYPLMCNWKXEIYNVNMEVZEVUODMHELDSADHLPLYLVVSFUFCJSJGTPBNEHCNLNSDPWMCLXBZSYTZUYCFSLMLAPBGWFTHSMMKKYMXVPWPOPPKQTQKEEWETZLQEGZYUOIEOVCMKABASSNILFSPJQWERJWXRYWMMGQCDUOQVQQNKFXYKRNVKLABWWZOWXAKFSNJNBBKTRZEZWCJPRFZFHDBFERCBRMIMBTBDULWOKCNIEYXYFZDMCGUGYYJRMTDONERJRPXDSMLWLLWSKBHOIBUIZFZNYFBLJSVDIUGCJUYWHXOTYVHIWDQXIQLIVOUGJRLTNUVWOTSVSJQTEXBDCSCMKNUHEQPNJBGXVBVLWQIPZYIDXLGZDJLPYFWCWMRFPXEKAAXXSFORDYUAJDBPOMEOTBRRPKZEIFQKHNHZSXQXVNZFSAUGOYUJBNBQYCWIJOSRBCQVZJSVYRCQTWYHWSRYIUQIYPQHDKYHMRCOCXJAQLQKJQTHIMHSIAAGPSQUDQBRHEFLDQLTDDFMTZWENDWYDZESRWNUNQOWUTIXKVTNBYCUZYAPBZNHYTBRQQMFHCDBVNBHLWXMWZIWZJNCKAJIVNZNDNSKPYMNNPUYLRKHSTFTCSWMUHWQUXDYNYIEWWTLLOKYHUICPNVRITFCDDUXDAXSYIWWEQHSGRSPOATDQPXYKECNKZNNZKFXSDVZVETDWLVMMORCFOCQVGDFFSSEDZDXEYYADRFBFAPRPGVUVZMQFQXNKRRPQVNWVNYAHEBMGQFVXASUBEMIWJVHANWSKLOHBNIITLUZCZXBBRXCXLMWUIFWXDQHPEQSTYAOKWQOVNRWGOADZMZVWETTIJCZNTRJTTZDPPRKCIIKYKOZYPUVWNQEYVFMOYXJTWNIMGUQREBPQRROINLEDEKBZPPPPMYILNSZUMRNSUCILVZUJKAMQLNPADESRFAESTDOHVBAPGKDBJZKWZYMKMCNRIFKNHPIASWKPYMFGWIHGHUEGSQTGUGZDLKSSBCVTZFJZTQFPAOXJIBRBSKJOQJTDVMYWQTRPAAQTSXKSMIDULVXFFHUYQNDLBBHSUYJWBAPVXCQJKTGXQDDYKXWCKZPODWGZXPWAPNXPPNYBJEZZKCXUBVXNXMBALHZKXXMOLJDAZEEKKDJUHJPIGOVDCXFPEHZDENSPZXSABWKMBVIIGZQNNNSSKYHRFJULWOBXMVXPRJDUFMCLLUABJTVUTCNANJLKAOJMJHDCQHWXTALGWLJGGEAZHPZUYNGYBSMLZQPRZMRSOEALRKRYOTZXIBSIOAJRSXETNUNOIGGWKJJBTABHTBFDEZOSBXLWUQPKMEYUKHSUQCYJCZSYCZDGYRYCQMYNCPXOUXKGECBWGBHLAALDBOJCIKEYYCLARKQNICUOEXLNYSYAUJFWXRYHBCIBGTBZGTNQVHEBGPOEKOEEXMCXDAEGEMHKIIKQDZGAGKBMCSSMGYSGKVDNVJTCWAMGKYWPXCPFOTRQLLETMZZWUCMRMHTKKISUGOMESBJIUDBHOFBAECZAHLUVSNFEVZBCPNIHORRLUSULAVLEAMHHXBCSQJWMIZQXMYGDRXOMQIXQGKWIXFPWGRQZAPNKOFHBFNGWMWKCGHUOUTWTALRJEIIGZVQPAZSFMYDZUODBVAPRVMMVZEEGOOMPJFELEXSTVWUSKZTHZKBWYNUATYGHPSWYZBMEAEXVCTNMSIWSVXQTKKTELZNAUMAVPMZPTYMXRCMKKIEFFWBRHUXSWNUSZUNQJPFCPRBJTNTGVZNCVOWEJTWHGQBHNOXWFEAVYBGTPBZMAPPXDLCOGAVNTYWGNWCUAERAFXUUYVHAKYYOJCEPCCEXADDPZHKBLBETBYPZVYAGWAWHCCZGEDGFILUJTGNGKRZLRRMMPOUMOSTSVSBBYHGGSDSNLFUXWVINMXBELWQAQLULGVNECVMVAEIOLELHCWWQTYUEUMGKYBYGWNKZKYWLFGBQNMAPIWFBUCGOOOBOPBUMOGNYHLLMRMEEZEVJBDLVFTMVHPKZQGLGNAEWLQKEEOLDVGPWLATQVHOEYADQGQWVQDRDTBKZSVFNDULRWGJRQXVOXBHGRDBKGVNBYZBQWGFCASTWZCPRAMHZNOFFSJPAEECCEFTANACPTVNSACLCOSBEHJLBSADWGHYMMTNZURQNPDHPFSRWMUCTDNWVPATVHSIWNXXHOOWDRFUZZNXMIZHLMEJBGCYPWILKFJTWZQBQXWRXJOLTNSFBYQEGUDWRLHDTSWPTOQMMODLYSWTHQYLPQPVLUREIBHBVFSPUKBIZGVZARSKJTVYLKWYFPCNSLQORIFNUIXTQSURLPBUKWVVIRWNGYCBMSRDCWSXGPSWJPPWEQSQONNXEJKNIPOUHFZMDTJLKDJVSZRYPJOEZCBDLNSVEIROPSAULLHVORQJQJHHTYLSCOXNESLICEWUXYOIJWGAPYJFISMDQAXSQWIUQVFVZDPWCFHNDPPSNYXXTMCJMBECAOZQLGNKJCJNISDNHSGWRFWKTAVFEBKERLWCRKNCOYQWQVMZNSXGZTSTWOAARMEJZALQMAVBYNZQILPVFNCHIWAGMCGERKNQNAHBBECBRCSZPJUXYYEJVGPHIWNZIAQXDZZEDDFUHZVXJRUJQYSNEIWOEKQOMGMPHNVMQDIYEDVNURXMRRZXZYLFIDUWJIMSVJELMOJRRGGOZFAQXCPYADEIGAESISKDERQQFAJZISNIZNYWROXRTBBZBIRLACQEVGXCGIBRCOZCEZAXPXPIAQIDYZOBDEHALGDTPEKRVJVBJWYAVPJWGRZGSQJWURWHXZDOGPIDZDEKBEMXUVVCMUIFMSDHLZQIBVZHLHKMKQYOUKNOGIQSCBZPVCYGEQQFMPOXYAJLSHZMRMDZUVSYYTPTWPBAGUHULVRKXCVPLUDEIIEEEYCERUANJBPRVWLHTCTQGOFRKLWSTAWZYAERUEFEHUVFTJOMNHDUVKNHVJZRLXQLZUDUAKAIGXNZGBMUIRQFDDMBPNSCMIQLDTHDFJNNJANRBBNLUFSXJEYATQCHBSVGNELSOZIZZVSDYGQSLJRWPSWLIZSLTNRHSDBICJJDGBIEJZYXKSTBKSMSTFEMUXTMAVWEGFINHQTSRSPDKLFUDROWYUITSCHUZGZFLHUUZONTGEWSPDOSVCOVZZQRDYNEEMLRTGOVUBQCHMWXQKRNMGINHBGKZUOFGBWCHMZDNPFXBBUTNLICTTPCUWMVQCAYEYANLZRAOYXSCTNPHWRARHFLFRIVWITCIWPVVIYMHXGJRTAARSCKBHVGZDDXNYZYUQTSZRGGRMRIHRIBLKLMUJUTOZSCYRCUJVOIPUQGIJQSDATOMGDGPZBEZTIZMMTWJIGYEZGPIYJLAECNKHVCGZIFSQEHCAFNKNMQMUHVVQIVUMKHTGJAFRHZJOINQNAADOSPJAMGQVBNHOUBWDDBUMCDCNQSCQSFFLVQNHYDCZQMPMPLPSOLGTOJGGBIZWOGJJYWSWBXXSJNGYYWSPJYIAJOGLWHJKNSVNOOJPLHJWWQWWOQLXQTXAJGNGNWSDOQQEGCTTLFPHXNFLDRKTMITWOIEDEYGUOZYUBUNOZEVWRCJUTTOIDJERSKXYIFTXERTHLHVMNSIFVTZQNPYQBEKTOHRZMMYTERCPAYCOSMTNIUGVKENNLZIBGBAVOYQSQSJSSNGLAZAIWGFGNUVAUDBCEEZSCPMUKWNEJTPLVSVRAAZNXUPRZRTDVVYZMKWWGJBSESDBKZSLBTAYPSROJNUGISHUCDTLMWDTOIUBJPOLKQLAIDQTSKZACHWHKRUZNZUEHOHTFVEQNRSWWIROTRQXAPGMGANWBHALYHEFEKVRBPPYYHORAHQAWXOCZEYBLAOLHSTLCOFDEUDEBUXBBNDXKUBMYAPLCDZKVSXZIEEOZISCCPEDDJCPDDDDFSPIXOUUGTTOYYDXIXZKNFPSPTHUWLYCFPKDFEZLXTBXTGUBEWNTBELSXSPTFPXNEHSJNRWNMXKFGHIMDXFGBQBYKQUSFRFLBZWQQSFFRSMZBVLGSQMWGPURHQLOKQZNPVDHPLMJDBIGWUMQKAMTQJMXZXMLNNYELENAPCJUDSAZOORYOERENFEOCSARFYVQELTVNEPQWRRMFILWMECBKGQOYQGEQDWXOPSBUKTSDKFJVSHHYJLKQBZQTFWLITIXKBAGLUZOEGZZAGJYSUJKXKAQRXBBSKAENBLYVMOBSQDSYOSQKDAHNDXECAGUKIAXJLXGXOKREPJEDEVNHXWVATBCTJYGSZFDKFKKTWBZLNDORADYYZVYUXDPGDVACDEPIQBDMCCXRHNIIQJGREGLDLAMPYMTBQKJGLMSQQRHXESFWBNNFUYJHBVWZJSCCCNIOBDERWLOBDWXGJLOFLXNOULNDDRFGEQUFVAWRNNUTJSZUFNAQMPFGAUMEMTMSLIAIIWAVLUOWOQRTDTKQKRYKNMQBIEUTMUCWSEUGAKCPAVKGQUWANWNBLFCTKYOWUSVNYPTZZXQAVAGLXEOKCBNNGSISQXRNRMAQBVRASHCNHIBGOPTRSGGAAPTTOKGFYGXZDOBVVELFMOLBDEUXNAXNPSIFEONCWKDZZFXUJKZXYNADRUCGXZUOUEUYTHBRRERQLQNUCOUABUFVRHBOIXCCCYDXFGOZMHRYXEUZTOBWLIRERTSCSWEUVJRCPGBCNTANZWOULSRYAICUDWWWSCQPMKSBQVFFQHUQEJKRDDPFMTZRPVNHAGZOQRRIOXPFEKXIVJBYNQDBJDSAAIKCOJQGAIQOFFVLPSWMCXKPQOSBTKCTUMYIXOQZYGPFMLRDDPQHMAYCQQGJDIFXWDITTYSSFJXTUQWAFOJSRIWHACTDMABIFJDAHXSOHSHDIGFOUPINXGVXJQDXSEGXPLXYLSNSKWXSCDIZSSMRZJQIBTFTZNSOBQNMKCGUYDODGZCAROTQAKABFIVFXNTYFIKPMSLLWCOEBSHUIANIKNKQXFXVUQVABIRNAFAWHQDKIKGRMTZXJLPGQODNGZPHHGXHLXGUOLEWVLPHGPGPAXWTLBISAXBJFYTRYBNMMSKJFASLRZBTYZOMCWGFVHOBIJUGKHUWBEHGEAUXZVRZWHLYERDBBUCLDWROELMHRWOYWIVXFOWDWKBCDHDEDGPGEIWKVLSNHINDQKAXZYAXIDZMKCSNKKWRSUBQFVFODSRVCTSDSSAAWZOIEHYORUHLQLBWGGKMAEHDXAGRUHUSIIBMPBDGXKUNVVLECWQECXHZZQRUZLOHVPWLSBTPLNFJLQNNMDTQCBQCTJYUWMDREZEWAYOONTXYLMNAPHQTKGVFRVZNICHOCLMELCSBXRZJDPJUWZOIILNBHMRR'
    k = 5424
    result = merge_the_tools.merge_the_tools(string, k)
    assert result == 'BWMNAKIJHOZXVGQYPLCEUDSFTR'

class CheckConfig(object):
    def __init__(self, config):
        self.config = self._check_input_data(config)

    def _check_input_data(self, data):
        if isinstance(data, list):
            return self._parse(data)
        elif os.path.isfile(data):
            with open(data) as f:
                return self._parse(f.readlines())

    def _parse(self, data):
        return data

@mock.patch('os.path.isfile')
def test_CheckConfig_with_file(mock_isfile):
    mock_isfile.return_value = True
    config_data = mock.mock_open(read_data='data')
    with mock.patch('mymodule.open', config_data) as mock_open:
        expected = parsed_file_data
        actual = CheckConfig('mocked/filename').config
        assert expected == actual