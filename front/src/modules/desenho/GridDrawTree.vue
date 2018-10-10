<template>
<div class="row">
  <div class="input-field col s2">
    <p>
      <label for="range">Raio</label>
      <input
        type="range"
        id="range"
        min="1"
        name="range"
        :max="circleMaxSize"
        v-model="opt.range"
        />
    </p>
  </div>
  <div class="input-field col s2">
    <p>
      <label for="density">Densidade da copa</label>
      <input
        type="range"
        id="density"
        min="1"
        name="density"
        :max="opt.densityMax"
        v-model="opt.density"               
        />
    </p>
  </div>
  <div class="input-field col s2">
    <a class="waves-effect waves-light btn-small" v-on:click="gerarGrid()">gerar desenho</a>
  </div>
</div>
</template>
<script>
export default {
    name: 'GridDrawTree',
    data: function() {
        return {},
    },
    methods: {
        setColor: function() {
            /*
                    if ((Math.abs(yIn) ** 2) + Math.abs(xIn ** 2) < (this.opt.range ** 2)) {
                        let hypo = (Math.sqrt(Math.abs(yIn ** 2) + Math.abs(xIn ** 2)));
                        color = Math.floor((this.opt.range - hypo) * (this.opt.density / (4)));
                    }
                    
                    if (color > maxColorByDensity) {
                        color = maxColorByDensity;
  '          }*/
        },
    },
}
</script>
