<template>
  <div class="areas">
    <p>Listagem:</p>
    <ul>
      <li v-for="area in listaAreas"
          :key="area.id"
          >
        <a :href="getAreaUrl(area.id)">{{area.nome}}</a>
      </li>
    </ul>
  </div>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';

export default {
    name: 'ListarAreas',
    created() {
        this.buscaAreas();
    },
    methods: {
        ...mapActions({
            buscaAreas: 'area/buscaAreas',
        }),
        getAreaUrl(id) {
            return `area/` + id;
        },
    },
    computed: {
        ...mapGetters({
            listaAreas: 'area/areas',
        }),
    },
};
</script>
