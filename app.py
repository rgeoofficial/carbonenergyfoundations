import streamlit as st
import numpy as np
import pandas as pd

with st.bottom:
    st.caption("© 2026 Desenvolvido por Rhonner Ramírez no Departamento de Geotecnia - EESC/USP · All rights reserved", text_alignment="center")

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

st.set_page_config(page_title="Calculadora de ECO2 e DEP", page_icon=":material/calculate:")

st.html("<h1 style='text-align: center; font-size: 1.5rem;'>CALCULADORA DE ECO2 E DEP INCORPORADAS NAS FUNDAÇÕES 🌎🏗️🧮</h1>")

with st.sidebar:
    with st.expander("Manual"):
        st.write("""
        # Objetivo

        Desenvolver uma calculadora que permita otimizar o desempenho ambiental dos projetos de fundações com base nos indicadores de ECO2 e DEP.

        # Marco teórico

        A calculadora está alinhada com o marco teórico do SIDAC. Os indicadores dos materiais de construção (fatores) utilizados na versão atual foram tomados do SIDAC.

        # Etapas do ciclo de vida

        Atualmente, a calculadora considera só a etapa de produto. Os cálculos da etapa de construção serão desenvolvidos futuramente.

        # Capacidade de carga
        
        A resistência de ponta das estacas hélice contínua segue a recomendação da norma ABNT NBR 6122. A área de ponta das estacas pré-moldadas centrifugadas considera a seção vazada.

        # Contato
        
        rhonnerprf@usp.br
        """)
    with st.expander("Glossário"):
        st.write("""
        - ECO2: Emissão de CO2
        - DEP: Demanda de energia primária
        """)
    with st.expander("Futuras implementações"):
        st.write("""
        - [ ] Etapa de construção
        - [ ] Soluções de mitigação por tipo de fundação
        """)

onACV = st.toggle("Análise de Ciclo de Vida")

if onACV:
    with st.container(border=True):
        st.html("<h1 style='text-align: center; font-size: 1.2rem;'>Análise de Ciclo de Vida</h1>")
        col1, col2 = st.columns(2)
        with col1:
            etapaProd = st.checkbox("Produto")
        with col2:
            etapaCons = st.checkbox("Construção (transporte)")

        if etapaProd:
            with st.container(border=True):
                st.html("<h1 style='text-align: left; font-size: 1.2rem;'>Produto</h1>")

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
                        st.write("Volume do bloco de coroamento (m³)", Vbc(diamLado))
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
                        with st.expander("ESTACAS"):
                            with st.container(border=True):
                                numEstDif = st.number_input("Número de grupos de estacas diferentes", min_value=1, step=1)
                                Sf, D, L, fcks = [], [], [], []
                                for i in range(numEstDif):
                                    with st.expander("Grupo " + str(i + 1)):
                                        Sf.append(st.selectbox("Tipo de estaca", ("Pré-moldada", "Hélice contínua"), key=f"tipo_estaca_{i + 1}"))
                                        if Sf[-1] == "Pré-moldada":
                                            D.append(st.number_input("Diâmetro ou lado da estaca (m)", min_value=0.15, step=0.01, key="D_estacaPM" + str(i + 1)))
                                        elif Sf[-1] == "Hélice contínua":
                                            D.append(st.number_input("Diâmetro da estaca (m)", min_value=0.15, step=0.01, key="D_estacaHC" + str(i + 1)))
                                        L.append(st.number_input("Comprimento da estaca (m)", min_value=1, step=1, key="L_estaca" + str(i + 1)))
                                        fcks.append(st.selectbox("fck (MPa)", (25, 30, 40), key="fck_estaca" + str(i + 1)))
                                Ned = st.number_input("Número de edificações", min_value=1, step=1)
                                st.write("Volume das estacas (m³)")
                                onVe = st.toggle("Manual / Automático")
                                if onVe:
                                    st.write("Em desenvolvimento")
                                    Ve = 10.00
                                    st.write("Volume da estacas (m³):", Ve)
                                else:
                                    Ve = st.number_input("Volume das estacas (m³)", min_value=10.00, step=0.01)
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
                        with st.expander("MESOESTRUTURA"):
                            with st.container(border=True):
                                st.write("BLOCOS DE COROAMENTO")
                                Vbc = st.number_input("Volume de blocos de coroamento (m³)", min_value=10.00, step=0.01)
                                Mab50bc = st.number_input("Massa de aço de barras CA-50 dos blocos de coroamento (kg)", min_value=0.00, step=0.01)
                                Mab60bc = st.number_input("Massa de aço de barras CA-60 dos blocos de coroamento (kg)", min_value=0.00, step=0.01)
                            with st.container(border=True):
                                st.write("VIGAS")
                                Vvi = st.number_input("Volume de vigas (m³)", min_value=10.00, step=0.01)
                                Mab50vi = st.number_input("Massa de aço de barras CA-50 das vigas (kg)", min_value=0.00, step=0.01)
                                Mab60vi = st.number_input("Massa de aço de barras CA-60 das vigas (kg)", min_value=0.00, step=0.01)
                                fck_ME = st.selectbox("fck (MPa)", (25, 30, 40), key="fck_ME")
                            ECO2MEmin = ECO2_ME(Vbc, Vvi, fec[fck_ME][0], Mab50bc, Mab50vi, fea50[0], Mab60bc, Mab60vi, fea60[0], Ned)
                            ECO2MEmax = ECO2_ME(Vbc, Vvi, fec[fck_ME][1], Mab50bc, Mab50vi, fea50[1], Mab60bc, Mab60vi, fea60[1], Ned)
                            DEPMEmin = DEP_ME(Vbc, Vvi, fdc[fck_ME][0], Mab50bc, Mab50vi, fda50[0], Mab60bc, Mab60vi, fda60[0], Ned)
                            DEPMEmax = DEP_ME(Vbc, Vvi, fdc[fck_ME][1], Mab50bc, Mab50vi, fda50[1], Mab60bc, Mab60vi, fda60[1], Ned)
                            with st.container(border=True):
                                st.write("**RESULTADOS**")
                                st.write("ECO2 (kg): ", ECO2MEmin, " - ", ECO2MEmax)
                                st.write("DEP (MJ): ", DEPMEmin, " - ", DEPMEmax)
                        with st.expander("RESULTADOS"):
                            st.write("Em desenvolvimento")
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
                        Ve = st.number_input("Volume das estacas (m³)", min_value=10.00, step=0.01)
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

        if etapaCons:
            with st.container(border=True):
                st.html("<h1 style='text-align: left; font-size: 1.2rem;'>Construção (transporte)</h1>")
                st.write("Em desenvolvimento")

