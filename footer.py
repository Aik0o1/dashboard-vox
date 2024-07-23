import streamlit as st

def footer():
    return( st.markdown(
        """<hr/><footer>
    <div class="container">
        <div class="row widget-footer">
            <div class="col-md-3">
                <img src="https://portal.pi.gov.br/jucepi/wp-content/uploads/sites/47/2023/03/jucepi_logo-768x177.jpg" alt="">
            </div>
            <div class="col-md-3">
			<div class="widget widget_text widget-none" id="text-15"><h3 class="title">Órgão</h3>			<div class="textwidget"><div id="text-14" class="widget widget_text widget-none" title="Pressione shift e clique para editar este widget.">
<div class="textwidget">
<p>Junta Comercial do Estado do Piauí<br>
CNPJ 06.690.994/0001 – 00<br>
Rua General Osório, 3002 – Cabral Teresina/PI CEP: 64000-580<br>
Telefone: (86) 3230-8800.</p>
<p>jucepi@jucepi.pi.gov.br</p>
</div>
</div>
</div>
		<div class="cleaner">&nbsp;</div></div>                            </div>
            <div class="col-md-3">
				        			<div class="widget widget_text widget-none" id="text-26"><h3 class="title">Atendimento</h3>			<div class="textwidget"><p><strong>Horário:<br>
</strong>De segunda a sexta-feira (<em>exceto feriado</em>), das 07h30 às 13h30.</p>
<p><strong>Telefones:</strong><br>
Telefone geral: (86) 3230-8800<br>
Telefone suporte: (86) 3230-8810</p>
</div>
	
</footer>""",
    unsafe_allow_html=True,
    )
    )