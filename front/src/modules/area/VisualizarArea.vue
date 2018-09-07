<template>
<div class="area">
  <p><strong>Visualizar área:</strong></p>
  {{dadosArea.nome}} | {{dadosArea.dimensao}}m2 | {{dadosArea.microclima}} | <br/>
  Localidade: <a :href="getLocalidadeUrl(dadosArea.localidade_id)">{{dadosArea.localidade}}</a>
  <br/>
  {{dadosArea.comprimento}}m x {{dadosArea.largura}}m

  <Grid>
  </Grid>
</div>
</template>
<style>
  
</style>
<script>
import '@/assets/css/materialize.min.css';
import { mapActions, mapGetters } from 'vuex';
import Grid from '@/components/Grid';

export default {
    name: 'VisualizarArea',
    components: {
        Grid,
    },
    created() {
        if (typeof this.$route.params.id !== 'undefined') {
            this.buscaArea(this.$route.params.id);
        }
    },
    mounted() {
        let materializeScript = document.createElement('script');
        materializeScript.setAttribute('src', '@/assets/materialize.min');
//        document.head.appendChild(materializeScript);
    },
    methods: {
        ...mapActions({
            buscaArea: 'area/buscaArea',
        }),
        getLocalidadeUrl(id) {
            return `/localidade/` + id;
        },
    },
    computed: {
        ...mapGetters({
            dadosArea: 'area/area',
        }),
    },
};
</script>
