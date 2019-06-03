<template>
    <v-container
        fluid
        grid-list-xl
    >
        <v-layout
            row
            wrap
        >
            <v-flex
                xs12
            >
                <v-card>
                    <div>
                        <v-text-field
                            v-model="dimensions.sizeX"
                            label="Altura"
                        />
                    </div>
                    <div>
                        <v-text-field
                            v-model="dimensions.sizeY"
                            label="Largura"
                        />
                    </div>
                </v-card>
            </v-flex>
            <v-flex
                xs12
            >
                <v-card>
                    <div
                        id="grid"
                        style="font-family: monospace">
                        <GenerateGrid
                            :opt="opt"
                            :dimensions="dimensions"
                            :color-scale="colorScale"/>
                    </div>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>
<script>
import { mapGetters } from 'vuex';
import GenerateGrid from './GenerateGrid';

export default {
    name: 'Grid',
    components: {
        GenerateGrid,
    },
    props: {
        dimensions: {
            type: Object,
            default: () => {},
        },
    },
    data() {
        return {
            opt: {
                boxSizeW: 20,
                boxSizeH: 20,
                range: 9,
                density: 2,
                densityMax: 15,
            },
            colorScale: {
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
    computed: {
        circleMaxSize() {
            return this.dimensions.sizeX / 2;
        },
        ...mapGetters({
            dadosArea: 'area/area',
        }),
    },
    watch: {
        dadosArea() {
            if (this.dadosArea.largura > 0) {
                this.dimensions.sizeY = this.dadosArea.largura;
            }
            if (this.dadosArea.comprimento > 0) {
                this.dimensions.sizeX = this.dadosArea.comprimento;
            }
        },
    },
};
</script>
