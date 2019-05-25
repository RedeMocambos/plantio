<template>
    <div class="row">
        <div class="col s12">

            <div class="card">
                <div class="card-title"/>
                <div class="card-content">
                    <div class="row">
                        <div class="input-field col s1">
                            <input
                                id="largura"
                                v-model="opt.sizeX"
                                placeholder="Altura"
                                type="text"
                                class="validate">
                            <label for="largura">Altura</label>
                        </div>
                        <div class="input-field col s1">
                            <input
                                id="altura"
                                v-model="opt.sizeY"
                                placeholder="Largura"
                                type="text"
                                class="validate">
                            <label for="altura">Largura</label>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="col s12">
            <div class="card">
                <div
                    id="grid"
                    style="font-family: monospace">
                    <GenerateGrid
                        :opt="opt"
                        :scale="scale"/>
                </div>
            </div>
        </div>

    </div>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';
import GenerateGrid from './GenerateGrid';

export default {
    name: 'Grid',
    components: {
        GenerateGrid,
    },
    data() {
        return {
            opt: {
                sizeX: null,
                sizeY: null,
                boxSizeW: 20,
                boxSizeH: 20,
                range: 9,
                density: 2,
                densityMax: 15,
            },
            scale: {
                '-1': 'grey lighten-3',
                0: '',
                1: 'light-green lighten-4',
                2: 'light-green lighten-3',
                3: 'green lighten-3',
                4: 'green lighten-2',
                5: 'green lighten-1',
                6: 'green',
                7: 'green darken-1',
                8: 'green darken-2',
                9: 'green darken-3',
                10: 'green darken-4',
            },
            output: '',
        };
    },
    created() {
    },
    methods: {
    },
    computed: {
        circleMaxSize() {
            return this.opt.sizeX / 2;
        },
        ...mapGetters({
            dadosArea: 'area/area',
        }),
    },
    watch: {
        dadosArea() {
            if (this.dadosArea.largura > 0) {
                this.opt.sizeY = this.dadosArea.largura;
            }
            if (this.dadosArea.comprimento > 0) {
                this.opt.sizeX = this.dadosArea.comprimento;
            }
        },
    },
};
</script>
