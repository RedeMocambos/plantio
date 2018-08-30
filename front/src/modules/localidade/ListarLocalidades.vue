<template>
  <div class="localidades">
    <p>Listagem:</p>
    <ul>
      <li v-for="localidade in listaLocalidades"
          :key="localidade.nome"
          >
        {{localidade.nome}} | {{localidade.bioma}} | {{localidade.clima}}
      </li>
    </ul>
  </div>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'Localidades',
  created() {
      this.buscaLocalidades();
  },
  methods: {
    ...mapActions({
      buscaLocalidades: 'localidade/buscaLocalidades',
    }),
  },
  computed: {
    ...mapGetters({
      listaLocalidades: 'localidade/localidades',
    }),
  },
};
</script>
