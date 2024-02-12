from concurrent.futures import ThreadPoolExecutor
import with_api_parser
import without_api_parser

# Created: Thursday, September 1, 2022, 2:05:40 PM


class AllPairsGetter:

    def get_all_pairs(self) -> dict:
        with ThreadPoolExecutor(max_workers=50) as executor:
            all_pairs = {}
            deepcoin_pairs = executor.submit(without_api_parser.DeepCoin().get_trading_pairs)
            phemex_pairs = executor.submit(without_api_parser.Phemex().get_trading_pairs)
            # coinw_pairs = executor.submit(without_api_parser.CoinW().get_trading_pairs)
            xt = executor.submit(with_api_parser.XT().get_trading_pairs)
            okx = executor.submit(with_api_parser.OKX().get_trading_pairs)
            mexc = executor.submit(with_api_parser.MEXC().get_trading_pairs)
            whitebit = executor.submit(with_api_parser.WhiteBit().get_trading_pairs)
            kucoin = executor.submit(with_api_parser.Kucoin().get_trading_pairs)
            hotcoin = executor.submit(with_api_parser.HotCoin().get_trading_pairs)
            bybit = executor.submit(with_api_parser.Bybit().get_trading_pairs)
            huobi = executor.submit(with_api_parser.Huobi().get_trading_pairs)
            bitrue = executor.submit(with_api_parser.Bitrue().get_trading_pairs)
            lbank = executor.submit(with_api_parser.LBank().get_trading_pairs)
            ascendex = executor.submit(with_api_parser.AscendEX().get_trading_pairs)
            # bigone = executor.submit(with_api_parser.BigONE().get_trading_pairs)
            bkex = executor.submit(with_api_parser.BKEX().get_trading_pairs)
            bingx = executor.submit(with_api_parser.BingX().get_trading_pairs)
            exmo = executor.submit(with_api_parser.Exmo().get_trading_pairs)
            poloniex = executor.submit(with_api_parser.Poloniex().get_trading_pairs)
            digifinex = executor.submit(with_api_parser.Digifinex().get_trading_pairs)
            # tapbit = executor.submit(with_api_parser.Tapbit().get_trading_pairs)
            fmfw = executor.submit(with_api_parser.FMFW().get_trading_pairs)
            aax = executor.submit(with_api_parser.AAX().get_trading_pairs)
            all_pairs['XT'] = xt.result()
            all_pairs['OKX'] = okx.result()
            all_pairs['MEXC'] = mexc.result()
            all_pairs['WhiteBit'] = whitebit.result()
            all_pairs['Kucoin'] = kucoin.result()
            all_pairs['HotCoin'] = hotcoin.result()
            all_pairs['Bybit'] = bybit.result()
            all_pairs['Huobi'] = huobi.result()
            all_pairs['Bitrue'] = bitrue.result()
            all_pairs['Lbank'] = lbank.result()
            all_pairs['AscendEX'] = ascendex.result()
            # all_pairs['BigONE'] = bigone.result()
            all_pairs['BKEX'] = bkex.result()
            all_pairs['BingX'] = bingx.result()
            all_pairs['EXMO'] = exmo.result()
            all_pairs['Poloniex'] = poloniex.result()
            all_pairs['Digifinex'] = digifinex.result()
            # all_pairs['Tapbit'] = tapbit.result()
            all_pairs['FMFW'] = fmfw.result()
            all_pairs['AAX'] = aax.result()
            all_pairs['DeepCoin'] = deepcoin_pairs.result()
            # all_pairs['CoinW'] = coinw_pairs.result()
            all_pairs['Phemex'] = phemex_pairs.result()
            return all_pairs
