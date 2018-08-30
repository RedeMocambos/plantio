<template>
  <div class="localidade">
    <h1>Localidade</h1>
    <VisualizarLocalidade></VisualizarLocalidade>
  </div>
</template>
<script>
import VisualizarLocalidade from '../modules/localidade/VisualizarLocalidade.vue';

export default {
    name: 'Localidade',
    components: {
        VisualizarLocalidade,
    },
};
</script>
