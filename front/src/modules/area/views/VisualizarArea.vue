<template>
<div class="row">
  <div class="col s9">
    <div class="card">
      <h3 class="card-title">
        Desenho de área
      </h3>
      <div class="card-content">
        <Grid>
        </Grid>
      </div>
    </div>
  </div>
  <div class="col s3">
    <div class="card">
      <h3 class="card-title">
        Dados da área
      </h3>
      <div class="card-content">
        <p>{{dadosArea.nome}}</p>
        <p>Localidade: <a :href="getLocalidadeUrl(dadosArea.localidade_id)">{{dadosArea.localidade}}</a></p>
        <p>Microclima: {{dadosArea.microclima}}</p>
        
        <br/>
        <p>Dimensões:</p>
        <p>{{dadosArea.comprimento}}m x {{dadosArea.largura}}m</p>
        <p>{{dadosArea.dimensao}}m2</p>
      </div>
    </div>
  </div> 
</div>
</template>
<script>

import { mapActions, mapGetters } from 'vuex';
import Grid from '@/modules/desenho/Grid';

export default {
    name: 'VisualizarArea',
    components: {
        Grid,
    },
    created() {
        if (typeof this.$route.params.id !== 'undefined') {
            this.buscarArea(this.$route.params.id);
        }
    },
    mounted() {
        let materializeScript = document.createElement('script');
        materializeScript.setAttribute('src', '@/assets/materialize.min');
//        document.head.appendChild(materializeScript);
    },
    methods: {
        ...mapActions({
            buscarArea: 'area/buscarArea',
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
