<template>
  <div class="localidades">
    <h1>Localidades</h1>
    <p>Lista de localidades</p>
    <ListarLocalidades></ListarLocalidades>
  </div>
</template>
<script>
import ListarLocalidades from '../modules/localidade/ListarLocalidades.vue';

export default {
  name: 'Localidades',
  components: {
    ListarLocalidades,
  },
};
</script>