# ANÁLISE DE SOLUÇÕES DE ESTACAS

onSim = st.toggle("Análise de soluções de estacas")

def inputs_estacas(key):
    Te = st.selectbox("Tipo de estaca",
                    ("Hélice contínua", "Pré-moldada centrifugada"),
                    key=f"Te_{key}"
    )
    if Te == "Pré-moldada centrifugada":
        col1, col2 = st.columns(2)
        with col1:
            De = st.number_input("Diâmetro externo (m)", min_value=0.20, step=0.01, key=f"De_{key}")
        with col2:
            Di = st.number_input("Diâmetro interno (m)", min_value=0.12, step=0.01, key=f"Di_{key}")
    else:
        De = st.number_input("Diâmetro (m)", min_value=0.20, step=0.01, key=f"De_{key}")
        Di = 0
    L = st.number_input("Comprimento (m)", min_value=1, step=1, key=f"L_{key}")
    fck = st.radio("fck (MPa)", (20, 25, 30, 40), key=f"fck_{key}")
    return Te, De, Di, L, fck

def F1_F2(tipoEst, D):
    if tipoEst == "Franki":
        F1 = 2.50
    elif tipoEst == "Metálica":
        F1 = 1.75
    elif (tipoEst == "Pré-moldada") or (tipoEst == "Pré-moldada centrifugada"):
        F1 = round(1 + D / 0.80, 2)
    elif tipoEst == "Strauss":
        F1 = 3.0
    elif tipoEst == "Raiz" or tipoEst == "Hélice contínua" or tipoEst == "Ômega":
        F1 = 2.0
    F2 = 2 * F1
    return F1, F2

def RL(alpha, K, NL, diam, espCamada, F2):
    U = np.pi * diam
    return np.around(alpha * K * NL * U * espCamada / F2).astype(int)

def RP(K, NP, diamExt, diamInt, F1):
    Ap = (np.pi / 4) * (diamExt ** 2 - diamInt ** 2)
    return np.around(K * NP * Ap / F1).astype(int)

