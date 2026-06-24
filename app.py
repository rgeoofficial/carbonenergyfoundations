import streamlit as st
import numpy as np

# FUNÇÕES DO CENÁRIO 1

def ECO2_ES_1(Ap, Mae, fec, fea, ne, Ae, Le, Ned):
    return round((ne * Ae * Le * Ap * fec + Mae * fea) * Ned)

def DEP_ES_1(Ap, Mae, fdc, fda, ne, Ae, Le, Ned):
    return round((ne * Ae * Le * Ap * fdc + Mae * fda) * Ned)

def ECO2_RE_1(er, ne, Ae, Le, Ap, fec, Mar, Mae, fea, Ned):
    return round(((er + ne * Ae * Le) * (Ap * fec) + (Mar + Mae) * fea) * Ned)

def DEP_RE_1(er, ne, Ae, Le, Ap, fdc, Mar, Mae, fda, Ned):
    return round(((er + ne * Ae * Le) * (Ap * fdc) + (Mar + Mae) * fda) * Ned)

def ECO2_ME_1(Vbc, ne, Ap, fec, Ned):
    return round(Vbc * ne * Ap * fec * Ned)

def DEP_ME_1(Vbc, ne, Ap, fdc, Ned):
    return round(Vbc * ne * Ap * fdc * Ned)

# Radier

def Mat60r(tipoTela, Ap):
    if tipoTela == "Q-113":
        return 1.80 * Ap * 2 # SINAPI
    elif tipoTela == "Q-138":
        return 2.20 * Ap * 2 # SINAPI
    elif tipoTela == "Q-159":
        return 2.52 * Ap * 2 # SINAPI
    elif tipoTela == "Q-196":
        return 3.11 * Ap * 2 # SINAPI
    elif tipoTela == "Q-283":
        return 4.48 * Ap * 2 # SINAPI
    elif tipoTela == "Q-503":
        return 7.93 * Ap * 2 # Gerdau

def Mab50r(er, Ap):
    return 7850 * 0.60 * 0.01 * er * Ap

# Estaca

def Ae(geomEst, diamLado):
    if geomEst == "Quadrada":
        Ae = diamLado ** 2
    elif geomEst == "Circular":
        Ae = (np.pi / 4) * diamLado ** 2
    return round(Ae, 2)

def Msmin(diamLado, gammaAco): # Elementos de Fundações em Concreto por João Carlos de Campos
    Asmin = 0.4 * 0.01 * (np.pi / 4) * diamLado ** 2
    Vsmin = Asmin * 4 # 4 comprimento mínimo em estacas hélice contínua
    return round(Vsmin * gammaAco, 2)

# Blocos de coroamento

def Vbc(diamLado):
    return round(((diamLado + 0.2) ** 2) * 1.1 * diamLado, 2)

def Mab50bc(P, diamLado, fyk, gammaAco, c):
    h = 1.1 * diamLado
    Lbc = diamLado + 0.2
    Rst = 0.28 * P * (Lbc - diamLado) / (h - 0.1)
    gammas = 1.15
    fyd = fyk / gammas
    Ast = Rst / fyd # armadura horizontal nas duas direções
    Asv = 0.004 * Lbc ** 2 # armadura vertical mínima
    return round((2 * Ast * (Lbc - 2 * c) + Asv * (h - 2 * c)) * gammaAco, 2)

# FUNÇÕES DO CENÁRIO 2

def ECO2_RA(Ar, er, fec, Mat60r, Mab60r, fea60, Mab50r, fea50, Mac190r, fea190, Ned):
    return round((Ar * er * fec + (Mat60r + Mab60r) * fea60 + Mab50r * fea50 + Mac190r * fea190) * Ned)

def DEP_RA(Ar, er, fdc, Mat60r, Mab60r, fda60, Mab50r, fda50, Mac190r, fda190, Ned):
    return round((Ar * er * fdc + (Mat60r + Mab60r) * fda60 + Mab50r * fda50 + Mac190r * fda190) * Ned)

def ECO2_ES(Ve, fec, Mab50e, fea50, Mab60e, fea60, Ned):
    return round((Ve * fec + Mab50e * fea50 + Mab60e * fea60) * Ned)

