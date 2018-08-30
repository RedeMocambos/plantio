<template>
  <div class="especie">
    <h1>Especie</h1>
    <VisualizarEspecie></VisualizarEspecie>
  </div>
</template>
<script>
import VisualizarEspecie from '../modules/especie/VisualizarEspecie.vue';

export default {
    name: 'Especie',
    components: {
        VisualizarEspecie,
    },
};
</script>