def Nlim(tipoEst, diam):
    if (tipoEst == "Pré-moldada") or (tipoEst == "Pré-moldada centrifugada"):
        if diam < 0.3:
            return [15, 25]
        elif diam >= 0.3:
            return [25, 35]
    elif tipoEst == "Hélice contínua":
        return [20, 45]
    elif tipoEst == "Strauss":
        return [10, 25]

def capacidade_carga(tipoEst, diamExt, diamInt, dataKAlpha, data):
    F1, F2 = F1_F2(tipoEst, diamExt)
    alpha = data["Tipo de solo"].map(dict(zip(dataKAlpha["Solo"], dataKAlpha["α (%)"]))) / 100
    K = data["Tipo de solo"].map(dict(zip(dataKAlpha["Solo"], dataKAlpha["K (MPa)"]))) * 1000
    RL_ = RL(alpha, K, data["NSPT"], diamExt, 1, F2).round().astype(int)
    RL_.index = range(2, len(RL_) + 2)
    RL_acum = RL_.cumsum()
    RL_acum.index = range(2, len(RL_acum) + 2)
    RP_ = RP(K, data["NSPT"], diamExt, diamInt, F1).round().astype(int)
    RP_.index = range(1, len(RP_) + 1)
    if tipoEst == "Hélice contínua": # ABNT NBR 6122
        mask = RP_.iloc[1:].values >= RL_acum[:-1].values
        RP_.iloc[1:] = np.where(mask, RL_acum[:-1].values, RP_.iloc[1:])
    R = RL_acum[:-1] + RP_[1:]
    return RL_acum, RP_, R