def DEP_ES(Ve, fdc, Mab50e, fda50, Mab60e, fda60, Ned):
    return round((Ve * fdc + Mab50e * fda50 + Mab60e * fda60) * Ned)

def ECO2_ME(Vbc, Vvi, fec, Mab50bc, Mab50vi, fea50, Mab60bc, Mab60vi, fea60, Ned):
    return round(((Vbc + Vvi) * fec + (Mab50bc + Mab50vi) * fea50 + (Mab60bc + Mab60vi) * fea60) * Ned)

def DEP_ME(Vbc, Vvi, fdc, Mab50bc, Mab50vi, fda50, Mab60bc, Mab60vi, fda60, Ned):
    return round(((Vbc + Vvi) * fdc + (Mab50bc + Mab50vi) * fda50 + (Mab60bc + Mab60vi) * fda60) * Ned)

def ECO2_RE(Ar, er, Ve, fec, Mat60r, Mab60r, Mab60e, fea60, Mab50r, Mab50e, fea50, Ned):
    return round(((Ar * er + Ve) * fec + (Mat60r + Mab60r + Mab60e) * fea60 + (Mab50r + Mab50e) * fea50) * Ned)

def DEP_RE(Ar, er, Ve, fdc, Mat60r, Mab60r, Mab60e, fda60, Mab50r, Mab50e, fda50, Ned):
    return round(((Ar * er + Ve) * fdc + (Mat60r + Mab60r + Mab60e) * fda60 + (Mab50r + Mab50e) * fda50) * Ned)

# FATORES DE CONVERSÃO

fec = {20: np.array([168.8, 283.5]), 25: np.array([200, 306.4]), 30: np.array([228.2, 339.4]), 35: np.array([256.6, 373.6]), 40: np.array([283.4, 395.5])}
fdc = {20: np.array([1325, 2244]), 25: np.array([1488, 2408]), 30: np.array([1650, 2629]), 35: np.array([1797, 2849]), 40: np.array([1928, 3002])}
fea50 = np.array([0.4259, 1.061])
fea60 = fea50
fda50 = np.array([8.025, 16.05])
fda60 = fda50
fea190 = 2.3
fda190 = fda50

# APLICATIVO

st.html("<h1 style='text-align: center; font-size: 1.5rem;'>CALCULADORA DE ECO2 E DEP INCORPORADAS NAS FUNDAÇÕES 🌍🏗️🧮</h1>")
st.html("<h1 style='text-align: center; font-size: 1.2rem; font-style: italic;'>Desenvolvido por Rhonner Ramírez no Departamento de Geotecnia - EESC/USP</h1>")

cenario = st.selectbox(
    "Cenário",
    ("Estudo preliminar", "Projeto executivo"), index=None, help="""
- Estudo preliminar: Estimativa com base em informações (preliminares ou não-definitivas)

- Projeto executivo: Cálculo com base em informações completas (semidefinitivas a definitivas)
"""
)

