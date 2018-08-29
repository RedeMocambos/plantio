<template>
  <div class="plantas">
    <h1>Plantas</h1>
    <p>Banco de dados de plantas</p>
    <ListarEspecies></ListarEspecies>
  </div>
</template>
<script>
import ListarEspecies from '../modules/especie/ListarEspecies.vue';

export default {
  name: 'Plantas',
  components: {
    ListarEspecies,
  },
};
</script>
