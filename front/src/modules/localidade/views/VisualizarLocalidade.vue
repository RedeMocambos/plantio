<template>
    <v-container fluid>
        <v-layout>
            <v-flex xs10>
                <v-card>
                    <v-card-title>
                        <div>
                            <div class="headline">
                                {{ dadosLocalidade.nome }}
                            </div>
                        </div>
                    </v-card-title>
                    <v-list>
                        <v-list-tile v-if="dadosLocalidade.bioma !== ''">
                            <v-icon class="pa-2">
                                landscape
                            </v-icon>
                            Bioma: {{ dadosLocalidade.bioma }}
                        </v-list-tile>
                        <v-list-tile v-if="dadosLocalidade.clima !== ''">
                            <v-icon class="pa-2">
                                brightness_low
                            </v-icon>
                            Clima:
                            <span
                                class="pl-2"
                                v-html="dadosLocalidade.clima"
                            />
                        </v-list-tile>
                        <v-list-tile v-if="dadosLocalidade.area !== ''">
                            <v-icon class="pa-2">
                                grid_on
                            </v-icon>
                            Área:
                            <span
                                class="pl-2"
                                v-html="dadosLocalidade.area"
                            />
                        </v-list-tile>
                        <h3>Áreas: </h3>
                        <v-data-table
                            :headers="headerAreas"
                            :items="areasLocalidade"
                        >
                            <template
                                v-slot:items="props"
                            >
                                <td>{{ props.index + 1 }}</td>
                                <td>
                                    <a
                                        :href="getAreaUrl(props.item.id)">
                                        {{ props.item.nome }}
                                    </a>
                                </td>
                                <td>{{ props.item.dimensao }}</td>
                                <td>{{ props.item.microclima }}</td>
                            </template>
                        </v-data-table>
                    </v-list>
                    <v-card-actions>
                        <v-btn
                            class="green lighten-1"
                        >
                            <v-icon
                                white
                            >
                                edit
                            </v-icon>
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</div>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';

export default {
    name: 'VisualizarLocalidade',
    data() {
        return {
            headerAreas: [
                {
                    text: '#',
                    align: 'left',
                    sortable: false,
                    value: 'numero',
                },
                {
                    text: 'nome',
                    value: 'nome',
                },
                {
                    text: 'área',
                    value: 'area',
                },
                {
                    text: 'microclima',
                    value: 'microclima',
                },
            ],
            areasLocalidade: [],
        };
    },
    watch: {
        dadosAreasLocalidade() {
            this.areasLocalidade = this.dadosAreasLocalidade;
        },
    },
    created() {
        if (typeof this.$route.params.id !== 'undefined') {
            this.buscarLocalidade(this.$route.params.id);
            this.buscarAreasPorLocalidade(this.$route.params.id);
        }
    },
    methods: {
        ...mapActions({
            buscarLocalidade: 'localidade/buscarLocalidade',
            buscarAreasPorLocalidade: 'localidade/buscarAreasPorLocalidade',
        }),
        getAreaUrl(id) {
            return `/area/${id}`;
        },
    },
    computed: {
        ...mapGetters({
            dadosLocalidade: 'localidade/localidade',
            dadosAreasLocalidade: 'localidade/areasLocalidade',
        }),
    },
};
</script>