if cenario == "Estudo preliminar":
    option = st.selectbox(
        "Tipo de fundação",
        ("Radier", "Estaca", "Radier estaqueado"), index=None,
    )
    if option == "Radier":
        Ned = st.number_input("Número de edificações", min_value=1, step=1)
        Ap = st.number_input("Área construída projetada (m2)", min_value=40.00, step=0.01)
        er = st.number_input("Espessura do radier (m)", min_value=0.095, max_value=0.450, step=0.001, format="%0.3f", help="""
        Valores típicos

        - Casa térrea: 0.100 m
        - Casa sobreposta e sobrado: 0.120 m - 0.150 m
        """
                             )
        tipoTela = st.selectbox("Tipo de tela",
                                ("Q-113", "Q-138", "Q-159", "Q-196", "Q-283", "Q-503"), index=5,
        )
        Mat60r = Mat60r(tipoTela, Ap)
        st.write("Massa de aço de telas (kg)", round(Mat60r, 2))
        Mab50r = Mab50r(er, Ap)
        st.write("Massa de aço de barras CA-50 (kg)", round(Mab50r, 2))
        Mab60r = st.number_input("Massa de aço de barras CA-60 (kg)", min_value=0.00, step=0.01)
        Mac190r = st.number_input("Massa de aço de cordoalhas CP190 RB 12,7 (kg)", min_value=0.00, step=0.01, help="Concreto protendido")
        fck = st.radio("fck (MPa)", (20, 25, 30))
        ECO2RAmin = ECO2_RA(Ap, er, fec[fck][0], Mat60r, Mab60r, fea60[0], Mab50r, fea50[0], Mac190r, fea190, Ned)
        ECO2RAmax = ECO2_RA(Ap, er, fec[fck][1], Mat60r, Mab60r, fea60[1], Mab50r, fea50[1], Mac190r, fea190, Ned)
        DEPRAmin = DEP_RA(Ap, er, fdc[fck][0], Mat60r, Mab60r, fda60[0], Mab50r, fda50[0], Mac190r, fda190[0], Ned)
        DEPRAmax = DEP_RA(Ap, er, fdc[fck][1], Mat60r, Mab60r, fda60[1], Mab50r, fda50[1], Mac190r, fda190[1], Ned)
        st.write("**RESULTADOS**")
        st.write("ECO2 (kg): ", ECO2RAmin, " - ", ECO2RAmax)
        st.write("DEP (MJ): ", DEPRAmin, " - ", DEPRAmax)
    elif option == "Estaca":
        st.write("**CARACTERÍSTICAS DAS ESTACAS**")
        numEstDif = st.number_input("Número de estacas diferentes", min_value=1, step=1)
        Sf, D, L = [], [], []
        for i in range(numEstDif):
            Sf.append(st.selectbox("Tipo de estaca " + str(i + 1), ("Pré-moldada", "Hélice contínua")))
            D.append(st.number_input("Diâmetro ou lado da estaca (m) " + str(i + 1), min_value=0.15, step=0.01))
            L.append(st.number_input("Comprimento da estaca (m) " + str(i + 1), min_value=1, step=1))
        st.write("**PARÂMETROS QUANTITATIVOS**")
        Ned = st.number_input("Número de edificações", min_value=1, step=1)
        Ap = st.number_input("Área construída projetada (m2)", min_value=40.00, step=0.01)
        fck = st.selectbox("fck (MPa)", (25, 30, 40))
        st.write("**ESTACA**")
        geomEst = st.selectbox("Geometria da seção transversal da estaca",
                               ("Circular", "Quadrada"), index=0,
        )
        diamLado = st.number_input("Diâmetro ou lado da estaca (m)", min_value=0.15, step=0.01)
        Ae = Ae(geomEst, diamLado)
        st.write("Área da seção transversal da estaca (m2): ", Ae)
        Le = st.number_input("Comprimento da estaca (m)", min_value=5, step=1)
        Mab50e = Msmin(diamLado, 7850)
        st.write("Massa de aço CA-50 da estaca (kg)", Mab50e)
        ne = st.number_input("Número de estacas por m2", min_value=0.16, step=0.01)
        st.write("**BLOCO DE COROAMENTO**")
        st.write("Volume do bloco de coroamento (m3)", Vbc(diamLado))
        st.write("Massa de aço CA-50 do bloco de coroamento (kg)", Mab50bc(0.75 * 800, diamLado, 500000, 7850, 0.05))
        ECO2ES_1_min = ECO2_ES_1(Ap, Mab50e, fec[fck][0], fea50[0], ne, Ae, Le, Ned)
        ECO2ES_1_max = ECO2_ES_1(Ap, Mab50e, fec[fck][1], fea50[1], ne, Ae, Le, Ned)
        DEPES_1_min = DEP_ES_1(Ap, Mab50e, fdc[fck][0], fda50[0], ne, Ae, Le, Ned)
        DEPES_1_max = DEP_ES_1(Ap, Mab50e, fdc[fck][1], fda50[1], ne, Ae, Le, Ned)
        st.write("**RESULTADOS DA FUNDAÇÃO**")
        st.write("ECO2 (kg): ", ECO2ES_1_min, " - ", ECO2ES_1_max)
        st.write("DEP (MJ): ", DEPES_1_min, " - ", DEPES_1_max)
        st.write("**RESULTADOS DOS BLOCOS DE COROAMENTO**")
        ECO2ME_1_min = ECO2_ME_1(Vbc(diamLado), ne, Ap, fec[fck][0], Ned)
        ECO2ME_1_max = ECO2_ME_1(Vbc(diamLado), ne, Ap, fec[fck][1], Ned)
        st.write("ECO2 (kg): ", ECO2ME_1_min, " - ", ECO2ME_1_max)
        DEPME_1_min = DEP_ME_1(Vbc(diamLado), ne, Ap, fdc[fck][0], Ned)
        DEPME_1_max = DEP_ME_1(Vbc(diamLado), ne, Ap, fdc[fck][1], Ned)
        st.write("DEP (MJ): ", DEPME_1_min, " - ", DEPME_1_max)
    elif option == "Radier estaqueado":
        st.write("**CARACTERÍSTICAS DAS ESTACAS**")
        numEstDif = st.number_input("Número de estacas diferentes", min_value=1, step=1)
        Sf, D, L = [], [], []
        for i in range(numEstDif):
            Sf.append(st.selectbox("Tipo de estaca " + str(i + 1), ("Pré-moldada", "Hélice contínua")))
            D.append(st.number_input("Diâmetro ou lado da estaca (m) " + str(i + 1), min_value=0.15, step=0.01))
            L.append(st.number_input("Comprimento da estaca (m) " + str(i + 1), min_value=1, step=1))
        st.write("**PARÂMETROS QUANTITATIVOS**")
        Ned = st.number_input("Número de edificações", min_value=1, step=1)
        Ap = st.number_input("Área construída projetada (m2)", min_value=40.00, step=0.01)
        er = st.number_input("Espessura do radier (m)", min_value=0.100, max_value=0.450, step=0.001, format="%0.3f")
        Ae = st.number_input("Área da seção transversal da estaca (m2)", min_value=0.03, step=0.01)
        Le = st.number_input("Comprimento da estaca (m)", min_value=5, step=1)
        ne = st.number_input("Número de estacas por m2", min_value=0.16, step=0.01)
        fck = st.selectbox("fck (MPa)", (25, 30))
        Mar = st.number_input("Massa de aço do radier (kg)", min_value=0.00, step=0.01)
        Mae = st.number_input("Massa de aço da estaca (kg)", min_value=0.00, step=0.01)
        ECO2RE_1_min = ECO2_RE_1(er, ne, Ae, Le, Ap, fec[fck][0], Mar, Mae, fea50[0], Ned)
        ECO2RE_1_max = ECO2_RE_1(er, ne, Ae, Le, Ap, fec[fck][1], Mar, Mae, fea50[1], Ned)
        DEPRE_1_min = DEP_RE_1(er, ne, Ae, Le, Ap, fdc[fck][0], Mar, Mae, fda50[0], Ned)
        DEPRE_1_max = DEP_RE_1(er, ne, Ae, Le, Ap, fdc[fck][1], Mar, Mae, fda50[1], Ned)
        st.write("**RESULTADOS**")
        st.write("ECO2 (kg): ", ECO2RE_1_min, " - ", ECO2RE_1_max)
        st.write("DEP (MJ): ", DEPRE_1_min, " - ", DEPRE_1_max)
