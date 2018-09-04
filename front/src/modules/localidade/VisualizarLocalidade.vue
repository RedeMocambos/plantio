<template>
<div class="localidade">
  <div class="dados">
    {{dadosLocalidade.nome}} | {{dadosLocalidade.bioma}} | {{dadosLocalidade.clima}}
  </div>

  <div class="areas">
    <a href="">adicionar áreas</a>

    <p><strong>Áreas:</strong></p>
    <ul>
      <li v-for="area in dadosAreasLocalidade"
          :key="area.id"
          >{{area.nome}} | {{area.dimensao}}m2 | {{area.microclima}}
      </li>
    </ul>
  </div>
  
</div>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';

export default {
    name: 'VisualizarLocalidade',
    created() {
        if (typeof this.$route.params.id !== 'undefined') {
            this.buscaLocalidade(this.$route.params.id);
            this.buscaAreasPorLocalidade(this.$route.params.id);
        }
    },  
    methods: {
        ...mapActions({
            buscaLocalidade: 'localidade/buscaLocalidade',
            buscaAreasPorLocalidade: 'localidade/buscaAreasPorLocalidade',
        }),
    },
    computed: {
        ...mapGetters({
            dadosLocalidade: 'localidade/localidade',
            dadosAreasLocalidade: 'localidade/areasLocalidade',
        }),
    },
};
</script>
