<template>
<div class="especie">
  <p>{{dadosEspecie.nome_cientifico}}</p>
  <em>{{dadosEspecie.nome_cientifico}}</em> - <strong> {{dadosEspecie.familia}}</strong>
  <p>Início da colheita: {{dadosEspecie.inicio_colheita}} dias</p>
  <p>Porte: {{dadosEspecie.porte}}</p>
  <p>Sucessão: {{dadosEspecie.sucessao}}</p>
  <p>Temperatura: <span style="color: #33c">{{dadosEspecie.temperatura_min}}C</span> a <span style="color: #c33">{{dadosEspecie.temperatura_max}}C</span></p>
  
</div>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';

export default {
    name: 'VisualizarEspecie',
    created() {
        if (typeof this.$route.params.id !== 'undefined') {
            this.buscaEspecie(this.$route.params.id);
        }
    },
    methods: {
        ...mapActions({
            buscaEspecie: 'especie/buscaEspecie',
        }),
    },
    computed: {
        ...mapGetters({
            dadosEspecie: 'especie/especie',
        }),
    },
};
</script>