elif cenario == "Projeto executivo":
    option = st.selectbox(
        "Tipo de fundação",
        ("Radier", "Estacas + Blocos de coroamento + Vigas", "Radier estaqueado"), index=None,
    )
    if option == "Radier":
        Ned = st.number_input("Número de edificações", min_value=1, step=1)
        st.write("**CONCRETO**")
        Ar = st.number_input("Área do radier (m2)", min_value=40.00, step=0.01)
        er = st.number_input("Espessura do radier (m)", min_value=0.095, max_value=0.450, step=0.001, format="%0.3f")
        fck = st.selectbox("fck (MPa)", (20, 25, 30))
        st.write("**AÇO**")
        Mat60r = st.number_input("Massa de aço de telas (kg)", min_value=0.00, step=0.01)
        Mab50r = st.number_input("Massa de aço de barras CA-50 (kg)", min_value=0.00, step=0.01)
        Mab60r = st.number_input("Massa de aço de barras CA-60 (kg)", min_value=0.00, step=0.01)
        Mac190r = st.number_input("Massa de aço de cordoalhas CP190 RB 12,7 (kg)", min_value=0.00, step=0.01, help="Concreto protendido")
        ECO2RAmin = ECO2_RA(Ar, er, fec[fck][0], Mat60r, Mab60r, fea60[0], Mab50r, fea50[0], Mac190r, fea190, Ned)
        ECO2RAmax = ECO2_RA(Ar, er, fec[fck][1], Mat60r, Mab60r, fea60[1], Mab50r, fea50[1], Mac190r, fea190, Ned)
        DEPRAmin = DEP_RA(Ar, er, fdc[fck][0], Mat60r, Mab60r, fda60[0], Mab50r, fda50[0], Mac190r, fda190[0], Ned)
        DEPRAmax = DEP_RA(Ar, er, fdc[fck][1], Mat60r, Mab60r, fda60[1], Mab50r, fda50[1], Mac190r, fda190[1], Ned)
        st.write("**RESULTADOS**")
        st.write("ECO2 (kg): ", ECO2RAmin, " - ", ECO2RAmax)
        st.write("DEP (MJ): ", DEPRAmin, " - ", DEPRAmax)
        st.write("**RESULTADOS POR ÁREA CONSTRUÍDA**")
        Ac = st.number_input("Área construída (m2)", min_value=40.00, step=0.01)
        st.write("ECO2 (kg/m2): ", round(ECO2RAmin / Ac), " - ", round(ECO2RAmax / Ac))
        st.write("DEP (MJ/m2): ", round(DEPRAmin / Ac), " - ", round(DEPRAmax / Ac))
    elif option == "Estacas + Blocos de coroamento + Vigas":
        st.html("<h1 style='text-align: center; font-size: 1rem;'>ESTACAS</h1>")
        st.write("**CARACTERÍSTICAS**")
        numEstDif = st.number_input("Número de estacas diferentes", min_value=1, step=1)
        Sf, D, L = [], [], []
        for i in range(numEstDif):
            Sf.append(st.selectbox("Tipo de estaca " + str(i + 1), ("Pré-moldada", "Hélice contínua")))
            D.append(st.number_input("Diâmetro ou lado da estaca (m) " + str(i + 1), min_value=0.15, step=0.01))
            L.append(st.number_input("Comprimento da estaca (m) " + str(i + 1), min_value=1, step=1))
        st.write("**PARÂMETROS QUANTITATIVOS**")
        Ned = st.number_input("Número de edificações", min_value=1, step=1)
        Ve = st.number_input("Volume das estacas (m3)", min_value=10.00, step=0.01)
        Mab50e = st.number_input("Massa de aço de barras CA-50 (kg)", min_value=0.00, step=0.01)
        Mab60e = st.number_input("Massa de aço de barras CA-60 (kg)", min_value=0.00, step=0.01)
        fck = st.selectbox("fck (MPa)", (25, 30, 40))
        ECO2ESmin = ECO2_ES(Ve, fec[fck][0], Mab50e, fea50[0], Mab60e, fea60[0], Ned)
        ECO2ESmax = ECO2_ES(Ve, fec[fck][1], Mab50e, fea50[1], Mab60e, fea60[1], Ned)
        DEPESmin = DEP_ES(Ve, fdc[fck][0], Mab50e, fda50[0], Mab60e, fda60[0], Ned)
        DEPESmax = DEP_ES(Ve, fdc[fck][1], Mab50e, fda50[1], Mab60e, fda60[1], Ned)
        st.write("**RESULTADOS**")
        st.write("ECO2 (kg): ", ECO2ESmin, " - ", ECO2ESmax)
        st.write("DEP (MJ): ", DEPESmin, " - ", DEPESmax)
        st.html("<h1 style='text-align: center; font-size: 1rem;'>MESOESTRUTURA</h1>")
        st.write("BLOCOS DE COROAMENTO")
        Vbc = st.number_input("Volume de blocos de coroamento (m3)", min_value=10.00, step=0.01)
        Mab50bc = st.number_input("Massa de aço de barras CA-50 dos blocos de coroamento (kg)", min_value=0.00, step=0.01)
        Mab60bc = st.number_input("Massa de aço de barras CA-60 dos blocos de coroamento (kg)", min_value=0.00, step=0.01)
        st.write("VIGAS")
        Vvi = st.number_input("Volume de vigas (m3)", min_value=10.00, step=0.01)
        Mab50vi = st.number_input("Massa de aço de barras CA-50 das vigas (kg)", min_value=0.00, step=0.01)
        Mab60vi = st.number_input("Massa de aço de barras CA-60 das vigas (kg)", min_value=0.00, step=0.01)
        fck_ME = st.selectbox("fck (MPa)", (25, 30, 40), key="fck_ME")
        ECO2MEmin = ECO2_ME(Vbc, Vvi, fec[fck_ME][0], Mab50bc, Mab50vi, fea50[0], Mab60bc, Mab60vi, fea60[0], Ned)
        ECO2MEmax = ECO2_ME(Vbc, Vvi, fec[fck_ME][1], Mab50bc, Mab50vi, fea50[1], Mab60bc, Mab60vi, fea60[1], Ned)
        DEPMEmin = DEP_ME(Vbc, Vvi, fdc[fck_ME][0], Mab50bc, Mab50vi, fda50[0], Mab60bc, Mab60vi, fda60[0], Ned)
        DEPMEmax = DEP_ME(Vbc, Vvi, fdc[fck_ME][1], Mab50bc, Mab50vi, fda50[1], Mab60bc, Mab60vi, fda60[1], Ned)
        st.write("**RESULTADOS**")
        st.write("ECO2 (kg): ", ECO2MEmin, " - ", ECO2MEmax)
        st.write("DEP (MJ): ", DEPMEmin, " - ", DEPMEmax)
    elif option == "Radier estaqueado":
        st.write("**CARACTERÍSTICAS DAS ESTACAS**")
        numEstDif = st.number_input("Número de estacas diferentes", min_value=1, step=1)
        Sf, D, L = [], [], []
        for i in range(numEstDif):
            Sf.append(st.selectbox("Tipo de estaca " + str(i + 1), ("Pré-moldada", "Hélice contínua")))
            D.append(st.number_input("Diâmetro ou lado da estaca (m) " + str(i + 1), min_value=0.15, step=0.01))
            L.append(st.number_input("Comprimento da estaca (m) " + str(i + 1), min_value=1, step=1))
        st.write("**PARÂMETROS QUANTITATIVOS**")
        Ned = st.number_input("Número de edificações", min_value=1, step=1)
        Ar = st.number_input("Área do radier (m2)", min_value=40.00, step=0.01)
        er = st.number_input("Espessura do radier (m)", min_value=0.100, max_value=0.450, step=0.001, format="%0.3f")
        Ve = st.number_input("Volume das estacas (m3)", min_value=10.00, step=0.01)
        Mat60r = st.number_input("Massa de aço de telas do radier (kg)", min_value=0.00, step=0.01)
        Mab60r = st.number_input("Massa de aço de barras CA-60 do radier (kg)", min_value=0.00, step=0.01)
        Mab60e = st.number_input("Massa de aço de barras CA-60 das estacas (kg)", min_value=0.00, step=0.01)
        Mab50r = st.number_input("Massa de aço de barras CA-50 do radier (kg)", min_value=0.00, step=0.01)
        Mab50e = st.number_input("Massa de aço de barras CA-50 das estacas (kg)", min_value=0.00, step=0.01)
        fck = st.selectbox("fck (MPa)", (25, 30))
        ECO2REmin = ECO2_RE(Ar, er, Ve, fec[fck][0], Mat60r, Mab60r, Mab60e, fea60[0], Mab50r, Mab50e, fea50[0], Ned)
        ECO2REmax = ECO2_RE(Ar, er, Ve, fec[fck][1], Mat60r, Mab60r, Mab60e, fea60[1], Mab50r, Mab50e, fea50[1], Ned)
        DEPREmin = DEP_RE(Ar, er, Ve, fdc[fck][0], Mat60r, Mab60r, Mab60e, fda60[0], Mab50r, Mab50e, fda50[0], Ned)
        DEPREmax = DEP_RE(Ar, er, Ve, fdc[fck][1], Mat60r, Mab60r, Mab60e, fda60[1], Mab50r, Mab50e, fda50[1], Ned)
        st.write("**RESULTADOS**")
        st.write("ECO2 (kg): ", ECO2REmin, " - ", ECO2REmax)
        st.write("DEP (MJ): ", DEPREmin, " - ", DEPREmax)