if onSim:
    with st.container(border=True):
        st.html("<h1 style='text-align: center; font-size: 1.2rem;'>Análise de soluções de estacas</h1>")
        dataKAlpha = pd.read_excel("k-alpha.xlsx", sheet_name="k-alpha", names=["Solo", "K (MPa)", "α (%)"])
        onSond = st.toggle("Sondagem de teste / Carregar sondagem")
        uploaded_file = None
        if onSond:
            uploaded_file = st.file_uploader("Carregar sondagem", type="xlsx")
            if uploaded_file is not None:
                data = pd.read_excel(uploaded_file, sheet_name="sub", names=["D (m)", "NSPT", "Tipo de solo"])
        else:
            data = pd.read_excel("sondagem.xlsx", sheet_name="sub", names=["D (m)", "NSPT", "Tipo de solo"])
        onSondagem = st.toggle("Mostrar sondagem")
        if onSondagem:
            st.write(data)
        col1, col2 = st.columns(2)
        with col1:
            with st.container(border=True):
                st.write("Alternativa 1")
                Te1, De1, Di1, L1, fck1 = inputs_estacas("1")
                Ne1 = st.number_input("Número de estacas", min_value=1, step=1, key="Ne1")
                if Te1 == "Hélice contínua":
                    V1 = round(Ae("Circular", De1) * L1 * Ne1, 2)
                else:
                    V1 = round((Ae("Circular", De1) - Ae("Circular", Di1)) * L1 * Ne1, 2)
                st.write("🪨 Volume (m³):", V1)
                st.write("🌎 ECO2 (kg): ", round(V1 * fec[fck1][0], 2), " - ", round(V1 * fec[fck1][1], 2))
                st.write("⚡ DEP (MJ): ", round(V1 * fdc[fck1][0], 2), " - ", round(V1 * fdc[fck1][1], 2))
                if (uploaded_file is not None) or (not onSond):
                    RL_acum1, RP_1, R1 = capacidade_carga(Te1, De1, Di1, dataKAlpha, data)
                    st.write("⬇️ Capacidade de carga (kN):", R1[L1 + 1] * Ne1)
                    with st.container(border=True):
                        col1R, col2R, col3R = st.columns(3)
                        with col1R:
                            st.write("RP (kN):", RP_1[L1 + 1] * Ne1)
                        with col2R:
                            st.write("RL (kN):", RL_acum1[L1 + 1] * Ne1)
                        with col3R:
                            st.write("R (kN):", R1[L1 + 1] * Ne1)
                custo1m3 = st.number_input("Custo do concreto (R$/m³)", min_value=200.00, value=246.09, key="custo1m3", help="Custo referencial do concreto fck = 20 MPa (R$/m3): 246.09")
                custo1 =  round(V1 * custo1m3, 2)
                st.write("💰 Custo (R$):", custo1)
        with col2:
            with st.container(border=True):
                st.write("Alternativa 2")
                Te2, De2, Di2, L2, fck2 = inputs_estacas("2")
                Ne2 = st.number_input("Número de estacas", min_value=1, step=1, key="Ne2")
                if Te2 == "Hélice contínua":
                    V2 = round(Ae("Circular", De2) * L2 * Ne2, 2)
                else:
                    V2 = round((Ae("Circular", De2) - Ae("Circular", Di2)) * L2 * Ne2, 2)
                st.write("🪨 Volume (m³):", V2)
                st.write("🌎 ECO2 (kg): ", round(V2 * fec[fck2][0], 2), " - ", round(V2 * fec[fck2][1], 2))
                st.write("⚡DEP (MJ): ", round(V2 * fdc[fck2][0], 2), " - ", round(V2 * fdc[fck2][1], 2))
                if (uploaded_file is not None) or (not onSond):
                    RL_acum2, RP_2, R2 = capacidade_carga(Te2, De2, Di2, dataKAlpha, data)
                    st.write("⬇️ Capacidade de carga (kN):", R2[L2 + 1] * Ne2)
                    with st.container(border=True):
                        col1R, col2R, col3R = st.columns(3)
                        with col1R:
                            st.write("RP (kN):", RP_2[L2 + 1] * Ne2)
                        with col2R:
                            st.write("RL (kN):", RL_acum2[L2 + 1] * Ne2)
                        with col3R:
                            st.write("R (kN):", R2[L2 + 1] * Ne2)
                custo2m3 = st.number_input("Custo do concreto (R$/m³)", min_value=200.00, value=246.09, key="custo2m3", help="Custo referencial do concreto fck = 20 MPa (R$/m3): 246.09")
                custo2 = round(V2 * custo2m3, 2)
                st.write("💰 Custo (R$):", custo2)
        with st.container(border=True):
            st.html("<p style='text-align: center; font-size: 1rem;'>Comparação entre Alternativa 2 e Alternativa 1</p>")
            col1comp, col2comp = st.columns(2)
            with col1comp:
                with st.container(border=True):
                    st.html("<p style='text-align: center; font-size: 1rem;'>Absoluta</p>")
                    st.write("🪨 Volume (m³):", round(V2 - V1, 2))
                    eco2min2 = round(V2 * fec[fck2][0], 2)
                    eco2min1 = round(V1 * fec[fck1][0], 2) 
                    eco2max2 = round(V2 * fec[fck2][1], 2)
                    eco2max1 = round(V1 * fec[fck1][1], 2)
                    depmin2 = round(V2 * fdc[fck2][0], 2)
                    depmin1 = round(V1 * fdc[fck1][0], 2) 
                    depmax2 = round(V2 * fdc[fck2][1], 2)
                    depmax1 = round(V1 * fdc[fck1][1], 2)
                    st.write("🌎 ECO2 (kg): ", round(eco2min2 - eco2min1, 2), " - ", round(eco2max2 - eco2max1, 2))
                    st.write("⚡DEP (MJ): ", round(depmin2 - depmin1, 2), " - ", round(depmax2 - depmax1, 2))
                    st.write("⬇️ Capacidade de carga (kN):", R2[L2 + 1] * Ne2 - R1[L1 + 1] * Ne1)
                    st.write("💰 Custo (R$):", round(custo2 - custo1, 2))
            with col2comp:
                with st.container(border=True):
                    st.html("<p style='text-align: center; font-size: 1rem;'>Relativa</p>")
                    st.write("🪨 Volume (%):", round((V2 - V1) / V1 * 100))
                    st.write("🌎 ECO2 (%): ", round((eco2min2 - eco2min1) / eco2min1 * 100), " - ", round((eco2max2 - eco2max1) / eco2max1 * 100))
                    st.write("⚡DEP (%): ", round((depmin2 - depmin1) / depmin1 * 100), " - ", round((depmax2 - depmax1) / depmax1 * 100))
                    st.write("⬇️ Capacidade de carga (%):", round((R2[L2 + 1] * Ne2 - R1[L1 + 1] * Ne1) / R1[L1 + 1] * Ne1 * 100))
                    st.write("💰 Custo (%):", round((custo2 - custo1) / custo1 * 100))

# ANÁLISE DE SOLUÇÕES DE MITIGAÇÃO

on = st.toggle("Soluções de mitigação")

if on:
    with st.container(border=True):
        st.write("Em desenvolvimento")
