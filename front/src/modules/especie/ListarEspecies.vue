<template>
  <div class="especies">
    <p>Listagem:</p>
    <ul>
      <li v-for="especie in listaEspecies"
          :key="especie.nome_cientifico"
          >
        {{especie.nomes_populares}} - <em>{{especie.nome_cientifico}}</em> - <strong> {{especie.familia}}</strong>
      </li>
    </ul>
  </div>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'Especies',
  created() {
    this.buscaEspecies();
  },
  methods: {
    ...mapActions({
      buscaEspecies: 'especie/buscaEspecies',
    }),
  },
  computed: {
    ...mapGetters({
      listaEspecies: 'especie/especies',
    }),
  },
};
</script>
