import talib
from talib import MA_Type


def get_talib_features(data):
    """
    TA-Libを使用して、テクニカル指標の特徴量を取得する。

    パラメータ:
        data (pandas.DataFrame): 'Open', 'High', 'Low', 'Close', 'Volume'を含むデータフレーム。

    リターン:
        pandas.DataFrame: 元のデータフレームにテクニカル指標の特徴量を追加したもの。
    """

    df = data.copy()
    op = df["Open"]
    hi = df["High"]
    lo = df["Low"]
    cl = df["Close"]
    vo = df["Volume"]

    # トレンド系指標の追加
    # ボリンジャーバンド
    df["BBANDS_upper"], df["BBANDS_middle"], df["BBANDS_lower"] = talib.BBANDS(
        cl, timeperiod=5, nbdevup=2, nbdevdn=2, matype=MA_Type.EMA
    )
    # 平均方向性指数
    df["ADX"] = talib.ADX(hi, lo, cl, timeperiod=14)
    # 移動平均収束拡散法
    df["MACD_macd"], df["MACD_macdsignal"], _ = talib.MACD(
        cl, fastperiod=12, slowperiod=26, signalperiod=9
    )

    # オシレーター系指標の追加
    # 相対力指数
    df["RSI"] = talib.RSI(cl, timeperiod=14)
    # ストキャスティック
    df["STOCH_slowk"], df["STOCH_slowd"] = talib.STOCH(
        hi,
        lo,
        cl,
        fastk_period=5,
        slowk_period=3,
        slowk_matype=0,
        slowd_period=3,
        slowd_matype=0,
    )

    return df
