#System
from typing import Union, Dict


#Other libraries
from flet import FontWeight


class ApplicationSettings:

    #General
    title_application: str = "Finance"
    weight_application: int = 800
    height_application: int = 600
    resizable_window: bool = False

    #Field
    field_width = 400

    #Error
    error_color: str = "red"
    error_text_weight: FontWeight = FontWeight.W_500

    #Buttons
    #Filled
    bg_color: str = "blue"
    color: str = "black"
    #Outline
    bd_color_outl: str = "blue"
    width_outl_btn: int = 250
    width_outl_btn_2: int = 150

    #DropDown
    dr_down_weight: int = 120

    #Wiki Application
    coin_value_data: Dict[str, Union[int, str]] = {
        "USD": "United States Dollar, курс доллара (Американский)",
        "AUD": "Australian Dollar, курс доллара (Австралийского)",
        "RUB": "Russian Ruble, курс русского рубля",
        "EUR": "Euro, курс евро",
        "AMD": "Armenian Dram, курс армянского драма",
        "CNY": "Chinese Yuan, курс китайского юаня",
        "JPY": "Japanese Yen, курс японского йена",
        "NOK": "Norwegian Krone, курс норвежского крона",
        "SEK": "Swedish Krona, курс шведского крона",
        "UAH": "Ukrainian Hryvnia, курс украинской гривны",
        "PLN": "Polish Zloty, курс польской злоты"
    }

    crypt_coin_value_data: Dict[str, Union[int, str]] = {
        'Bitcoin': 'Актуальный курс Bitcoin',
        'Ethereum': 'Актуальный курс Ethereum',
        'Tether': 'Актуальный курс Tether',
        'BNB': 'Актуальный курс BNB',
        'Solana': 'Актуальный курс Solana',
        'USDC': 'Актуальный курс USDC',
        'Lido Staked Ether': 'Актуальный курс Lido Staked Ether',
        'XRP': 'Актуальный курс XRP',
        'Toncoin': 'Актуальный курс Toncoin',
        'Dogecoin': 'Актуальный курс Dogecoin',
        'Cardano': 'Актуальный курс Cardano',
        'TRON': 'Актуальный курс TRON',
        'Avalanche': 'Актуальный курс Avalanche',
        'SHIBA INU': 'Актуальный курс SHIBA INU',
        'Wrapped Bitcoin': 'Актуальный курс Wrapped Bitcoin',
        'Polkadot': 'Актуальный курс Polkadot',
        'ChainLink': 'Актуальный курс ChainLink',
        'Bitcoin Cash': 'Актуальный курс Bitcoin Cash',
        'Uniswap': 'Актуальный курс Uniswap',
        'Near Protocol': 'Актуальный курс Near Protocol',
        'Litecoin': 'Актуальный курс Litecoin',
        'UNUS SED LEO': 'Актуальный курс UNUS SED LEO',
        'Dai': 'Актуальный курс Dai',
        'Polygon': 'Актуальный курс Polygon',
        'Wrapped eETH': 'Актуальный курс Wrapped eETH',
        'Pepe': 'Актуальный курс Pepe',
        'Kaspa': 'Актуальный курс Kaspa',
        'Ethena USDe': 'Актуальный курс Ethena USDe',
        'Internet Computer': 'Актуальный курс Internet Computer',
        'Ethereum Classic': 'Актуальный курс Ethereum Classic',
        'Artificial Superintelligence Alliance': 'Актуальный курс Artificial Superintelligence Alliance',
        'Monero': 'Актуальный курс Monero',
        'Aptos': 'Актуальный курс Aptos',
        'Render': 'Актуальный курс Render',
        'Stellar': 'Актуальный курс Stellar',
        'Hedera': 'Актуальный курс Hedera',
        'OKB': 'Актуальный курс OKB',
        'Cosmos Hub': 'Актуальный курс Cosmos Hub',
        'Arbitrum': 'Актуальный курс Arbitrum',
        'Mantle': 'Актуальный курс Mantle',
        'Cronos': 'Актуальный курс Cronos',
        'Stacks': 'Актуальный курс Stacks',
        'Filecoin': 'Актуальный курс Filecoin',
        'Immutable': 'Актуальный курс Immutable',
        'Maker': 'Актуальный курс Maker',
        'Injective': 'Актуальный курс Injective',
        'VeChain': 'Актуальный курс VeChain',
        'First Digital USD': 'Актуальный курс First Digital USD',
        'Sui': 'Актуальный курс Sui',
        'The Graph': 'Актуальный курс The Graph',
        'dogwifhat': 'Актуальный курс dogwifhat',
        'Optimism': 'Актуальный курс Optimism',
        'Arweave': 'Актуальный курс Arweave',
        'Bittensor': 'Актуальный курс Bittensor',
        'Ondo Finance': 'Актуальный курс Ondo Finance',
        'Bitget Token': 'Актуальный курс Bitget Token',
        'FLOKI': 'Актуальный курс FLOKI',
        'Lido': 'Актуальный курс Lido',
        'Bonk': 'Актуальный курс Bonk',
        'Theta Network': 'Актуальный курс Theta Network',
        'Based Brett': 'Актуальный курс Based Brett',
        'Fantom': 'Актуальный курс Fantom',
        'WhiteBIT Coin': 'Актуальный курс WhiteBIT Coin',
        'Notcoin': 'Актуальный курс Notcoin',
        'THORChain': 'Актуальный курс THORChain',
        'Aave': 'Актуальный курс Aave',
        'Jasmy': 'Актуальный курс Jasmy',
        'Algorand': 'Актуальный курс Algorand',
        'EOS': 'Актуальный курс EOS',
        'Pyth Network': 'Актуальный курс Pyth Network',
        'Quant': 'Актуальный курс Quant',
        'Core DAO': 'Актуальный курс Core DAO',
        'Jupiter': 'Актуальный курс Jupiter',
        'Celestia': 'Актуальный курс Celestia',
        'GateToken': 'Актуальный курс GateToken',
        'Flare': 'Актуальный курс Flare',
        'Sei': 'Актуальный курс Sei',
        'Gala': 'Актуальный курс Gala',
        'KuCoin Token': 'Актуальный курс KuCoin Token',
        'Flow': 'Актуальный курс Flow',
        'Axie Infinity': 'Актуальный курс Axie Infinity',
        'MultiversX': 'Актуальный курс MultiversX',
        'Beam': 'Актуальный курс Beam',
        'Bitcoin SV': 'Актуальный курс Bitcoin SV',
        'Ethereum Name Service': 'Актуальный курс Ethereum Name Service',
        'StarkNet': 'Актуальный курс StarkNet',
        'BitTorrent (new)': 'Актуальный курс BitTorrent (new)',
        'NEO': 'Актуальный курс NEO',
        'Marinade Staked SOL': 'Актуальный курс Marinade Staked SOL',
        'Akash Network': 'Актуальный курс Akash Network',
        'ORDI': 'Актуальный курс ORDI',
        'Tezos': 'Актуальный курс Tezos',
        'USDD': 'Актуальный курс USDD',
        'The Sandbox': 'Актуальный курс The Sandbox',
        'Gnosis': 'Актуальный курс Gnosis',
        'Fasttoken': 'Актуальный курс Fasttoken',
        'Ethena': 'Актуальный курс Ethena',
        'MANTRA': 'Актуальный курс MANTRA',
        'zkSync': 'Актуальный курс zkSync',
        'Conflux': 'Актуальный курс Conflux'
    }