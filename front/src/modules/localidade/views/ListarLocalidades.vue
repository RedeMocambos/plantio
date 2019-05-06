<template>
  <div class="localidades">
    <p>Listagem:</p>
    <ul>
      <li v-for="localidade in listaLocalidades"
          :key="localidade.id"
          >
        <a :href="getLocalidadeUrl(localidade.id)">{{localidade.nome}}</a> | {{localidade.bioma}} | {{localidade.clima}}
      </li>
    </ul>
  </div>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';

export default {
    name: 'ListarLocalidades',
    created() {
        this.buscaLocalidades();
    },
    methods: {
        ...mapActions({
            buscaLocalidades: 'localidade/buscaLocalidades',
        }),
        getLocalidadeUrl(id) {
            return `localidade/` + id;
        },
    },
    computed: {
        ...mapGetters({
            listaLocalidades: 'localidade/localidades',
        }),
    },
};
</script>
