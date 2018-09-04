<template>
<div class="area">
  <p><strong>Visualizar área:</strong></p>
  <ul>
    {{dadosArea.nome}} | {{dadosArea.dimensao}}m2 | {{dadosArea.microclima}}
    </li>
  </ul>
</div>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';

export default {
    name: 'VisualizarArea',
    created() {
        if (typeof this.$route.params.id !== 'undefined') {
            this.buscaArea(this.$route.params.id);
        }
    },  
    methods: {
        ...mapActions({
            buscaArea: 'area/buscaArea',
        }),
    },
    computed: {
        ...mapGetters({
            dadosArea: 'area/area',
        }),
    },
};
</script>
