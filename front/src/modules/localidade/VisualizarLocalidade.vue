<template>
  <div class="localidade">
    {{dadosLocalidade.nome}} | {{dadosLocalidade.bioma}} | {{dadosLocalidade.clima}}
  </div>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';

export default {
    name: 'VisualizarLocalidade',
    created() {
        if (typeof this.$route.params.id !== 'undefined') {
            this.buscaLocalidade(this.$route.params.id);
        }
    },    
    methods: {
        ...mapActions({
            buscaLocalidade: 'localidade/buscaLocalidade',
        }),
    },
    computed: {
        ...mapGetters({
            dadosLocalidade: 'localidade/localidade',
        }),
    },
};
</script>
